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
Meanwhile there is a paper about my work on semantic classification in 3D point clouds. As this paper also introduces Blender2Helios, please cite this paper when using the tool.
The paper can be found here: https://link.springer.com/chapter/10.1007/978-3-031-22216-0_24

Here is how you can cite the paper:
### Bibtex / .BIB-Format
```
@InProceedings{10.1007/978-3-031-22216-0_24,
author="Neumann, Michael
and Borrmann, Dorit
and N{\"u}chter, Andreas",
editor="Petrovic, Ivan
and Menegatti, Emanuele
and Markovi{\'{c}}, Ivan",
title="Semantic Classification in Uncolored 3D Point Clouds Using Multiscale Features",
booktitle="Intelligent Autonomous Systems 17",
year="2023",
publisher="Springer Nature Switzerland",
address="Cham",
pages="342--359",
abstract="While the semantic segmentation of 2D images is already a well-researched field, the assignment of semantic labels to 3D data is lagging behind. This is partly due to the fact that prelabeled training data is only rarely available since not only the training and application of classification methods but also the manual labeling process are much more time-consuming in 3D. This paper focuses on the more classical approach of first calculating features and subsequently applying a classification algorithm. Existing handcrafted feature definitions are enhanced by using multiple selected reductions of the point cloud as approximations. This serves as input to train a well-studied random forest classifier. A comparison to a recently presented deep learning approach, i.e., the Kernel Point Convolution method, reveals that there are well-justified applications for both modern and classical machine learning methods. To enable the smooth conversion of existing 3D scenes to semantically labeled 3D point clouds the tool Blender2Helios is presented. We show that the therewith generated artificial data is a good choice for training real-world classifiers.",
isbn="978-3-031-22216-0"
}
```

### Endnote / .ENW-Format
```
%0 Conference Proceedings
%T Semantic Classification in Uncolored 3D Point Clouds Using Multiscale Features
%A Neumann, Michael
%A Borrmann, Dorit
%A Nüchter, Andreas
%Y Petrovic, Ivan
%Y Menegatti, Emanuele
%Y Marković, Ivan
%S Intelligent Autonomous Systems 17
%D 2023
%I Springer Nature Switzerland
%C Cham
%@ 978-3-031-22216-0
%F 10.1007/978-3-031-22216-0_24
%X While the semantic segmentation of 2D images is already a well-researched field, the assignment of semantic labels to 3D data is lagging behind. This is partly due to the fact that prelabeled training data is only rarely available since not only the training and application of classification methods but also the manual labeling process are much more time-consuming in 3D. This paper focuses on the more classical approach of first calculating features and subsequently applying a classification algorithm. Existing handcrafted feature definitions are enhanced by using multiple selected reductions of the point cloud as approximations. This serves as input to train a well-studied random forest classifier. A comparison to a recently presented deep learning approach, i.e., the Kernel Point Convolution method, reveals that there are well-justified applications for both modern and classical machine learning methods. To enable the smooth conversion of existing 3D scenes to semantically labeled 3D point clouds the tool Blender2Helios is presented. We show that the therewith generated artificial data is a good choice for training real-world classifiers.
%P 342-359
```

### Refman / .RIS-Format
```
TY  - CONF
AU  - Neumann, Michael
AU  - Borrmann, Dorit
AU  - Nüchter, Andreas
ED  - Petrovic, Ivan
ED  - Menegatti, Emanuele
ED  - Marković, Ivan
PY  - 2023
DA  - 2023//
TI  - Semantic Classification in Uncolored 3D Point Clouds Using Multiscale Features
BT  - Intelligent Autonomous Systems 17
SP  - 342
EP  - 359
PB  - Springer Nature Switzerland
CY  - Cham
AB  - While the semantic segmentation of 2D images is already a well-researched field, the assignment of semantic labels to 3D data is lagging behind. This is partly due to the fact that prelabeled training data is only rarely available since not only the training and application of classification methods but also the manual labeling process are much more time-consuming in 3D. This paper focuses on the more classical approach of first calculating features and subsequently applying a classification algorithm. Existing handcrafted feature definitions are enhanced by using multiple selected reductions of the point cloud as approximations. This serves as input to train a well-studied random forest classifier. A comparison to a recently presented deep learning approach, i.e., the Kernel Point Convolution method, reveals that there are well-justified applications for both modern and classical machine learning methods. To enable the smooth conversion of existing 3D scenes to semantically labeled 3D point clouds the tool Blender2Helios is presented. We show that the therewith generated artificial data is a good choice for training real-world classifiers.
SN  - 978-3-031-22216-0
ID  - 10.1007/978-3-031-22216-0_24
ER  - 
```
