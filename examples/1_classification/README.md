# Example 1: Classification

Basic example: Create a point cloud with semantic labels of existing Blender scene.

Input: Blender file with objects separated in classes (ground plane, two cubes, one sphere)

Output: Point cloud with semantic labels (Ground, Cube, Sphere)

## TODOs

1. Download [Helios](https://github.com/3dgeo-heidelberg/helios) (feel free to use a [precompiled release](https://github.com/3dgeo-heidelberg/helios/releases)) and [Blender](https://www.blender.org/download/) (latest test with Blender 3.6.4 on Windows 10)
2. In Blender go to *Edit > Preferences > Add-ons* and install *Blender2Helios.py*
3. Activate the addon (checkbox)
4. Change addon-settings as follows: (see screenshot 1)
   - *Helios Base Directory* to the helios directory (path that contains helios folders like *data*, *assets*)
   - Tick *Use own materials for classification*
5. Load the example file in Blender using *File > Open* and select *example1.blend* of this directory
6. Start the export to Helios format in Blender by clicking *Render > Run Blender2Helios Export* (see screenshot 2)
7. Check that in the Helios directory a *blender2heliosScene.xml" was created in subdirectory *data/scenes*. More folders like *Cubes* und *Ground* were created in the *data/sceneparts* subdirectory.
8. Copy *materials.mtl* to Helios subdirectory *data/sceneparts*. This file defines the class labels (*helios_classification*):
   - Class 1: Ground
   - Class 2: Cubes
   - Class 3: Spheres
9. Run Helios++ e.g. by opening the command line and running *run\helios.exe data/surveys/blender2heliosScene.xml*
10. The resulting point cloud can be found in Helios directory *output/blender2heliosScene/...*
11. Done! An example output point cloud can be found in folder *output* (note that the class label is the 10th feature of each point in the xyz-format)

## Screenshots

### Screenshot 1: Blender2Helios settings
<img src="https://github.com/neumicha/Blender2Helios/blob/master/examples/1_classification/images/screenshot_Blender2Helios_settings.png" height="300px" />

### Screenshot 2: Blender scene
<img src="https://github.com/neumicha/Blender2Helios/blob/master/examples/1_classification/images/screenshot_BlenderScene.png" height="300px" />

## Further help
For further help consult:
- [Blender2Helios Wiki: Installation](https://github.com/neumicha/Blender2Helios/wiki/Installation)
- [Blender2Helios Wiki: Collections](https://github.com/neumicha/Blender2Helios/wiki/Collections-and-Semantic-Classification)
- [Helios: Material files](https://github.com/3dgeo-heidelberg/helios/wiki/Scene#material-files)
- [Blender: Add-ons](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html)
