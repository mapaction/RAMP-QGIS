"""
/***************************************************************************
 test
                                 A QGIS plugin
 test
                             -------------------
        begin                : 2012-10-16
        copyright            : (C) 2012 by abc
        email                : abc
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "test"
def description():
    return "test"
def version():
    return "Version abc"
def icon():
    return "tools.png"
def qgisMinimumVersion():
    return "1.7"
def classFactory(iface):
    # load MapActionTools class from file MapActionTools
    from mapactiontools import MapActionTools
    return MapActionTools(iface)
