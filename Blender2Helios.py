#####
# Blender2Helios
# Blender 2.8x Add-On
# by Michael Neumann
# GNU GPLv3
###
# Can be used to convert a Blender scene into a Helios scene.
# See https://github.com/neumicha/Blender2Helios/wiki for instructions
# When used in your work, please cite https://github.com/neumicha/Blender2Helios
# Helios LiDAR simulator: https://github.com/3dgeo-heidelberg/helios
# 3D-Toolkit for viewing pointclouds, learn classifiers, ...: http://threedtk.de
# Special thanks to my supervisor Prof. Dr. Andreas Nüchter (University Würzburg)
#####


import bpy
from bpy import context
from bpy.types import Operator, AddonPreferences, Panel
from bpy.props import StringProperty, IntProperty, BoolProperty, EnumProperty
import os
from os.path import expanduser
import math
import numpy as np

bl_info = {
    "name": "Blender2Helios",
    "author": "Michael Neumann",
    "version": (0, 0, 2),
    "blender": (2, 80, 0),
    "category": "Scene",
    "location": "Render > Run Blender2Helios Export",
    "wiki_url": "https://github.com/neumicha/Blender2Helios/wiki",
    "tracker_url": "https://github.com/neumicha/Blender2Helios/issues",
    "description": "Exports Blender scene as Helios XML scene"
}


class Blender2HeliosPreferences(AddonPreferences):
    bl_idname = __name__
    
    pref_heliosBaseDir: StringProperty(name="Helios Base Directory", description="Directory containing 'assets' and 'data' directories", subtype='DIR_PATH', default=os.getcwd()+os.sep)
    pref_sceneName: StringProperty(name="Scene Name (Helios)", description="Later name of the Helios scene (also used as filename)", default="blender2heliosScene")
    pref_alsoWriteSurveyFile: BoolProperty(name="Also write Helios survey file (3D Cursor is used for positioning the scanner)", description="Not only scene XML is generated but also the survey XML (defines the laser scanner position etc.)", default=True)
    pref_alwaysOverrideModels: BoolProperty(name="Always Override Models (SLOW!)", description="If enabled, exported objects with same names are not cached and always overriden. This decreses export speed significantly!", default=True)
    pref_deleteCachedScene: BoolProperty(name="Delete cached Helios scene", description="Deletes the cached scene of Helios. So when you run Helios the next time the newly exported Blender scene is used. Without deletion of the tree cache of Helios you will load an old version.", default=True)
    pref_useMaterials: BoolProperty(name="Use materials", description="Use for a classified pointcloud! Each object gets a material according to the collection it belongs to. Attention: You have to provide materials.mtl file", default=True)
    pref_useOwnMaterials: BoolProperty(name="Use own materials for classification", description="Object files are linked to materials.lib on sceneparts root folder. There you can easily provide classlabels", default=False)
    
    def draw(self, context):
        layout = self.layout
        layout.label(text='Blender2Helios Preferences:')
        rowBaseDir = layout.row()
        rowBaseDir.prop(self, 'pref_heliosBaseDir', icon='FILE_FOLDER', expand=True)
        rowSceneName = layout.row()
        rowSceneName.prop(self, 'pref_sceneName', icon='SCENE', expand=True)
        rowUseMaterials = layout.row()
        rowUseMaterials.prop(self, 'pref_useMaterials', expand=True)
        rowUseOwnMaterials = layout.row()
        rowUseOwnMaterials.prop(self, 'pref_useOwnMaterials', expand=True)
        rowAlsoWriteSurveyFile = layout.row()
        rowAlsoWriteSurveyFile.prop(self, 'pref_alsoWriteSurveyFile', expand=True)
        rowAlwaysOverrideModels = layout.row()
        rowAlwaysOverrideModels.prop(self, 'pref_alwaysOverrideModels', expand=True)
        rowDeleteCachedScene = layout.row()
        rowDeleteCachedScene.prop(self, 'pref_deleteCachedScene', expand=True)

