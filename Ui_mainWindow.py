# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(600, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/download.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 350, 591, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.set_src_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.set_src_button.setObjectName("set_src_button")
        self.horizontalLayout.addWidget(self.set_src_button)
        self.set_des_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.set_des_button.setObjectName("set_des_button")
        self.horizontalLayout.addWidget(self.set_des_button)
        self.open_dst_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.open_dst_button.setObjectName("open_dst_button")
        self.horizontalLayout.addWidget(self.open_dst_button)
        self.del_old_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.del_old_button.setObjectName("del_old_button")
        self.horizontalLayout.addWidget(self.del_old_button)
        self.start_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.quit_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.quit_button.setObjectName("quit_button")
        self.horizontalLayout.addWidget(self.quit_button)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 410, 581, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 571, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 581, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.src_floder_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.src_floder_label.setObjectName("src_floder_label")
        self.verticalLayout.addWidget(self.src_floder_label)
        self.dst_floder_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dst_floder_label.setObjectName("dst_floder_label")
        self.verticalLayout.addWidget(self.dst_floder_label)
        self.project_name_label = QtWidgets.QLabel(self.centralwidget)
        self.project_name_label.setGeometry(QtCore.QRect(70, 10, 131, 29))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.project_name_label.setFont(font)
        self.project_name_label.setObjectName("project_name_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 61, 29))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.file_open = QtWidgets.QAction(MainWindow)
        self.file_open.setObjectName("file_open")
        self.file_save = QtWidgets.QAction(MainWindow)
        self.file_save.setObjectName("file_save")
        self.file_set = QtWidgets.QAction(MainWindow)
        self.file_set.setObjectName("file_set")
        self.file_quit = QtWidgets.QAction(MainWindow)
        self.file_quit.setCheckable(False)
        self.file_quit.setChecked(False)
        self.file_quit.setObjectName("file_quit")
        self.help_help = QtWidgets.QAction(MainWindow)
        self.help_help.setObjectName("help_help")
        self.help_abut = QtWidgets.QAction(MainWindow)
        self.help_abut.setObjectName("help_abut")
        self.menu.addAction(self.file_open)
        self.menu.addAction(self.file_save)
        self.menu.addSeparator()
        self.menu.addAction(self.file_set)
        self.menu.addAction(self.file_quit)
        self.menu_2.addAction(self.help_help)
        self.menu_2.addAction(self.help_abut)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.quit_button.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "最新文件获取小工具"))
        self.set_src_button.setText(_translate("MainWindow", "设置源文件夹"))
        self.set_des_button.setText(_translate("MainWindow", "设置目标文件夹"))
        self.open_dst_button.setText(_translate("MainWindow", "打开目标文件夹"))
        self.del_old_button.setText(_translate("MainWindow", "删除旧文件"))
        self.start_button.setText(_translate("MainWindow", "开始"))
        self.quit_button.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "进度："))
        self.src_floder_label.setText(_translate("MainWindow", "源文件夹："))
        self.dst_floder_label.setText(_translate("MainWindow", "目标文件夹："))
        self.project_name_label.setText(_translate("MainWindow", "202S-B"))
        self.label_2.setText(_translate("MainWindow", "项目名称："))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.file_open.setText(_translate("MainWindow", "打开配置"))
        self.file_save.setText(_translate("MainWindow", "保存配置"))
        self.file_set.setText(_translate("MainWindow", "设置"))
        self.file_quit.setText(_translate("MainWindow", "退出"))
        self.help_help.setText(_translate("MainWindow", "使用说明"))
        self.help_abut.setText(_translate("MainWindow", "关于"))

import picture_rc