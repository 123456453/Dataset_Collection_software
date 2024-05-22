
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMessageBox, QVBoxLayout, QMainWindow
from pyorbbecsdk import Pipeline, FrameSet
from pyorbbecsdk import Config
from pyorbbecsdk import OBSensorType, OBFormat
from pyorbbecsdk import OBError
from pyorbbecsdk import VideoStreamProfile
import cv2
import numpy as np
from utils import frame_to_bgr_image
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from tool import TemporalFilter
import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from skeleton_data import draw_landmarks_on_image
import os
import time
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1101, 738)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 10, 20, 681))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 680, 171, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(170, 10, 20, 681))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 0, 171, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(190, 10, 20, 591))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(200, 590, 881, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(1010, 10, 151, 591))
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(200, 0, 881, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 171, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 210, 111, 21))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(211, 30, 282, 171))
        self.label_8.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(600, 210, 111, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(880, 210, 121, 21))
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(280, 13, 131, 21))
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(580, 10, 161, 21))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(880, 13, 161, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 660, 151, 28))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(800, 660, 151, 28))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(500, 30, 282, 171))
        self.label_9.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(790, 30, 282, 171))
        self.label_10.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(790, 230, 282, 171))
        self.label_11.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(211, 230, 282, 171))
        self.label_12.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(500, 230, 282, 171))
        self.label_13.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 160, 171, 31))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 450, 151, 221))
        self.textBrowser.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 610, 171, 28))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(410, 610, 671, 31))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 210, 151, 231))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_8 = QCheckBox(self.layoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout.addWidget(self.checkBox_8)

        self.checkBox_3 = QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.checkBox_7 = QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout.addWidget(self.checkBox_7)

        self.checkBox_6 = QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout.addWidget(self.checkBox_6)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(80, 60, 91, 85))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_20 = QLineEdit(self.layoutWidget1)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_2.addWidget(self.lineEdit_20)

        self.lineEdit_22 = QLineEdit(self.layoutWidget1)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.verticalLayout_2.addWidget(self.lineEdit_22)

        self.lineEdit_21 = QLineEdit(self.layoutWidget1)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.verticalLayout_2.addWidget(self.lineEdit_21)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 60, 71, 81))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.layoutWidget2)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_3.addWidget(self.label_19)

        self.label_21 = QLabel(self.layoutWidget2)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_3.addWidget(self.label_21)

        self.label_20 = QLabel(self.layoutWidget2)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_3.addWidget(self.label_20)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(210, 420, 282, 171))
        self.label_17.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(500, 420, 282, 171))
        self.label_18.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(790, 420, 282, 171))
        self.label_22.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(270, 400, 131, 21))
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(590, 400, 131, 21))
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(870, 400, 131, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1101, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.checkBox.toggled.connect(self.lineEdit_21.setEnabled)
        self.checkBox.toggled.connect(self.lineEdit_20.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Parameters setting</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">IR Data</span></p></body></html>", None))
        self.label_8.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">OF Data</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Maksed Data</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Front RGB Data</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Skeleton Data</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Depth Data</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start record", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"End record", None))
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Modal selection</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">A checkmark in front of the checkbox indicates that the relevant modes need to be collected (point cloud modes are not not shown). Extending modality can be further modified if necessary\uff01</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save Address Settting", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Front RGB Data", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Up RGB Data", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Depth Data", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Skeleton Data", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"IR Data", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"OF Data", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Maksed Data", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"PC Data", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Up RGB Data</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Extending Modality</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Extending Modality</span></p></body></html>", None))
    # retranslateUi

        
