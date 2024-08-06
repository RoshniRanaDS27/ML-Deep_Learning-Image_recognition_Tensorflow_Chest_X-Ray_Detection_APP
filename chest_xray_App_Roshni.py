import warnings
from PIL import Image, ImageEnhance
warnings.filterwarnings('ignore')
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
from tensorflow.keras.preprocessing import image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QMovie
from win32com.client import Dispatch
from threading import Thread

def speak_async(text):
    """Speak asynchronously using a separate thread."""
    def speak():
        speaker = Dispatch(("SAPI.SpVoice"))
        speaker.Speak(text)
    Thread(target=speak).start()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("background-color: black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 20, 600, 400))
        self.label.setText("Deep learning")
        self.gif = QMovie("giphy-downsized-large.gif")
        self.gif.setCacheMode(QMovie.CacheAll)
        self.gif.setSpeed(100)
        self.label.setMovie(self.gif)
        self.gif.start()
        self.label.setObjectName("label")

        self.imageNameLabel = QtWidgets.QLabel(self.frame)
        self.imageNameLabel.setGeometry(QtCore.QRect(150, 430, 600, 30))
        self.imageNameLabel.setStyleSheet("color: white; font-size: 18px;")
        self.imageNameLabel.setObjectName("imageNameLabel")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 470, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("patient.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
        "border-radius: 10px;\n"
        " background-color:#DF582C;\n"
        "\n"
        "} \n"
        "QPushButton:hover {\n"
        " background-color: #7D93E0;\n"
        "}")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
        "border-radius: 10px;\n"
        " background-color:#DF582C;\n"
        "\n"
        "} \n"
        "QPushButton:hover {\n"
        " background-color: #7D93E0;\n"
        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.upload_image)
        self.pushButton_2.clicked.connect(self.predict_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PNEUMONIA Detection Apps"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/giphy-downsized-large.gif\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Chest X_ray PNEUMONIA Detection"))
        self.pushButton.setText(_translate("MainWindow", "Upload Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Prediction"))

    def upload_image(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        path = str(path)
        self.imageNameLabel.setText(f"Uploaded Image: {path.split('/')[-1]}")
        print(path)
        self.model = load_model('chest_xray_Roshnis_Model.h5')
        img_file = image.load_img(path, target_size=(224, 224))
        x = image.img_to_array(img_file)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        global result
        result = self.model.predict(img_data)

    def clear_image(self):
        self.label.clear()  # Clear the current image display
        self.imageNameLabel.setText("")  # Clear the image name display
        self.gif.stop()  # Stop the GIF
        self.gif.setFileName("giphy-downsized-large.gif")  # Restart the GIF
        self.label.setMovie(self.gif)
        self.gif.start()  # Restart the GIF

    def predict_result(self):
        if 'result' not in globals():
            QMessageBox.warning(None, "No Image", "Please upload an image first.")
            return

        result_text = "Result is Normal" if result[0][0] > 0.5 else "Affected By PNEUMONIA"
        color = "green" if result[0][0] > 0.5 else "red"

        # Show result popup with color
        msg_box = QMessageBox()
        msg_box.setText(result_text)
        msg_box.setStyleSheet(f"QLabel {{ color: {color}; font-size: 18px; }}")
        
        # Start speech asynchronously
        speak_async(result_text)
        
        # Show the message box
        msg_box.exec_()
        
        self.clear_image()  # Clear the image display and restart the GIF for the next prediction

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





