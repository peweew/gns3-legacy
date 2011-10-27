#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:
#
# Copyright (c) 2007-2011 Thomas Pani, Jeremy Grossmann & Alexey Eromenko "Technologov"
#
# Contributions by Pavel Skovajsa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

#Written for GNS3.
#This module is used for actual control of VMs, sending commands to VBox controllers.
#VBox controllers implement VirtualBox version-specific API calls.
#This is the server part, it can be started manually, or automatically from "VBoxManager"
#Client part is named "dynagen_vbox_lib".

#debuglevel: 0=disabled, 1=default, 2=debug, 3=deep debug
debuglevel = 0

import csv
import cStringIO
import os
import select
import socket
import sys
import threading
import SocketServer
import time

import vboxcontroller_4_1

if debuglevel > 0:
    if sys.platform == 'win32':
        debugfilename = "C:\TEMP\gns3-vboxwrapper-log.txt"
    else:
        debugfilename = "/tmp/gns3-vboxwrapper-log.txt"
    try:
        dfile = open(debugfilename, 'wb')
    except:
        dfile = False
        print "WARNING: log file cannot be created !"
    if dfile:
        print "Log file = %s" % str(debugfilename)

def debugmsg(level, message):
    if debuglevel == 0:
        return
    if debuglevel >= level:
        print message
        if dfile:
            #In python 2.6, print with redirections always uses UNIX line-ending,
            # so I must add os-neutral line-endings.
            print >> dfile, message,
            dfile.write(os.linesep)
            dfile.flush()

msg = "WELCOME to vboxwrapper.py"
debugmsg(2, msg)
debugmsg(1, "debuglevel =  %s" % debuglevel + os.linesep)

__author__ = 'Thomas Pani, Jeremy Grossmann and Alexey Eromenko "Technologov"'
__version__ = '0.8.0-RC1'

try:
    from vboxapi import VirtualBoxManager
except:
    msg = "ERROR: cannot load 'vboxapi' module !" + os.linesep
    msg += "Please check your Python and VirtualBox installation."
    print msg
    debugmsg(1, msg)
    exit()

PORT = 11525
IP = ""
VBOX_INSTANCES = {}
FORCE_IPV6=False
VBOX_STREAM = 0
VBOXVER = 0.0
CACHED_REPLY = ""
CACHED_REQUEST = ""
CACHED_TIME = 0.0
g_stats=""
g_vboxManager=0
g_result=""

#Working Dir in VirtualBox is mainly needed for "Traffic Captures".
WORKDIR = os.getcwd()
if os.environ.has_key("TEMP"):
    WORKDIR = unicode(os.environ["TEMP"], errors='replace')
elif os.environ.has_key("TMP"):
    WORKDIR = unicode(os.environ["TMP"], errors='replace')

class UDPConnection:
    def __init__(self, sport, daddr, dport):
        debugmsg(3, "class UDPConnection::__init__(%s, %s, %s)" % (str(sport), str(daddr), str(dport)))
        self.sport = sport
        self.daddr = daddr
        self.dport = dport

    def resolve_names(self):
        try:
            addr = socket.gethostbyname(self.daddr)
            self.daddr = addr
        except socket.error, e:
            print >> sys.stderr, "Unable to resolve hostname %s", self.daddr
            print >> sys.stderr, e
        except socket.herror, e:
            print >> sys.stderr, "Unable to resolve hostname %s", self.daddr
            print >> sys.stderr, e


