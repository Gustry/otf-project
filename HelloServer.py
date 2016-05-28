# -*- coding: utf-8 -*-

"""
***************************************************************************
    HelloServer.py
    ---------------------
    Date                 : August 2014
    Copyright            : (C) 2014-2015 by Alessandro Pasotti
    Email                : apasotti at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alessandro Pasotti'
__date__ = 'August 2014'
__copyright__ = '(C) 2014, Alessandro Pasotti - ItOpen'

import sys
import os

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
try:
    from qgis.server import *
except:
    pass

# Remote console filter auth defaults

# The filter will issue a 403 Forbidden if the following
# environment vars are not passed by FCGI:

DEFAULT_REMOTE_ADDR = '127.0.0.1'

"""
HTTP_AUTH BASIC
May need proper fcgid apache configuration:

    RewriteEngine On
    <IfModule mod_fcgid.c>
        RewriteCond %{HTTP:Authorization} .
        RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
    </IfModule>

"""

DEFAULT_USERID = 'test'
DEFAULT_PASSWORD = 'qgis'


class HelloServerServer:
    """Test plugin for QGIS server
    this plugin loads all filters from the 'filters' directory and logs
    errors"""

    def __init__(self, serverIface):
        # Save reference to the QGIS server interface
        self.serverIface = serverIface
        import filters
        priority = 1

        QgsMessageLog.logMessage("SUCCESS - HelloServer init", 'plugin', QgsMessageLog.INFO)
        for filter_name in filters.local_modules:
            QgsLogger.debug("HelloServerServer - loading filter %s" % filter_name)
            try:
                serverIface.registerFilter( getattr(filters, filter_name)(serverIface), priority * 100 )
                priority += 1
            except Exception, e:
                QgsLogger.debug("HelloServerServer - Error loading filter %s : %s" % (filter_name, e))


if __name__ == "__main__":
    pass
