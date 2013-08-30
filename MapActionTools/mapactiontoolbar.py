"""
/***************************************************************************
layerTools.py
                            
 Contains several classes to support MapAction QGIS plugins
                              -------------------
        begin                : 2012-10-09
        copyright            : (C) 2012 by Greg Vaughan
        email                : greg@geospatial-services.com
 ***************************************************************************/

"""

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from qgis.core import *
import sys
import os
import re
from datetime import datetime
from xml.dom.minidom import Document
from xml.dom.minidom import parse
import xml.parsers.expat
import urllib2
from datanametooldialog import DataNameTool

class LayerTools:
    def __init__(self, canvas, ui, layers=None, layer=None):
        self.canvas = canvas
        self.layers = self.canvas.layers()
        self.layer = layer
        self.ui = ui
    
    def setSelectedLayer(self, layers, cbo):                            
        for i in layers:
            if i.name() != cbo.currentText():
                continue
            else:
                self.layer = i
    
    #creates a list of layers in the table of content
    #Error with a mix of raster and vector layers ~~~
    
    ##Get layers from TOC and add them to a select combo box
    def getTocLayers(self, canvas):        
        allLayers = canvas.layers()      
        return allLayers

    def addTocLayersCBO(self, layers, cbo):
        cbo.clear()
        cbo.addItem("")
        for i in layers: cbo.addItem(i.name())            
    
    def getSelectedLayer(self, canvas, cbo, layer_list):                            
        for i in layer_list:
            if i.name() != cbo.currentText():
                continue
            else:
                layer = i
                return layer            
            