class xVBOXInstance(object):

    def __init__(self, name):
        debugmsg(2, "class xVBOXInstance::__init__(%s)" % str(name))
        self.name = name
        self.console = ''
        self.image = ''
        self.nic = {}
        self.nics = '6'
        self.udp = {}
        self.capture = {}
        self.netcard = 'automatic'
        self.guestcontrol_user = ''
        self.guestcontrol_password = ''
        self.process = None
        self.workdir = WORKDIR
        self.valid_attr_names = ['image',  'console', 'nics', 'netcard', 'guestcontrol_user', 'guestcontrol_password']
        self.mgr = g_vboxManager
        self.vbox = self.mgr.vbox
        # Future-proof way to control several major versions of VBox:
        #if VBOXVERSION == 4.1:
        self.vbc = vboxcontroller_4_1.VBoxController_4_1(self.mgr)
        #elif VBOXVERSION == 4.2:
        #    self.vbc = vboxcontroller_4_2.VBoxController_4_2(mgr, name)
        #...
        # Init win32 com
        if sys.platform == 'win32':
            self.prepareWindowsCOM()

    def prepareWindowsCOM(self):
        # Microsoft COM behaves differently than Mozilla XPCOM, and requires special multi-threading code.
        debugmsg(2, "xVBOXInstance::prepareWindowsCOM()")
        # Get the VBox interface from previous thread
        global VBOX_STREAM
        i = pythoncom.CoGetInterfaceAndReleaseStream(VBOX_STREAM, pythoncom.IID_IDispatch)
        self.vbox = win32com.client.Dispatch(i)
        VBOX_STREAM = pythoncom.CoMarshalInterThreadInterfaceInStream(pythoncom.IID_IDispatch, self.vbox)

    def create(self):
        debugmsg(2, "xVBOXInstance::create()")
        self.workdir = os.path.join(os.getcwd(), self.name)
        if not os.path.exists(self.workdir):
            os.makedirs(self.workdir)

    def clean(self):
        pass

    def unbase_disk(self):
        pass

    def start(self):
        debugmsg(2, "xVBOXInstance::start()")
        self.vmname = self.image

        return self.vbc.start(self.vmname, self.nics, self.udp, self.capture, self.netcard)

    def reset(self):
        debugmsg(2, "xVBOXInstance::reset()")
        return self.vbc.reset()

    def stop(self):
        debugmsg(2, "xVBOXInstance::stop()")
        return self.vbc.stop()

    def suspend(self):
        debugmsg(2, "xVBOXInstance::suspend()")
        return self.vbc.suspend()

    def resume(self):
        debugmsg(2, "xVBOXInstance::resume()")
        return self.vbc.resume()

    def create_udp(self, i_vnic, sport, daddr, dport):
        debugmsg(2, "xVBOXInstance::create_udp(%s, %s, %s, %s)" % (str(i_vnic), str(sport), str(daddr), str(dport)))
        # FlexiNetwork: Link hot-add
        return self.vbc.create_udp(i_vnic, sport, daddr, dport)

    def delete_udp(self, i_vnic):
        debugmsg(2, "xVBOXInstance::delete_udp(%s)" % str(i_vnic))
        # FlexiNetwork: Link hot-remove
        return self.vbc.delete_udp(i_vnic)

    def get_nio_stats(self, vnic):
        # This function retrieves sent/received bytes from VMs.
        debugmsg(3, "xVBOXInstance::get_nio_stats(%s)" % str(vnic))
        global g_stats
        if self.vbc.get_nio_stats(vnic):
            g_stats = self.vbc.stats
            debugmsg(3, "self.vbc.stats = %s" % str(self.vbc.stats))
            return True
        else:
            g_stats = ""
            return False

    def vboxexec(self, command):
        # This function executes arbitary commands on VMs, and gets STDOUT results.
        debugmsg(3, "xVBOXInstance::vboxexec(%s)" % str(command))
        global g_result
        if self.vbc.vboxexec(command, self.guestcontrol_user, self.guestcontrol_password):
            g_result = self.vbc.result
            #debugmsg(3, "self.vbc.result = %s" % str(self.vbc.result))
            return True
        else:
            g_result = ""
            return False

    def displayWindowFocus(self):
        # Bring VM's display as foreground window and focus on it
        debugmsg(2, "xVBOXInstance::displayWindowFocus()")
        global g_result
        if self.vbc.displayWindowFocus():
            #eturn the window handler to the client
            g_result = self.vbc.hwnd
            return True
        else:
            g_result = "0"
            return False

class VBOXInstance(xVBOXInstance):

    def __init__(self, name):
        debugmsg(2, "class VBOXInstance::__init__(%s)" % str(name))
        super(VBOXInstance, self).__init__(name)

