# Blender2Helios
Blender addon to convert a Blender scene into a Helios scene (LiDAR simulation, 3D point clouds).  
Semantic classification is also supported and can be combined easily by using collections in Blender.  
by Michael Neumann

## Documentation
Documentation can be found on the Wiki pages: https://github.com/neumicha/Blender2Helios/wiki

## How to install/run
In Blender, install the .py file as addon and activate it. In the addon preferences choose the correct path to your Helios base directory (usually where your 'assets' and 'data' folders are located). Setup your scene as shown in the Wiki (Collection 'Ignore' is ignored, all others are exported) and initiate the export by clicking *Render -> Run Blender2Helios Export*

## Screenshots
Conversion of a Blender parking lot scene (left). The right image shows the result of two merged laserscans in *3DTK - The 3D Toolkit* (http://threedtk.de) including class labels:

<img src="https://github.com/neumicha/Blender2Helios/blob/master/images/screenshot_ParkingLotScene_Blender.png" height="200px" /><img src="https://github.com/neumicha/Blender2Helios/blob/master/images/screenshot_ParkingLotScene_3DTK.png" height="200px" />
