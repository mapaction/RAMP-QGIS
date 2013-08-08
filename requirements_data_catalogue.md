#QGIS Plugin Requirements: Data Catalogue #
# Purpose #
To provide QGIS users with a catalogue of raster or vector files held within a given folder structure, allow filtering and sorting of the list, and individual files to be selected for loading into the current QGIS project.

## Use case ##
**Pre- and post-conditions**

It is assumed before using the tool, the user will have

- A target folder structure on a network or local drive which contains supported spatial data or image formats 

After using the tool, the user will have

- A viewable catalogue listing all the files in supported formats contained in the folder structure
- The ability to filter and sort the catalogue by any column
- The ability to select one or more files for inclusion in the layer tree for the current QGIS project

## UI Storyboard ##
1. User selects plugin
2. Prompt for root of folder structure (defaulting to last used, with ability to browse to root)
3. User selects 'Generate Catalogue'
4. Plugin searches folder for all supported files, presents list to user
5. User sorts/filters as required
6. User selects one or more files
7. User selects 'Load layers to QGIS'
8. Selected layers are loaded to QGIS
9. User closes dialogue when finished

## Architecture Notes ##


- A metadata harvesting script already exists which meets a substantial part of these requirements - see[ https://github.com/spatialguru/NME](https://github.com/spatialguru/NME)
- It is assumed the plugin will incorporate this script, providing a UI for the user to run it and manage the returned data
- The script already contains an XSLT file which processes the returned XML catalogue for presentation to the user. This could be extended to allow the data to be presented in appropriate ways, according to usage. 
- It would be possible for users to develop their own XSLT to allow presentation to be customised
- Sorting and filtering of the returned data table could be met using JavaScript/CSS