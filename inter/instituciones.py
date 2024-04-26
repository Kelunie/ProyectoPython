# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instituciones.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_instituciones(QWidget):
    def setupUi(self, instituciones):
        if not instituciones.objectName():
            instituciones.setObjectName(u"instituciones")
        instituciones.resize(872, 709)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        instituciones.setFont(font)
        self.gridLayout = QGridLayout(instituciones)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(instituciones)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.innom = QLineEdit(instituciones)
        self.innom.setObjectName(u"innom")

        self.gridLayout.addWidget(self.innom, 0, 1, 1, 1)

        self.label_2 = QLabel(instituciones)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.inperju = QLineEdit(instituciones)
        self.inperju.setObjectName(u"inperju")

        self.gridLayout.addWidget(self.inperju, 1, 1, 1, 1)

        self.label_3 = QLabel(instituciones)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.invige = QLineEdit(instituciones)
        self.invige.setObjectName(u"invige")

        self.gridLayout.addWidget(self.invige, 2, 1, 1, 1)

        self.label_4 = QLabel(instituciones)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.insfunciones = QTextEdit(instituciones)
        self.insfunciones.setObjectName(u"insfunciones")

        self.gridLayout.addWidget(self.insfunciones, 3, 1, 1, 1)

        self.label_5 = QLabel(instituciones)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.indis = QLineEdit(instituciones)
        self.indis.setObjectName(u"indis")

        self.gridLayout.addWidget(self.indis, 4, 1, 1, 1)

        self.label_6 = QLabel(instituciones)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.inubi = QLineEdit(instituciones)
        self.inubi.setObjectName(u"inubi")

        self.gridLayout.addWidget(self.inubi, 5, 1, 1, 1)

        self.label_7 = QLabel(instituciones)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.intel = QLineEdit(instituciones)
        self.intel.setObjectName(u"intel")

        self.gridLayout.addWidget(self.intel, 6, 1, 1, 1)

        self.label_8 = QLabel(instituciones)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.incorreo = QLineEdit(instituciones)
        self.incorreo.setObjectName(u"incorreo")

        self.gridLayout.addWidget(self.incorreo, 7, 1, 1, 1)

        self.label_9 = QLabel(instituciones)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.inpresi = QLineEdit(instituciones)
        self.inpresi.setObjectName(u"inpresi")

        self.gridLayout.addWidget(self.inpresi, 8, 1, 1, 1)

        self.label_10 = QLabel(instituciones)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.intesorero = QLineEdit(instituciones)
        self.intesorero.setObjectName(u"intesorero")

        self.gridLayout.addWidget(self.intesorero, 9, 1, 1, 1)

        self.btncancelarins = QPushButton(instituciones)
        self.btncancelarins.setObjectName(u"btncancelarins")

        self.gridLayout.addWidget(self.btncancelarins, 10, 0, 1, 1)

        self.btningreins = QPushButton(instituciones)
        self.btningreins.setObjectName(u"btningreins")

        self.gridLayout.addWidget(self.btningreins, 10, 1, 1, 1)


        self.retranslateUi(instituciones)

        QMetaObject.connectSlotsByName(instituciones)
    # setupUi

    def retranslateUi(self, instituciones):
        instituciones.setWindowTitle(QCoreApplication.translate("instituciones", u"Ingreso de Instituciones", None))
        self.label.setText(QCoreApplication.translate("instituciones", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("instituciones", u"Personer\u00eda Jur\u00eddica", None))
        self.label_3.setText(QCoreApplication.translate("instituciones", u"Vigencia", None))
        self.label_4.setText(QCoreApplication.translate("instituciones", u"Funciones", None))
        self.label_5.setText(QCoreApplication.translate("instituciones", u"Distrito", None))
        self.label_6.setText(QCoreApplication.translate("instituciones", u"Ubicaci\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("instituciones", u"Telefono", None))
        self.label_8.setText(QCoreApplication.translate("instituciones", u"Correo", None))
        self.label_9.setText(QCoreApplication.translate("instituciones", u"Presidente", None))
        self.label_10.setText(QCoreApplication.translate("instituciones", u"Tesorero", None))
        self.btncancelarins.setText(QCoreApplication.translate("instituciones", u"Cancelar", None))
        self.btningreins.setText(QCoreApplication.translate("instituciones", u"Ingresar Datos", None))
    # retranslateUi
    def __init__(self):
        super(Ui_instituciones, self).__init__()
        self.setupUi(self)
