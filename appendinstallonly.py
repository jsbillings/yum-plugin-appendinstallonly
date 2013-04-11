# A plugin for yum which will add to the installonlypkgs directive without
# overwritting what's in /etc/yum.conf or overriding the defaults contained 
# in yum's config.py code
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# @Author - Adam Miller <maxamillion@fedoraproject.org>
#
# version 0.0.1

from yum.plugins import TYPE_CORE

requires_api_version = "2.6"
plugin_type = (TYPE_CORE)

def postconfig_hook(conduit):
    appendinstallonly_pkgs = conduit.confString("main","appendinstallonlypkgs")
    
    if appendinstallonly_pkgs != None:
        for append_pkg in appendinstallonly_pkgs.replace(',',' ').split():
            conduit._base.conf.installonlypkgs.append(append_pkg)