class Metadata:
    def __init__(self, layer, ui, dlg, feature_type=None, elements=None):
        self.layer = layer
        self.ui = ui
        self.dlg = dlg
        self.elements = elements
        self.feature_type = self.setFeatureType()
    
    def setFeatureType(self):
        if str(self.layerType(self.layer.type())) == 'Vector':
            return 'Vector'          
        else:
            return 'Raster' 
    
    ##Create the elements dictionary variable with the empty fields
    def createElements(self):
        self.elements = {}
        
        ##Elements from the layer
        if self.feature_type == 'Vector':
            self.elements['feature count'] = str(self.layer.featureCount())
            self.elements['storage type'] = str(self.layer.storageType())            
        else:
            self.elements['feature count'] = 'No value for raster layer'
            self.elements['storage type'] = 'No value for raster layer'            
        
        self.elements['name'] = str(self.layer.name())
        self.elements['path'] = str(self.layer.source())
        self.elements['type'] = str(self.layerType(self.layer.type()))
        self.elements['extension'] = str(self.layerExtension(self.layer.source()))
        self.elements['crs'] = str(self.layer.crs().description())
        self.elements['xMin'] = str(round(self.layer.extent().xMinimum(),2))
        self.elements['xMax'] = str(round(self.layer.extent().xMaximum(),2))
        self.elements['yMin'] = str(round(self.layer.extent().yMinimum(),2))
        self.elements['yMax'] = str(round(self.layer.extent().yMaximum(),2))
        #add geometry type for vectors
        
        ##Elements from the the user form
        self.elements['organisation'] = self.ui.txtOrganisation.text()
        self.elements['author'] = self.ui.txtAuthor.text()
        self.elements['email'] = self.ui.txtEmail.text()
        self.elements['www'] = self.ui.txtWWW.text()
        self.elements['description'] = self.ui.txtDescription.toPlainText()
        
    def layerType(self, type_enum):
            if type_enum == 0:
                    return 'Vector'
            elif type_enum == 1:
                    return 'raster'
            elif type_enum == 2:
                    return 'QGIS plugin layer'
            else:
                    return 'Layer type not recognised'
        
    def layerExtension(self, layerSource):
        s = str(layerSource)
        fileExtension = s.split('.', 1)[1]
        return fileExtension 
        
    def getMetadataParameterValues(self):
        #set up the variables 
        filename = os.path.basename(str(self.layer.source()))
        filename = filename[:-4]
        dir = os.path.dirname(str(self.layer.source())) + '/'
        #write the variables to the dictionary
        params = {}
        params['time'] = str(datetime.now().replace(microsecond=0))
        params['path'] = dir
        params['meta_name_text'] = filename + '_metadata.txt'
        params['meta_name_pdf'] = filename + '_metadata.pdf'
        params['meta_name_xml'] = filename + '_metadata.xml'
        #return the dictionary
        return params

    def writeMetaXmlFile(self):
        
        params = self.getMetadataParameterValues()
        
        doc = Document()
        # Create the <mapaction> base element
        ma = doc.createElement("mapaction")
        doc.appendChild(ma)
        # Create the main <deployment> element
        layer_node = doc.createElement("layer_metadata")
        ma.appendChild(layer_node)
        ##Create the elements and populate them from the deployment dialog
        for key in sorted(self.elements.iterkeys()):
            #create 2 temporary variables
            var1 = key
            var2 = key + '_txt'
            # Create the first element from the deployment dialog, value sourced from elements dictionary
            var1 = doc.createElement(str(key))
            layer_node.appendChild(var1)
            # Give the the above element its text value
            var2 = doc.createTextNode(str(self.elements[key]))
            var1.appendChild(var2)      

        ##create and write the output xml
        #get the path from the dialog
        f = open(params['path'] + params['meta_name_xml'], 'w')
        f.write(doc.toprettyxml(indent="  ", encoding = 'utf-8'))
        f.close()
        
    def writeMetaTextFile(self):

        params = self.getMetadataParameterValues()
        f = open(params['path'] + params['meta_name_text'], 'w')
        #write a metadata header
        f.write('**  Metadata created by MapAction\r\n**  ' + params['time'] + '\r\n**  www.mapaction.org/\r\n-----------------------------\r\n\r\n')
        #write the data values
        f.write('name: ' + self.elements['name'] + '\r\n')
        f.write('path: ' + self.elements['path'] + '\r\n')
        f.write('type: ' + self.elements['type'] + '\r\n')
        if self.feature_type == 'Vector':
            f.write('file type: ' + self.elements['storage type'] + '\r\n')
        f.write('extension: ' + self.elements['extension'] + '\r\n')
        if self.feature_type == 'Vector':
            f.write('feature count: ' + self.elements['feature count'] + '\r\n')   
        f.write('crs: ' + self.elements['crs'] + '\r\n')
        f.write('xMin: ' + self.elements['xMin'] + '\r\n')
        f.write('xMax: ' + self.elements['xMax'] + '\r\n')
        f.write('yMin: ' + self.elements['yMin'] + '\r\n')
        f.write('yMax: ' + self.elements['yMax'] + '\r\n')
        
        f.close()     

    def writeMetaPDFFile(self, path):
        test = '<tr><td> work? </td><td> Yes!</td></tr>'
        #get parameters
        params = self.getMetadataParameterValues()
        # Create a document object
        doc = QTextDocument()
        # Create a cursor pointing to the beginning of the document
        cursor = QTextCursor(doc)
        
        #create variables to hold values that are only present for vector layers
        if self.feature_type == 'Vector':
            feat_count = "<tr><td> Feature count </td><td> %s </td></tr>" % (self.elements['feature count'])
            storage_type = "<tr><td> File type </td><td> %s </td></tr>" % (self.elements['storage type'])
        else:
            feat_count = ''
            storage_type = ''

        #set up the HTML templage for values
        html_content = """
        <div style="margin-left: 115px;"><img src="%s\\icons\\mapaction.png" /></div>
        <div style="font-size: 14px; color: black;">
        <p><b><hr>
        Document:</b>
        <table border="0" cellspacing="7" cellpadding="0" style="color:black; margin-left: 5px; width="550"> 
            <tr><td> Created </td><td> %s </td></tr>
            <tr><td> Author </td><td> %s</td></tr>
            <tr><td> Email </td><td> %s </td></tr>
            <tr><td> Standard </td><td> Project Zebra </td></tr>
            <tr><td> Organisation </td><td> %s </td></tr>
            <tr><td> www </td><td> %s </td></tr>
            
        </table>
        <hr></p></div>
        
        <div style="font-size: 14px; color: black;">
        <p>
        <b>Metadata:</b>
        <table border="0" cellspacing="10" cellpadding="0" style="color:black; margin-left: 5px;" width="750" > 
            <!--<tr><th> Layer parameter </th><th>Value</th></tr>-->
            <tr><td> Layer </td><td> %s </td></tr>
            <tr><td> Path </td><td> %s </td></tr>
            <tr><td> Feature type</td><td> %s </td></tr>
            %s
            <tr><td> extension </td><td> %s </td></tr>
            <tr><td> CRS </td><td> %s </td></tr>
            <tr><td> Description </td><td> %s </td></tr>
            %s
            <tr><td> xMin </td><td> %s </td></tr>
            <tr><td> xMax </td><td> %s </td></tr>
            <tr><td> yMin </td><td> %s </td></tr>
            <tr><td> yMax </td><td> %s </td></tr>
        </table>
        </p>
        </div>
         """ % (path, params['time'],self.elements['author'],self.elements['email'], self.elements['organisation'],self.elements['www'], self.elements['name'], \
                self.elements['path'],self.elements['type'], storage_type, self.elements['extension'],  self.elements['crs'], self.elements['description'], \
                feat_count, self.elements['xMin'], self.elements['xMax'], self.elements['yMin'], self.elements['yMax'])
    
        cursor.insertHtml(html_content)        
        # Create a writer to save the document
        writer = QTextDocumentWriter()
        writer.supportedDocumentFormats()
        odf_format = writer.supportedDocumentFormats()[1]
        writer.setFormat(odf_format)
        #writer.setFileName('C:/gis/python/pdf/hello_world.odt')
        #writer.write(doc)
        print 'output complete'
        #create a printer object, set the print parameters and print the pdf to the file directory
        printer = QPrinter()
        printer.setResolution(96)
        printer.setPaperSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(params['path'] + params['meta_name_pdf'])
        doc.setPageSize(QSizeF(printer.pageRect().size()))
        doc.print_(printer)



