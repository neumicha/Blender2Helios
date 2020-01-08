# Blender2Helios
Blender addon to convert a Blender scenes to Helios scenes (Heidelberg LiDAR Simulator, 3D point clouds).  
Semantic labels are also supported and can be combined easily by using collections in Blender.  
by Michael Neumann

*Blender:* https://www.blender.org/

*Helios:* https://github.com/GIScience/helios

*3DTK - The 3D Toolkit:* http://threedtk.de

## Documentation
Documentation can be found on the Wiki pages: https://github.com/neumicha/Blender2Helios/wiki

## How to Install/Run
In Blender, install the .py file as addon and activate it. In the addon preferences choose the correct path to your Helios base directory (usually where your 'assets' and 'data' folders are located). Setup your scene as shown in the Wiki (Collection 'Ignore' is ignored, all others are exported) and initiate the export by clicking *Render -> Run Blender2Helios Export*

## Screenshots
Conversion of a Blender parking lot scene (left) to a point cloud using two laser scans simulated with Helios. The right image shows the two scans merged and colored by their semantic classes using *3DTK - The 3D Toolkit* (http://threedtk.de):

<img src="https://github.com/neumicha/Blender2Helios/blob/master/images/screenshot_ParkingLotScene_Blender.png" height="200px" /><img src="https://github.com/neumicha/Blender2Helios/blob/master/images/screenshot_ParkingLotScene_3DTK.png" height="200px" />

## How to Cite
As long as there is no publication, please cite https://github.com/neumicha/Blender2Helios when you use Blender2Helios in your work.

@misc{Blender2Helios,

  title = {{Blender2Helios} - Github Repository},
  
  author = {Michael Neumann},
  
  howpublished = {\url{https://github.com/neumicha/Blender2Helios}},
  
  year = {Accessed: 2010-09-30}
  
}
