# Deep-learning-for-OSCC
# Introduction
This repository contains five implementations of one-dimensional classical neural networks for the detection of multiple oral cancer types. The purpose of this study is to test, compare and analyze the performance of existing classical deep neural network models (AlexNet, VGGNet, ResNet50, MobileNetV2, Transformer) for identifying multiple types of oral cancer tissues. In order to adapt Raman spectroscopy to the application scenario of oral cancer, this study complete model training at the subject level. Based on this, we further develope a prototype intelligent detection system with the above five classical deep neural network models to achieve multiple types of oral cancer tissue detection, which provides an auxiliary diagnostic basis for surgeons to diagnose oral cancer. This work was completed by Intelligent Sensing and Computing Laboratory affiliated to Beijing Information Science and Technology University. It has been submitted to the Journal of "Photodiagnosis and Photodynamic Therapy" published by Elsevier.

![image](https://user-images.githubusercontent.com/102946092/196730241-919f4431-e287-4512-8659-04570f8b11c5.png)

Fig. 1. The network structure of AlexNet.

![image](https://user-images.githubusercontent.com/102946092/196730995-7b95b511-082e-4316-beb7-6f333a3004de.png)

Fig. 2. The network structure of VGGNet.

![image](https://user-images.githubusercontent.com/102946092/196730828-65280cf7-2ee4-4bb4-a86f-486ef5d47915.png)

Fig. 3. The network structure of ResNet50.

![image](https://user-images.githubusercontent.com/102946092/196731093-078a4d3e-b756-4a1a-875e-97da3fc3a288.png)

Fig. 4. The network structure of MobileNetV2.

![image](https://user-images.githubusercontent.com/102946092/196731157-6c49845c-75d8-45c5-830b-adabaf58720f.png)

Fig. 5. The network structure of Transformer.

# Result
According to Fig. 6, five network performance scenarios are presented. Among them, the Res-Net50 model is the highest in all evaluation metrics, with 91.17% accuracy, 91.60% precision, and 91.46% sensitivity. Then, the performance evaluation of Transformer results in 84.49% accuracy, 85.27% preci-sion, and 84.21% sensitivity, which is at the bottom of the five network models used in this study.

![image](https://user-images.githubusercontent.com/102946092/196731549-8be34b50-5c62-4e43-83fc-866823b1982d.png)

Fig. 6. Experimental results of deep learning methods. 

# Application
the five network models are deployed on edge computing device to develop a prototype system for intelligent detection of oral cancer. Currently, we have completed the offline testing of the system. The software interface of the system is developed based on Qt, as shown in Fig. 7.

![image](https://user-images.githubusercontent.com/102946092/196734365-ec6b5305-a2ea-4892-8002-f8a93befbe4d.png)

Fig. 7. Software interface of oral cancer intelligent detection system.

# Summary and Prospect
In this study, we use five classical deep neural networks, including AlexNet, VGGNet, ResNet50, MobileNetV2, and Transformer, to perform oral cancer detection. After that, the five network models are deployed on edge computing device to develop a prototype system for intelligent detection of oral cancer. Currently, we have completed the offline testing of the system. Experiments show that the deep learning method has obvious advantages in Raman spectrum recognition. The next step of work will be to conduct animal experiments in vivo in order to test the system performance further.