class DeploymentXML:
    def __init__(self, dlg, elements=None):
        self.dlg = dlg
        self.layer = elements
        

    def setElements(self):
        self.elements = {}
        #populate the elements dictionary with the dialog values
        self.elements['01operation_name'] = self.dlg.ui.txtOperationName.text()
        self.elements['02operation_id'] = self.dlg.ui.txtOperationId.text()
        self.elements['03path_to_original_dir'] = self.dlg.ui.txtPath1Original.text()
        self.elements['04path_to_active_dir'] = self.dlg.ui.txtPath2Active.text()
        self.elements['05path_to_mapping_dir'] = self.dlg.ui.txtPath3Mapping.text()
        self.elements['06path_to_mxd_dir'] = self.dlg.ui.txtPathMxd.text()
        self.elements['07path_to_export_dir'] = self.dlg.ui.txtPathExportProducts.text()
        self.elements['08path_to_lyr_files_dir'] = self.dlg.ui.txtPathLayerStyles.text()
        self.elements['09sourceorg'] = self.dlg.ui.txtSourceOrganisation.text()
        self.elements['10default_languages'] = self.dlg.ui.txtDefaultLanguage.text()
        self.elements['11default_countries'] = self.dlg.ui.txtDefaultCountry.text()
        self.elements['12default_status'] = self.dlg.ui.txtDefaultMapStatus.text()
        self.elements['13default_jpgfilename_pattern'] = self.dlg.ui.txtDefaultJpegFilePattern.text()
        self.elements['14default_pdffilename_pattern'] = self.dlg.ui.txtDefaultPdfFilePattern.text()
        self.elements['15default_qclevel'] = self.dlg.ui.txtDefaultQcLevel.text()
        self.elements['16glideno'] = self.dlg.ui.txtGlideNo.text()
        self.elements['17default_Jpgresolutiondpi'] = self.dlg.ui.txtDefaultJpegDpi.text()
        self.elements['18default_Pdfresolutiondpi'] = self.dlg.ui.txtDefaultPdfDpi.text()
        self.elements['19default_Kmzfilename_pattern'] = self.dlg.ui.txtDefaultKmzFilePattern.text()
        self.elements['20default_point_of_contact'] = self.dlg.ui.txtPointContact.text()
        self.elements['21default_metadata_contact'] = self.dlg.ui.txtMetadataContact.text()

    def createXML(self):
        # Create the minidom document
        doc = Document()
        # Create the <mapaction> base element
        ma = doc.createElement("mapaction")
        doc.appendChild(ma)
        # Create the main <deployment> element
        deploy = doc.createElement("deploy_config")
        ma.appendChild(deploy)
        
        ##Create the elements and populate them from the deployment dialog
        for key in sorted(self.elements.iterkeys()):
            #create 2 temporary variables
            var1 = key
            var2 = key + '_txt'
            # Create the first element from the deployment dialog, value sourced from elements dictionary
            var1 = doc.createElement(str(key)[2:])
            deploy.appendChild(var1)
            # Give the the above element its text value
            var2 = doc.createTextNode(str(self.elements[key]))
            var1.appendChild(var2)      

        ##create and write the output xml
        #get the path from the dialog
        path = self.dlg.ui.txtNewFilePath.text()
        try:
            f = open(path + '\deployment_config.xml', 'w')
            f.write(doc.toprettyxml(indent="  ", encoding = 'utf-8'))
            f.close()
        except IOError as err:
            QMessageBox.warning(self.dlg, 'Permission error', "File not saved. Please make sure you have permissions to write to the path: " + path)

    def getXmlFromURL(self):
        if self.dlg.ui.txtConnectConfigUrl.text() == '':
            QMessageBox.warning(self.dlg, 'URL missing', "Please enter the URL to deployment configuration file.")
        else:
            url = str(self.dlg.ui.txtConnectConfigUrl.text())
            try:
                con = urllib2.urlopen(url)
            except urllib2.HTTPError, e:
                 QMessageBox.warning(self.dlg, 'HTTP error', "There has been a HTTP error")
                 return
            except urllib2.URLError, e:
                 QMessageBox.warning(self.dlg, 'URL error', "There is a problem with the URL.")
                 return
            except ValueError:
                 QMessageBox.warning(self.dlg, 'Value error', "There is a problem with the URL.")
                 return
            else:
                try:
                    xmldoc = parse(con)
                except xml.parsers.expat.ExpatError:
                    QMessageBox.warning(self.dlg, 'Xml parse error', "There is a problem with the URL.")
                    return
                except UnboundLocalError:
                    QMessageBox.warning(self.dlg, 'Unbound error', "This url is not correct, please try another.")
                    return
                else: 
                    con.close()
                    operation_name = str(xmldoc.getElementsByTagName('operation_name')[0].firstChild.nodeValue).strip()
                    operation_id = str(xmldoc.getElementsByTagName('operation_id')[0].firstChild.nodeValue).strip()
                    path_to_original_dir = str(xmldoc.getElementsByTagName('path_to_original_dir')[0].firstChild.nodeValue).strip()
                    path_to_active_dir = str(xmldoc.getElementsByTagName('path_to_active_dir')[0].firstChild.nodeValue).strip()
                    path_to_mapping_dir = str(xmldoc.getElementsByTagName('path_to_mapping_dir')[0].firstChild.nodeValue).strip()
                    path_to_mxd_dir = str(xmldoc.getElementsByTagName('path_to_mxd_dir')[0].firstChild.nodeValue).strip()
                    path_to_export_dir = str(xmldoc.getElementsByTagName('path_to_export_dir')[0].firstChild.nodeValue).strip()
                    path_to_lyr_files_dir = str(xmldoc.getElementsByTagName('path_to_lyr_files_dir')[0].firstChild.nodeValue).strip()
                    sourceorg = str(xmldoc.getElementsByTagName('sourceorg')[0].firstChild.nodeValue).strip()
                    default_languages = str(xmldoc.getElementsByTagName('default_languages')[0].firstChild.nodeValue).strip()
                    default_countries = str(xmldoc.getElementsByTagName('default_countries')[0].firstChild.nodeValue).strip()
                    default_status = str(xmldoc.getElementsByTagName('default_status')[0].firstChild.nodeValue).strip()
                    default_jpgfilename_pattern = str(xmldoc.getElementsByTagName('default_jpgfilename_pattern')[0].firstChild.nodeValue).strip()
                    default_pdffilename_pattern = str(xmldoc.getElementsByTagName('default_pdffilename_pattern')[0].firstChild.nodeValue).strip()
                    default_qclevel = str(xmldoc.getElementsByTagName('default_qclevel')[0].firstChild.nodeValue).strip()
                    glideno = str(xmldoc.getElementsByTagName('glideno')[0].firstChild.nodeValue).strip()
                    default_Jpgresolutiondpi = str(xmldoc.getElementsByTagName('default_Jpgresolutiondpi')[0].firstChild.nodeValue).strip()
                    default_Pdfresolutiondpi = str(xmldoc.getElementsByTagName('default_Pdfresolutiondpi')[0].firstChild.nodeValue).strip()
                    default_Kmzfilename_pattern = str(xmldoc.getElementsByTagName('default_Kmzfilename_pattern')[0].firstChild.nodeValue).strip()
                    default_point_of_contact = str(xmldoc.getElementsByTagName('default_point_of_contact')[0].firstChild.nodeValue).strip()
                    default_metadata_contact = str(xmldoc.getElementsByTagName('default_metadata_contact')[0].firstChild.nodeValue).strip()
                    
                    self.dlg.ui.txtOperationName.setText(operation_name)
                    self.dlg.ui.txtOperationId.setText(operation_id)
                    self.dlg.ui.txtPath1Original.setText(path_to_original_dir)
                    self.dlg.ui.txtPath2Active.setText(path_to_active_dir)
                    self.dlg.ui.txtPath3Mapping.setText(path_to_mapping_dir)
                    self.dlg.ui.txtPathMxd.setText(path_to_mxd_dir)
                    self.dlg.ui.txtPathExportProducts.setText(path_to_export_dir)
                    self.dlg.ui.txtPathLayerStyles.setText(path_to_lyr_files_dir)
                    self.dlg.ui.txtSourceOrganisation.setText(sourceorg)
                    self.dlg.ui.txtDefaultLanguage.setText(default_languages)
                    self.dlg.ui.txtDefaultCountry.setText(default_countries)
                    self.dlg.ui.txtDefaultMapStatus.setText(default_status)
                    self.dlg.ui.txtDefaultJpegFilePattern.setText(default_jpgfilename_pattern)
                    self.dlg.ui.txtDefaultPdfFilePattern.setText(default_pdffilename_pattern)
                    self.dlg.ui.txtDefaultQcLevel.setText(default_qclevel)
                    self.dlg.ui.txtGlideNo.setText(glideno)
                    self.dlg.ui.txtDefaultJpegDpi.setText(default_Jpgresolutiondpi)
                    self.dlg.ui.txtDefaultPdfDpi.setText(default_Pdfresolutiondpi)
                    self.dlg.ui.txtDefaultKmzFilePattern.setText(default_Kmzfilename_pattern)
                    self.dlg.ui.txtPointContact.setText(default_point_of_contact)
                    self.dlg.ui.txtMetadataContact.setText(default_metadata_contact)
            
       
