# Deep-learning-for-OSCC
## Introduction
This repository contains five implementations of one-dimensional classical neural networks for the detection of multiple oral cancer types. The purpose of this study is to test, compare and analyze the performance of existing classical deep neural network models (AlexNet, VGGNet, ResNet50, MobileNetV2, Transformer) for identifying multiple types of oral cancer tissues. In order to adapt Raman spectroscopy to the application scenario of oral cancer, this study complete model training at the subject level. Based on this, we further develope a prototype intelligent detection system with the above five classical deep neural network models to achieve multiple types of oral cancer tissue detection, which provides an auxiliary diagnostic basis for surgeons to diagnose oral cancer. This work was completed by Intelligent Sensing and Computing Laboratory affiliated to Beijing Information Science and Technology University. It has been published by Elsevier's Vibrational Spectroscopy.https://doi.org/10.1016/j.vibspec.2023.103522
<p align="center">
 <img src="https://user-images.githubusercontent.com/102946092/196730241-919f4431-e287-4512-8659-04570f8b11c5.png">
</p>
<p align="center">
Fig. 1. The network structure of AlexNet.
</p>
<p align="center">
 <img src="https://user-images.githubusercontent.com/102946092/196730995-7b95b511-082e-4316-beb7-6f333a3004de.png">
</p>
<p align="center">
Fig. 2. The network structure of VGGNet.
</p>
<p align="center">
 <img src="https://user-images.githubusercontent.com/102946092/196730828-65280cf7-2ee4-4bb4-a86f-486ef5d47915.png">
</p>
<p align="center">
Fig. 3. The network structure of ResNet50.
</p>
<p align="center">
 <img src="https://user-images.githubusercontent.com/102946092/196731093-078a4d3e-b756-4a1a-875e-97da3fc3a288.png">
</p>
<p align="center">
Fig. 4. The network structure of MobileNetV2.
</p>
<p align="center">
 <img src="https://user-images.githubusercontent.com/102946092/196731157-6c49845c-75d8-45c5-830b-adabaf58720f.png">
</p>
<p align="center">
Fig. 5. The network structure of Transformer.
</p>

## Result

According to Fig. 6, five network performance scenarios are presented. Among them, the Res-Net50 model is the highest in all evaluation metrics, with 92.81% accuracy, 92.93% precision, and 92.86% recall. Then, the performance evaluation of Transformer results in 85.81% accuracy, 86.01% preci-sion, and 85.10% recall, which is at the bottom of the five network models used in this study.
<p align="center">
 <img src="https://user-images.githubusercontent.com/102946092/226380930-3a00f83a-d443-4e7d-be14-45f3f5989827.png">
</p>
<p align="center">
Fig. 6. Experimental results of deep learning methods. 
</p>


## Application

the five network models are deployed on edge computing device to develop a prototype system for intelligent detection of oral cancer. Currently, we have completed the offline testing of the system. The software interface of the system is developed based on Qt, as shown in Fig. 7.
<p align="center">
  <img src="https://github.com/ISCLab-Bistu/deep-learning-for-OSCC/blob/main/images/software.png">
</p>
<p align="center">
Fig. 7. Software interface of oral cancer intelligent detection system.
</p>

## Summary and Prospect

In this study, we use five classical deep neural networks, including AlexNet, VGGNet, ResNet50, MobileNetV2, and Transformer, to perform oral cancer detection. After that, the five network models are deployed on edge computing device to develop a prototype system for intelligent detection of oral cancer. Currently, we have completed the offline testing of the system. Experiments show that the deep learning method has obvious advantages in Raman spectrum recognition. The next step of work will be to conduct animal experiments in vivo in order to test the system performance further.
