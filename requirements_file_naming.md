# QGIS Plugin Requirements: File Naming #
## Purpose ##
Where vector and raster files are stored in a pre-determined folder hierarchy, and filenames are structured, this plugin supports users in saving data to the correct folder with the correct filename. This supports effective data management and selection of appropriate data for use in mapping products, particularly where data structures are shared.

## Use Case ##
**Pre- and post-conditions**

It is assume that before using the plugin, the user will have

- A structured folder structure, no more than three layers deep, which corresponds to a data classification schema
- A file naming schema containing up to five atomic components, corresponding to the data classification schema
- One or more vector or raster files which are capable of being classified in the schema
- Configuration files which define the instance of the structure

After using the plugin, the user will have

- Vector or raster layers which have been saved in the correct location in the folder structure, with an appropriate valid filename

## UI Storyboard ##

The following diagrams describe the UI process flow, and a possible UI design (implemented in the prototype version of the plugin)


## Configuration ##

A config file contains pointers to the code/value pairs for the filename and folder structure, and other settings. This file should be located in a standard QGIS plugin config file location. It includes:

- the root of folder structure
- location of code/description sets for folder and file names (default location in same folder as main config file
- config for codes and descriptions for folder names, including for each folder: UI label; filename of code/description set; flag indicating whether value set can be added to by users; parent folder code
- for each folder set, file containing code/description pairs
- config for codes and descriptions for file names, including for each filename segment: UI label; filename of code/description set; sequence in filename;  
- for each filename segment, file containing code/description pairs

## Architecture notes ##

- Ideally, config files (including schedule of code/description pairs) should be in XML, to support integration with other components of this plugin set, and in particular metadata collection and editing.
- A prototype plugin which implements much of this functionality has been developed by MapAction, and is available in this repository
- It is intended in a later stage to use the metadata implicit in the folder location and file names to populate metadata files for individual layers 