#class Blender2HeliosPanel(Panel):
#    bl_idname = 'blender2helios.panel'
#    bl_label = 'BLENDER2HELIOS_PANEL'
#    bl_space_type = 'VIEW_3D'
#    bl_region_type = 'UI'
#    bl_category = 'ALL'
# 
#    def draw(self, context):
#        self.layout.operator("object.blender2helios", icon='MESH_CUBE', text="Add Cube")
#
class Blender2Helios(Operator):
    """Export Blender scene to Helios LiDAR Simulation"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "scene.blender2helios"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Blender2Helios"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    

    def execute(self, context):        # execute() is called when running the operator.
        print("Basedir is "+context.preferences.addons['Blender2Helios'].preferences.pref_heliosBaseDir)
        # The original script
        print("Running Blender2Helios export...")
        
        blender2heliosHelper = Blender2HeliosHelper(
            context.preferences.addons['Blender2Helios'].preferences.pref_heliosBaseDir,
            context.preferences.addons['Blender2Helios'].preferences.pref_sceneName,
            context.preferences.addons['Blender2Helios'].preferences.pref_alsoWriteSurveyFile,
            context.preferences.addons['Blender2Helios'].preferences.pref_alwaysOverrideModels,
            context.preferences.addons['Blender2Helios'].preferences.pref_useMaterials,
            context.preferences.addons['Blender2Helios'].preferences.pref_useOwnMaterials,
            bpy.context.scene.cursor.location)
        
        if (context.preferences.addons['Blender2Helios'].preferences.pref_deleteCachedScene):
            blender2heliosHelper.deleteCachedScene()
        blender2heliosHelper.export2Helios()
        
        print("Done!")
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.
    
# END OF CLASS Blender2Helios(Operator):

def menu_func_blender2helios_export(self, context):
    self.layout.operator(Blender2Helios.bl_idname, text="Run Blender2Helios Export")

def register():
    bpy.utils.register_class(Blender2Helios)
    #bpy.utils.register_class(Blender2HeliosPanel)
    bpy.utils.register_class(Blender2HeliosPreferences)
    bpy.types.TOPBAR_MT_render.append(menu_func_blender2helios_export)
    
def unregister():
    bpy.types.TOPBAR_MT_render.remove(menu_func_blender2helios_export)
    bpy.utils.unregister_class(Blender2HeliosPreferences)
    #bpy.utils.unregister_class(Blender2HeliosPanel)
    bpy.utils.unregister_class(Blender2Helios)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
   
    
    
class Blender2HeliosHelper():
    """Helper functions for Blender2Helios"""
        
    def __init__(self, heliosDir, sceneName, alsoWriteSurveyFile, alwaysOverrideModels, useMaterials, useOwnMaterials, scannerLocation):
        if not heliosDir.endswith("\\") or heliosDir.endswith("/"):
            heliosDir = heliosDir + "\\"
        self.heliosDir = heliosDir
        self.sceneName = sceneName
        self.alsoWriteSurveyFile = alsoWriteSurveyFile
        self.alwaysOverrideModels = alwaysOverrideModels
        self.useMaterials = useMaterials
        self.useOwnMaterials = useOwnMaterials
        self.scannerLocation = scannerLocation
    
    def deleteCachedScene(self):
        sceneFile = self.heliosDir + 'data/scenes/' + self.sceneName + '.scene'
        if (os.path.exists(sceneFile)):
            os.remove(sceneFile)
            
    def cutString(self, string,delim):
        split_string = string.split(delim)
        if split_string[0] == "":
            print("Dot is first in name")
            return split_string[1]
        else:
            return split_string[0]

    def create_collection(self, collection_name):
        # Add or find collection
        collection = bpy.data.collections.get(collection_name)
        if collection is None:
            collection = bpy.data.collections.new(collection_name)
            bpy.context.scene.collection.children.link(collection)
        return collection

    def buildSceneParts(self):
        out=""
        inst_coll_dict,instance_obj_names, degp = self.createInstanceDict()
        print("Found following particles")
        print(instance_obj_names)
        for c in bpy.data.collections:
            for o in c.all_objects:
                if (c.name != 'Ignore' or o.name in instance_obj_names):
                    if o.name in instance_obj_names:
                        collection_name = inst_coll_dict[o.name][0]
                    else:
                        collection_name = self.cutString(c.name,'.')
                    try:
                        object_name = self.cutString(o.name,'.')
                        if not self.hasParticleModifiers(o):
                            print('-')
                            print('Found object:', collection_name, '/', object_name)
                            out += self.exportObject(c, o, collection_name, object_name,instance_obj_names)
                        else:
                            print('-')
                            print('Found Particle System:', collection_name, '/', object_name)
                            out += self.exportParticleInstances(degp, o, collection_name)
                    except Exception as e:
                        print(e)
        self.hideInstancedObject(instance_obj_names)
        return out

    def exportObject(self, c, o, collection_name, object_name,instance_obj_names):
        out = ""
        objFileSizeExtension = self.dim2Text(self.dimScale2Original(o.dimensions, o.scale))
        collectionDir = self.heliosDir + 'data/sceneparts/' + collection_name
        if (not os.path.exists(collectionDir)):
            os.mkdir(collectionDir)
        objFile = collectionDir + '/' + object_name + '-' + objFileSizeExtension + '.obj'
        scale = o.scale[0]
        o.rotation_mode = 'QUATERNION' # Otherwise we only get zeros later,                            
        # export .obj file if needed
        if (not os.path.exists(objFile) or self.alwaysOverrideModels):
            print('We have to export the file... ' + collection_name + '/' + object_name + '-' + objFileSizeExtension + '.obj')
            self.exportObjectAsOBJ(collection_name, o, objFile, scale)
        if (c.name != 'Ignore' and object_name not in instance_obj_names): # Only add to xml if not an instanced obj
            out = self.object2XML(collection_name, object_name + '-' + objFileSizeExtension + '.obj', o.location, self.quaternion2RPY(o.rotation_quaternion), scale)
        return out

    def exportParticleInstances(self, degp, o, collection_name):
        obj_evaluated = o.evaluated_get(degp)
        out = ""
        for object_instance in degp.object_instances:
            if object_instance.is_instance and object_instance.parent == obj_evaluated:
                obj = object_instance.object
                obj_inst = object_instance.instance_object
                object_name = self.cutString(obj.name,'.')
                objFileSizeExtension = self.dim2Text(self.dimScale2Original(obj_inst.dimensions, obj.scale))
                location = object_instance.matrix_world.to_translation()
                rotation = self.quaternion2RPY(object_instance.matrix_world.to_quaternion())
                size = object_instance.matrix_world.to_scale()[0]
                out += self.object2XML(collection_name, object_name + '-' + objFileSizeExtension + '.obj', location, rotation, size)
        return out

    def hideInstancedObject(self, instance_obj_names):
        for inst_obj in instance_obj_names:
            try:
                bpy.data.objects[inst_obj].hide_set(True)
            except:
                pass

    def createInstanceDict(self):
        inst_coll_dict = {}
        degp = bpy.context.evaluated_depsgraph_get()
        for i, object_instance in enumerate(degp.object_instances):
            if object_instance.is_instance:
                object_name = object_instance.object.name
                parent_name = object_instance.parent.name
                collection_name = bpy.data.objects[parent_name].users_collection[0].name
                bpy.data.objects[object_name].hide_set(False)
                if object_name not in inst_coll_dict:
                    inst_coll_dict[object_name] = [collection_name]
                else:
                    if collection_name not in inst_coll_dict[object_name]:
                        inst_coll_dict[object_name].append(collection_name)
        return inst_coll_dict, list(inst_coll_dict), degp

    def hasParticleModifiers(self,obj):
        mod_list = []
        for mod in obj.modifiers:
            mod_list.append(mod.type)
        return any(instance_mod in mod_list for instance_mod in ['PARTICLE_SYSTEM','NODES'])

    def exportObjectAsOBJ(self, collection_name, obj, objFile, scale):
        # Maybe we have to rescale the object before exporting (Always bring X to 1)
        backupTranslation = obj.location.copy()
        backupRotation = obj.rotation_quaternion.copy()
        obj.location.zero()
        obj.rotation_quaternion.identity()
        obj.scale /= scale
        self.selectOneObject(obj)
        self.exportSelectedObject(objFile)
        obj.scale *= scale
        obj.location = backupTranslation
        obj.rotation_quaternion = backupRotation
        if (self.useOwnMaterials):
            self.prependMaterial2File(collection_name, objFile)

    def export2Helios(self):
        if (bpy.context.mode != 'OBJECT'):
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False) # Change to object mode
                    
        # Scene
        #fScene = open(self.heliosDir + "data/scenes/" + self.sceneName + ".xml","w+")
        fScene = open(os.path.join(self.heliosDir, "data", "scenes", self.sceneName+".xml"),"w+")
        fScene.write(self.xmlSceneHead())
        fScene.write(self.buildSceneParts())
        fScene.write(self.xmlSceneFoot())
        fScene.close()
        
        # Survey
        if (self.alsoWriteSurveyFile):
            fSurvey = open(os.path.join(self.heliosDir, "data" , "surveys", self.sceneName+".xml"),"w+")
            fSurvey.write(self.xmlSurvey())
            fSurvey.close()

    

    # return the xml head of the scene
    def xmlSceneHead(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
    <document>
        <scene id=\"""" + self.sceneName + """" name=\"""" + self.sceneName + """">
    """
    # returns xml code for survey (my be changed later for more scans etc.)
    def xmlSurvey(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
    <document>
        <!-- Default scanner settings: -->
        <scannerSettings id="profile1" active="true" pulseFreq_hz="100000" scanAngle_deg="50.0" scanFreq_hz="120" headRotatePerSec_deg="10.0" headRotateStart_deg="0.0" headRotateStop_deg="0.0" />
        <survey defaultScannerSettings="profile1" name=\"""" + self.sceneName + """" scene=\"""" + self.heliosDir + """data/scenes/""" + self.sceneName + """.xml#""" + self.sceneName + """" platform=\"""" + self.heliosDir + """data/platforms.xml#tripod" scanner=\"""" + self.heliosDir + """data/scanners_tls.xml#riegl_vz400">
            <leg>
                <platformSettings x=\"""" + str(self.scannerLocation[0]) + """" y=\"""" + str(self.scannerLocation[1]) + """" z=\"""" + str(self.scannerLocation[2]) + """" onGround="true" />
                <scannerSettings template="profile1" headRotateStart_deg="0" headRotateStop_deg="360" />
            </leg>
        </survey>
    </document>
    """

    # Converts object to valid Helios XML part. Remember, that you have to do a PRY rotation in Helios (using RPY angles in degree)
    def object2XML(self, collection, objectFile, translation, rotation, scale):
        return """        <part>
                <filter type="objloader">
                    <param type="string" key="filepath" value=\"""" + self.heliosDir + """data/sceneparts/""" + collection + '/' + objectFile + """" />
                </filter>
                <filter type="rotate">
                    <param type="rotation" key="rotation">
                        <rot axis="x" angle_deg=\"""" + str(rotation[0]) + """" />
                        <rot axis="y" angle_deg=\"""" + str(rotation[1]) + """"  />
                        <rot axis="z" angle_deg=\"""" + str(rotation[2]) + """"  />
                    </param>
                </filter>
                <filter type="translate">
                    <param type="vec3" key="offset" value=\"""" + str(translation[0]) + ';' + str(translation[1]) + ';' + str(translation[2]) + """" />
                </filter>
                <filter type="scale">
                    <param type="double" key="scale" value=\"""" + str(scale) + """" />
                </filter>
            </part>
    """
    
    # returns the xml footer of the scene
    def xmlSceneFoot(self):
        return """    </scene>
    </document>
    """

    # Brings first dimension to scale 1 and returns the 3 dimensions
    def dimScale2Original(self, dimensions, scale):
        return (dimensions/scale[0])

    def dim2Text(self, dimensions):
        return str(int(dimensions[0]*100)) + '-' + str(int(dimensions[1]*100)) + '-' + str(int(dimensions[2]*100))

    def exportSelectedObject(self, file):
        export_materials = self.useMaterials and not self.useOwnMaterials
        bpy.ops.export_scene.obj(filepath=file, check_existing=False, use_mesh_modifiers=True, use_selection=True, use_normals=False, use_materials=export_materials, use_uvs=False, axis_forward='Y', axis_up='Z')

    def selectOneObject(self, object):
        bpy.ops.object.select_all(action='DESELECT')
        object.select_set(True)
        bpy.context.view_layer.objects.active = object # Also make it active. May be needed later

    def selectOneObject(self, object):
        bpy.ops.object.select_all(action='DESELECT')
        try:
            object.select_set(True)
        except:
            # Link object to ignore collection if not in view layer
            ignore_coll = self.create_collection("Ignore")
            ignore_coll.objects.link(object)
            object.select_set(True)
        bpy.context.view_layer.objects.active = object # Also make it active. May be needed later

    # Quaternion (w,x,y,z) to Tiat Bryan (r,p,y); Output in degrees
    def quaternion2RPY(self, q):
        r = 180/math.pi*math.atan2(2*(q[0]*q[1]+q[2]*q[3]), 1-2*(math.pow(q[1],2)+math.pow(q[2],2)))
        p = 180/math.pi*math.asin(round(2*(q[0]*q[2]-q[3]*q[1]),4)) # Round fixes issues of numbers > 1
        y = 180/math.pi*math.atan2(2*(q[0]*q[3]+q[1]*q[2]), 1-2*(math.pow(q[2],2)+math.pow(q[3],2)))
        return(r,p,y)

    def prependMaterial2File(self, materialName, fileName):
        #We read the existing text from file in READ mode
        src=open(fileName,"r")
        prepend="mtllib ../materials.mtl\nusemtl " + materialName + "\n"    #Prepending string
        xml=src.readlines()
        #Here, we prepend the string we want to on first line
        xml.insert(0,prepend)
        src.close()
        #We again open the file in WRITE mode 
        src=open(fileName,"w")
        src.writelines(xml)
        src.close()