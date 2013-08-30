"""
/***************************************************************************
 MapAction Tools
                             -------------------
        begin                : 2012-10-12
        copyright            : (C) 2012 by Greg Vaughan
        email                : greg@geospatial-services.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_mapactiontools import Ui_MapActionTools
# create the dialog for zoom to point
class MapActionToolsDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MapActionTools()
        self.ui.setupUi(self)
