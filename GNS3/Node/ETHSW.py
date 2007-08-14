#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:
#
# Copyright (C) 2007 GNS-3 Dev Team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# Contact: contact@gns3.net
#

from GNS3.Node.AbstractNode import AbstractNode
from GNS3.Config.Objects import ETHSWConf
import GNS3.Dynagen.dynamips_lib as lib
import GNS3.Dynagen.Globals as dynagen
import GNS3.Globals as globals 

ethsw_id = 0

class ETHSW(AbstractNode):
    """ ETHSW class
    """

    def __init__(self, renderer_normal, renderer_select):
        
        AbstractNode.__init__(self, renderer_normal, renderer_select)
        
        # assign a new hostname
        global ethsw_id
        self.hostname = 'S' + str(ethsw_id)
        ethsw_id = ethsw_id + 1
        self.setCustomToolTip()

        self.config = self.getDefaultConfig()
        self.dev = None
        
    def getDefaultConfig(self):
        """ Returns the default configuration
        """

        return ETHSWConf()

    def getInterfaces(self):
        """ Returns all interfaces
        """

        ports = map(str,  self.config.ports.keys())
        return (ports)
        
    def configNode(self):
    
        if self.config.hypervisor_host:
            hypervisorkey = hypervisor_host + ':' + str(hypervisor_port)
            if globals.GApp.hypervisors.has_key(hypervisorkey):
                hypervisor = globals.GApp.hypervisors[hypervisorkey ]
                self.configHypervisor(hypervisor_host,  hypervisor_port,  hypervisor.workdir,  hypervisor.baseUDP)
            else:
                print 'Hypervisor ' + hypervisorkey + ' not registered !'
                return
        else:
            dynamips = globals.GApp.systconf['dynamips']
            self.configHypervisor('localhost',  dynamips.port,  dynamips.workdir,  10000)

        hypervisor = self.getHypervisor()
        self.dev = lib.ETHSW(hypervisor, name = '"' + self.hostname + '"')
        
    def startNode(self):
    
        if self.dev == None:
            return

        connected_interfaces = self.getConnectedInterfaceList()
        for interface in connected_interfaces:
            destinterface = self.getConnectedNeighbor(interface)
            print destinterface
        
        #TODO: finish connetion to NIO
        
        connected_interfaces = map(int,  connected_interfaces)
        for (vlan,  portlist) in self.config.vlans.iteritems():
            for port in portlist:
                if port in connected_interfaces:
                    porttype = self.config.ports[port]
                    self.dev.set_port(port, porttype, vlan)

        for edge in self.getEdgeList():
                edge.setLocalInterfaceStatus(self.id, True)

    def stopNode(self):

        if self.dev:
            self.shutdownInterfaces()

    def resetHypervisor(self):
        
        key = self.hypervisor_host + ':' + str(self.hypervisor_port)
        if dynagen.dynamips.has_key(key):
            del dynagen.dynamips[key]
        self.hypervisor_host = None
        self.hypervisor_port = None
        self.baseUDP = None
        
    def resetNode(self):
        """ Delete the IOS instance
        """

        if self.dev != None:
            self.dev.delete()
#            if dynagen.devices.has_key(self.hostname):
#                del dynagen.devices[self.hostname]
#            self.shutdownInterfaces()
        
    def console(self):
        
        pass 
