# -*- coding: utf-8 -*-
##
##
## This file is part of Indico
## Copyright (C) 2002 - 2013 European Organization for Nuclear Research (CERN)
##
## Indico is free software: you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.
##
## Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Indico.  If not, see <http://www.gnu.org/licenses/>.

from flask import request

import MaKaC.webinterface.pages.admins as adminPages
import MaKaC.webinterface.rh.admins as admins
from MaKaC.common.info import HelperMaKaCInfo
from MaKaC.plugins.base import PluginsHolder
import MaKaC.webinterface.urlHandlers as urlHandlers


class RHRoomBookingPluginAdminBase(admins.RHAdminBase):
    pass


class RHRoomBookingPluginAdmin(RHRoomBookingPluginAdminBase):

    def _checkParams(self):
        admins.RHAdminBase._checkParams(self, request.args)

    def _process(self):
        return adminPages.WPRoomBookingPluginAdmin(self, request.args).display()


class RHSwitchRoomBookingModuleActive(RHRoomBookingPluginAdminBase):

    def _checkParams(self):
        admins.RHAdminBase._checkParams(self, request.args)

    def _process(self):
        minfo = HelperMaKaCInfo.getMaKaCInfoInstance()

        active = minfo.getRoomBookingModuleActive()
        if not active:
            PluginsHolder().reloadAllPlugins()
            if not PluginsHolder().getPluginType("RoomBooking").isActive():
                PluginsHolder().getPluginType("RoomBooking").setActive(True)

        minfo.setRoomBookingModuleActive(not active)
        self._redirect(urlHandlers.UHRoomBookingPluginAdmin.getURL())