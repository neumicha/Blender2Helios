'''
Script to preprocess big scenes for Blender2Helios (e.g. .fbx exports from Unreal Engine)
by Michael Neumann
More information: https://github.com/neumicha/Blender2Helios

You only need this if you want to create point clouds with semantic labels with Blender2Helios
This script puts all the objects in the scene into the correct collections (which correspond to semantic labels)
Just open this file in the Blender "Scripting" tab and click "Run Script"

Input:
    - Scene with all unlabeled objects in one collection (here "Rest")
    - A number of rules (semantic labels according to an object's name)
    
Output:
    - Scene with all the objects moved to the correct collections
    
You should only change the parts in ### CONFIG ###, not in ### CODE ###
'''

import bpy
import fnmatch


### CONFIG ###
# Blender collection where your unclassified objects are stored/linked
originCollection = "Rest"

# Rules where to put the objects
# Order of the rules DOES matter
# Note the last rule which contains only the wildcard *: Move all other objects to the ignored class
#
# e.g.
# dict["targetColl"] = [ "objPattern1", "objPattern2" ]
# will move all objects with names where objPattern1 or objPattern2 occurs (case insensitive) to collection "targetColl"
dict = {}
dict["Benches"] = ["Bench"]
dict["VegetationLow"] = ["Bamboo", "Juniper", "Hedge"]
dict["VegetationHigh"] = ["Birch", "Beech", "Acia", "Elm", "Maple", "Oak", "Fir"]
dict["Ground"] = ["Bürgersteig", "Boden", "Weg", "Vorgarten", "Landscape"]
dict["Cars"] = ["Porsche", "Gelendwagen", "Jeep", "Mercedes"]
dict["Buildings"] = ["Roof", "Wall", "Balkon", "Fenster", "Tür", "Wand", "Haus", "Vorhänge", "Tunnel", "Ziegel", "Garage", "Vorbaute"]
dict["Lamps"] = ["Laterne"]
dict["Ground"] = ["Bürgersteig", "Boden", "Weg", "Vorgarten", "Landscape"]
dict["Signs"] = ["schild"]
dict["SmallObjects"] = ["Pickup", "Müll"]
dict["Stairs"] = ["Treppe"]
dict["Ignore"] = ["LKW", "*"] # The collection 'Ingore' in ignored in the later called Blender2Helios script


### CODE ###
print("Applying dict on scene...")

origColl = bpy.data.collections[originCollection]

for collectionName in dict:
    print(collectionName);
    
    # Create collection if needed
    if bpy.data.collections.get(collectionName) is None:
        newColl = bpy.data.collections.new(collectionName)
        bpy.context.scene.collection.children.link(newColl)
    tarColl = bpy.data.collections[collectionName]
    
    # For all the object name patterns...
    for objectPattern in dict[collectionName]:
        
        pattern = "*"+objectPattern+"*"
        objs2move = [obj for obj in origColl.all_objects if fnmatch.fnmatch(obj.name.lower(), pattern.lower())]

        # For each found object
        for obj in objs2move:
            tarColl.objects.link(obj)
            origColl.objects.unlink(obj)
            # print('Moved to ' + tarColl + ': ' + obj.name)
        print(" - "+objectPattern+" (found: "+str(len(objs2move))+")")