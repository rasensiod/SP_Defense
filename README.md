# SP_Defense

## Intro
The objective of this project is to create a simple smart hospital website and database with patient data to attack it
using both DDoS and SQL injections. Then, in order to protect the confidentiality and accessibility of the data, we create a set of measures such as identifying different attacks by using machine learning techniques and publishing notification by AWS SNS.



The final accuracy results is shown in the following table:
|  | Task A1 | Task A2 | Task B1 | Task B2 |
| :----:| :----:| :----: |:----: |:----: |
| CNN1 | 91% | 81% | 100% | 82% |
| CNN1(VGG) | / | / | / | 70.2% |
| SVM | 88% | 83% | / | / |
| SVM(&detector) | 98% | 72% | 60.7% | 71% |
| SVM(&landmarks) | / | 90% | / | / |

## Role of each file
The current project structure is shown below
```
.
├── A1
│   └── a1.py
├── A2
│   └── a2.py
├── B1
│   └── b1.py
├── B2
│   └── b2.py
├── Datasets
├── Modules
│   ├── feature_extraction.py
│   ├── plot_result.py
│   ├── pre_processing_A.py
│   └── pre_processing_generator.py
├── dlib_face_recognition_resnet_model_v1.dat
├── main.py
├── results_img
│   ├── emotion_detection_cnn.jpg
│   ├── eye_color_cnn.jpg
│   ├── face_shape_cnn.jpg
│   └── gender_detection_cnn.jpg
└── shape_predictor_68_face_landmarks.dat
```

**main.py**: Contains all the core functions that will be executed sequentially for data pre-processing, model instance creation, model training, result prediction, evaluation and other modules. 

**a1.py**: Contains two classes that can perform task A1, the CNN class and the SVM class, the CNN class contains initialization methods (for building the model), training methods (training of the model, plotting of accuracy and loss value curves), testing methods (result prediction, confusion matrix plotting). 

**a2.py**: Contains two classes that can perform task A2, the CNN class and the SVM class, the CNN class contains initialization methods (for building the model), training methods (training of the model, plotting of accuracy and loss value curves), testing methods (result prediction, confusion matrix plotting). 

**b1.py**: Contains two classes that can perform task B1, the CNN class and the SVM class, the CNN class contains initialization methods (for building the model), training methods (training of the model, plotting of accuracy and loss value curves), testing methods (result prediction, confusion matrix plotting). 

**b2.py**: Contains two classes that can perform task B2, the CNN class and the SVM class, the CNN class contains initialization methods (for building the model), training methods (training of the model, plotting of accuracy and loss value curves), testing methods (result prediction, confusion matrix plotting). 

**feature_extraction.py**: For scenarios using the SVM model, a pre-feature extraction is performed, calling the face detector in the dlib library to identify faces and return a rectangle with faces and landmarks.

**pre_processing_A.py**: Perform image processing such as normalization and greyscaling on the image data in Task A. Divide the training set, validation set and test set.  

**pre_processing_generator.py**: Perform image processing such as normalization and greyscaling on the image data in Task A. Divide the training set, validation set and test set. Note that when dividing the test and training sets, the generator needs different paths for the training data and the test data, so it needs to randomly select 1000 images and put them in the new path, and delete them from the original path.
**plot_result.py**: Plotting accuracy results and loss value curves, plotting prediction result confusion matrix.

**shape_predictor_68_face_landmarks.dat**: shape_predictor() is a tool that takes in an image region containing some object and outputs a set of point locations that define the pose of the object. 

**dlib_face_recognition_resnet_model_v1.dat**: This model is a ResNet network with 29 conv layers. It's essentially a version of the ResNet-34 network from the paper Deep Residual Learning for Image Recognition by He, Zhang, Ren, and Sun with a few layers removed and the number of filters per layer reduced by half. The network was trained from scratch on a dataset of about 3 million faces.

## How to start

If all the dependencies required for the current project are already installed, you can run main.py after placing the dataset in a blank Datasets directory.
```
python main.py
```
The program will read in the sample images from the Datasets directory and start pre-processing, model building, model training, prediction and evaluation. 

**Note**: when you copy the datasets to the Datasets directory, you only need to copy the cartoon_set and celeba folders. The program will automatically divide the test set from the above datasets and create a new directory to store the test data for Task B2. The ratio of training set, validation set and test set is 8:1:1. 

Due to the monthly limitation of Git LFS uploading large files, it is not possible to upload the trained model files to github, so it will take more time to train each task when using the CNN model. Specific hyperparameters can be found at the end instruction.


