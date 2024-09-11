# Pneumonia Detection - Machine Learning
![image](https://github.com/user-attachments/assets/f4e3fdef-557e-4ec9-9c0c-a6446e67760e)

# Chest_x_ray_Detection- [ML]Deep Learning (Image Recognition)
![image](https://github.com/user-attachments/assets/b745e340-ff17-4fb5-9e1e-f002edc70dab) ![image](https://github.com/user-attachments/assets/e43b7d1f-01af-4570-b5cb-6ddad26fc0de) 


  
# Pneumonia Detection App
![ezgif com-optimize](https://github.com/user-attachments/assets/f91fb51a-efcf-4b4a-a07c-f0656b703466) ![image](https://github.com/user-attachments/assets/7a19e67f-452c-4dd9-ae17-93103bbe1986)
#
## Overview

The Pneumonia Detection App is a desktop application designed to detect pneumonia from chest X-ray images using deep learning. The application features a user-friendly interface built with PyQt5 and utilizes a TensorFlow-KERAS based model for image recognition. 
It provides real-time results through visual and audio feedback.

Also, image-based data Numonia detection dashboard, powered by a deep learning model built on the VGG16 architecture.   
- This model leverages the power of neural networks to classify and analyze medical images with high accuracy.  
- At the heart of our solution is the VGG16 model, pre-trained on the ImageNet dataset. We've fine-tuned it by adding custom layers on top. To maintain efficiency, we've kept the original VGG16 layers frozen and focused our training on the custom layers we've added.  
- Our dashboard is designed to process and classify medical images seamlessly. Users can upload an image, and the system will analyze it, predict the class of the image.   
- One of the standout features of our dashboard is the real-time audio announcement of results. Once the model makes a prediction, also popup  result will immediately displayed on the screen with a color-coded message—green for positive results and red for negative results. making it easy for users to understand the outcome instantly. Additionally, we've included a text-to-speech function to read out the results loundly all kind of users.  
- This functionality is particularly useful in clinical settings where quick and clear communication is critical. Additionally, the text-to-speech capability enhances accessibility, making our system user-friendly.
#
### Video For App Demo: (Turn on the audio for speak_async(text) experience)
https://github.com/user-attachments/assets/25027ef8-c278-4ee9-83c6-50534341c1b7

## App Features

### Video for How to upload Scanned Chest X-ray Images :   
https://github.com/user-attachments/assets/2fa688f1-2151-412e-a564-b3786c04e483
  
- **Image Upload:** Allows users to upload chest X-ray images.  
- **Prediction:** Classifies the uploaded image to detect pneumonia.
#
![ai_](https://github.com/user-attachments/assets/a7233ec5-5628-41f5-9b9e-660e9da39f4d)
#
-  **Result Feedback:** Displays results via pop-ups and text-to-speech (Audio Results)
- **Animated Loading GIF:** Shows a GIF while processing the image.
#
Dataset link : https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
#
## Technologies Used
![giphy](https://github.com/user-attachments/assets/7029b824-d15b-433b-8e5b-61e07c68678f)
- **Python:** Programming language used for the application.
- **PyQt5:** Framework for creating the graphical user interface (GUI).
- **TensorFlow:** Library for deep learning and model inference.
- **PIL (Pillow):** Used for image processing.
- **win32com:** Provides text-to-speech functionality.
- **Warnings and PIL:** Used to handle image processing and suppress warnings.
- **NumPy:** For numerical operations on image data.
- **Threading:** To run text-to-speech operations asynchronously.
- VGG16 Architecture

## Installation
![f825f793957677 5e7242767044b](https://github.com/user-attachments/assets/fed4db2b-6491-4af4-9b2a-279148e4193f)
### Prerequisites

- Python 3.x
- TensorFlow
- PyQt5
- Pillow
- pywin32

# Machine Learning Model
### ML- Prediction Model Code file : ML_Model_Code_Roshni.ipynb
### Model File: chest_xray_Roshnis_Model.h5 
![Understanding the Hype Around Machine Learning](https://github.com/user-attachments/assets/9cdfc433-c334-4164-ac9e-c0a23376c60f)

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
  
  ![neuron-animation-blog](https://github.com/user-attachments/assets/cf9c7633-0f42-479a-8689-078dc603ad23)
#
# APP Usage

1. Run the Application: chest_xray_App_Roshni.py 
2. Upload an Image:  Click the "Upload Image" button to select and upload a chest X-ray image. 
3. Predict Results: Click the "Prediction" button to analyze the image and receive the result.
4. View Results: A message box will display the result, and the result will be announced via speech synthesis.

# ML Prediction model Code Overview
![87f3f1425b217691da645e97dbb50d55](https://github.com/user-attachments/assets/1fa5ab05-fb0b-44bb-b62c-dd1803ed80ed)
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
![0_M50IPKZz58Fyy178](https://github.com/user-attachments/assets/01954378-eff0-4953-ad57-4f2c43aca0c5)
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
![image](https://github.com/user-attachments/assets/a8d64f75-85f1-4a0e-8d9d-fddb5e7ab792)



