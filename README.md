# Chest_x_ray_Detection


# Pneumonia Detection App

## Overview

The Pneumonia Detection App is a desktop application designed to detect pneumonia from chest X-ray images using deep learning. The application features a user-friendly interface built with PyQt5 and utilizes a TensorFlow-based model for image recognition. It provides real-time results through visual and audio feedback.

## Features

- **Image Upload:** Allows users to upload chest X-ray images.  
### Video for How to upload Scanned Chest X-ray Images :   
https://github.com/user-attachments/assets/2fa688f1-2151-412e-a564-b3786c04e483

- **Prediction:** Classifies the uploaded image to detect pneumonia.
- **Result Feedback:** Displays results via pop-ups and text-to-speech.
- **Animated Loading GIF:** Shows a GIF while processing the image.

## Technologies Used

- **Python:** Programming language used for the application.
- **PyQt5:** Framework for creating the graphical user interface (GUI).
- **TensorFlow:** Library for deep learning and model inference.
- **PIL (Pillow):** Used for image processing.
- **win32com:** Provides text-to-speech functionality.
- **Warnings and PIL:** Used to handle image processing and suppress warnings.
- **NumPy:** For numerical operations on image data.
- **Threading:** To run text-to-speech operations asynchronously.

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

# APP Usage

1. Run the Application: chest_xray_App_Roshni.py 
2. Upload an Image:  Click the "Upload Image" button to select and upload a chest X-ray image. 
3. Predict Results: Click the "Prediction" button to analyze the image and receive the result.
4. View Results: A message box will display the result, and the result will be announced via speech synthesis.

# ML Prediction model Code Overview
### Main Application Code
The codebase for the Pneumonia Detection App consists of several key components. Here's an overview of the main sections:

# Imports

- **Warnings and PIL:** Used to handle image processing and suppress warnings.
- **TensorFlow:** For loading the pre-trained deep learning model and making predictions.
- **NumPy:** For numerical operations on image data.
- **PyQt5:** For creating the graphical user interface (GUI) of the application.
- **win32com.client:** Provides text-to-speech functionality.
- **Threading:** To run text-to-speech operations asynchronously.

# Functions

### speak_async(text)
- Purpose: To perform text-to-speech operations asynchronously.
- Implementation: Uses the *win32com.client* library to convert text to speech in a separate thread.

### Ui_MainWindow Class

- setupUi(self, MainWindow)

- Purpose: Initializes the main window, sets up the layout, and configures widgets.
- Components:
   - Labels and GIF: For displaying an animated GIF and image names.
   - Buttons: For uploading images and making predictions.
   - Styling: Customizes the appearance of widgets.

- retranslateUi(self, MainWindow)

   - Purpose: Sets the text for various UI elements and configures tooltips.
   - Functionality: Updates widget texts and tooltips based on the application's language settings.
    
- upload_image(self)
   - Purpose: Handles the image upload process.
   - Functionality: Opens a file dialog to select an image, displays the image name, and prepares the image for prediction using a pre-trained model.

- clear/reset_image(self) (Automated)
    - Purpose: Resets the image display and restarts the GIF animation.
    - Functionality: Clears the current image and restarts the GIF animation.

- predict_result(self)
    - Purpose: Makes predictions on the uploaded image and displays the result.
    - Functionality: Shows a message box with the prediction result (Normal or Affected By PNEUMONIA) and applies color coding to the text.

# Thank you for Viewing my Project 

![Optimized GIF](ezgif.com-optimize.gif)