class MainWindow_RGB(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow_RGB, self).__init__(parent)
        # UI界面
        self.setupUi(self)
        self.background()
        self.config = Config()
        self.pipeline = Pipeline()
        self.timer = QTimer()
        self.temporal_filter = TemporalFilter(alpha=0.5)
        self.cap = cv2.VideoCapture(701)
        _, self.frame1 = self.cap.read()
        self.cap.release()
        self.prvs = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2GRAY)
        self.hsv = np.zeros_like(self.frame1)
        self.hsv[..., 1] = 255
        self.save_path = self.lineEdit.text()
    def background(self):
        self.label_8.setEnabled(False)
        self.label_9.setEnabled(False)
        self.label_10.setEnabled(False)
        self.label_11.setEnabled(False)
        self.label_12.setEnabled(False)
        self.label_13.setEnabled(False)
        self.label_17.setEnabled(False)
        # 链接相机打开和关闭
        self.pushButton.clicked.connect(self.open_camera)
        self.pushButton_2.clicked.connect(self.close_camera)
        #如果按下按钮，则禁用输入框
        self.pushButton.clicked.connect(self.set_disEnbaled)
        self.pushButton.setEnabled(True)
        # 初始状态不能关闭摄像头
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.clicked.connect(self.open_foloder)
    # 打开相机采集视频
    def open_camera(self):
        self.cap2 = cv2.VideoCapture(702)
               # 幕布可以播放
        self.label_8.setEnabled(False)
        self.label_9.setEnabled(False)
        self.label_10.setEnabled(False)
        self.label_11.setEnabled(False)
        self.label_12.setEnabled(False)
        self.label_13.setEnabled(False)
        self.label_17.setEnabled(False)
            # 打开摄像头按钮不能点击
        self.pushButton.setEnabled(False)
            # 关闭摄像头按钮可以点击
        self.pushButton_2.setEnabled(True)
        self.timer.start(50)
        self.pipeline.start(self.config)
        self.timer.timeout.connect(self.show_img)
        self.timer.timeout.connect(self.show_of)
        self.timer.timeout.connect(self.show_skeleton)
        self.timer.timeout.connect(self.show_IR)
        self.timer.timeout.connect(self.show_depth)
        self.timer.timeout.connect(self.up_show_img)
        print("beginning!")
    def up_show_img(self):
        ret, frame = self.cap2.read()
        if ret:
            color_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            height, width = color_image.shape[0], color_image.shape[1]
            
            pixmap = QImage(color_image, width, height, 3*width, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
                        # 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label_17.width(), height / self.label_17.height())
            pixmap.setDevicePixelRatio(ratio)
            self.Up_RGB_modal_save(RGB=frame)
                        # 视频流置于label中间部分播放
            self.label_17.setAlignment(Qt.AlignCenter)
            self.label_17.setPixmap(pixmap)
            self.label_17.show()            
            self.label_17.setEnabled(True)
                        # 打开摄像头按钮不能点击
            self.pushButton.setEnabled(False)
                        # 关闭摄像头按钮可以点击
            self.pushButton_2.setEnabled(True)
    #前端RGB数据采集与展示
    def show_img(self):
        start_time = time.time()
        try:
            profile_list = self.pipeline.get_stream_profile_list(OBSensorType.COLOR_SENSOR)
            try:
                color_profile: VideoStreamProfile = profile_list.get_video_stream_profile(640, 0, OBFormat.RGB, 30)
            except OBError as e:
                print(e)
                color_profile = profile_list.get_default_video_stream_profile()
                print("color profile: ", color_profile)
            self.config.enable_stream(color_profile)
        except Exception as e:
            print(e)
            return
        try:
            frames: FrameSet = self.pipeline.wait_for_frames(100)
            if frames is None:
                print("frames is None")
            color_frame = frames.get_color_frame()
            if color_frame is None:
                print("color_frames is None")
            color_image = frame_to_bgr_image(color_frame)
            if color_image is None:
                print("failed to convert frame to image")
            # print(color_image.shape)
            height, width = color_image.shape[0], color_image.shape[1]
            color_image2 = cv2.cvtColor(color_image,cv2.COLOR_BGR2RGB)
            self.RGB_OF_modal_save(RGB=color_image)           
            # print(f'color_image shape: {color_image.shape}')
            pixmap = QImage(color_image2, width, height, 3*width, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
            # 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label_8.width(), height / self.label_8.height())
            pixmap.setDevicePixelRatio(ratio)
            # 视频流置于label中间部分播放
            self.label_8.setAlignment(Qt.AlignCenter)
            self.label_8.setPixmap(pixmap)
            self.label_8.show()
            # 幕布可以播放
            self.label_8.setEnabled(True)                        # 打开摄像头按钮不能点击
            self.pushButton.setEnabled(False)
                        # 关闭摄像头按钮可以点击
            self.pushButton_2.setEnabled(True)
            print("beginning!")
            end_time = time.time()
        except KeyboardInterrupt:
                print('key interrupt')
    #骨骼点数据采集与展示
    def show_of(self):
        start_time = time.time()
        try:
            profile_list = self.pipeline.get_stream_profile_list(OBSensorType.COLOR_SENSOR)
            try:
                color_profile: VideoStreamProfile = profile_list.get_video_stream_profile(640, 0, OBFormat.RGB, 30)
            except OBError as e:
                print(e)
                color_profile = profile_list.get_default_video_stream_profile()
                print("color profile: ", color_profile)
            self.config.enable_stream(color_profile)
        except Exception as e:
            print(e)
            return
        try:
            frames: FrameSet = self.pipeline.wait_for_frames(100)
            if frames is None:
                print("frames is None")
            color_frame = frames.get_color_frame()
            if color_frame is None:
                print("color_frames is None")
            color_image = frame_to_bgr_image(color_frame)
            if color_image is None:
                print("failed to convert frame to image")
            # print(color_image.shape)
            height, width = color_image.shape[0], color_image.shape[1]
            color_image2 = cv2.cvtColor(color_image,cv2.COLOR_BGR2RGB)
            next = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(self.prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            self.hsv[..., 0] = ang*180/np.pi/2
            self.hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            bgr = cv2.cvtColor(self.hsv, cv2.COLOR_HSV2BGR)
            self.OF_save(optical_flow=bgr)
            pixmap = QImage(bgr, width, height, 3*width, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
                        # 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label_13.width(), height / self.label_13.height())
            pixmap.setDevicePixelRatio(ratio)
                        # 视频流置于label中间部分播放
  
            self.label_13.setAlignment(Qt.AlignCenter)
            self.label_13.setPixmap(pixmap)
            self.label_13.show()
                        # 幕布可以播放
            self.label_13.setEnabled(True)
                        # 打开摄像头按钮不能点击
            self.pushButton.setEnabled(False)
                        # 关闭摄像头按钮可以点击
            self.pushButton_2.setEnabled(True)
            print("beginning!")
            end_time = time.time()
            self.prvs = next
        except KeyboardInterrupt:
                print('key interrupt')  
    def show_skeleton(self):
        try:
            profile_list = self.pipeline.get_stream_profile_list(OBSensorType.COLOR_SENSOR)
            try:
                color_profile: VideoStreamProfile = profile_list.get_video_stream_profile(640, 0, OBFormat.RGB, 30)
            except OBError as e:
                print(e)
                color_profile = profile_list.get_default_video_stream_profile()
                print("color profile: ", color_profile)
            self.config.enable_stream(color_profile)
        except Exception as e:
            print(e)
            return
        try:
            frames: FrameSet = self.pipeline.wait_for_frames(100)
            if frames is None:
                print("frames is None")
            color_frame = frames.get_color_frame()
            if color_frame is None:
                print("color_frames is None")
            color_image = frame_to_bgr_image(color_frame)
            if color_image is None:
                print("failed to convert frame to image")
            # print(color_image.shape)
            height, width = color_image.shape[0], color_image.shape[1]
            color_image = cv2.cvtColor(color_image,cv2.COLOR_BGR2RGB)
            base_options = python.BaseOptions(model_asset_path = 'pose_landmarker_heavy.task')
            options = vision.PoseLandmarkerOptions(base_options = base_options,
                                           output_segmentation_masks=True)
            detector = vision.PoseLandmarker.create_from_options(options)
            image = mp.Image(image_format=mp.ImageFormat.SRGB, data=color_image)
            detection_result = detector.detect(image)
            annotated_image = cv2.cvtColor(draw_landmarks_on_image(image.numpy_view(), detection_result),cv2.COLOR_BGR2RGB)
            pixmap = QImage(annotated_image, width, height, 3*width, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
                        # 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label_8.width(), height / self.label_8.height())
            pixmap.setDevicePixelRatio(ratio)
                        # 视频流置于label中间部分播放
            self.label_9.setAlignment(Qt.AlignCenter)
            self.label_9.setPixmap(pixmap)
            self.label_9.show()
                        # 幕布可以播放
            self.label_9.setEnabled(True)
                        # 打开摄像头按钮不能点击
            self.pushButton.setEnabled(False)
                        # 关闭摄像头按钮可以点击
            self.pushButton_2.setEnabled(True)
            #MASK
            segmentation_mask = detection_result.segmentation_masks[0].numpy_view()
            visualized_mask = np.repeat(segmentation_mask[:, :, np.newaxis], 3, axis=2) * 255
            # cv2.imshow(f'visualized_mask', visualized_mask)
            visualized_mask = cv2.cvtColor(visualized_mask, cv2.COLOR_BGR2RGB)
            visualized_mask = visualized_mask.astype(np.uint8)
            self.Skeleton_mask_modal_save(skeleton=detection_result, mask=visualized_mask)
            # print(f'visualized_mask: {visualized_mask.shape}')
            pixmap = QImage(visualized_mask, width, height, 3*width, QImage.Format_RGB888)
            # pixmap.setColorTable([qRgb(i, i, i) for i in range(256)])
            pixmap = QPixmap.fromImage(pixmap)
            #获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label_11.width(), height / self.label_11.height())
            pixmap.setDevicePixelRatio(ratio)
                        # 视频流置于label中间部分播放
            self.label_11.setAlignment(Qt.AlignCenter)
            self.label_11.setPixmap(pixmap)
            self.label_11.show()
                        # 幕布可以播放
            self.label_11.setEnabled(True)
                        # 打开摄像头按钮不能点击
            self.pushButton.setEnabled(False)
                        # 关闭摄像头按钮可以点击
            self.pushButton_2.setEnabled(True)           
            print("beginning!")
        except KeyboardInterrupt:
                print('key interrupt')  
    
    #深度数据采集与展示
    def show_depth(self):
        start_time = time.time()
        try:
            profile_list = self.pipeline.get_stream_profile_list(OBSensorType.DEPTH_SENSOR)
            assert profile_list is not None
            try:
                depth_profile = profile_list.get_video_stream_profile(640, 0, OBFormat.Y16, 30)
            except OBError as e:
                print("Error: ", e)
                depth_profile = profile_list.get_default_video_stream_profile()
            assert depth_profile is not None
            print("depth profile: ", depth_profile)
            self.config.enable_stream(depth_profile)
        except Exception as e:
            print(e)
            return
        try:
            frames  = self.pipeline.wait_for_frames(100)
            if frames is None:
                print("frames is None")
            depth_frame = frames.get_depth_frame()
            if depth_frame is None:
                print("depth_frames is None")
            width = depth_frame.get_width()
            height = depth_frame.get_height()
            scale = depth_frame.get_depth_scale()
            depth_data = np.frombuffer(depth_frame.get_data(), dtype=np.uint16)
            depth_data = depth_data.reshape((height, width))

            depth_data = depth_data.astype(np.float32) * scale
            depth_data = np.where((depth_data > 20) & (depth_data < 10000), depth_data, 0)
            depth_data = depth_data.astype(np.uint16)
            # Apply temporal filtering
            depth_data = self.temporal_filter.process(depth_data)
            # print(f'dept_data: {depth_data.shape}')
            depth_image = cv2.normalize(depth_data, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            depth_image = cv2.applyColorMap(depth_image, cv2.COLORMAP_JET)
            depth_image = cv2.resize(depth_image, (640, 480))
            self.depth_modal_save(depth_image=depth_image)
            pixmap = QImage(depth_image, 640, 480, 3*640, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
                        # 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label_10.width(), height / self.label_10.height())
            pixmap.setDevicePixelRatio(ratio)
                        # 视频流置于label中间部分播放
            self.label_10.setAlignment(Qt.AlignCenter)
            self.label_10.setPixmap(pixmap)
            self.label_10.show()
                        # 幕布可以播放
            self.label_10.setEnabled(True)
                        # 打开摄像头按钮不能点击
            self.pushButton.setEnabled(False)
                        # 关闭摄像头按钮可以点击
            self.pushButton_2.setEnabled(True)
            # self.timer.start(10)
            print("beginning!")
            end_time = time.time()

        except KeyboardInterrupt:
            print('key interrupt')
    #红外数据采集与展示
    def show_IR(self):
        # self.modal_save()
        try:
            profile_list = self.pipeline.get_stream_profile_list(OBSensorType.IR_SENSOR)
            try:
                ir_profile = profile_list.get_video_stream_profile(640, 0, OBFormat.Y16, 30)
            except OBError as e:
                print(e)
                ir_profile = profile_list.get_default_video_stream_profile()
            self.config.enable_stream(ir_profile)
        except Exception as e:
            print(e)
            return
        try:
            frames  = self.pipeline.wait_for_frames(100)
            if frames is None:
                print("frames is None")
            ir_frame = frames.get_ir_frame()
            if ir_frame is None:
                print("ir_frames is None")
            ir_data = np.asanyarray(ir_frame.get_data())
            width = 640
            height = 480
            ir_format = ir_frame.get_format()
            if ir_format == OBFormat.Y8:
                ir_data = np.resize(ir_data, (height, width, 1))
                data_type = np.uint8
                image_dtype = cv2.CV_8UC1
                max_data = 255
            elif ir_format == OBFormat.MJPG:
                ir_data = cv2.imdecode(ir_data, cv2.IMREAD_UNCHANGED)
                data_type = np.uint8
                image_dtype = cv2.CV_8UC1
                max_data = 255
                if ir_data is None:
                    print("decode mjpeg failed")
                ir_data = np.resize(ir_data, (height, width, 1))
            else:
                ir_data = np.frombuffer(ir_data, dtype=np.uint16)
                data_type = np.uint16
                image_dtype = cv2.CV_16UC1
                max_data = 65535
                ir_data = np.resize(ir_data, (height, width, 1))
            ir_data = cv2.normalize(ir_data, ir_data, 0, max_data, cv2.NORM_MINMAX, dtype=image_dtype)
            ir_data = ir_data.astype(data_type)
            ir_image = cv2.cvtColor(ir_data, cv2.COLOR_GRAY2RGB)
            self.IR_modal_save(IR=ir_image)
            ir_image = cv2.resize(src=ir_image,dsize=(640,480))
            ir_image = ir_image.astype(np.uint8)
            pixmap = QImage(ir_image, width, height, 3*width, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
                        # 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label_12.width(), height / self.label_12.height())
            pixmap.setDevicePixelRatio(ratio)
                        # 视频流置于label中间部分播放
            self.label_12.setAlignment(Qt.AlignCenter)
            self.label_12.setPixmap(pixmap)
            self.label_12.show()
            # 幕布可以播放
            self.label_12.setEnabled(True)
            # 打开摄像头按钮不能点击
            self.pushButton.setEnabled(False)
            # 关闭摄像头按钮可以点击
            self.pushButton_2.setEnabled(True)
            # print(ir_image.shape)
            print("beginning!")
        except KeyboardInterrupt:
            print('key interrupt')
        
    # 关闭相机
    def close_camera(self):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pipeline.stop()
        self.timer.stop()
        self.cap2.release()
    
    def get_paras(self):
        width = self.lineEdit_20.text()
        height = self.lineEdit_22.text()
        fsp = self.lineEdit_21.text()
        return width, height, fsp
    def set_disEnbaled(self):
        #如果按下数据采集按钮，则禁用输入框
        self.lineEdit_20.setEnabled(False)
        self.lineEdit_21.setEnabled(False)
        self.lineEdit_22.setEnabled(False)
    def open_foloder(self):
        folder_path = QFileDialog.getExistingDirectory(None, '选择文件夹')
        if folder_path:
            QMessageBox.information(self, f'你选择的文件夹是: {folder_path}',"文件已选择")
            self.lineEdit.setText(folder_path)
            self.lineEdit.setEnabled(False)
            self.pushButton_3.setEnabled(False)
        return folder_path
    def RGB_OF_modal_save(self,RGB):
        #根据是否选择模态前面的复选框，判断是否保存响应模态
        #获取保存路径
        width, height,_ = self.get_paras()
        save_path = self.lineEdit.text()
        curr_time = int(time.time()*1000000)
        if self.checkBox.isChecked():
            RGB_modal = cv2.resize(src=RGB, dsize=(eval(width), eval(height)))
            cv2.imwrite(f'{save_path}/RGB/RGB_{curr_time}.jpg',RGB_modal)            
    def OF_save(self,optical_flow):
        width, height,_ = self.get_paras()
        save_path = self.lineEdit.text()
        curr_time = int(time.time()*1000000)         
        if self.checkBox_5.isChecked():
            of_modal = cv2.resize(src=optical_flow, dsize=(eval(width), eval(height)))
            cv2.imwrite(f'{save_path}/Optical_flow/optical_flow_{curr_time}.jpg',of_modal)        
    def Up_RGB_modal_save(self,RGB):
        #根据是否选择模态前面的复选框，判断是否保存响应模态
        #获取保存路径
        width, height,_ = self.get_paras()
        save_path = self.lineEdit.text()
        curr_time = int(time.time()*1000000)
        if self.checkBox_8.isChecked():
            RGB_modal = cv2.resize(src=RGB, dsize=(eval(width), eval(height)))
            cv2.imwrite(f'{save_path}/Up_RGB/Up_RGB_{curr_time}.jpg',RGB_modal)
    def Skeleton_mask_modal_save(self, skeleton, mask):
        #根据是否选择模态前面的复选框，判断是否保存响应模态
        #获取保存路径
        width, height,_ = self.get_paras()
        save_path = self.lineEdit.text()
        curr_time = int(time.time()*1000000)
        if self.checkBox_2.isChecked():
                x = []
                y = []
                z = []
                v = []
                p = []
                for i, marks in enumerate(skeleton.pose_world_landmarks[0]):
                    x.append(marks.x)
                    y.append(marks.y)
                    z.append(marks.z)
                    v.append(marks.visibility)
                    p.append(marks.presence)
                all_data = np.array([x, y, z, v, p]).T
                df = pd.DataFrame(all_data)
                df.columns = ['x', 'y', 'z', 'visibility', 'presence']
                df.to_csv(f'{save_path}/Skeleton/Skeleton_{curr_time}.txt',header=True, sep='\t', index=False)           
        if self.checkBox_7.isChecked():
            masked_modal = cv2.resize(src=mask, dsize=(eval(width), eval(height)))
            cv2.imwrite(f'{save_path}/Masked_data/Masked_data_{curr_time}.jpg',masked_modal)
    def depth_modal_save(self,depth_image):
        width, height,_ = self.get_paras()
        save_path = self.lineEdit.text()
        curr_time = int(time.time()*1000000)
        if self.checkBox_3.isChecked():
            depth_image = cv2.resize(src=depth_image, dsize=(eval(width), eval(height)))
            cv2.imwrite(f'{save_path}/Depth/Depth_{curr_time}.jpg', depth_image)
    def IR_modal_save(self,IR):
        width, height, _ = self.get_paras()
        curr_time = int(time.time()*1000000)
        save_path = self.lineEdit.text()
        if self.checkBox_4.isChecked():
            ir_modal = cv2.resize(src=IR, dsize=(eval(width), eval(height)))
            cv2.imwrite(f'{save_path}/IR/IR_{curr_time}.jpg', ir_modal)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow_RGB()
    main.show()
    sys.exit(app.exec_())
