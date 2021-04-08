#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from AnaSayfa import Ui_AnaSayfa
import cv2, numpy as np
import matplotlib.pyplot as plt

class Menu0(QMainWindow):
    image1 = None
    image2 = None
    file_name = ""
    img_list = []
    hist_list = []
    hist_img_list = []

    def __init__(self):
        super().__init__()

        self.menu0 = Ui_AnaSayfa()
        self.menu0.setupUi(self)

        """if (type(self.org_image) == np.ndarray): self.FOTO_GOSTER(self.org_image)"""


    def RESIM_AC(self):
        self.file_name, type = QFileDialog().getOpenFileName(filter="Image Files (*.png *.jpg *.bmp *.gif)")
        self.menu0.label_1.setPixmap(QtGui.QPixmap(self.file_name))
        self.menu0.label_1.setScaledContents(True)
        self.image1 = cv2.imread(self.file_name,0)

    def RESIM_AC2(self):
        self.file_name, type = QFileDialog().getOpenFileName(filter="Image Files (*.png *.jpg *.bmp *.gif)",)
        self.menu0.label_2.setPixmap(QtGui.QPixmap(self.file_name))
        self.menu0.label_2.setScaledContents(True)
        self.image2 = cv2.imread(self.file_name,0)

    def HISTOGRAM(self):
        if type(self.image1) == np.ndarray and type(self.image2) == np.ndarray:
            self.img_list = []
            self.hist_list = []
            self.hist_img_list = []
            self.img_list.append(self.image1)
            self.img_list.append(self.image2)

            for img in self.img_list:
                hist = np.zeros([256])

                for x in range(img.shape[0]):
                    for y in range(img.shape[1]):
                        px_vl = img[x, y]
                        hist[px_vl] += 1

                def f(x):
                    return np.int(x)

                f2 = np.vectorize(f)

                fig = plt.figure()
                plt.title("Histogram")
                plt.bar(np.arange(len(hist)), f2(hist))
                plt.xlabel("Gray Level")
                plt.ylabel("No. of Pixel (Counting)")

                self.hist_list.append(hist)

                fig.savefig('histogram.png', dpi=200)

                img = cv2.imread("histogram.png")
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                temp_image = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0],QtGui.QImage.Format_RGB888)
                self.hist_img_list.append(temp_image)

            self.menu0.label_3.setPixmap(QtGui.QPixmap.fromImage(self.hist_img_list[0]))
            self.menu0.label_3.setScaledContents(True)
            self.menu0.label_4.setPixmap(QtGui.QPixmap.fromImage(self.hist_img_list[1]))
            self.menu0.label_4.setScaledContents(True)

    def EQUALIZATION(self):
        if len(self.img_list) != 0 and len(self.hist_list) != 0:
            self.hist_img_list = []
            eq_img_list = []
            for i in range(len(self.img_list)):
                img = self.img_list[i]
                hist = self.hist_list[i]
                GL = 256

                eq_hist = np.zeros_like(hist)
                eq_img = np.zeros_like(img)

                for i in range(len(hist)):
                    eq_hist[i] = int((GL - 1) * np.sum(hist[0:i]))

                for x in range(img.shape[0]):
                    for y in range(img.shape[1]):
                        px_vl = int(img[x, y])
                        eq_img[x, y] = eq_hist[px_vl]

                def f(x):
                    return np.int(x)

                f2 = np.vectorize(f)

                fig = plt.figure()
                plt.title("Histogram Equalization")
                plt.bar(np.arange(len(eq_hist)), f2(eq_hist))
                plt.xlabel("Gray Level")
                plt.ylabel("No. of Pixel (Counting)")

                fig.savefig('eq_histogram.png', dpi=200)

                img = cv2.imread("eq_histogram.png")
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                temp_image = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_RGB888)
                self.hist_img_list.append(temp_image)

                eq_img = cv2.cvtColor(eq_img, cv2.COLOR_BGR2RGB)
                temp_image = QtGui.QImage(eq_img, eq_img.shape[1], eq_img.shape[0], eq_img.strides[0], QtGui.QImage.Format_RGB888)
                eq_img_list.append(temp_image)

            self.menu0.label_3.setPixmap(QtGui.QPixmap.fromImage(self.hist_img_list[0]))
            self.menu0.label_3.setScaledContents(True)
            self.menu0.label_4.setPixmap(QtGui.QPixmap.fromImage(self.hist_img_list[1]))
            self.menu0.label_4.setScaledContents(True)
            self.menu0.label_5.setPixmap(QtGui.QPixmap.fromImage(eq_img_list[0]))
            self.menu0.label_5.setScaledContents(True)
            self.menu0.label_6.setPixmap(QtGui.QPixmap.fromImage(eq_img_list[1]))
            self.menu0.label_6.setScaledContents(True)

    def SPECIFICATION(self):
        if len(self.img_list) != 0 and len(self.hist_list) != 0:
            self.hist_img_list = []
            eq_img_list = []
            for i in range(len(self.img_list)):
                img = self.img_list[i]
                hist = self.hist_list[i]
                GL = 256

                eq_hist = np.zeros_like(hist)
                eq_img = np.zeros_like(img)

                for i in range(len(hist)):
                    eq_hist[i] = int(((GL - 1) * np.sum(hist[0:i]))/(img.shape[0]*img.shape[1]))

                for x in range(img.shape[0]):
                    for y in range(img.shape[1]):
                        px_vl = int(img[x, y])
                        eq_img[x, y] = eq_hist[px_vl]

                def f(x):
                    return np.int(x)

                f2 = np.vectorize(f)

                fig = plt.figure()
                plt.title("Histogram Equalization")
                plt.bar(np.arange(len(eq_hist)), f2(eq_hist))
                plt.xlabel("Gray Level")
                plt.ylabel("No. of Pixel (Counting)")

                fig.savefig('eq_histogram.png', dpi=200)

                img = cv2.imread("eq_histogram.png")
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                temp_image = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_RGB888)
                self.hist_img_list.append(temp_image)

                eq_img = cv2.cvtColor(eq_img, cv2.COLOR_BGR2RGB)
                temp_image = QtGui.QImage(eq_img, eq_img.shape[1], eq_img.shape[0], eq_img.strides[0], QtGui.QImage.Format_RGB888)
                eq_img_list.append(temp_image)

            self.menu0.label_3.setPixmap(QtGui.QPixmap.fromImage(self.hist_img_list[0]))
            self.menu0.label_3.setScaledContents(True)
            self.menu0.label_4.setPixmap(QtGui.QPixmap.fromImage(self.hist_img_list[1]))
            self.menu0.label_4.setScaledContents(True)
            self.menu0.label_5.setPixmap(QtGui.QPixmap.fromImage(eq_img_list[0]))
            self.menu0.label_5.setScaledContents(True)
            self.menu0.label_6.setPixmap(QtGui.QPixmap.fromImage(eq_img_list[1]))
            self.menu0.label_6.setScaledContents(True)