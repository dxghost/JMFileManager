# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psutil
import os
import threading
import shutil
import socket
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import mp3Player
from PIL import Image
import subprocess as sp
from os import startfile
import glob
from mutagen.mp3 import MP3
import otherwindows
import Openfilewindows
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from  PyQt5.QtCore import QDir, Qt
import favourite
import renamewindows
import connection_win
import download_win
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import zipfile
import json
import server as SERVER
import client as CLIENT

mp3Player = mp3Player.mp3Player()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 860)
        MainWindow.setMinimumWidth(1125)
        MainWindow.setMinimumHeight(860)
        MainWindow.setMaximumWidth(1125)
        MainWindow.setMaximumHeight(860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # -----------
        self.Toolbox = QtWidgets.QGroupBox(self.centralwidget)
        self.Toolbox.setGeometry(QtCore.QRect(10, 0, 1101, 101))
        self.Toolbox.setFlat(False)
        self.Toolbox.setCheckable(False)
        self.Toolbox.setChecked(False)
        self.Toolbox.setObjectName("Toolbox")
        # -----------
        self.toolButton = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton.setGeometry(QtCore.QRect(10, 20, 71, 68))
        # -----------
        self.iconrar = QtGui.QIcon()
        self.iconrar.addPixmap(QtGui.QPixmap(
            "ui icons/rar-file-formats-document-export-extension-format-33d17157644c7eff-512x512.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.iconpdf = QtGui.QIcon()
        self.iconpdf.addPixmap(QtGui.QPixmap(
            "ui icons/pdf-file-format-symbol.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.icontxt = QtGui.QIcon()
        self.icontxt.addPixmap(QtGui.QPixmap(
            "ui icons/txt-text-file-extension-symbol.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.iconpng = QtGui.QIcon()
        self.iconpng.addPixmap(QtGui.QPixmap(
            "ui icons/png-file-extension-interface-symbol.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.iconjpg = QtGui.QIcon()
        self.iconjpg.addPixmap(QtGui.QPixmap(
            "ui icons/jpg-image-file-format.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.iconblank = QtGui.QIcon()
        self.iconblank.addPixmap(QtGui.QPixmap(
            "ui icons/document-icon.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.icon7zip = QtGui.QIcon()
        self.icon7zip.addPixmap(QtGui.QPixmap(
            "ui icons/zip-file.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.iconmp3 = QtGui.QIcon()
        self.iconmp3.addPixmap(QtGui.QPixmap(
            "ui icons/mp3-file-format-variant.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.iconexe = QtGui.QIcon()
        self.iconexe.addPixmap(QtGui.QPixmap(
            "ui icons/exe-file-format-symbol.png"),
            QtGui.QIcon.Active, QtGui.QIcon.On)

        self.pyicon = QtGui.QIcon()
        self.pyicon.addPixmap(QtGui.QPixmap("ui icons/py.png"),
                              QtGui.QIcon.Active, QtGui.QIcon.On)
        self.staricon = QtGui.QIcon()
        self.staricon.addPixmap(QtGui.QPixmap("ui icons/star-icon.png"),
                                QtGui.QIcon.Active, QtGui.QIcon.On)

        self.extracticon = QtGui.QIcon()
        self.extracticon.addPixmap(QtGui.QPixmap("ui icons/extract-image.png"),
                                   QtGui.QIcon.Active, QtGui.QIcon.On)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui icons/icons8-add-file-100.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("ui icons/folder_open.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("ui icons/document-icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        # -----------
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(35, 35))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_2.setGeometry(QtCore.QRect(70, 20, 71, 68))
        # -----------
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap("ui icons/folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # -----------
        self.toolButton_2.setIcon(self.icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_3.setGeometry(QtCore.QRect(130, 20, 71, 68))
        # -----------
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui icons/Files-Delete-File-icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        # -----------
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.setDisabled(True)

        self.toolButton_4 = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_4.setGeometry(QtCore.QRect(190, 20, 71, 68))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_4.setDisabled(True)
        self.toolButton_5 = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_5.setGeometry(QtCore.QRect(250, 20, 71, 68))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.setDisabled(True)
        self.toolButton_6 = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_6.setGeometry(QtCore.QRect(380, 20, 71, 68))
        self.icon5 = QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap("ui icons/zip-file-format-vector-icon.png"), QtGui.QIcon.Normal,
                             QtGui.QIcon.Off)
        self.toolButton_6.setIcon(self.icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(37, 37))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_6.setDisabled(True)
        self.toolButton_7 = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_7.setGeometry(QtCore.QRect(670, 20, 71, 68))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui icons/Go Back-595b40b75ba036ed117d8029.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_7.setAutoRaise(True)
        self.toolButton_7.setObjectName("toolButton_7")

        self.toolButton_9 = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_9.setGeometry(QtCore.QRect(460, 20, 71, 68))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ui icons/fav.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon8)
        self.toolButton_9.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_9.setAutoRaise(True)
        self.toolButton_9.setObjectName("toolButton_9")

        self.toolButton_extract = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_extract.setGeometry(QtCore.QRect(600, 20, 71, 68))
        self.toolButton_extract.setIcon(self.extracticon)
        self.toolButton_extract.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_extract.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_extract.setAutoRaise(True)
        self.toolButton_extract.setObjectName("Extractbutton")
        self.toolButton_extract.setDisabled(True)

        self.toolButton_ren = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_ren.setGeometry(QtCore.QRect(530, 20, 71, 68))
        icon8_ren = QtGui.QIcon()
        icon8_ren.addPixmap(QtGui.QPixmap("ui icons/rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_ren.setIcon(icon8_ren)
        self.toolButton_ren.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_ren.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_ren.setAutoRaise(True)
        self.toolButton_ren.setObjectName("toolButton_9")
        self.toolButton_ren.setDisabled(True)
        self.toolButton_13 = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_13.setGeometry(QtCore.QRect(310, 20, 71, 68))

        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13.setIcon(icon9)
        self.toolButton_13.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_13.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_13.setAutoRaise(True)
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton_13.setDisabled(True)
        # -----------
        self.toolButton_conn = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_conn.setGeometry(QtCore.QRect(740, 20, 71, 68))
        self.toolButton_conn.setInputMethodHints(QtCore.Qt.ImhNone)
        icon_link = QtGui.QIcon()
        icon_link.addPixmap(QtGui.QPixmap("ui icons/Link-03.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_conn.setIcon(icon_link)
        self.toolButton_conn.setIconSize(QtCore.QSize(31, 31))
        self.toolButton_conn.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_conn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_conn.setAutoRaise(True)
        self.toolButton_conn.setObjectName("toolButton_14")
        self.toolButton_download = QtWidgets.QToolButton(self.Toolbox)
        self.toolButton_download.setGeometry(QtCore.QRect(810, 20, 71, 68))
        self.toolButton_download.setInputMethodHints(QtCore.Qt.ImhNone)
        icon_download = QtGui.QIcon()
        icon_download.addPixmap(QtGui.QPixmap("ui icons/File-download-01.png"), QtGui.QIcon.Normal,
                                QtGui.QIcon.Off)
        self.toolButton_download.setIcon(icon_download)
        self.toolButton_download.setIconSize(QtCore.QSize(45, 45))
        self.toolButton_download.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_download.setAutoRaise(True)
        self.toolButton_download.setObjectName("toolButton_15")
        self.toolButton_download.setDisabled(True)
        self.label = QtWidgets.QLabel(self.Toolbox)
        self.label.setGeometry(QtCore.QRect(1010, 20, 81, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui icons/152086959861286098.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 110, 751, 31))
        self.comboBox_2.setToolTipDuration(0)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_2.setIconSize(QtCore.QSize(22, 22))
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.setObjectName("comboBox_2")
        self.icon18 = QtGui.QIcon()
        self.icon18.addPixmap(QtGui.QPixmap("ui icons/HDD-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # ---------------- Create partition in tree view


        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("ui icons/my-computer-icon-81972.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("ui icons/Hdd-595b40b75ba036ed117d969e.svg"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("ui icons/93096_235205_folder_open.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap("ui icons/folder_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.icon13 = QtGui.QIcon()
        self.icon13.addPixmap(QtGui.QPixmap("ui icons/folder_open.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        self.icon13.addPixmap(QtGui.QPixmap("ui icons/93096_235205_folder_open.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.On)

        self.dps_defualt = psutil.disk_partitions()
        fmt_str = "{:<8}"
        fmt_str.format("Opts")
        self.dps = []
        for i in range(len(self.dps_defualt)):
            if self.dps_defualt[i].opts != 'cdrom':
                self.dps.append(self.dps_defualt[i])

        self.items = []

        for t in range(len(self.dps)):
            self.comboBox_2.addItem(self.icon18, self.dps[t][0])

        # --------------------------
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(11, 110, 256, 689))
        self.treeView.setObjectName("treeView")
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.treeView.setModel(self.model)
        self.treeView.setAnimated(True)
        self.treeView.setIndentation(20)
        self.treeView.setSortingEnabled(True)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 150, 831, 540))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget.setIconSize(QtCore.QSize(25, 25))
        self.tableWidget.setStatusTip("")
        self.tableWidget.setAccessibleName("")
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setIconSize(QtCore.QSize(25, 25))
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")

        self.path = self.comboBox_2.currentText()
        self.lisrdir = os.listdir(self.path)
        self.lisrdir.sort()
        self.row = len(self.lisrdir)
        self.tableWidget.setRowCount(self.row)
        self.tableWidget.setColumnCount(3)
        self.horiitems = []
        self.vertiitems = []
        self.title = ["Name", "Type", "Size"]
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("ui icons/document-icon.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)

        for j in range(len(
                self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(self.lisrdir) radif b tor ofoqi
            for i in range(1, 3):
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.vertiitems.append(item)
                item.setFlags(QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(j, i, item)

        for t in range(3):  # sakhtane header
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

        for i in range(self.row):  # sakhte radif aval hamrah ba icon
            item = QtWidgets.QTableWidgetItem()  # amodi
            self.horiitems.append(item)
            if self.lisrdir[i].endswith(''):
                item.setIcon(self.iconblank)
            fileName, fileExtension = os.path.splitext(self.lisrdir[i])
            fileExtension = fileExtension.lower()

            if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                item.setIcon(self.icon1)
            if self.lisrdir[i].endswith('.zip'):
                item.setIcon(self.icon5)
            if self.lisrdir[i].endswith('.rar'):
                item.setIcon(self.iconrar)
            if self.lisrdir[i].endswith('.pdf'):
                item.setIcon(self.iconpdf)
            if self.lisrdir[i].endswith('.mp3'):
                item.setIcon(self.iconmp3)
            if self.lisrdir[i].endswith('.7zip'):
                item.setIcon(self.icon7zip)
            if self.lisrdir[i].endswith('.jpg'):
                item.setIcon(self.iconjpg)
            if self.lisrdir[i].endswith('.png'):
                item.setIcon(self.iconpng)
            if self.lisrdir[i].endswith('.txt'):
                item.setIcon(self.icontxt)
            if self.lisrdir[i].endswith('.exe'):
                item.setIcon(self.iconexe)
            if self.lisrdir[i].endswith('.py'):
                item.setIcon(self.pyicon)

            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.tableWidget.setItem(i, 0, item)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(230)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(280, 700, 831, 101))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setDisabled(True)
        self.groupBox.setTitle("Media Player")

        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 70, 811, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.toolButton_11 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_11.setGeometry(QtCore.QRect(390, 20, 41, 41))
        self.toolButton_11.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui icons/pause-icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon)
        self.toolButton_11.setIconSize(QtCore.QSize(42, 46))
        self.toolButton_11.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_11.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_11.setAutoRaise(True)
        self.toolButton_11.setObjectName("toolButton_11")

        self.toolButton_10 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_10.setGeometry(QtCore.QRect(345, 20, 41, 41))
        self.toolButton_10.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui icons/media.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon1)
        self.toolButton_10.setIconSize(QtCore.QSize(42, 46))
        self.toolButton_10.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_10.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_10.setAutoRaise(True)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_12 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_12.setGeometry(QtCore.QRect(1040, 110, 31, 31))
        self.toolButton_12.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("ui icons/a5d6aeadedbecb97856e1339f1cb2477.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon19)
        self.toolButton_12.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_12.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_12.setAutoRaise(True)
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_12.setToolTip('Refresh')

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuView_2 = QtWidgets.QMenu(self.menubar)
        self.menuView_2.setObjectName("menuView_2")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.actionOpen_directiory = QtWidgets.QAction(MainWindow)
        self.actionOpen_directiory.setObjectName("actionOpen_directiory")
        self.menuFile.addAction(self.actionOpen_directiory)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuView_2.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolButton_14 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_14.setGeometry(QtCore.QRect(300, 20, 41, 41))
        self.toolButton_14.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui icons/fast-forward - 2Copy.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon)
        self.toolButton_14.setIconSize(QtCore.QSize(42, 46))
        self.toolButton_14.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_14.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_14.setAutoRaise(True)
        self.toolButton_14.setObjectName("toolButton_14")
        self.toolButton_15 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_15.setGeometry(QtCore.QRect(437, 20, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_15.sizePolicy().hasHeightForWidth())
        self.toolButton_15.setSizePolicy(sizePolicy)
        self.toolButton_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_15.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui icons/fast-forward - Copy.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon1)
        self.toolButton_15.setIconSize(QtCore.QSize(42, 46))
        self.toolButton_15.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_15.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_15.setAutoRaise(True)
        self.toolButton_15.setObjectName("toolButton_15")

        # self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        # self.textBrowser.setGeometry(QtCore.QRect(1150, 180, 101, 30))
        # palette = QtGui.QPalette()
        # brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        # brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        # brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        # self.textBrowser.setPalette(palette)
        # self.textBrowser.setInputMethodHints(QtCore.Qt.ImhNone)
        # self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setText('Image Preview')

        self.toolButton_switch = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_switch.setGeometry(QtCore.QRect(1080, 110, 31, 31))
        self.toolButton_switch.setText("")
        icon_switch = QtGui.QIcon()
        icon_switch.addPixmap(QtGui.QPixmap("ui icons/switch-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_switch.setIcon(icon_switch)
        self.toolButton_switch.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_switch.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_switch.setAutoRaise(True)
        self.toolButton_switch.setObjectName("toolButton_16")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.FTP = False
        self.helpFtp = True

        self.tableWidget.cellClicked.connect(self.Mediaplayer)
        self.tableWidget.cellClicked.connect(self.Delete)
        self.tableWidget.cellClicked.connect(self.Copy)
        self.tableWidget.cellClicked.connect(self.Cut)
        self.tableWidget.cellClicked.connect(self.Zip)
        self.tableWidget.cellClicked.connect(self.rename)
        self.tableWidget.cellClicked.connect(self.extract)
        self.tableWidget.cellClicked.connect(self.download)

        # self.tableWidget.cellClicked.connect(self.Imagepreview)

        self.comboBox_2.currentIndexChanged.connect(self.setDisabledDelete)
        self.comboBox_2.currentIndexChanged.connect(self.setDisabledCopy)
        self.comboBox_2.currentIndexChanged.connect(self.setDisabledCut)
        self.comboBox_2.currentIndexChanged.connect(self.setmediaPlayerDis)
        self.comboBox_2.currentIndexChanged.connect(self.setDisZip)
        self.comboBox_2.currentIndexChanged.connect(self.setDisrename)
        self.comboBox_2.currentIndexChanged.connect(self.setDisextract)
        self.comboBox_2.currentIndexChanged.connect(self.setDisdownload)

        self.comboBox_2.currentTextChanged.connect(self.setDisabledDelete)
        self.comboBox_2.currentTextChanged.connect(self.setDisabledCopy)
        self.comboBox_2.currentTextChanged.connect(self.setDisabledCut)
        self.comboBox_2.currentTextChanged.connect(self.setmediaPlayerDis)
        self.comboBox_2.currentTextChanged.connect(self.setDisZip)
        self.comboBox_2.currentTextChanged.connect(self.setDisrename)
        self.comboBox_2.currentTextChanged.connect(self.setDisextract)
        self.comboBox_2.currentTextChanged.connect(self.setDisdownload)

        self.toolButton_3.clicked.connect(self.DeleteItems)
        self.toolButton_4.clicked.connect(self.CopyItems)
        self.toolButton_13.clicked.connect(self.PasteItem)
        self.toolButton_5.clicked.connect(self.CutItems)
        self.toolButton_6.clicked.connect(self.ZipItems)
        self.toolButton.clicked.connect(self.openWindow)
        self.toolButton_12.clicked.connect(self.Refresh)
        self.toolButton_7.clicked.connect(self.Backward)
        self.toolButton_10.clicked.connect(self.playButton)
        self.toolButton_11.clicked.connect(self.pauseButton)
        self.toolButton_15.clicked.connect(self.nextButton)
        self.toolButton_14.clicked.connect(self.previousButton)
        self.toolButton_2.clicked.connect(self.openwindows_2)
        self.treeView.doubleClicked.connect(self.ConnectTreetoTable)
        self.toolButton_9.clicked.connect(self.favourite)
        self.toolButton_ren.clicked.connect(self.renameitems)
        self.toolButton_extract.clicked.connect(self.extractitems)
        self.toolButton_conn.clicked.connect(self.Openconnectionwindows)
        self.toolButton_download.clicked.connect(self.opendownloadwindow)
        #self.pushButton.clicked.connect(self.sendmessege)
        self.toolButton_switch.clicked.connect(self.Switchmode)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_allDuuration = QtWidgets.QLabel(self.centralwidget)
        self.label_allDuuration.setGeometry(QtCore.QRect(1078, 733, 55, 16))
        self.label_allDuuration.setObjectName("label_duration")
        self.label_allDuuration.setDisabled(True)

        self.label_seek = QtWidgets.QLabel(self.centralwidget)
        self.label_seek.setGeometry(QtCore.QRect(1031, 733, 55, 16))
        self.label_seek.setObjectName("label_seek")
        self.label_seek.setDisabled(True)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Toolbox.setTitle(_translate("MainWindow", "Toolbox"))
        self.toolButton.setText(_translate("MainWindow", "New "))
        self.toolButton_2.setText(_translate("MainWindow", "Open"))
        self.toolButton_3.setText(_translate("MainWindow", "Delete"))
        self.toolButton_4.setText(_translate("MainWindow", "Copy"))
        self.toolButton_5.setText(_translate("MainWindow", "Cut"))
        self.toolButton_6.setText(_translate("MainWindow", "Compress"))
        self.toolButton_7.setText(_translate("MainWindow", "Back"))
        self.toolButton_9.setText(_translate("MainWindow", "Favorites"))
        self.toolButton_13.setText(_translate("MainWindow", "Paste"))
        self.toolButton_ren.setText(_translate("MainWindow", "Rename"))
        self.toolButton_extract.setText(_translate("MainWindow", "Extract"))
        self.toolButton_download.setText(_translate("MainWindow", "Download"))
        self.toolButton_conn.setText(_translate("MainWindow", "Make\n""Connection"))
        self.tableWidget.setSortingEnabled(True)

        #        item = self.tableWidget.verticalHeaderItem(0)  # amodi
        #        item.setText(_translate("MainWindow", "1"))

        for j in range(len(self.lisrdir)):  # name gozari type , size ba onvane fuck
            for i in range(1, 2):
                item = self.tableWidget.item(j, i)
                item.setText(_translate("MainWindow", 'File Folder'))
                self.ext = ''
                fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                fileExtension = fileExtension.lower()
                item_2 = self.tableWidget.item(j, i + 1)
                if '.' in fileExtension and len(fileExtension) == 4:
                    self.ext = fileExtension
                    self.size = os.path.getsize(self.path + self.lisrdir[j])
                    item_2.setText(_translate("MainWindow", str(self.size)))
                    item.setText(_translate("MainWindow", self.ext))
                if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                    item.setText(_translate("MainWindow", 'File Folder'))
                item.setFlags(QtCore.Qt.ItemIsSelectable)
                item_2.setFlags(QtCore.Qt.ItemIsSelectable)

        for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
            item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
            item.setText(_translate("MainWindow", self.title[t]))

        for i in range(len(self.lisrdir)):  # name gozari file ha
            item = self.tableWidget.item(i, 0)  # amodi ofoqi
            item.setText(_translate("MainWindow", self.lisrdir[i]))

        # __sortingEnabled = self.tableWidget.isSortingEnabled()
        # self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget.setSortingEnabled(False)

        self.comboBox_2.setToolTip(_translate("MainWindow", "Enter Your Direction and press enter to save"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "D:"))
        self.comboBox_2.currentIndexChanged.connect(self.selectionchange)

        # for j in range(len(self.items)):
        # self.comboBox_2.addItem(self.dps[j][0])
        # self.comboBox_2.setItemText(j, _translate("MainWindow", self.dps[j][0]))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Edit"))
        self.menuView_2.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_directiory.setText(_translate("MainWindow", "Open"))

        self.tableWidget.cellDoubleClicked.connect(self.forward)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("You dont have permission to access this directory")
        self.msg.setWindowTitle("Something went wrong!")
        self.msg.setStandardButtons(QMessageBox.Ok)

        self.msg_new = QMessageBox()
        self.msg_new.setIcon(QMessageBox.Information)
        self.msg_new.setText("The folder already exist")
        self.msg_new.setWindowTitle("Something went wrong!")
        self.msg_new.setStandardButtons(QMessageBox.Ok)

        self.msg_1 = QMessageBox()
        self.msg_1.setIcon(QMessageBox.Information)
        self.msg_1.setText("Directory Error")
        self.msg_1.setWindowTitle("Something went wrong!")
        self.msg_1.setStandardButtons(QMessageBox.Ok)

        self.favaddres_list = []

        self.connectionerrormsg = QMessageBox()
        self.connectionerrormsg.setIcon(QMessageBox.Information)
        self.connectionerrormsg.setText("There is no any connection ! ")
        self.connectionerrormsg.setWindowTitle("Something went wrong!")
        self.connectionerrormsg.setStandardButtons(QMessageBox.Ok)
        self.ftppartition = QtGui.QIcon()
        self.ftppartition.addPixmap(QtGui.QPixmap("ui icons/avaea12247b7eca13ed4b.png"),
                                    QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def Openconnectionwindows(self):
        self.connection_window = QtWidgets.QMainWindow()
        self.ui_connection_window = connection_win.Ui_MainWindow()
        self.ui_connection_window.setupUi(self.connection_window)
        self.connection_window.show()
        self.ui_connection_window.pushButton_2.clicked.connect(self.closeconnectionwindows)
        self.ui_connection_window.pushButton.clicked.connect(self.runserver)
        self.ui_connection_window.pushButton_3.clicked.connect(self.closeconnectionwindows)
        self.ui_connection_window.pushButton_4.clicked.connect(self.runclient)

    def closeconnectionwindows(self):
        self.connection_window.close()

    def runserver(self):
        global status
        status = 'SERVER'
        self.connection_window.close()
        self.runserver1()


    def runserver1(self):
        self.se = SERVER.server()
        self.se.message = ''
        threading.Thread(target=self.se.dicision).start()
        os.startfile('chatserver.py')
        # import chatserver

    def runclient(self):
        status = 'CLIENT'
        threading.Thread(target=self.runclient1()).start()
        os.startfile('chatclient.py')

    def runclient1(self):
        self.Host = self.ui_connection_window.lineEdit_3.text()
        self.file = open("ip.txt", 'w')
        self.file.write(self.Host)
        self.file.close()
        self.cl = CLIENT.client(8080, 8088, self.Host)
        self.cl.connectToServer()
        self.connection_window.close()
        # 2- receive :)
        # 3- self.json_data = self.recieve
        # chatclient.main()

    def download(self):
        if self.FTP == True:
            try:
                self.dlfilepath = os.path.join(self.comboBox_2.currentText(), self.tableWidget.currentItem().text())
            except:
                return None
            if not os.path.isdir(self.dlfilepath):
                self.toolButton_download.setDisabled(False)
            else:
                self.toolButton_download.setDisabled(True)

    def setDisdownload(self):
        self.toolButton_download.setDisabled(True)

    def opendownloadwindow(self):

        # self.download_windows = QtWidgets.QMainWindow()
        # self.ui_download_windows = download_win.Ui_MainWindow()
        # self.ui_download_windows.setupUi(self.download_windows)
        self.itempath = os.path.join(self.comboBox_2.currentText(), self.tableWidget.currentItem().text())
        # self.ui_download_windows.label_6.setText(self.itempath)
        # self.download_windows.show()
        # self.downloadfile()
        # self.progresbar()
        t1 = threading.Thread(target=self.downloadfile())
        # t2 = threading.Thread(target=self.progresbar())
        # t2.start()
        t1.start()

    def downloadfile(self):
        self.cl.sendFileRequest(self.itempath)

    def progresbar(self):
        print(self.cl.filesize)
        self.originalsize = self.cl.filesize
        self.ui_download_windows.progressBar.setRange(1, 100)
        self.sizefile = convert_bytes(self.cl.filesize)
        self.ui_download_windows.label_8.setText(str(self.sizefile))

        self.recvsize = 0
        while self.recvsize != self.originalsize:
            print(self.recvsize)
            self.recvsize = os.path.getsize(self.cl.filename.decode('ascii'))
            self.progressvalue = int((self.recvsize / self.originalsize) * 100)
            # print(self.progressvalue)
            self.ui_download_windows.progressBar.setValue(self.progressvalue)
            self.download_windows.show()

    def Switchmode(self, json_data):
        # self.json_data = json.dumps(json_data)
        # yek list recv mishavad az samt on yeki :)

        self.FTP, self.helpFtp = self.helpFtp, self.FTP
        # 1-send request to get  another system partition
        # 4-if self.json_data['title'] == 'Parition':
        # 5-self.drivelist = self.json_data['content']

        self.drivelist = []
        for i in self.cl.dps:
            self.drivelist.append(i + '\\')

        self.pathlist = []
        self.connection = True
        if self.connection == True:
            if self.FTP == False:
                for t in range(len(self.dps) - len(self.drivelist)):
                    self.comboBox_2.addItem(self.icon18, self.dps[t][0])
                for q in range(len(self.dps)):
                    self.comboBox_2.setItemText(q, self.dps[q][0])
                    self.comboBox_2.setItemIcon(q, self.icon18)
                    # self.toolButton.setDisabled(False)
                    self.toolButton_2.setDisabled(False)
                    self.toolButton_9.setDisabled(False)
                    self.selectionchange()
                return None
            if len(self.drivelist) >= len(self.dps):
                for t in range(len(self.drivelist) - len(self.dps)):
                    self.comboBox_2.addItem(self.icon18, "None")
                for t in range(len(self.drivelist)):
                    self.comboBox_2.setItemText(t, self.drivelist[t])
            if len(self.drivelist) <= len(self.dps):
                for t in range(len(self.drivelist)):
                    self.comboBox_2.setItemText(t, self.drivelist[t])
                for q in range(len(self.drivelist), len(self.dps)):
                    self.comboBox_2.removeItem(q)
            # self.toolButton.setDisabled(True)
            self.toolButton_2.setDisabled(True)
            self.toolButton_9.setDisabled(True)
            self.selectionchange()

        else:
            self.connectionerrormsg.show()

    def selectionchange(self):
        _translate = QtCore.QCoreApplication.translate
        # print("Current index", i, "selection changed ", self.comboBox_2.currentText())
        self.path = self.comboBox_2.currentText()
        if self.FTP == False:
            # if self.FTP == TRUE:
            # send : self.comboBox_2.currentText()
            # Receive: directory list :)
            self.lisrdir = os.listdir(self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)
                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size ba onvane fuck
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        self.size = os.path.getsize(self.path + self.lisrdir[j])
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)

                # if self.FTP == True:
        if self.FTP == True:
            self.lisrdir = self.cl.listdirRequest(self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)
                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size ba onvane fuck
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)
                # if self.FTP == True:

    def forward(self):
        _translate = QtCore.QCoreApplication.translate
        if self.FTP == False:
            self.clickeditem = self.tableWidget.currentItem()
            fileName, fileExtension = os.path.splitext(self.clickeditem.text())
            self.opendirfile = self.comboBox_2.currentText()
            self.opendirfile = os.path.join(self.comboBox_2.currentText(), self.clickeditem.text())

            if fileExtension == '.png' or fileExtension == '.jpg' or fileExtension == '.jpeg' or fileExtension == '.gif':
                img = Image.open(self.opendirfile)
                img.show()
            elif fileExtension == '.txt':
                programName = "notepad.exe"
                sp.Popen([programName, self.opendirfile])

            elif fileExtension == '.txt':
                programName = "notepad.exe"
                sp.Popen([programName, self.opendirfile])

            elif fileExtension == '.mp4' or fileExtension == '.mpg' or fileExtension == '.mkv' or fileExtension == '.mov' or fileExtension == '.flv' or fileExtension == '.3gp' or fileExtension == '.mpeg':
                startfile(self.opendirfile)

            elif fileExtension == '.pdf':
                sp.Popen([self.opendirfile], shell=True)

            elif fileExtension == '.exe':
                os.startfile(self.opendirfile)

            elif not os.path.isdir(self.opendirfile) and fileExtension != '.zip':
                try:
                    os.startfile(self.opendirfile)
                except:
                    pass

            if os.path.isdir(self.opendirfile):
                # if fileExtension == '' or len(fileExtension) > 4 or len(fileExtension) == 2:
                self.addpath = self.clickeditem.text()
                self.path = self.comboBox_2.currentText()
                self.path = os.path.join(self.path, self.addpath)
                try:
                    self.lisrdir = os.listdir(self.path)
                except PermissionError:
                    self.msg.exec_()
                    self.path = self.comboBox_2.currentText()
                except NotADirectoryError:
                    self.msg_1.exec_()
                    self.path = self.comboBox_2.currentText()
                self.num = self.comboBox_2.currentIndex()
                self.comboBox_2.setItemText(self.num, self.path)
                self.lisrdir.sort()
                self.row = len(self.lisrdir)
                # print(self.row)
                self.tableWidget.clear()
                self.tableWidget.setRowCount(self.row)
                self.tableWidget.setIconSize(QtCore.QSize(25, 25))
                self.vertiitems = []
                self.horiitems = []
                # print(self.lisrdir)
                # print(len(self.lisrdir))
                for j in range(len(
                        self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                    # self.lisrdir) radif b tor ofoqi
                    for i in range(1, 3):
                        item = QtWidgets.QTableWidgetItem()  # amodi
                        self.vertiitems.append(item)
                        item.setFlags(QtCore.Qt.ItemIsEnabled)
                        self.tableWidget.setItem(j, i, item)

                for t in range(3):  # sakhtane header
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

                for i in range(self.row):  # sakhte radif aval hamrah ba icon
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.horiitems.append(item)
                    if self.lisrdir[i].endswith(''):
                        item.setIcon(self.iconblank)
                    fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                    fileExtension = fileExtension.lower()
                    # if len(fileExtension) != 4 and len(fileExtension) != 6 and len(fileExtension) != 5:
                    #    item.setIcon(self.icon1)
                    if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                        item.setIcon(self.icon1)

                    # print(fileExtension)
                    if self.lisrdir[i].endswith('.zip'):
                        item.setIcon(self.icon5)
                    if self.lisrdir[i].endswith('.rar'):
                        item.setIcon(self.iconrar)
                    if self.lisrdir[i].endswith('.pdf'):
                        item.setIcon(self.iconpdf)
                    if self.lisrdir[i].endswith('.mp3'):
                        item.setIcon(self.iconmp3)
                    if self.lisrdir[i].endswith('.7zip'):
                        item.setIcon(self.icon7zip)
                    if self.lisrdir[i].endswith('.jpg'):
                        item.setIcon(self.iconjpg)
                    if self.lisrdir[i].endswith('.png'):
                        item.setIcon(self.iconpng)
                    if self.lisrdir[i].endswith('.txt'):
                        item.setIcon(self.icontxt)
                    if self.lisrdir[i].endswith('.exe'):
                        item.setIcon(self.iconexe)
                    if self.lisrdir[i].endswith('.py'):
                        item.setIcon(self.pyicon)

                    item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                    self.tableWidget.setItem(i, 0, item)

                for i in range(len(self.lisrdir)):  # name gozari file ha
                    item = self.tableWidget.item(i, 0)  # amodi ofoqi
                    item.setText(_translate("MainWindow", self.lisrdir[i]))

                for j in range(len(self.lisrdir)):  # name gozari type , size
                    for i in range(1, 2):
                        item = self.tableWidget.item(j, i)
                        if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                            item.setText(_translate("MainWindow", 'File Folder'))
                        self.ext = ''
                        fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                        item_2 = self.tableWidget.item(j, i + 1)
                        if '.' in fileExtension and len(fileExtension) >= 4:
                            self.ext = fileExtension
                            self.size = os.path.getsize(os.path.join(self.path, self.lisrdir[j]))
                            item_2.setText(_translate("MainWindow", str(self.size)))
                            item.setText(_translate("MainWindow", self.ext))
                        if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                            item.setText(_translate("MainWindow", 'File Folder'))
                        item.setFlags(QtCore.Qt.ItemIsSelectable)
                        item_2.setFlags(QtCore.Qt.ItemIsSelectable)

                for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                    item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                    item.setText(_translate("MainWindow", self.title[t]))
                    # self.comboBox_2.addItem(self.path)
                    # self.comboBox_2.setCurrentText(self.path)

            self.pathMusics = []
            self.currentpathmusic = self.comboBox_2.currentText()
            self.listmusic = os.listdir(self.currentpathmusic)
            for i in range(len(self.listmusic)):
                if self.listmusic[i].endswith('.mp3'):
                    self.pathMusics.append(self.currentpathmusic + self.listmusic[i])

        if self.FTP == True:
            self.clickeditem = self.tableWidget.currentItem()
            fileName, fileExtension = os.path.splitext(self.clickeditem.text())
            self.opendirfile = self.comboBox_2.currentText()
            self.opendirfile = os.path.join(self.comboBox_2.currentText(), self.clickeditem.text())

            self.addpath = self.clickeditem.text()
            self.path = self.comboBox_2.currentText()
            self.path = os.path.join(self.path, self.addpath)
            try:
                self.lisrdir = self.cl.listdirRequest(self.path)
            except PermissionError:
                self.msg.exec_()
                self.path = self.comboBox_2.currentText()
            except NotADirectoryError:
                self.msg_1.exec_()
                self.path = self.comboBox_2.currentText()
            self.num = self.comboBox_2.currentIndex()
            self.comboBox_2.setItemText(self.num, self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                # if len(fileExtension) != 4 and len(fileExtension) != 6 and len(fileExtension) != 5:
                #    item.setIcon(self.icon1)
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)

                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)

    def Backward(self):
        _translate = QtCore.QCoreApplication.translate
        if self.FTP == False:
            self.path = self.comboBox_2.currentText()
            try:
                os.chdir(self.path)
                os.chdir('..')
                self.path = os.getcwd()
                self.lisrdir = os.listdir(self.path)
            except:
                pass
            self.num = self.comboBox_2.currentIndex()
            self.comboBox_2.setItemText(self.num, self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)
                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size ba onvane fuck
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        self.size = os.path.getsize(os.path.join(self.path, self.lisrdir[j]))
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)

                # def Imagepreview(self):
                #    self.clickeditem_img = self.tableWidget.currentItem()
                #    self.imagepath = self.comboBox_2.currentText()
                #    self.imagepath += self.clickeditem_img.text()
                #    self.label_2.setScaledContents(True)
                #    self.label_2.setPixmap(QtGui.QPixmap(self.imagepath))

        if self.FTP == True:
            self.path = self.comboBox_2.currentText()
            self.lst = self.path.split("\\")
            self.path = ''
            for i in range(len(self.lst) - 1):
                self.path += self.lst[i] + '\\'
            if len(self.path) > 4:
                self.path = self.path[0:len(self.path) - 1]
            try:
                self.lisrdir = self.cl.listdirRequest(self.path)
            except:
                pass
            self.num = self.comboBox_2.currentIndex()
            self.comboBox_2.setItemText(self.num, self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)
                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size ba onvane fuck
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)

                # def Imagepreview(self):
                #    self.clickeditem_img = self.tableWidget.currentItem()
                #    self.imagepath = self.comboBox_2.currentText()
                #    self.imagepath += self.clickeditem_img.text()
                #    self.label_2.setScaledContents(True)
                #    self.label_2.setPixmap(QtGui.QPixmap(self.imagepath))

    def Mediaplayer(self):
        self.clickeditem = self.tableWidget.currentItem()
        if not self.clickeditem and not mp3Player.playing and not mp3Player.paused:
            # print(1, mp3Player.paused)
            self.groupBox.setDisabled(True)
            return None

        self.name = self.clickeditem.text()
        self.musicname = ''
        if self.name.endswith('.mp3'):
            self.groupBox.setDisabled(False)
            self.musicname = self.clickeditem.text()
        elif not mp3Player.playing and not mp3Player.paused:
            # print(2, mp3Player.paused)
            self.groupBox.setDisabled(True)

        self.musicpath = self.comboBox_2.currentText()
        if self.groupBox.setDisabled:
            self.musicpath += self.musicname
            # print(self.musicpath)
        # self.musicpath = self.musicpath.replace("\\","/")
        print(self.musicpath)

    def playButton(self):
        if mp3Player.playList == self.pathMusics and not mp3Player.playing:
            mp3Player.play()
        elif mp3Player.playList == self.pathMusics and mp3Player.playing:
            mp3Player.pause()
            mp3Player.jumpInPlayList(self.musicpath)
        elif mp3Player.playList != self.pathMusics:
            mp3Player.pause()
            mp3Player.clearPlayList()
            mp3Player.playList = self.pathMusics
            mp3Player.jumpInPlayList(self.musicpath)
        self.movingSlider = threading.Thread(target=self.moveSlider)
        self.movingSlider.start()

    def pauseButton(self):
        mp3Player.pause()

    def nextButton(self):
        mp3Player.next()

    def previousButton(self):
        mp3Player.previous()

    def moveSlider(self):
        _translate = QtCore.QCoreApplication.translate
        self.musicDuration = MP3(mp3Player.playList[mp3Player.n]).info.length
        while (mp3Player.player.time != self.musicDuration):
            self.horizontalSlider.setSliderPosition(round((mp3Player.player.time / self.musicDuration) * 1000))
            self.label_allDuuration.setText(_translate("MainWindow", str(int(self.musicDuration))))
            self.label_seek.setText(_translate("MainWindow", str(int(mp3Player.player.time)) + "  |"))

    def setmediaPlayerDis(self):
        if not mp3Player.playing and not mp3Player.paused:
            # print(3, mp3Player.paused)
            self.groupBox.setDisabled(True)
            self.label.setDisabled(True)

    def rename(self):
        if self.FTP == False:
            self.clickeditem_ren = self.tableWidget.currentItem()
            if not self.clickeditem_ren:
                self.toolButton_ren.setDisabled(True)
            else:
                self.toolButton_ren.setDisabled(False)

            self.renamepath = self.comboBox_2.currentText()
            try:
                self.renamepath += self.clickeditem_1.text()
            except:
                pass

    def renameitems(self):

        self.window_4 = QtWidgets.QMainWindow()
        self.ui_4 = renamewindows.Ui_OtherWindows()
        self.ui_4.setupUi(self.window_4)
        self.ui_4.lineEdit.setText(self.clickeditem_ren.text())

        self.window_4.show()

        self.ui_4.pushButton.clicked.connect(self.closerename)

    def closerename(self):
        self.newname = self.ui_4.lineEdit.text()
        self.renamepathdir = self.comboBox_2.currentText()
        self.renameitem = self.tableWidget.currentItem().text()
        if self.FTP == False:
            try:
                os.rename(os.path.join(self.renamepathdir, self.renameitem),
                          os.path.join(self.renamepathdir, self.newname))
            except:
                pass

        self.window_4.close()
        self.Refresh()

    def setDisrename(self):
        self.toolButton_ren.setDisabled(True)

    def Delete(self):
        self.clickeditem_1 = self.tableWidget.currentItem()
        if not self.clickeditem_1:
            self.toolButton_3.setDisabled(True)
        else:
            self.toolButton_3.setDisabled(False)
        self.deletepath = self.comboBox_2.currentText()
        self.rootpath = self.comboBox_2.currentText()
        try:
            self.deletepath += self.clickeditem_1.text()
        except:
            pass

    def DeleteItems(self):
        # delete file
        # file path is = self.deletepath
        if self.FTP == False:
            if os.path.isdir(self.deletepath):
                try:
                    shutil.rmtree(self.deletepath)
                except:
                    pass

            if os.path.isdir(self.deletepath):
                try:
                    os.removedirs(self.deletepath)
                except:
                    pass

            if not os.path.isdir(self.deletepath):
                try:
                    os.remove(self.deletepath)
                except:
                    pass
            self.Refresh()

        if self.FTP == True:
            self.cl.deleteRequest(self.deletepath)
            self.Refresh()

    def setDisabledDelete(self):
        self.toolButton_3.setDisabled(True)

    def setDisextract(self):
        self.toolButton_extract.setDisabled(True)

    def extract(self):
        if self.FTP == False:
            try:
                self.clickeditem_extract = self.tableWidget.currentItem().text()
            except:
                pass
            try:
                if self.clickeditem_extract.endswith(".zip"):
                    self.toolButton_extract.setDisabled(False)
                else:
                    self.toolButton_extract.setDisabled(True)
            except:
                pass
            try:
                self.extractpath = os.path.join(self.comboBox_2.currentText(), self.clickeditem_extract)
            except:
                pass

    def extractitems(self):
        _translate = QtCore.QCoreApplication.translate
        if self.FTP == False:
            self.myzip = zipfile.ZipFile(self.extractpath)
            self.havepass = False
            for zinfo in self.myzip.infolist():
                have_pass = zinfo.flag_bits & 0x1
                if have_pass:
                    self.havepass = True
                else:
                    self.havepass = False

            self.window_extract = QtWidgets.QMainWindow()
            self.ui_extract = otherwindows.Ui_OtherWindos()
            self.ui_extract.setupUi(self.window_extract)
            self.ui_extract.label.setText(_translate("OtherWindos", "Enter Password:"))
            if have_pass:
                self.window_extract.show()

            self.ui_extract.pushButton.clicked.connect(self.Closewindowsext)
            if not have_pass:
                self.extractfile()

    def Closewindowsext(self):
        self.pwd = self.ui_extract.lineEdit.text()
        try:
            self.myzip.extractall(path=self.extractpath[:len(self.extractpath) - 4], pwd=self.pwd.encode('ascii'))
        except:
            pass
        self.window_extract.close()
        self.Refresh()

    def extractfile(self):
        if self.FTP == False:
            try:
                self.myzip.extractall(path=self.extractpath[:len(self.extractpath) - 4])
            except:
                pass
            self.Refresh()

    def Copy(self):
        self.clickeditem_2 = self.tableWidget.currentItem()
        if not self.clickeditem_2:
            self.toolButton_4.setDisabled(True)
        else:
            self.toolButton_4.setDisabled(False)

    def setDisabledCopy(self):
        self.toolButton_4.setDisabled(True)

    def CopyItems(self):
        self.method = 'Copy'
        self.copyingfile = self.comboBox_2.currentText()
        try:
            # self.copyingfile = self.copyingfile + "\\" + self.clickeditem_2.text()
            self.copyingfile = os.path.join(self.copyingfile, self.clickeditem_2.text())

        except:
            pass

        if self.copyingfile:
            self.toolButton_13.setDisabled(False)
        print('cp' + self.copyingfile)

    def Cut(self):
        self.clickeditem_3 = self.tableWidget.currentItem()
        if not self.clickeditem_3:
            self.toolButton_5.setDisabled(True)
        else:
            self.toolButton_5.setDisabled(False)

    def CutItems(self):
        self.method = 'Cut'
        self.copyingfile = self.comboBox_2.currentText()
        try:
            self.copyingfile = os.path.join(self.copyingfile, self.clickeditem_3.text())
        except:
            pass

        if self.copyingfile:
            self.toolButton_13.setDisabled(False)
        print(self.copyingfile)

    def setDisabledCut(self):
        self.toolButton_5.setDisabled(True)

    def PasteItem(self):
        # print('cp' + self.copyingfile)
        # paste to addressi k ma migim
        self.pastetoadrs = self.comboBox_2.currentText()
        if self.FTP == False:
            try:
                shutil.copy2(self.copyingfile, self.pastetoadrs)
            except:
                pass
            if self.method == 'Cut':
                try:
                    os.remove(self.copyingfile)
                except:
                    pass
            self.Refresh()
            print('ps' + self.pastetoadrs)
            self.toolButton_13.setDisabled(True)
        if self.FTP == True:
            if self.method == 'Copy':
                self.cl.copyRequest(self.copyingfile, self.pastetoadrs)
            if self.method == 'Cut':
                self.cl.copyRequest(self.copyingfile, self.pastetoadrs)
                self.cl.deleteRequest(self.copyingfile)
            self.Refresh()

    def Zip(self):
        if self.FTP == False:
            self.clickeditem_4 = self.tableWidget.currentItem()
            if not self.clickeditem_4:
                self.toolButton_6.setDisabled(True)
            else:
                self.toolButton_6.setDisabled(False)

    def ZipItems(self):
        if self.FTP == False:
            self.Zipingpath = self.comboBox_2.currentText()
            fileName, fileExtension = os.path.splitext(self.clickeditem_4.text())
            if fileExtension == '' or len(fileExtension) > 4 or len(fileExtension) == 23:
                self.dis = self.comboBox_2.currentText()
                try:
                    self.Zipingpath += self.clickeditem_4.text()
                except:
                    pass

                shutil.make_archive(os.path.join(self.dis, self.clickeditem_4.text()), "zip", self.Zipingpath)
                self.Refresh()
                # print(self.Zipingpath)
                # zip kon to adres feli

    def setDisZip(self):
        self.toolButton_6.setDisabled(True)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = otherwindows.Ui_OtherWindos()
        self.ui.setupUi(self.window)
        self.window.show()

        self.currentpath = self.comboBox_2.currentText()
        # creata dir to in masir feli
        self.currentElements = os.listdir()

        self.ui.pushButton.clicked.connect(self.Closewindows)

    def Closewindows(self):
        if self.FTP == False:
            self.window.close()
            os.chdir(self.currentpath)
            self.newdirname = self.ui.lineEdit.text()
            try:
                os.mkdir(self.newdirname)
            except:
                self.msg_new.show()
            self.Refresh()
        if self.FTP == True:
            self.window.close()
            self.newdirname = self.ui.lineEdit.text()
            self.newpath = os.path.join(self.comboBox_2.currentText(), self.newdirname)
            try:
                self.cl.mkdirRequest(self.newpath)
            except:
                self.msg_new.show()
            self.Refresh()

    def openwindows_2(self):
        self.window_2 = QtWidgets.QMainWindow()
        self.ui_2 = Openfilewindows.Ui_Openfolder()
        self.ui_2.setupUi(self.window_2)
        self.window_2.show()

        self.ui_2.pushButton.clicked.connect(self.Closewindows_2)

    def Closewindows_2(self):
        _translate = QtCore.QCoreApplication.translate
        if self.FTP == False:
            self.window_2.close()
            self.godir = self.ui_2.comboBox.currentText()
            print(self.godir)
            self.comboBox_2.setCurrentText(self.godir)
            self.path = self.godir
            try:
                self.lisrdir = os.listdir(self.path)
            except PermissionError:
                self.msg.exec_()
                self.path = self.comboBox_2.currentText()
            except NotADirectoryError:
                self.msg_1.exec_()
                self.path = self.comboBox_2.currentText()
            except FileNotFoundError:
                self.msg_1.exec_()
                self.path = self.comboBox_2.currentText()
            self.num = self.comboBox_2.currentIndex()
            self.comboBox_2.setItemText(self.num, self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)
                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size ba onvane fuck
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        self.size = os.path.getsize(os.path.join(self.path, self.lisrdir[j]))
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)

            self.pathMusics = []
            self.currentpathmusic = self.comboBox_2.currentText()
            self.listmusic = os.listdir(self.currentpathmusic)
            for i in range(len(self.listmusic)):
                if self.listmusic[i].endswith('.mp3'):
                    self.pathMusics.append(self.currentpathmusic + self.listmusic[i])

    def Refresh(self):
        self.toolButton_6.setDisabled(True)
        self.toolButton_4.setDisabled(True)
        self.toolButton_5.setDisabled(True)
        self.toolButton_3.setDisabled(True)
        self.toolButton_ren.setDisabled(True)

        _translate = QtCore.QCoreApplication.translate
        # print("Current index", i, "selection changed ", self.comboBox_2.currentText())
        if self.FTP == False:
            self.path = self.comboBox_2.currentText()
            self.lisrdir = os.listdir(self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), + self.lisrdir[i])):
                    item.setIcon(self.icon1)
                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size ba onvane fuck
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                    self.size = os.path.getsize(os.path.join(self.path, self.lisrdir[j]))
                    item_2.setText(_translate("MainWindow", str(self.size)))
                    item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

                    for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                        item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                    item.setText(_translate("MainWindow", self.title[t]))
                    # self.comboBox_2.addItem(self.path)
                    # self.comboBox_2.setCurrentText(self.path)

        if self.FTP == True:
            self.path = self.comboBox_2.currentText()
            try:
                self.lisrdir = self.cl.listdirRequest(self.path)
            except PermissionError:
                self.msg.exec_()
                self.path = self.comboBox_2.currentText()
            except NotADirectoryError:
                self.msg_1.exec_()
                self.path = self.comboBox_2.currentText()
            self.num = self.comboBox_2.currentIndex()
            self.comboBox_2.setItemText(self.num, self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                # if len(fileExtension) != 4 and len(fileExtension) != 6 and len(fileExtension) != 5:
                #    item.setIcon(self.icon1)
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)

                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)

    def ConnectTreetoTable(self):
        _translate = QtCore.QCoreApplication.translate
        if self.FTP == False:
            self.pathfromtree = self.model.filePath(self.treeView.currentIndex())
            self.path = self.pathfromtree
            self.path = self.path.replace("/", "\\")
            self.comboBox_2.setCurrentText(self.path)
            try:
                self.lisrdir = os.listdir(self.path)
            except PermissionError:
                self.msg.exec_()
                self.path = self.comboBox_2.currentText()
            except NotADirectoryError:
                self.msg_1.exec_()
                self.path = self.comboBox_2.currentText()
            self.num = self.comboBox_2.currentIndex()
            self.comboBox_2.setItemText(self.num, self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                # if len(fileExtension) != 4 and len(fileExtension) != 6 and len(fileExtension) != 5:
                #    item.setIcon(self.icon1)
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)

                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)
            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        self.size = os.path.getsize(os.path.join(self.path, self.lisrdir[j]))
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)
            self.pathMusics = []
            self.currentpathmusic = self.comboBox_2.currentText()
            self.listmusic = os.listdir(self.currentpathmusic)
            for i in range(len(self.listmusic)):
                if self.listmusic[i].endswith('.mp3'):
                    self.pathMusics.append(self.currentpathmusic + self.listmusic[i])

    def favourite(self):
        _translate = QtCore.QCoreApplication.translate
        if self.FTP == False:
            self.window_3 = QtWidgets.QMainWindow()
            self.ui_3 = favourite.Ui_Openfolder()
            self.ui_3.setupUi(self.window_3)
            self.window_3.show()
            self.favaddres = self.comboBox_2.currentText()
            self.ui_3.label_2.setText(_translate("Openfolder", self.favaddres))
            self.ui_3.pushButton_2.clicked.connect(self.addToFav)
            for i in range(len(self.favaddres_list)):
                self.ui_3.comboBox.addItem(self.staricon, self.favaddres_list[i])

            self.ui_3.pushButton_2.clicked.connect(self.Closewindows_3)
            self.ui_3.pushButton.clicked.connect(self.gotofavadrs)

    def addToFav(self):
        if self.FTP == False:
            self.favaddres = self.comboBox_2.currentText()
            if not self.favaddres in self.favaddres_list:
                self.favaddres_list.append(self.favaddres)

            self.ui_3.comboBox.setCurrentIndex(len(self.favaddres_list) - 1)

    def gotofavadrs(self):
        _translate = QtCore.QCoreApplication.translate
        if self.FTP == False:
            self.window_3.close()

            self.godir = self.ui_3.comboBox.currentText()
            self.comboBox_2.setCurrentText(self.godir)
            self.path = self.godir
            try:
                self.lisrdir = os.listdir(self.path)
            except PermissionError:
                self.msg.exec_()
                self.path = self.comboBox_2.currentText()
            except NotADirectoryError:
                self.msg_1.exec_()
                self.path = self.comboBox_2.currentText()
            except FileNotFoundError:
                self.msg_1.exec_()
                self.path = self.comboBox_2.currentText()

            self.num = self.comboBox_2.currentIndex()
            self.comboBox_2.setItemText(self.num, self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            # print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            # print(self.lisrdir)
            # print(len(self.lisrdir))
            for j in range(len(
                    self.lisrdir)):  # sakht radif aval radif dovom radif sevom be tor amodi , sakht 1 ta len(
                # self.lisrdir) radif b tor ofoqi
                for i in range(1, 3):
                    item = QtWidgets.QTableWidgetItem()  # amodi
                    self.vertiitems.append(item)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(j, i, item)

            for t in range(3):  # sakhtane header
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setHorizontalHeaderItem(t, item)  # ofoqi

            for i in range(self.row):  # sakhte radif aval hamrah ba icon
                item = QtWidgets.QTableWidgetItem()  # amodi
                self.horiitems.append(item)
                if self.lisrdir[i].endswith(''):
                    item.setIcon(self.iconblank)
                fileName, fileExtension = os.path.splitext(self.lisrdir[i])
                fileExtension = fileExtension.lower()
                if os.path.isdir(os.path.join(self.comboBox_2.currentText(), self.lisrdir[i])):
                    item.setIcon(self.icon1)
                # print(fileExtension)
                if self.lisrdir[i].endswith('.zip'):
                    item.setIcon(self.icon5)
                if self.lisrdir[i].endswith('.rar'):
                    item.setIcon(self.iconrar)
                if self.lisrdir[i].endswith('.pdf'):
                    item.setIcon(self.iconpdf)
                if self.lisrdir[i].endswith('.mp3'):
                    item.setIcon(self.iconmp3)
                if self.lisrdir[i].endswith('.7zip'):
                    item.setIcon(self.icon7zip)
                if self.lisrdir[i].endswith('.jpg'):
                    item.setIcon(self.iconjpg)
                if self.lisrdir[i].endswith('.png'):
                    item.setIcon(self.iconpng)
                if self.lisrdir[i].endswith('.txt'):
                    item.setIcon(self.icontxt)
                if self.lisrdir[i].endswith('.exe'):
                    item.setIcon(self.iconexe)
                if self.lisrdir[i].endswith('.py'):
                    item.setIcon(self.pyicon)

                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.tableWidget.setItem(i, 0, item)

            for i in range(len(self.lisrdir)):  # name gozari file ha
                item = self.tableWidget.item(i, 0)  # amodi ofoqi
                item.setText(_translate("MainWindow", self.lisrdir[i]))

            for j in range(len(self.lisrdir)):  # name gozari type , size ba onvane fuck
                for i in range(1, 2):
                    item = self.tableWidget.item(j, i)
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    self.ext = ''
                    fileName, fileExtension = os.path.splitext(self.lisrdir[j])
                    item_2 = self.tableWidget.item(j, i + 1)
                    if '.' in fileExtension and len(fileExtension) >= 4:
                        self.ext = fileExtension
                        self.size = os.path.getsize(os.path.join(self.path, self.lisrdir[j]))
                        item_2.setText(_translate("MainWindow", str(self.size)))
                        item.setText(_translate("MainWindow", self.ext))
                    if os.path.isdir(os.path.join(self.path, self.lisrdir[j])):
                        item.setText(_translate("MainWindow", 'File Folder'))
                    item.setFlags(QtCore.Qt.ItemIsSelectable)
                    item_2.setFlags(QtCore.Qt.ItemIsSelectable)

            for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
                item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
                item.setText(_translate("MainWindow", self.title[t]))
                # self.comboBox_2.addItem(self.path)
                # self.comboBox_2.setCurrentText(self.path)

            self.pathMusics = []
            self.currentpathmusic = self.comboBox_2.currentText()
            self.listmusic = os.listdir(self.currentpathmusic)
            for i in range(len(self.listmusic)):
                if self.listmusic[i].endswith('.mp3'):
                    self.pathMusics.append(self.currentpathmusic + self.listmusic[i])

    def Closewindows_3(self):
        self.window_3.close()

    '''
    def sendmessege(self):
        self.message = self.lineEdit.text()
        self.message = "Client : " + self.message
        self.cl.chat(self.message)
        item = QtWidgets.QListWidgetItem()
        icon_client = QtGui.QIcon()
        icon_client.addPixmap(QtGui.QPixmap("ui icons/78373.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon_client)
        self.listWidget.addItem(item)
        item.setText(self.message)
        self.lineEdit.clear()
        # self.recivemsg()

    def recivemsg(self):
        global status

        while True:
            self.chatfile = open('chatfile.txt', 'r')
            for i in self.chatfile:
                self.recmessage = i
                if status == 'SERVER':
                    self.recmessage = "client : " + self.recmessage
                elif status == 'Client':
                    self.recmessage = "server : " + self.recmessage
                item = QtWidgets.QListWidgetItem()
                icon_server = QtGui.QIcon()
                if status == 'SERVER':
                    icon_server.addPixmap(QtGui.QPixmap("ui icons/7837543 (1).png"), QtGui.QIcon.Normal,
                                          QtGui.QIcon.Off)
                elif status == 'CLIENT':
                    icon_client.addPixmap(QtGui.QPixmap("ui icons/78373.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon_server)
                self.listWidget.addItem(item)
                item.setText(self.recmessage)
        '''
    '''
    item = QtWidgets.QListWidgetItem()
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap("ui icons/78373.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    item.setIcon(icon5)
    self.listWidget.addItem(item)
    item = self.listWidget.item(1)
    item.setText(_translate("MainWindow", "Client : "))
    item = self.listWidget.item(2)
    item.setText(_translate("MainWindow", "Server:"))
    item = QtWidgets.QListWidgetItem()
    self.listWidgetitems.append(item)
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap("ui icons/78373.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    item.setIcon(icon5)
    self.listWidget.addItem(item)
    item = QtWidgets.QListWidgetItem()
    self.listWidgetitems.append(item)
    item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
    icon6 = QtGui.QIcon()
    icon6.addPixmap(QtGui.QPixmap("ui icons/7837543 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    item.setIcon(icon6)
    self.listWidget.addItem(item)
    '''


if __name__ == "__main__":
    import sys


    def convert_bytes(num):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    if app.exec_() == 0:
        if mp3Player.player.source != None:
            mp3Player.seek(ui.musicDuration)
            mp3Player.stop()
        '''ui.movingSlider._is_stopped = True
        ui.movingSlider._tstate_lock = None'''

    sys.exit(app.exec_())
