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
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import mp3Player
from mutagen.mp3 import MP3

mp3Player = mp3Player.mp3Player()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 860)
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
        self.toolButton_7.setGeometry(QtCore.QRect(530, 20, 71, 68))
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
        self.label = QtWidgets.QLabel(self.Toolbox)
        self.label.setGeometry(QtCore.QRect(1010, 20, 81, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui icons/152086959861286098.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 110, 791, 31))
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

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QtCore.QRect(10, 110, 256, 691))
        self.treeWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropOverwriteMode(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")

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
        self.treeWidget.headerItem().setIcon(0, icon10)
        '''
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget) #create one drive
        item_0.setIcon(0, icon11)
        item_1 = QtWidgets.QTreeWidgetItem(item_0) # create two drive

        item_1.setIcon(0, icon12)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)#
        item_0.setIcon(0, icon11)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_1.setIcon(0, icon13)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        '''

        self.dps_defualt = psutil.disk_partitions()
        fmt_str = "{:<8}"
        fmt_str.format("Opts")
        self.dps = []
        for i in range(len(self.dps_defualt)):
            if self.dps_defualt[i].opts != 'cdrom':
                self.dps.append(self.dps_defualt[i])

        self.items = []
        for i in range(len(self.dps)):
            j_item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            j_item.setIcon(0, icon11)
            # self.dir = os.listdir(self.dps[i][0])
            '''3
            for root, dirs, files in os.walk("H:\\"):
                a = dirs
                for t in range(len())

            for t in range(len(self.dir)):
                self.folder = QtWidgets.QTreeWidgetItem(j_item)
                self.folder.setIcon(0, icon13)
                self.treeWidget.topLevelItem(i).child(t).setText(0, _translate("MainWindow", self.dir[t]))
                #self.dir_2 = os.listdir(self.dps[i][0] + self.dir[t])
            '''
            self.items.append(j_item)

        for t in range(len(self.dps)):
            self.comboBox_2.addItem(self.icon18, self.dps[t][0])

        # --------------------------

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

            if fileExtension == '':
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
        self.toolButton_11.setGeometry(QtCore.QRect(60, 20, 41, 41))
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
        self.toolButton_10.setGeometry(QtCore.QRect(10, 20, 41, 41))
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
        self.toolButton_12.setGeometry(QtCore.QRect(1080, 110, 31, 31))
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
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_directiory = QtWidgets.QAction(MainWindow)
        self.actionOpen_directiory.setObjectName("actionOpen_directiory")
        self.menuFile.addAction(self.actionOpen_directiory)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuView_2.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.toolButton_14 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_14.setGeometry(QtCore.QRect(110, 20, 41, 41))
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
        self.toolButton_15.setGeometry(QtCore.QRect(160, 20, 41, 41))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1121, 8, 471, 793))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_2.setText(_translate("MainWindow", "No image For preview"))
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1150, -5, 101, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser.setPalette(palette)
        self.textBrowser.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText('Image Preview')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.cellClicked.connect(self.Mediaplayer)
        self.tableWidget.cellClicked.connect(self.Delete)
        self.tableWidget.cellClicked.connect(self.Copy)
        self.tableWidget.cellClicked.connect(self.Cut)
        self.tableWidget.cellClicked.connect(self.Zip)
        self.comboBox_2.currentIndexChanged.connect(self.setDisabledDelete)
        self.comboBox_2.currentIndexChanged.connect(self.setDisabledCopy)
        self.comboBox_2.currentIndexChanged.connect(self.setDisabledCut)
        self.comboBox_2.currentIndexChanged.connect(self.setmediaPlayerDis)
        self.comboBox_2.currentIndexChanged.connect(self.setDisZip)
        self.comboBox_2.currentTextChanged.connect(self.setDisabledDelete)
        self.comboBox_2.currentTextChanged.connect(self.setDisabledCopy)
        self.comboBox_2.currentTextChanged.connect(self.setDisabledCut)
        self.comboBox_2.currentTextChanged.connect(self.setmediaPlayerDis)
        self.comboBox_2.currentTextChanged.connect(self.setDisZip)
        self.toolButton_3.clicked.connect(self.DeleteItems)
        self.toolButton_4.clicked.connect(self.CopyItems)
        self.toolButton_13.clicked.connect(self.PasteItem)
        self.toolButton_5.clicked.connect(self.CutItems)
        self.toolButton_6.clicked.connect(self.ZipItems)
        self.toolButton.clicked.connect(self.NewDir)
        self.toolButton_12.clicked.connect(self.Refresh)
        self.toolButton_10.clicked.connect(self.playButton)
        self.toolButton_11.clicked.connect(self.pauseButton)
        self.toolButton_15.clicked.connect(self.nextButton)
        self.toolButton_14.clicked.connect(self.previousButton)

        # self.label_2.setPixmap(QtGui.QPixmap("../../../../Users/m.reza/Desktop/series_1_ap/ui icons/blank-file.png"))

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
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "My Computer "))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        '''
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "C:/"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Mamad"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "mamaly"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "D:/"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Reza"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "file1"))

        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "C:/"))
        '''
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        for i in range(len(self.items)):
            self.treeWidget.topLevelItem(i).setText(0, _translate("MainWindow", self.dps[i][0]))

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

    def selectionchange(self, i):
        _translate = QtCore.QCoreApplication.translate

        for t in range(len(self.dps)):
            self.comboBox_2.setItemText(t, self.dps[t][0])

        print("Current index", i, "selection changed ", self.comboBox_2.currentText())
        self.path = self.comboBox_2.currentText()
        self.lisrdir = os.listdir(self.path)
        self.lisrdir.sort()
        self.row = len(self.lisrdir)
        print(self.row)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(self.row)
        self.tableWidget.setIconSize(QtCore.QSize(25, 25))
        self.vertiitems = []
        self.horiitems = []
        print(self.lisrdir)
        print(len(self.lisrdir))
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
            if len(fileExtension) != 4 and len(fileExtension) != 6 and len(fileExtension) != 5:
                item.setIcon(self.icon1)
            print(fileExtension)
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
                item.setFlags(QtCore.Qt.ItemIsSelectable)
                item_2.setFlags(QtCore.Qt.ItemIsSelectable)

        for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
            item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
            item.setText(_translate("MainWindow", self.title[t]))
            # self.comboBox_2.addItem(self.path)
            # self.comboBox_2.setCurrentText(self.path)

    def forward(self):
        _translate = QtCore.QCoreApplication.translate
        self.clickeditem = self.tableWidget.currentItem()
        fileName, fileExtension = os.path.splitext(self.clickeditem.text())
        if fileExtension == '' or len(fileExtension) > 4 or len(fileExtension) == 23:
            self.addpath = self.clickeditem.text()
            self.path = self.comboBox_2.currentText()
            self.path += self.addpath + "\\"
            try:
                self.lisrdir = os.listdir(self.path)
            except PermissionError:
                self.msg.exec_()
                self.path = self.comboBox_2.currentText()
            self.num = self.comboBox_2.currentIndex()
            self.comboBox_2.setItemText(self.num, self.path)
            self.lisrdir.sort()
            self.row = len(self.lisrdir)
            print(self.row)
            self.tableWidget.clear()
            self.tableWidget.setRowCount(self.row)
            self.tableWidget.setIconSize(QtCore.QSize(25, 25))
            self.vertiitems = []
            self.horiitems = []
            print(self.lisrdir)
            print(len(self.lisrdir))
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
                if len(fileExtension) != 4 and len(fileExtension) != 6 and len(fileExtension) != 5:
                    item.setIcon(self.icon1)
                print(fileExtension)
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

    def Mediaplayer(self):
        self.clickeditem = self.tableWidget.currentItem()
        if not self.clickeditem:
            self.groupBox.setDisabled(True)
            return None

        self.name = self.clickeditem.text()
        self.musicname = ''
        if self.name.endswith('.mp3'):
            self.groupBox.setDisabled(False)
            self.musicname = self.clickeditem.text()
        else:
            self.groupBox.setDisabled(True)

        self.musicpath = self.comboBox_2.currentText()
        if self.groupBox.setDisabled:
            self.musicpath += self.musicname
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
        self.musicDuration = MP3(mp3Player.playList[mp3Player.n]).info.length
        while (mp3Player.player.time != self.musicDuration):
            self.horizontalSlider.setSliderPosition(round((mp3Player.player.time / self.musicDuration) * 1000))

    def setmediaPlayerDis(self):
        self.groupBox.setDisabled(True)

    def Delete(self):
        self.clickeditem_1 = self.tableWidget.currentItem()
        if not self.clickeditem_1:
            self.toolButton_3.setDisabled(True)
        else:
            self.toolButton_3.setDisabled(False)
        self.deletepath = self.comboBox_2.currentText()
        try:
            self.deletepath += self.clickeditem_1.text()
        except:
            pass

    def DeleteItems(self):
        # delete file
        # file path is = self.deletepath
        print(self.deletepath)

    def setDisabledDelete(self):
        self.toolButton_3.setDisabled(True)

    def Cut(self):
        self.clickeditem_3 = self.tableWidget.currentItem()
        if not self.clickeditem_3:
            self.toolButton_5.setDisabled(True)
        else:
            self.toolButton_5.setDisabled(False)

        self.cuttingfile = self.comboBox_2.currentText()
        try:
            self.cuttingfile += self.clickeditem_3.text()
        except:
            pass

    def CutItems(self):
        if self.cuttingfile:
            self.toolButton_13.setDisabled(False)
        print(self.cuttingfile)

    def setDisabledCut(self):
        self.toolButton_5.setDisabled(True)

    def Copy(self):
        self.clickeditem_2 = self.tableWidget.currentItem()
        if not self.clickeditem_2:
            self.toolButton_4.setDisabled(True)
        else:
            self.toolButton_4.setDisabled(False)

        self.copyingfile = self.comboBox_2.currentText()
        try:
            self.copyingfile += self.clickeditem_2.text()
        except:
            pass

    def setDisabledCopy(self):
        self.toolButton_4.setDisabled(True)

    def CopyItems(self):
        if self.copyingfile:
            self.toolButton_13.setDisabled(False)
        print(self.copyingfile)

    def PasteItem(self):
        print(self.copyingfile)
        # paste to addressi k ma migim
        self.pastetoadrs = self.comboBox_2.currentText()
        print(self.pastetoadrs)

    def Zip(self):
        self.clickeditem_4 = self.tableWidget.currentItem()
        if not self.clickeditem_4:
            self.toolButton_6.setDisabled(True)
        else:
            self.toolButton_6.setDisabled(False)
        self.Zipingpath = self.comboBox_2.currentText()
        try:
            self.Zipingpath += self.clickeditem_4.text()
        except:
            pass

    def ZipItems(self):
        print(self.Zipingpath)
        # zip kon to adres feli

    def setDisZip(self):
        self.toolButton_6.setDisabled(True)

    def NewDir(self):
        self.currentpath = self.comboBox_2.currentText()
        # creata dir to in masir feli
        print('fuck')

    def Refresh(self, i):
        self.toolButton_6.setDisabled(True)
        self.toolButton_4.setDisabled(True)
        self.toolButton_5.setDisabled(True)
        self.toolButton_3.setDisabled(True)

        _translate = QtCore.QCoreApplication.translate
        print("Current index", i, "selection changed ", self.comboBox_2.currentText())
        self.path = self.comboBox_2.currentText()
        self.lisrdir = os.listdir(self.path)
        self.lisrdir.sort()
        self.row = len(self.lisrdir)
        print(self.row)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(self.row)
        self.tableWidget.setIconSize(QtCore.QSize(25, 25))
        self.vertiitems = []
        self.horiitems = []
        print(self.lisrdir)
        print(len(self.lisrdir))
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
            if len(fileExtension) != 4 and len(fileExtension) != 6 and len(fileExtension) != 5:
                item.setIcon(self.icon1)
            print(fileExtension)
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
                item.setFlags(QtCore.Qt.ItemIsSelectable)
                item_2.setFlags(QtCore.Qt.ItemIsSelectable)

        for t in range(len(self.title)):  # name gozari header ba onvane name,type, size
            item = self.tableWidget.horizontalHeaderItem(t)  # ofoqi
            item.setText(_translate("MainWindow", self.title[t]))
            # self.comboBox_2.addItem(self.path)
            # self.comboBox_2.setCurrentText(self.path)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    if app.exec_()==0:
        mp3Player.seek(ui.musicDuration)
        '''ui.movingSlider._is_stopped = True
        ui.movingSlider._tstate_lock = None'''

    sys.exit(app.exec_())

