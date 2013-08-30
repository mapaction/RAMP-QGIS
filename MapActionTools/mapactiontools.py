"""
/***************************************************************************
MapActionTools                           -------------------
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from qgis.core import *
import sys
import os
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
#from mapactiontoolsdialog import MapActionToolsDialog
from deploymentxmltooldialog import DeploymentXmlTool
from layermetadatatooldialog import LayerMetadataTool
from toolbarconfigtooldialog import ToolbarConfigTool
from datanametooldialog import DataNameTool
# Import custom pyqgis classes
from mapactiontoolbar import *

class MapActionTools:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_path = os.path.abspath(__file__)        
        self.plugin_dir = os.path.dirname(self.plugin_path)
        self.tools = None

    def initGui(self):
        # Create action that will start plugin configuration
        
        self.action = QAction(QIcon(":/plugins/MapActionTools/icons/tools.png"), \
        "MapAction Message", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        
        self.configTool = QAction(QIcon(self.plugin_dir+"\\icons\\config_tool.png"),
        "Toolbar Configuration", self.iface.mainWindow())
        
        self.metaTool = QAction(QIcon(self.plugin_dir+"\\icons\\meta_tool.png"), \
        "Layer Metadata Tool", self.iface.mainWindow())
        
        self.nameTool= QAction(QIcon(self.plugin_dir+"\\icons\\name_tool.png"), \
        "Data Name Tool", self.iface.mainWindow())
        
        self.deployXMLTool= QAction(QIcon(self.plugin_dir+"\\icons\\depxml_tool.png"), \
        "Deployment XML Tool", self.iface.mainWindow())
        
        # connect the action to the run method
        QObject.connect(self.configTool, SIGNAL("triggered()"), self.launchToolbarConfigTool)
        QObject.connect(self.metaTool, SIGNAL("triggered()"), self.launchLayerMetadataTool)
        QObject.connect(self.nameTool, SIGNAL("triggered()"), self.launchDataNameTool)
        QObject.connect(self.deployXMLTool, SIGNAL("triggered()"), self.launchDeploymentXMLTool)

        # Add toolbar button and menu item
        
        self.iface.addPluginToMenu("&MapAction Tools", self.configTool)
        self.iface.addPluginToMenu("&MapAction Tools", self.metaTool)
        self.iface.addPluginToMenu("&MapAction Tools", self.nameTool)
        self.iface.addPluginToMenu("&MapAction Tools", self.deployXMLTool)

        self.toolBar = self.iface.addToolBar(QCoreApplication.translate("MapAction Tools", "MapAction Tools"))
        self.toolBar.setObjectName(QCoreApplication.translate("MapAction Tools", "MapAction Tools"))
        
        self.toolBar.addAction(self.configTool)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.metaTool)
        
        self.toolBar.addAction(self.nameTool)
        
        self.toolBar.addAction(self.deployXMLTool)
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&MapAction Tools",self.configTool)
        self.iface.removeToolBarIcon(self.configTool)
        self.iface.removePluginMenu("&MapAction Tools",self.metaTool)
        self.iface.removeToolBarIcon(self.metaTool)
        self.iface.removePluginMenu("&MapAction Tools",self.nameTool)
        self.iface.removeToolBarIcon(self.nameTool)
        self.iface.removePluginMenu("&MapAction Tools",self.deployXMLTool)
        self.iface.removeToolBarIcon(self.deployXMLTool)
        
        
        del self.toolBar
    # run method that performs all the real work
    def run(self):

        # create and show the dialog
        self.dlg = MapActionToolsDialog()
        # show the dialog
        self.dlg.show()
    
    #===========================================================================
    # Toolbar configuration tool dialog and methods
    # 
    # 
    #===========================================================================
    def launchToolbarConfigTool(self):
        self.dlg = ToolbarConfigTool()
        if os.path.isfile(self.plugin_dir + '/config/toolbar_config.xml') == True:
            toolbar_config = ToolbarConfig(self.dlg.ui, self.plugin_dir)
            toolbar_config.findUpdateXML()
            self.dlg.ui.btnCreateSave.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Save", None, QtGui.QApplication.UnicodeUTF8))
            #self.dlg.ui.btnCreateSave.label.setText('Save')
        
        QObject.connect(self.dlg.ui.btnCreateSave, SIGNAL('clicked()'), self.createToolbarConfigXML)
        QObject.connect(self.dlg.ui.btnCancel, SIGNAL('clicked()'), self.closeDialog)
        QObject.connect(self.dlg.ui.btnDefaultPath, SIGNAL('clicked()'), self.getToolbarConfigDefaultPathDir)
        QObject.connect(self.dlg.ui.btnDeployConfigPath, SIGNAL('clicked()'), self.getToolbarConfigDeployPathDir)
        # show the dialog
        self.dlg.exec_()
        
    def createToolbarConfigXML(self):     
        toolbar_config = ToolbarConfig(self.dlg.ui, self.plugin_dir)
        toolbar_config.setElements()
        toolbar_config.createXML()
        self.closeDialog()
        
    def getToolbarConfigDefaultPathDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self.dlg,'Set Directory','c:\\',QtGui.QFileDialog.ShowDirsOnly)
        self.dlg.ui.txtDefaultPath.setText(dirname)
    
    def getToolbarConfigDeployPathDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self.dlg,'Set Directory','c:\\',QtGui.QFileDialog.ShowDirsOnly)
        self.dlg.ui.txtDeployConfigPath.setText(dirname)

    #===========================================================================
    # Deployment XML generator tool methods
    # 
    # 
    #===========================================================================
    
    def launchDeploymentXMLTool(self):
        self.dlg = DeploymentXmlTool()
        QObject.connect(self.dlg.ui.btnCancel, SIGNAL('clicked()'), self.closeDialog)
        #QObject.connect(self.dlg.ui.radbtnEditExistingFile, SIGNAL("clicked(bool)"), self.radioButtonSelect)
        QObject.connect(self.dlg.ui.btnCreateSave, SIGNAL('clicked()'), self.createXML)
        QObject.connect(self.dlg.ui.btnNewFilePathDir, SIGNAL('clicked()'), self.getDeployConfigDir)
        QObject.connect(self.dlg.ui.btnPath1Original, SIGNAL('clicked()'), self.getPath1OriginalDir)
        QObject.connect(self.dlg.ui.btnPath2Active, SIGNAL('clicked()'), self.getPath2ActiveDir)
        QObject.connect(self.dlg.ui.btnPath3Mapping, SIGNAL('clicked()'), self.getPath3MappingDir)
        QObject.connect(self.dlg.ui.btnPathMxd, SIGNAL('clicked()'), self.getPathMxdDir)
        QObject.connect(self.dlg.ui.btnConnectConfigUrl, SIGNAL('clicked()'), self.launchUrlConnection)
    
        # show the dialog
        self.dlg.exec_()
    
    def createXML(self):
        if os.path.isdir(self.dlg.ui.txtNewFilePath.text()) != True:
            QMessageBox.warning(self.dlg, 'Directory not valid', "Please choose a valid directory to save the file.")
        else:      
            deploy = DeploymentXML(self.dlg)
            deploy.setElements()
            deploy.createXML()
            self.closeDialog()
    
    def launchUrlConnection(self):
        deploy_url = DeploymentXML(self.dlg)
        deploy_url.getXmlFromURL()
        
    
    #Disable the other option on the dialog between existing / create new file options        
    def radioButtonSelect(self):
        self.dlg.ui.txtNewFilePath.setEnabled(False)
        self.dlg.ui.txtExistingFilePath.setEnabled(True)

    def getDeployConfigDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self.dlg,'Set Directory','c:\\',QtGui.QFileDialog.ShowDirsOnly)
        self.dlg.ui.txtNewFilePath.setText(dirname)
    
    def getPath1OriginalDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self.dlg,'Set Directory','c:\\',QtGui.QFileDialog.ShowDirsOnly)
        self.dlg.ui.txtPath1Original.setText(dirname)    

    def getPath2ActiveDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self.dlg,'Set Directory','c:\\',QtGui.QFileDialog.ShowDirsOnly)
        self.dlg.ui.txtPath2Active.setText(dirname)     

    def getPath3MappingDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self.dlg,'Set Directory','c:\\',QtGui.QFileDialog.ShowDirsOnly)
        self.dlg.ui.txtPath3Mapping.setText(dirname) 

    def getPathMxdDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self.dlg,'Set Directory','c:\\',QtGui.QFileDialog.ShowDirsOnly)
        self.dlg.ui.txtPathMxd.setText(dirname) 
    
    
    #===========================================================================
    # Layer metadtatool dialog and methods
    # 
    # 
    #===========================================================================
    
    def launchLayerMetadataTool(self):
        self.dlg = LayerMetadataTool()
        
        self.tools = LayerTools(self.iface.mapCanvas(), self.dlg.ui)
        self.tools.addTocLayersCBO(self.tools.layers, self.tools.ui.cboTocLayers)
        
        QObject.connect(self.dlg.ui.btnCancel, SIGNAL('clicked()'), self.closeDialog)
        QObject.connect(self.dlg.ui.btnCreateMetadata, SIGNAL('clicked()'), self.launchMetadataCreation)
        QObject.connect(self.dlg.ui.btnUpdateFromToolbarConfig, SIGNAL('clicked()'), self.updateValuesFromCongif)
        #QObject.connect(self.dlg.ui.btnCreateMetadata, SIGNAL('clicked()'), self.showDialog)
        self.dlg.exec_()
        #QObject.connect(self.dlgLayMeta.ui.btnCreateMetadata, SIGNAL('clicked()'), self.createMetadata)

    def launchMetadataCreation(self):
        #create metadata using Metadata class
        if self.dlg.ui.cboTocLayers.currentText() == "":
            QMessageBox.warning(self.dlg, "Layer not selected", "Please select a layer from the list.")
        else:
            if self.dlg.ui.chkOutputTXT.isChecked() != True and self.dlg.ui.chkOutputXML.isChecked() != True and self.dlg.ui.chkOutputPDF.isChecked() != True:
                QMessageBox.warning(self.dlg, "Output format", "Please select on or more output formats from xml, text or pdf.")
            else:
                #Get the selected layer variable
                self.tools.setSelectedLayer(self.tools.layers, self.tools.ui.cboTocLayers)
                if self.dlg.ui.chkOutputTXT.isChecked() == True:
                    self.createTXTMetadata()
                    
                if self.dlg.ui.chkOutputXML.isChecked() == True:
                    self.createXMLMetadata()
                    
                if self.dlg.ui.chkOutputPDF.isChecked() == True:
                    self.createPDFMetadata()
            
    def createTXTMetadata(self):
        meta = Metadata(self.tools.layer, self.tools.ui, self.dlg)
        meta.createElements()
        meta.writeMetaTextFile()
        self.closeDialog()

    def createXMLMetadata(self):
        meta = Metadata(self.tools.layer, self.tools.ui, self.dlg)
        meta.createElements()
        meta.writeMetaXmlFile()
        self.closeDialog()

    def createPDFMetadata(self):
        meta = Metadata(self.tools.layer, self.tools.ui, self.dlg)
        meta.createElements()
        meta.writeMetaPDFFile(self.plugin_dir)
        self.closeDialog()

    def updateValuesFromCongif(self):
        #check toolbar config exists
        if os.path.isfile(self.plugin_dir + '/config/toolbar_config.xml') != True:
            QMessageBox.warning(self.dlg, 'Config file missing', "A toolbar configuration file has not yet been created. Please create one first using the MapAction Toolbar. You can still enter the values manually below.")
            return
        
        dom = parse(self.plugin_dir + '/config/toolbar_config.xml')
         #storge xml node value for each nodes in a variable, first removing any whitespace using re.sub
        firstname = str(dom.getElementsByTagName('firstname')[0].firstChild.nodeValue).strip()
        surname = str(dom.getElementsByTagName('surname')[0].firstChild.nodeValue).strip()
        organisation = str(dom.getElementsByTagName('organisation')[0].firstChild.nodeValue).strip()
        email = str(dom.getElementsByTagName('email')[0].firstChild.nodeValue).strip()
        www = str(dom.getElementsByTagName('www')[0].firstChild.nodeValue).strip()
        #set the text in the dialog to the variables above
        self.dlg.ui.txtAuthor.setText(firstname + ' ' + surname)
        self.dlg.ui.txtOrganisation.setText(organisation)
        self.dlg.ui.txtEmail.setText(email)
        self.dlg.ui.txtWWW.setText(www)
        
    #===========================================================================
    # Data name tool constructor and methods
    # 
    # 
    #===========================================================================
    def launchDataNameTool(self):
        #dnt = DataNameTool()
        #dnt.constructor()

        self.dlg = DataNameTool()
        
        self.populateCbo(self.dlg.ui.cboGeoExtent, "geoextent.csv")
        self.populateCbo(self.dlg.ui.cboDataCategory, "category.csv")
        self.populateCbo(self.dlg.ui.cboDataTheme, "theme.csv")
        self.populateCbo(self.dlg.ui.cboDataType, "type.csv")
        self.populateCbo(self.dlg.ui.cboScale, "scale.csv")
        self.populateCbo(self.dlg.ui.cboSource, "source.csv")
        self.populateCbo(self.dlg.ui.cboPermission, "permission.csv")
         
        tools = LayerTools(self.iface.mapCanvas(), self.dlg.ui)
        tools.addTocLayersCBO(tools.layers, tools.ui.cboTocLayers)      
        
        #Button to check the layer name before saving
        QObject.connect(self.dlg.ui.btnCheckName, SIGNAL('clicked()'), self.callValidateName)   
        
        QObject.connect(self.dlg.ui.btnSaveShapefile, SIGNAL('clicked()'), self.saveShapefile)
        QObject.connect(self.dlg.ui.btnCancel, SIGNAL('clicked()'), self.closeDialog)
        QObject.connect(self.dlg.ui.btnGetDirectory, SIGNAL('clicked()'), self.getDirectory)
        #Form checkbox connections
        QObject.connect(self.dlg.ui.chkGeoExtent, SIGNAL("clicked(bool)"), self.geoState)
        QObject.connect(self.dlg.ui.chkDataCategory, SIGNAL("clicked(bool)"), self.catState)
        QObject.connect(self.dlg.ui.chkDataTheme, SIGNAL("clicked(bool)"), self.themeState)
        QObject.connect(self.dlg.ui.chkDataType, SIGNAL("clicked(bool)"), self.typeState)
        QObject.connect(self.dlg.ui.chkScale, SIGNAL("clicked(bool)"), self.scaleState)
        QObject.connect(self.dlg.ui.chkSource, SIGNAL("clicked(bool)"), self.sourceState)
        QObject.connect(self.dlg.ui.chkPermission, SIGNAL("clicked(bool)"), self.perState)
        
        self.dlg.exec_()

    def populateCbo(self, y, z):        
        y.clear()        
        path = self.plugin_dir + "\\lookup\\" + z        
        file = open(path, "r" )
        array = []
        for line in file:
            array.append(line.strip())
        file.close()   
        
        country = []
        dic = {}
        for x in array:
            key, value = x.split(',')
            dic[key] = value
            
        for key in dic.keys():
            country.append(dic[key])
        
        country.sort() 
        for item in country: y.addItem(item)  

    def saveShapefile_(self):        
        directory = self.dlg.ui.txtDirectory.text()       
        name = self.dlg.ui.cboGeoExtent.currentText()
        path = "C:\gis\data\Australia.shp"
        save_path = directory + "\\" + name + ".shp"
        
        provider = "ogr"
        layer = QgsVectorLayer(path, name, provider)
        
        error = QgsVectorFileWriter.writeAsVectorFormat(layer, save_path, "CP1250", None, "ESRI Shapefile")
        str_msg = "New layer successfully created: " + name + ".shp"
        
        if error == QgsVectorFileWriter.NoError:
          QMessageBox.information(self.dlg, 'Save shapefile', str_msg)
        else:
          QMessageBox.information(self.dlg, 'Save shapefile',"Try again.")
        #QgsVectorFileWriter.writeAsVectorFormat(layer, "my_shapes.shp", "CP1250", None, "ESRI Shapefile")
 
    def getDirectory(self):      
        dirname=QtGui.QFileDialog.getExistingDirectory(self.dlg,'Get Directory','c:\\',QtGui.QFileDialog.ShowDirsOnly)
        self.dlg.ui.txtDirectory.setText(dirname) 
        
    #Enables / disables the parameter drop down or free text field depending on the state of the checkbox
    def geoState(self):   
        #chkGeoExtent
        self.checkState(self.dlg.ui.cboGeoExtent, self.dlg.ui.chkGeoExtent, self.dlg.ui.txtGeoExtent, self.populateCbo(self.dlg.ui.cboGeoExtent, "geoextent.csv")) 
 
    def catState(self):   
        #chkGeoExtent
        self.checkState(self.dlg.ui.cboDataCategory, self.dlg.ui.chkDataCategory, self.dlg.ui.txtDataCategory, self.populateCbo(self.dlg.ui.cboDataCategory, "category.csv")) 
   
    def themeState(self):   
        #chkGeoExtent
        self.checkState(self.dlg.ui.cboDataTheme, self.dlg.ui.chkDataTheme, self.dlg.ui.txtDataTheme, self.populateCbo(self.dlg.ui.cboDataTheme, "theme.csv")) 
 
    def typeState(self):   
        #chkGeoExtent
        self.checkState(self.dlg.ui.cboDataType, self.dlg.ui.chkDataType, self.dlg.ui.txtDataType, self.populateCbo(self.dlg.ui.cboDataType, "type.csv")) 
   
    def scaleState(self):   
        #chkGeoExtent
        self.checkState(self.dlg.ui.cboScale, self.dlg.ui.chkScale, self.dlg.ui.txtScale, self.populateCbo(self.dlg.ui.cboScale, "scale.csv")) 
 
    def sourceState(self):   
        #chkGeoExtent
        self.checkState(self.dlg.ui.cboSource, self.dlg.ui.chkSource, self.dlg.ui.txtSource, self.populateCbo(self.dlg.ui.cboSource, "source.csv"))
        
    def perState(self):   
        #chkGeoExtent
        self.checkState(self.dlg.ui.cboPermission, self.dlg.ui.chkPermission, self.dlg.ui.txtPermission, self.populateCbo(self.dlg.ui.cboPermission, "permission.csv"))      

    #Enables / disables the parameter drop down or free text field depending on the state of the checkbox
    def checkState(self, cbo, chk, txt, cboValues):   
        #chkGeoExtent
        if chk.isChecked() == True:
            cbo.clear()
            cbo.setEnabled(False)
            txt.setEnabled(True)
        elif chk.isChecked() == False:      
            cbo.setEnabled(True)
            cboValues
            txt.clear()
            txt.setEnabled(False)  

    #Simply calls the validate name function and passes a parameter as this cannot be done on the button initialisation call above. 
    def callValidateName(self):      
        self.validateName(self.layerNewName())
        
    #gets the values for each parameter, processes them
    #determines if all parameters criteria have been met and returns the result on the 'Validate' click event
    def layerNewName(self):      
        geo = self.cboOrChk(self.dlg.ui.cboGeoExtent, self.dlg.ui.chkGeoExtent, self.dlg.ui.txtGeoExtent, "geoextent.csv")
        cat = self.cboOrChk(self.dlg.ui.cboDataCategory, self.dlg.ui.chkDataCategory, self.dlg.ui.txtDataCategory,"category.csv")
        theme = self.cboOrChk(self.dlg.ui.cboDataTheme, self.dlg.ui.chkDataTheme, self.dlg.ui.txtDataTheme, "theme.csv")
        type_ = self.cboOrChk(self.dlg.ui.cboDataType, self.dlg.ui.chkDataType, self.dlg.ui.txtDataType, "type.csv")
        scale = self.cboOrChk(self.dlg.ui.cboScale, self.dlg.ui.chkScale, self.dlg.ui.txtScale, "scale.csv")
        source = self.cboOrChk(self.dlg.ui.cboSource, self.dlg.ui.chkSource, self.dlg.ui.txtSource, "source.csv")
        perm = self.cboOrChk(self.dlg.ui.cboPermission, self.dlg.ui.chkPermission, self.dlg.ui.txtPermission, "permission.csv")
        f_text = self.dlg.ui.txtFreeText.displayText()
        
        #if discretionary variables are left blank remove underscores
        #scale
        if scale == "":
            scale = "_"
        else:
            scale = "_" + scale + "_"
        #permission
        if perm == "":
            perm = ""
        else:
            perm = "_" + perm
            
        if f_text == "":
            f_text = ""
        else:
            f_text = "_" + f_text
            
        layerName = geo + "_" + cat + "_" + theme + "_" + type_ + "_" + cat + scale + source + perm + f_text + ".shp"
        return layerName

    def validateName(self, layerNewName):       
        null = self.numberMandatoryNull()    
        strName = str(null)   
        
        nullIntro = " mandatory parameter(s) still require a value."
        
        if null > 0:
            QMessageBox.information(self.dlg, 'Parameter required', strName + nullIntro) 
        else:
            QMessageBox.information(self.dlg, 'New layer name', self.layerNewName())
    
    def numberMandatoryNull(self):
        geo = self.cboOrChk(self.dlg.ui.cboGeoExtent, self.dlg.ui.chkGeoExtent, self.dlg.ui.txtGeoExtent, "geoextent.csv")
        cat = self.cboOrChk(self.dlg.ui.cboDataCategory, self.dlg.ui.chkDataCategory, self.dlg.ui.txtDataCategory,"category.csv")
        theme = self.cboOrChk(self.dlg.ui.cboDataTheme, self.dlg.ui.chkDataTheme, self.dlg.ui.txtDataTheme, "theme.csv")
        type_ = self.cboOrChk(self.dlg.ui.cboDataType, self.dlg.ui.chkDataType, self.dlg.ui.txtDataType, "type.csv")
        source = self.cboOrChk(self.dlg.ui.cboSource, self.dlg.ui.chkSource, self.dlg.ui.txtSource, "source.csv")
        
        null = self.checkDataNull(geo, cat, theme, type_, source)      
        return null     
    
    #values in lookup tables are stored in a dictionary - this returns the value for a given key
    def dictValueKey(self, lookup, key_value ):
        path = self.plugin_dir + "\\lookup\\" + lookup        
        file = open(path, "r" )
        array = []
        for line in file:
            array.append(line.strip())
        file.close()   
        
        dic = {}
        for x in array:
            key, value = x.split(',')
            dic[value] = key
    
        return dic[key_value]
        
    #Assign name variable for each parameter depending on whether the combobox or textbox was used
    def cboOrChk(self, cbo, chk, txt, lookup):
        #value = ""        
        if chk.isChecked() == True:
            value = txt.displayText()
        elif chk.isChecked() == False:
            value = self.dictValueKey(lookup, str(cbo.currentText()))
        
        return value
    
    #check mandatory fields are filled out
    def checkDataNull(self, geo, cat, theme, type_, source):
        null = 0        
        array = [geo, cat, theme, type_, source]        
        for x in array:
            if x == "":
                null += 1
    
        return null
    #check discretionary fields are filled out  
    #def checkDataNull(self, scale, perm, f_text):
     #   for each 

    def saveShapefile(self): 
        
        tools = LayerTools(self.iface.mapCanvas(), self.dlg.ui)
                      
        null = self.numberMandatoryNull()
                
        if self.dlg.ui.cboTocLayers.currentText() == "":
            QMessageBox.warning(self.dlg, 'Layer missing', "Select a layer in Step 1 to rename")
        elif null > 0:
            QMessageBox.warning(self.dlg, 'Parameters missing', "Parameters are missing in Step 2")
        elif self.dlg.ui.txtDirectory.text() == "":
            QMessageBox.warning(self.dlg, 'Directory missing', "Select a directory in Step 3")
        else:
            name = self.layerNewName()
            directory = self.dlg.ui.txtDirectory.text() + "\\" + name
            #layer = self.getSelectedLayer()
            layer = tools.getSelectedLayer(tools.canvas, tools.ui.cboTocLayers, tools.layers)
            #provider = "shp"
            #layer_add = QgsVectorLayer(directory, name, provider)
            #if not layer_add.isValid():
            #  raise IOError, "Failed to open the layer"
            error = QgsVectorFileWriter.writeAsVectorFormat(layer, directory, "utf-8", None, "ESRI Shapefile")
            str_msg = "New layer successfully created: " + name
            if error == QgsVectorFileWriter.NoError:
              QMessageBox.information(self.dlg, 'Save shapefile', str_msg)
              #QgsMapLayerRegistry.instance().addMapLayer(layer_add)
              if self.dlg.ui.chkAddMapLayer.isChecked() == True:             
                self.addLayer()
                self.dlg.close()
              else: 
                self.dlg.close()
            else:
              QMessageBox.information(self.dlg, 'Save shapefile',"Try again.") 
        
        
    def getSelectedLayer(self):                
        canvas = self.iface.mapCanvas()
        allLayers = canvas.layers()      
        
        for i in allLayers:
            if i.name() != self.dlg.ui.cboTocLayers.currentText():
                continue
            else:
                layer = i
                return layer
            
    def addLayer(self):
        name = self.layerNewName()
        pre_dir = self.dlg.ui.txtDirectory.text()
        path = pre_dir + "\\" + name      
        provider = "ogr"
        layer_add = QgsVectorLayer(path, name, provider)
        if not layer_add.isValid():
          raise IOError, "Failed to open the layer"
        QgsMapLayerRegistry.instance().addMapLayer(layer_add)


    #===========================================================================
    # common methods for all dialogs
    # 
    # 
    #===========================================================================
 
    def closeDialog(self): 
        self.dlg.close()   
        
  
    
        