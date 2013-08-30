## File-based Data Management Support: Requirements Overview ##
MapAction is working on an ongoing project to provide information management and GIS support to disaster management agencies in countries vulnerable to disasters including flooding and earthquakes as well as smaller-scale emergencies arising from, for example, major road traffic accidents.

We are using QGIS as a central part of the project, and have run a number of courses to train both GIS and non-GIS personnel to produce a range of commonly used maps for disaster response.

To support the project, we also deliver a set of standard file-based data storage structures, with (primarily) shapefiles organised in a three-level classification, using structured filenames to provide guidance to users on the data which is avialable to them, and help with using it. This approach mirrors that used in MapAction's emergency deployments, and is also intended to be consistent with UN OCHA approaches, including [Common Operational Datasets](http://cod.humanitarianresponse.info/about-codfod) (CODs).

For example, a file might be located and name as follows:
> ...\base\admin\zmb_ad2_wfp.shp

This would indicate that

- It contains 'base' data (as opposed to e.g. thematic or topographical data
- It contains data on administrative boundaries
- It relates to Zambia
- The admin data is level 2
- The data provider is WFP

Details of the folder and file naming structures are provided elsewhere.

To help users to maximise the value of this approach, MapAction envisages plugins for QGIS which will, in summary


- Help users save data to the correct location in the repository with a valid filename, with a dialogue to prompt for classifications
- Use these implicit metadata which is inherent in the classificaions to created structured metadata for files
- Enhance this metadata with programmatically-derived metadata, covering for example bounds, CRS, number of features
- Use the combined metadata to provide the user with a data catalogue, from which they can select data which meets their needs

Although these requirements arise from the emergency mapping domain, they could be seen as generic, and ideally  any plugins developed would be applicable to an arbitrary folder and filename structure, within certain constraints.

There are already some resources, developed by MapAction and others, which contribute to this vision - these are referenced below. Requirements documentation for individual plugins is contained elsewhere in this repository.

- spatialguru's [Network Mapping Engine (NME)](https://github.com/spatialguru/NME)
- MapAction's prototype [QGIS plugins](https://github.com/mapaction/RAMP-QGIS/tree/master/MapActionTools)
- The [metatools](https://github.com/nextgis/metatools) metadata browser/editor for QGIS