class ToolbarConfig:
    def __init__(self, ui, path, elements=None):
        self.ui = ui
        self.path = path
        self.layer = elements
        

    def setElements(self):
        self.elements = {}
        #populate the elements dictionary with the dialog values
        self.elements['01firstname'] = self.ui.txtFirstName.text()
        self.elements['02surname'] = self.ui.txtSurname.text()
        self.elements['03organisation'] = self.ui.txtOrganisation.text()
        self.elements['04email'] = self.ui.txtEmail.text()
        self.elements['05www'] = self.ui.txtWWW.text()
        self.elements['03defaultpath'] = self.ui.txtDefaultPath.text()
        self.elements['01deployconfigpath'] = self.ui.txtDeployConfigPath.text()

    def createXML(self):
        # Create the minidom document
        doc = Document()
        # Create the <mapaction> base element
        ma = doc.createElement("mapaction")
        doc.appendChild(ma)
        # Create the main <deployment> element
        toolbar = doc.createElement("toolbar_config")
        ma.appendChild(toolbar)
        
        ##Create the elements and populate them from the deployment dialog
        for key in sorted(self.elements.iterkeys()):
            #create 2 temporary variables
            var1 = key
            var2 = key + '_txt'
            # Create the first element from the deployment dialog, value sourced from elements dictionary
            var1 = doc.createElement(str(key)[2:])
            toolbar.appendChild(var1)
            # Give the the above element its text value
            var2 = doc.createTextNode(str(self.elements[key]))
            var1.appendChild(var2)      

        ##create and write the output xml
        #get the path from the dialog
        f = open(self.path + '/config/toolbar_config.xml', 'w')
        f.write(doc.toprettyxml(indent="  ", encoding = 'utf-8'))
        f.close()
        
    def findUpdateXML(self):
        #parse toolbar config xml
        dom = parse(self.path + '/config/toolbar_config.xml')
        #storge xml node value for each nodes in a variable, first removing any whitespace using re.sub
        firstname = str(dom.getElementsByTagName('firstname')[0].firstChild.nodeValue).strip()
        surname = str(dom.getElementsByTagName('surname')[0].firstChild.nodeValue).strip()
        organisation = str(dom.getElementsByTagName('organisation')[0].firstChild.nodeValue).strip()
        email = str(dom.getElementsByTagName('email')[0].firstChild.nodeValue).strip()
        www = str(dom.getElementsByTagName('www')[0].firstChild.nodeValue).strip()
        defaultpath = str(dom.getElementsByTagName('defaultpath')[0].firstChild.nodeValue).strip()
        deployconfigpath = str(dom.getElementsByTagName('deployconfigpath')[0].firstChild.nodeValue).strip()
        
        #set the text in the dialog to the variables above
        self.ui.txtFirstName.setText(firstname)
        self.ui.txtSurname.setText(surname)
        self.ui.txtOrganisation.setText(organisation)
        self.ui.txtEmail.setText(email)
        self.ui.txtWWW.setText(www)
        self.ui.txtDefaultPath.setText(defaultpath)
        self.ui.txtDeployConfigPath.setText(deployconfigpath)

class DataNameMethods:
   #class variables 
    def __init__(self, path):
       #self.dlg = dlg
       self.path = path
    
    #add values to each of the combo boxes from the lookup folder in the plugin 
    def populateCbo(self, y, z):        
        y.clear()        
        path = self.path + "\\lookup\\" + z        
        file = open( path, "r" )
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
    

        
        