class VBoxDeviceInstance(VBOXInstance):

    def __init__(self, *args, **kwargs):
        debugmsg(3, "class VBoxDeviceInstance::__init__(%s, %s)" % (str(*args), str(**kwargs)))
        super(VBoxDeviceInstance, self).__init__(*args, **kwargs)
        self.netcard = 'automatic'

    def clean(self):
        pass

    def unbase_disk(self):
        pass

class VBoxWrapperRequestHandler(SocketServer.StreamRequestHandler):
    debugmsg(2, "class VBoxWrapperRequestHandler")
    modules = {
        'vboxwrapper' : {
            'version' : (0, 0),
            'parser_test' : (0, 10),
            'module_list' : (0, 0),
            'cmd_list' : (1, 1),
            'working_dir' : (1, 1),
            'reset' : (0, 0),
            'close' : (0, 0),
            'stop' : (0, 0),
            },
        'vbox' : {
            'version' : (0, 0),
            'create' : (2, 2),
            'delete' : (1, 1),
            'setattr' : (3, 3),
            'create_nic' : (2, 2),
            'create_udp' : (5, 5),
            'delete_udp' : (2, 2),
            'create_capture' : (3, 3),
            'delete_capture' : (2, 2),
            'start' : (1, 1),
            'stop' : (1, 1),
            'reset' : (1, 1),
            'suspend' : (1, 1),
            'resume' : (1, 1),
            'clean': (1, 1),
            'unbase': (1, 1),
            'get_nio_stats': (2, 2),
            'exec': (2, 256),
            'display_window_focus': (1, 1),
            }
        }

    vbox_classes = {
        'vbox': VBoxDeviceInstance,
        }

    # dynamips style status codes
    HSC_INFO_OK         = 100  #  ok
    HSC_INFO_MSG        = 101  #  informative message
    HSC_INFO_DEBUG      = 102  #  debugging message
    HSC_ERR_PARSING     = 200  #  parse error
    HSC_ERR_UNK_MODULE  = 201  #  unknown module
    HSC_ERR_UNK_CMD     = 202  #  unknown command
    HSC_ERR_BAD_PARAM   = 203  #  bad number of parameters
    HSC_ERR_INV_PARAM   = 204  #  invalid parameter
    HSC_ERR_BINDING     = 205  #  binding error
    HSC_ERR_CREATE      = 206  #  unable to create object
    HSC_ERR_DELETE      = 207  #  unable to delete object
    HSC_ERR_UNK_OBJ     = 208  #  unknown object
    HSC_ERR_START       = 209  #  unable to start object
    HSC_ERR_STOP        = 210  #  unable to stop object
    HSC_ERR_FILE        = 211  #  file error
    HSC_ERR_BAD_OBJ     = 212  #  bad object

    close_connection = 0

    def do_vbox_display_window_focus(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_display_window_focus(%s)" % str(data))
        name, = data
        if not VBOX_INSTANCES[name].displayWindowFocus():
            self.send_reply(self.HSC_ERR_STOP, 1,
                            "unable to display window focus of instance '%s'" % name)
        else:
            self.send_reply(self.HSC_INFO_OK, 1, "%s %s" % ("hwnd", str(g_result)))

    def do_vbox_get_nio_stats(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_get_nio_stats(%s)" % str(data))
        name, vnic = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        if not VBOX_INSTANCES[name].get_nio_stats(int(vnic)):
            self.send_reply(self.HSC_ERR_BAD_OBJ, 1,
                            "unable to get statistics from VBox '%s'" % name)
        else:
            self.send_reply(self.HSC_INFO_OK, 1, "%s %s" % ("nio_stat", str(g_stats)))

    def do_vbox_exec(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_exec(%s)" % str(data))
        #name, command = data
        name = data[0]
        raw_command = data[1:]
        debugmsg(3, "raw_command = %s" % str(raw_command))
        processed_command = ""
        for x in range(len(raw_command)):
            # First-and-the-only command, we strip [' and '] or for First-command, we strip [' and ',
            if x == 0:
                processed_command += raw_command[0][2:-2]
            # Last command, we strip ' and '], and for the middle of the pack command, we strip ' and ',
            else:
                processed_command += " " + raw_command[x][1:-2]
        debugmsg(3, "processed_command = %s" % str(processed_command))
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        if not VBOX_INSTANCES[name].vboxexec(processed_command):
            self.send_reply(self.HSC_ERR_BAD_OBJ, 1,
                            "unable to get result from VBox '%s'" % name)
        else:
            self.send_reply(self.HSC_INFO_OK, 1, "%s %s" % ("result", str(g_result)))

    def send_reply(self, code, done, msg):
        debugmsg(2, "VBoxWrapperRequestHandler::send_reply(code=%s, done=%s, msg=%s)" % (str(code), str(done), str(msg)))
        sep = '-'
        if not done:
            sep = ' '
        global CACHED_REPLY, CACHED_TIME
        CACHED_TIME = time.time()
        CACHED_REPLY = "%3d%s%s\r\n" % (code, sep, msg)
        self.wfile.write(CACHED_REPLY)

    def handle(self):
        debugmsg(2, "VBoxWrapperRequestHandler::handle()")
        print "Connection from", self.client_address
        try:
            self.handle_one_request()
            while not self.close_connection:
                self.handle_one_request()
        except socket.error:
            pass

    def __get_tokens(self, request):
        debugmsg(3, "VBoxWrapperRequestHandler::__get_tokens(%s)" % str(request))
        input_ = cStringIO.StringIO(request)
        tokens = []
        try:
            tokens = csv.reader(input_, delimiter=' ').next()
        except StopIteration:
            pass
        #debugmsg(3, ("VBoxWrapperRequestHandler::__get_tokens(),    returns original_tokens = ", tokens))
        #tokens = request.split(' ')
        #debugmsg(3, ("VBoxWrapperRequestHandler::__get_tokens(),    returns alternative_tokens = ", tokens))

        #exec command exception:
        # This is a gross hack, because original code converts one Windows back-slash into four.
        #if tokens[1] is 'exec':
        #    tokens[3] = request.split()[3:]
        debugmsg(3, ("VBoxWrapperRequestHandler::__get_tokens(),    returns tokens = ", tokens))

        return tokens

    def handle_one_request(self):
        debugmsg(3, "VBoxWrapperRequestHandler::handle_one_request()")
        request = self.rfile.readline()
        debugmsg(3, "handle_one_request(), request = %s" % request)
        # If command exists in cache (=cache hit), we skip further processing
        if self.check_cache(request):
            return
        global CACHED_REQUEST
        CACHED_REQUEST = request
        request = request.rstrip()      # Strip package delimiter.

        # Parse request.
        tokens = self.__get_tokens(request)
        if len(tokens) < 2:
            self.send_reply(self.HSC_ERR_PARSING, 1,
                            "At least a module and a command must be specified")
            return

        module, command = tokens[:2]
        data = tokens[2:]
        debugmsg(3, ("handle_one_request(), module = ", module, " command = ", command, " data = ", data))
        if not module in self.modules.keys():
            self.send_reply(self.HSC_ERR_UNK_MODULE, 1,
                            "Unknown module '%s'" % module)
            return

        # Prepare to call the do_<command> function.
        mname = 'do_%s_%s' % (module, command)
        debugmsg(3, ("handle_one_request(), 1: mname = ", mname))
        if not hasattr(self, mname):
            self.send_reply(self.HSC_ERR_UNK_CMD, 1,
                            "Unknown command '%s'" % command)
            return
        debugmsg(3, ("handle_one_request(), if not hasattr success"))
        try:
            if len(data) < self.modules[module][command][0] or \
                len(data) > self.modules[module][command][1]:
                self.send_reply(self.HSC_ERR_BAD_PARAM, 1,
                                "Bad number of parameters (%d with min/max=%d/%d)" %
                                    (len(data),
                                      self.modules[module][command][0],
                                      self.modules[module][command][1])
                                    )
                return
        except Exception, e:
            # This can happen, if you add send command, but forget to define it in class modules
            self.send_reply(self.HSC_ERR_INV_PARAM, 1, "Unknown Exception")
            debugmsg(1, ("handle_one_request(), ERROR: Unknown Exception: ", e))
            return
        debugmsg(3, ("handle_one_request(), if len(data) success"))
        # Call the function.
        method = getattr(self, mname)
        method(data)

    def check_cache(self, request):
        debugmsg(3, "VBoxWrapperRequestHandler::check_cache(%s)" % str(request.replace("\n", "")))
        # TCP Server cache is needed due to async nature of the server;
        # Often TCP client (dynagen) received a reply from previous request.
        # This workaround allows us to send two requests and get two replies per query.
        #
        # Checks command cache, and sends cached reply immediately.
        # Returns True, if cached request/reply found within reasonable time period. (=cache hit)
        # Otherwise returns false, which means cache miss, and further processing
        # by handle_one_request() is required.
        global CACHED_REQUEST, CACHED_REPLY, CACHED_TIME
        cur_time = time.time()
        debugmsg(3, "cur_time = %s, CACHED_TIME = %s" % (str(cur_time), str(CACHED_TIME)))
        if (cur_time - CACHED_TIME) > 1.0:
            # Too much time elapsed... cache is invalid
            debugmsg(3, "cache miss on time")
            return False
        if request != CACHED_REQUEST:
            # different request means a cache miss
            debugmsg(3, "cache miss on instruction")
            return False
        debugmsg(3, "cache hit")
        CACHED_TIME = 0.0  # Reset timer disallows to use same cache more than 2 times in a row
        self.wfile.write(CACHED_REPLY)
        return True

    def do_vboxwrapper_version(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vboxwrapper_version(%s)" % str(data))
        self.send_reply(self.HSC_INFO_OK, 1, __version__)

    def do_vboxwrapper_parser_test(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vboxwrapper_parser_test(%s)" % str(data))
        for i in range(len(data)):
            self.send_reply(self.HSC_INFO_MSG, 0,
                            "arg %d (len %u): \"%s\"" % \
                            (i, len(data[i]), data[i])
                            )
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vboxwrapper_module_list(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vboxwrapper_module_list(%s)" % str(data))
        for module in self.modules.keys():
            self.send_reply(self.HSC_INFO_MSG, 0, module)
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vboxwrapper_cmd_list(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vboxwrapper_cmd_list(%s)" % str(data))
        module, = data

        if not module in self.modules.keys():
            self.send_reply(self.HSC_ERR_UNK_MODULE, 1,
                            "unknown module '%s'" % module)
            return

        for command in self.modules[module].keys():
            self.send_reply(self.HSC_INFO_MSG, 0,
                            "%s (min/max args: %d/%d)" % \
                            (command,
                             self.modules[module][command][0],
                             self.modules[module][command][1])
                            )

        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vboxwrapper_working_dir(self, data):
        #"""
        debugmsg(2, "VBoxWrapperRequestHandler::do_vboxwrapper_working_dir(%s)" % str(data))
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

        working_dir, = data
        try:
            os.chdir(working_dir)
            for vbox_name in VBOX_INSTANCES.keys():
                VBOX_INSTANCES[vbox_name].workdir = os.path.join(os.getcwd(), VBOX_INSTANCES[vbox_name].name)
            self.send_reply(self.HSC_INFO_OK, 1, "OK")
        except OSError, e:
            self.send_reply(self.HSC_ERR_INV_PARAM, 1,
                            "chdir: %s" % e.strerror)
        #"""

    def do_vboxwrapper_reset(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vboxwrapper_reset(%s)" % str(data))
        cleanup()
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vboxwrapper_close(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vboxwrapper_close(%s)" % str(data))
        self.send_reply(self.HSC_INFO_OK, 1, "OK")
        self.close_connection = 1

    def do_vboxwrapper_stop(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vboxwrapper_stop(%s)" % str(data))
        self.send_reply(self.HSC_INFO_OK, 1, "OK")
        self.close_connection = 1
        self.server.stop()

    def do_vbox_version(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_version(%s)" % str(data))
        self.send_reply(self.HSC_INFO_OK, 1, VBOXVER)

    def __vbox_create(self, dev_type, name):
        debugmsg(2, "VBoxWrapperRequestHandler::__vbox_create(dev_type=%s, name=%s)" % (str(dev_type), str(name)))

        try:
            devclass = self.vbox_classes[dev_type]
        except KeyError:
            debugmsg(2, "No device type %s" % dev_type)
            print >> sys.stderr, "No device type %s" % dev_type
            return 1
        if name in VBOX_INSTANCES.keys():
            debugmsg(2, "Unable to create VBox instance %s" % name)
            debugmsg(2, "%s already exists" % name)
            print >> sys.stderr, "Unable to create VBox instance", name
            print >> sys.stderr, "%s already exists" % name
            return 1

        vbox_instance = devclass(name)

        try:
            vbox_instance.create()
        except OSError, e:
	    debugmsg(2, "Unable to create VBox instance %s" % name)
            print >> sys.stderr, "Unable to create VBox instance", name
            print >> sys.stderr, e
            return 1

        VBOX_INSTANCES[name] = vbox_instance
        return 0

    def do_vbox_create(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_create(%s)" % str(data))
        dev_type, name = data
        if self.__vbox_create(dev_type, name) == 0:
            self.send_reply(self.HSC_INFO_OK, 1, "VBox '%s' created" % name)
        else:
            self.send_reply(self.HSC_ERR_CREATE, 1,
                            "unable to create VBox instance '%s'" % name)

    def __vbox_delete(self, name):
        debugmsg(2, "VBoxWrapperRequestHandler::__vbox_delete(%s)" % str(name))
        if not name in VBOX_INSTANCES.keys():
            return 1
        if VBOX_INSTANCES[name].process and not VBOX_INSTANCES[name].stop():
            return 1
        del VBOX_INSTANCES[name]
        return 0

    def do_vbox_delete(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_delete(%s)" % str(data))
        name, = data
        if self.__vbox_delete(name) == 0:
            self.send_reply(self.HSC_INFO_OK, 1, "VBox '%s' deleted" % name)
        else:
            self.send_reply(self.HSC_ERR_DELETE, 1,
                            "unable to delete VBox instance '%s'" % name)

    def do_vbox_setattr(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_setattr(%s)" % str(data))
        name, attr, value = data
        try:
            instance = VBOX_INSTANCES[name]
        except KeyError:
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                             "unable to find VBox '%s'" % name)
            return
        if not attr in instance.valid_attr_names:
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "Cannot set attribute '%s' for '%s" % (attr, name))
            return
        print >> sys.stderr, '!! %s.%s = %s' % (name, attr, value)
        setattr(VBOX_INSTANCES[name], attr, value)
        self.send_reply(self.HSC_INFO_OK, 1, "%s set for '%s'" % (attr, name))

    def do_vbox_create_nic(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_create_nic(%s)" % str(data))
        #name, vnic, mac = data
        name, vnic = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        #VBOX_INSTANCES[name].nic[int(vnic)] = mac
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vbox_create_udp(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_create_udp(%s)" % str(data))
        name, vnic, sport, daddr, dport = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        #Try to create UDP:
        VBOX_INSTANCES[name].create_udp(vnic, sport, daddr, dport)
        #if not VBOX_INSTANCES[name].create_udp(vnic, sport, daddr, dport):
        #    self.send_reply(self.HSC_ERR_CREATE, 1,
        #                    "unable to create UDP connection '%s'" % vnic)
        #    return
        udp_connection = UDPConnection(sport, daddr, dport)
        udp_connection.resolve_names()
        VBOX_INSTANCES[name].udp[int(vnic)] = udp_connection
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vbox_delete_udp(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_delete_udp(%s)" % str(data))
        name, vnic = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        # ***************
        #Try to delete UDP:
        VBOX_INSTANCES[name].delete_udp(vnic)
        #if not VBOX_INSTANCES[name].delete_udp(vnic):
        #    self.send_reply(self.HSC_ERR_DELETE, 1,
        #                    "unable to remove UDP connection '%s'" % vnic)
        #    return
        if VBOX_INSTANCES[name].udp.has_key(int(vnic)):
            del VBOX_INSTANCES[name].udp[int(vnic)]
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vbox_create_capture(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_create_capture(%s)" % str(data))
        name, vnic, path = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return

        VBOX_INSTANCES[name].capture[int(vnic)] = path
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vbox_delete_capture(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_delete_capture(%s)" % str(data))
        name, vnic = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        if VBOX_INSTANCES[name].capture.has_key(int(vnic)):
            del VBOX_INSTANCES[name].capture[int(vnic)]
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vbox_start(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_start(%s)" % str(data))
        name, = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        if not VBOX_INSTANCES[name].start():
            self.send_reply(self.HSC_ERR_START, 1,
                            "unable to start instance '%s'" % name)
        else:
            self.send_reply(self.HSC_INFO_OK, 1, "VBox '%s' started" % name)

    def do_vbox_stop(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_stop(%s)" % str(data))
        name, = data
        if not VBOX_INSTANCES[name].stop():
            self.send_reply(self.HSC_ERR_STOP, 1,
                            "unable to stop instance '%s'" % name)
        else:
            self.send_reply(self.HSC_INFO_OK, 1, "VBox '%s' stopped" % name)

    def do_vbox_reset(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_reset(%s)" % str(data))
        name, = data
        if not VBOX_INSTANCES[name].reset():
            self.send_reply(self.HSC_ERR_STOP, 1,
                            "unable to reset instance '%s'" % name)
        else:
            self.send_reply(self.HSC_INFO_OK, 1, "VBox '%s' rebooted" % name)

    def do_vbox_suspend(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_suspend(%s)" % str(data))
        name, = data
        if not VBOX_INSTANCES[name].suspend():
            self.send_reply(self.HSC_ERR_STOP, 1,
                            "unable to suspend instance '%s'" % name)
        else:
            self.send_reply(self.HSC_INFO_OK, 1, "VBox '%s' suspended" % name)

    def do_vbox_resume(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_resume(%s)" % str(data))
        name, = data
        if not VBOX_INSTANCES[name].resume():
            self.send_reply(self.HSC_ERR_STOP, 1,
                            "unable to resume instance '%s'" % name)
        else:
            self.send_reply(self.HSC_INFO_OK, 1, "VBox '%s' resumed" % name)

    def do_vbox_clean(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_clean(%s)" % str(data))
        name, = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        VBOX_INSTANCES[name].clean()
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

    def do_vbox_unbase(self, data):
        debugmsg(2, "VBoxWrapperRequestHandler::do_vbox_unbase(%s)" % str(data))
        name, = data
        if not name in VBOX_INSTANCES.keys():
            self.send_reply(self.HSC_ERR_UNK_OBJ, 1,
                            "unable to find VBox '%s'" % name)
            return
        VBOX_INSTANCES[name].unbase_disk()
        self.send_reply(self.HSC_INFO_OK, 1, "OK")

class DaemonThreadingMixIn(SocketServer.ThreadingMixIn):
    daemon_threads = True


#class VBoxWrapperServer(SocketServer.TCPServer):
class VBoxWrapperServer(DaemonThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        debugmsg(2, "VBoxWrapperServer::__init__()")
        global FORCE_IPV6
        if server_address[0].__contains__(':'):
            FORCE_IPV6 = True
        if FORCE_IPV6:
            # IPv6 address support
            self.address_family = socket.AF_INET6
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)
        self.stopping = threading.Event()
        self.pause = 0.1
        self.VBoxInit()

    def VBoxInit(self):
        global g_vboxManager, VBOXVER, __version__, debuglevel
        # This part is generic init for all versions of VBox
        try:
            g_vboxManager = VirtualBoxManager(None, None)
        except Exception, e:
            # This can happen, if your VBoxPython module is broken, or incorrectly installed
            debugmsg(1, "ERROR: Cannot start vboxapi module !")
            print >> sys.stderr, e
            exit()

        VBOXVER = g_vboxManager.vbox.version
        RUNNING_VBOX_STRING = "Running VirtualBox %s r%d" % (VBOXVER, g_vboxManager.vbox.revision)
        if debuglevel > 0:
            debugmsg(1, RUNNING_VBOX_STRING)
        else:
            print RUNNING_VBOX_STRING
        __version__ += " (%s)" % RUNNING_VBOX_STRING

        vboxver_maj = VBOXVER.split('.')[0]
        vboxver_min = VBOXVER.split('.')[1]
        vboxver = float(str(vboxver_maj)+'.'+str(vboxver_min))
        vboxver_required = 4.1
        if vboxver < vboxver_required:
            print "ERROR: Detected VirtualBox version %s, which is too old." % VBOXVER + os.linesep + "Minimum required is: %s" % str(vboxver_required)
            print ""
            exit()

        if sys.platform == 'win32':
            debugmsg(3, "VBoxWrapperServer::VBoxInit(), CoMarshal..()")
            global VBOX_STREAM
            VBOX_STREAM = pythoncom.CoMarshalInterThreadInterfaceInStream(pythoncom.IID_IDispatch, g_vboxManager.vbox)

    def serve_forever(self):
        while not self.stopping.isSet():
            if select.select([self.socket], [], [], self.pause)[0]:
                self.handle_request()
        cleanup()

    def stop(self):
        self.stopping.set()

def cleanup():
    print "Shutdown in progress..."
    for name in VBOX_INSTANCES.keys():
        if VBOX_INSTANCES[name].process:
            VBOX_INSTANCES[name].stop()
        del VBOX_INSTANCES[name]
    print "Shutdown completed."

def main():
    debugmsg(2, "vboxwrapper.py    main()")
    global IP
    from optparse import OptionParser

    usage = "usage: %prog [--listen <ip_address>] [--port <port_number>] [--forceipv6 true]"
    parser = OptionParser(usage, version="%prog " + __version__)
    parser.add_option("-l", "--listen", dest="host", help="IP address or hostname to listen on (default is to listen on all interfaces)")
    parser.add_option("-p", "--port", type="int", dest="port", help="Port number (default is 11525)")
    parser.add_option("-w", "--workdir", dest="wd", help="Working directory (default is current directory)")
    parser.add_option("-6", "--forceipv6", dest="force_ipv6", help="Force IPv6 usage (default is false; i.e. IPv4)")

    try:
        (options, args) = parser.parse_args()
    except SystemExit:
        sys.exit(1)

    if options.host:
        host = options.host
        global IP
        IP = host
    else:
        host = IP

    if options.port:
        port = options.port
        global PORT
        PORT = port
    else:
        port = PORT

    if options.wd:
        global WORKDIR
        WORKDIR = options.wd

    if options.force_ipv6 and not (options.force_ipv6.lower().__contains__("false") or options.force_ipv6.__contains__("0")):
        global FORCE_IPV6
        FORCE_IPV6 = options.force_ipv6

    debugmsg(3, "starting server on host %s (port %s)" % (str(host), str(port)))
    server = VBoxWrapperServer((host, port), VBoxWrapperRequestHandler)

    print "VBoxWrapper TCP control server started (port %d)." % port


    if FORCE_IPV6:
        LISTENING_MODE = "Listening in IPv6 mode"
    else:
        LISTENING_MODE = "Listening"

    if IP:
        print "%s on %s" % (LISTENING_MODE, IP)
    else:
        print "%s on all network interfaces" % LISTENING_MODE
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        cleanup()


if __name__ == '__main__':
    print "VirtualBox Wrapper (version %s)" % __version__
    print 'Copyright (c) 2007-2011'
    print 'Thomas Pani, Jeremy Grossmann and Alexey Eromenko "Technologov"'
    print

    if sys.platform == 'win32':
        try:
            import win32com, pythoncom
        except ImportError:
            print >> sys.stderr, "You need pywin32 installed to run vboxwrapper!"
            sys.exit(1)

    main()