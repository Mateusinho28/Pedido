# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_uivzjhWg.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_MeuAmor(object):
    def setupUi(self, MeuAmor):
        if not MeuAmor.objectName():
            MeuAmor.setObjectName(u"MeuAmor")
        MeuAmor.resize(450, 438)
        MeuAmor.setMaximumSize(QSize(450, 500))
        self.centralwidget = QWidget(MeuAmor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(236, 0, 0, 255), stop:1 rgba(255, 101, 101, 255));\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size: 40px;\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	font-size: 20px;\n"
"	color: red;\n"
"	min-height: 45px;\n"
"	border-radius: 20px;\n"
"	background-color: white;\n"
"}\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 431, 121))
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_yes = QFrame(self.centralwidget)
        self.frame_yes.setObjectName(u"frame_yes")
        self.frame_yes.setGeometry(QRect(30, 160, 171, 101))
        self.frame_yes.setFrameShape(QFrame.NoFrame)
        self.frame_yes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_yes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_yes = QPushButton(self.frame_yes)
        self.button_yes.setObjectName(u"button_yes")

        self.horizontalLayout.addWidget(self.button_yes)

        self.frame_no = QFrame(self.centralwidget)
        self.frame_no.setObjectName(u"frame_no")
        self.frame_no.setGeometry(QRect(250, 160, 171, 101))
        self.frame_no.setFrameShape(QFrame.NoFrame)
        self.frame_no.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_no)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_no = QPushButton(self.frame_no)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout_2.addWidget(self.button_no)

        self.coracao = QLabel(self.centralwidget)
        self.coracao.setObjectName(u"coracao")
        self.coracao.setGeometry(QRect(80, 110, 281, 251))
        self.coracao.setStyleSheet(u"")
        self.coracao.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao.setScaledContents(True)
        MeuAmor.setCentralWidget(self.centralwidget)

        self.retranslateUi(MeuAmor)

        QMetaObject.connectSlotsByName(MeuAmor)
    # setupUi

    def retranslateUi(self, MeuAmor):
        MeuAmor.setWindowTitle(QCoreApplication.translate("MeuAmor", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MeuAmor", u"<html><head/><body><p>Ana L\u00edvia</p><p><span style=\" font-size:30pt;\">Quer namorar comigo?</span></p></body></html>", None))
        self.button_yes.setText(QCoreApplication.translate("MeuAmor", u"Sim \u2665", None))
        self.button_no.setText(QCoreApplication.translate("MeuAmor", u"N\u00e3o", None))
        self.coracao.setText("")
    # retranslateUi

