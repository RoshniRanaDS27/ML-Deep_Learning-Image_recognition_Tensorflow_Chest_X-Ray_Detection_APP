# Chest_x_ray_Detection
![Optimized GIF](ezgif.com-optimize.gif)

# Pneumonia Detection App

## Overview

The Pneumonia Detection App is a desktop application designed to detect pneumonia from chest X-ray images using deep learning. The application features a user-friendly interface built with PyQt5 and utilizes a TensorFlow-based model for image recognition. It provides real-time results through visual and audio feedback.

## Features

- **Image Upload:** Allows users to upload chest X-ray images.
- **Prediction:** Classifies the uploaded image to detect pneumonia.
- **Result Feedback:** Displays results via pop-ups and text-to-speech.
- **Animated Loading GIF:** Shows a GIF while processing the image.

## Technologies Used

- **Python:** Programming language used for the application.
- **PyQt5:** Framework for creating the graphical user interface (GUI).
- **TensorFlow:** Library for deep learning and model inference.
- **PIL (Pillow):** Used for image processing.
- **win32com:** Provides text-to-speech functionality.

## Installation

### Prerequisites

- Python 3.x
- TensorFlow
- PyQt5
- Pillow
- pywin32

# Machine Learning Model
### ML- Prediction Model Code file : ML_Model_Code_Roshni.ipynb
### Model File: chest_xray_Roshnis_Model.h5 

# Model Creation
1. Prepare Data:

- Training Path: Datasets_Chest_xrays/train
- Validation Path: Datasets_Chest_xrays/test
  
2. Model Architecture:

- Base Model: VGG16 with ImageNet weights (excluding top layers).
- Custom Layers: Added Flatten and Dense layers for classification.

3. Code for Model Creation: ML_Model_Code_Roshni.ipynb
4. Training and Saving
Used the code snippet above to train the model and saved it as chest_xray_Roshnis_Model.h5.

# Usage

1. Run the Application:
-
3. Upload an Image: 
- Click the "Upload Image" button to select and upload a chest X-ray image.

3. Predict Results:
- Click the "Prediction" button to analyze the image and receive the result.

4. View Results:
- A message box will display the result, and the result will be announced via speech synthesis.
