# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hogar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Hogar(QWidget):
    def setupUi(self, Hogar):
        if not Hogar.objectName():
            Hogar.setObjectName(u"Hogar")
        Hogar.resize(889, 895)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        Hogar.setFont(font)
        self.gridLayout = QGridLayout(Hogar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Hogar)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Hogar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)

        self.label_3 = QLabel(Hogar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 3)

        self.label_4 = QLabel(Hogar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_4, 0, 7, 1, 1)

        self.insPJ = QLineEdit(Hogar)
        self.insPJ.setObjectName(u"insPJ")

        self.gridLayout.addWidget(self.insPJ, 1, 0, 1, 1)

        self.insTV = QLineEdit(Hogar)
        self.insTV.setObjectName(u"insTV")

        self.gridLayout.addWidget(self.insTV, 1, 1, 1, 2)

        self.insdis = QLineEdit(Hogar)
        self.insdis.setObjectName(u"insdis")

        self.gridLayout.addWidget(self.insdis, 1, 3, 1, 4)

        self.insubi = QLineEdit(Hogar)
        self.insubi.setObjectName(u"insubi")

        self.gridLayout.addWidget(self.insubi, 1, 7, 1, 1)

        self.label_5 = QLabel(Hogar)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(Hogar)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 2)

        self.label_7 = QLabel(Hogar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_7, 2, 3, 1, 3)

        self.label_8 = QLabel(Hogar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_8, 2, 6, 1, 2)

        self.instel = QLineEdit(Hogar)
        self.instel.setObjectName(u"instel")

        self.gridLayout.addWidget(self.instel, 3, 0, 1, 1)

        self.inscorreo = QLineEdit(Hogar)
        self.inscorreo.setObjectName(u"inscorreo")

        self.gridLayout.addWidget(self.inscorreo, 3, 1, 1, 2)

        self.insTC = QLineEdit(Hogar)
        self.insTC.setObjectName(u"insTC")

        self.gridLayout.addWidget(self.insTC, 3, 3, 1, 3)

        self.insVP = QLineEdit(Hogar)
        self.insVP.setObjectName(u"insVP")

        self.gridLayout.addWidget(self.insVP, 3, 6, 1, 2)

        self.label_17 = QLabel(Hogar)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_9 = QLabel(Hogar)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 2)

        self.label_10 = QLabel(Hogar)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 3)

        self.label_11 = QLabel(Hogar)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_11, 4, 6, 1, 2)

        self.insnomb = QLineEdit(Hogar)
        self.insnomb.setObjectName(u"insnomb")

        self.gridLayout.addWidget(self.insnomb, 5, 0, 1, 1)

        self.insHA = QLineEdit(Hogar)
        self.insHA.setObjectName(u"insHA")

        self.gridLayout.addWidget(self.insHA, 5, 1, 1, 2)

        self.insPA = QLineEdit(Hogar)
        self.insPA.setObjectName(u"insPA")

        self.gridLayout.addWidget(self.insPA, 5, 4, 1, 2)

        self.insFEP = QLineEdit(Hogar)
        self.insFEP.setObjectName(u"insFEP")

        self.gridLayout.addWidget(self.insFEP, 5, 6, 1, 2)

        self.label_12 = QLabel(Hogar)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 2)

        self.label_13 = QLabel(Hogar)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_13, 6, 2, 1, 3)

        self.label_14 = QLabel(Hogar)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_14, 6, 5, 1, 3)

        self.insFPI = QLineEdit(Hogar)
        self.insFPI.setObjectName(u"insFPI")

        self.gridLayout.addWidget(self.insFPI, 7, 0, 1, 2)

        self.inspresi = QLineEdit(Hogar)
        self.inspresi.setObjectName(u"inspresi")

        self.gridLayout.addWidget(self.inspresi, 7, 2, 1, 3)

        self.insteso = QLineEdit(Hogar)
        self.insteso.setObjectName(u"insteso")

        self.gridLayout.addWidget(self.insteso, 7, 5, 1, 3)

        self.label_15 = QLabel(Hogar)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)

        self.label_16 = QLabel(Hogar)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_16, 8, 1, 1, 3)

        self.insbanco = QLineEdit(Hogar)
        self.insbanco.setObjectName(u"insbanco")

        self.gridLayout.addWidget(self.insbanco, 9, 0, 1, 1)

        self.insCC = QLineEdit(Hogar)
        self.insCC.setObjectName(u"insCC")

        self.gridLayout.addWidget(self.insCC, 9, 1, 1, 3)

        self.btncancelar = QPushButton(Hogar)
        self.btncancelar.setObjectName(u"btncancelar")

        self.gridLayout.addWidget(self.btncancelar, 10, 1, 1, 2)

        self.btningresar = QPushButton(Hogar)
        self.btningresar.setObjectName(u"btningresar")

        self.gridLayout.addWidget(self.btningresar, 10, 5, 1, 3)

        QWidget.setTabOrder(self.insPJ, self.insTV)
        QWidget.setTabOrder(self.insTV, self.insdis)
        QWidget.setTabOrder(self.insdis, self.insubi)
        QWidget.setTabOrder(self.insubi, self.instel)
        QWidget.setTabOrder(self.instel, self.inscorreo)
        QWidget.setTabOrder(self.inscorreo, self.insTC)
        QWidget.setTabOrder(self.insTC, self.insVP)
        QWidget.setTabOrder(self.insVP, self.insnomb)
        QWidget.setTabOrder(self.insnomb, self.insHA)
        QWidget.setTabOrder(self.insHA, self.insPA)
        QWidget.setTabOrder(self.insPA, self.insFEP)
        QWidget.setTabOrder(self.insFEP, self.insFPI)
        QWidget.setTabOrder(self.insFPI, self.inspresi)
        QWidget.setTabOrder(self.inspresi, self.insteso)
        QWidget.setTabOrder(self.insteso, self.insbanco)
        QWidget.setTabOrder(self.insbanco, self.insCC)
        QWidget.setTabOrder(self.insCC, self.btningresar)
        QWidget.setTabOrder(self.btningresar, self.btncancelar)

        self.retranslateUi(Hogar)

        QMetaObject.connectSlotsByName(Hogar)
    # setupUi

    def retranslateUi(self, Hogar):
        Hogar.setWindowTitle(QCoreApplication.translate("Hogar", u"Ingresar Hogares", None))
        self.label.setText(QCoreApplication.translate("Hogar", u"Personer\u00eda Jur\u00eddica", None))
        self.label_2.setText(QCoreApplication.translate("Hogar", u"Tiempo de Vigencia", None))
        self.label_3.setText(QCoreApplication.translate("Hogar", u"Distrito", None))
        self.label_4.setText(QCoreApplication.translate("Hogar", u"Ubicaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("Hogar", u"Telefono", None))
        self.label_6.setText(QCoreApplication.translate("Hogar", u"Correo", None))
        self.label_7.setText(QCoreApplication.translate("Hogar", u"Tipo de Centro", None))
        self.label_8.setText(QCoreApplication.translate("Hogar", u"Valoraci\u00f3n de Puntos", None))
        self.label_17.setText(QCoreApplication.translate("Hogar", u"Nombre", None))
        self.label_9.setText(QCoreApplication.translate("Hogar", u"Horario de Atenci\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("Hogar", u"Poblaci\u00f3n Anual", None))
        self.label_11.setText(QCoreApplication.translate("Hogar", u"Fecha de Entrega del Plan", None))
        self.label_12.setText(QCoreApplication.translate("Hogar", u"Fecha de Presentacion del Informe", None))
        self.label_13.setText(QCoreApplication.translate("Hogar", u"Presidente", None))
        self.label_14.setText(QCoreApplication.translate("Hogar", u"Tesorero", None))
        self.label_15.setText(QCoreApplication.translate("Hogar", u"Banco", None))
        self.label_16.setText(QCoreApplication.translate("Hogar", u"Cuenta Corriente", None))
        self.btncancelar.setText(QCoreApplication.translate("Hogar", u"Cancelar", None))
        self.btningresar.setText(QCoreApplication.translate("Hogar", u"ingresar Datos", None))
    # retranslateUi
    def __init__(self):
        super(Ui_Hogar, self).__init__()
        self.setupUi(self)
