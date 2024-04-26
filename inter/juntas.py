# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'juntas.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form_juntas(QWidget):
    def setupUi(self, Form_juntas):
        if not Form_juntas.objectName():
            Form_juntas.setObjectName(u"Form_juntas")
        Form_juntas.resize(944, 827)
        self.verticalLayout = QVBoxLayout(Form_juntas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group = QGroupBox(Form_juntas)
        self.group.setObjectName(u"group")
        self.formLayout = QFormLayout(self.group)
        self.formLayout.setObjectName(u"formLayout")
        self.label_PJ = QLabel(self.group)
        self.label_PJ.setObjectName(u"label_PJ")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        self.label_PJ.setFont(font)
        self.label_PJ.setFrameShape(QFrame.Shape.Panel)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_PJ)

        self.insPJ = QLineEdit(self.group)
        self.insPJ.setObjectName(u"insPJ")
        self.insPJ.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.insPJ)

        self.label_FV = QLabel(self.group)
        self.label_FV.setObjectName(u"label_FV")
        self.label_FV.setFont(font)
        self.label_FV.setFrameShape(QFrame.Shape.Panel)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_FV)

        self.insFV = QLineEdit(self.group)
        self.insFV.setObjectName(u"insFV")
        self.insFV.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.insFV)

        self.label_Dis = QLabel(self.group)
        self.label_Dis.setObjectName(u"label_Dis")
        self.label_Dis.setFont(font)
        self.label_Dis.setFrameShape(QFrame.Shape.Panel)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_Dis)

        self.insDis = QLineEdit(self.group)
        self.insDis.setObjectName(u"insDis")
        self.insDis.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.insDis)

        self.label_Ubi = QLabel(self.group)
        self.label_Ubi.setObjectName(u"label_Ubi")
        self.label_Ubi.setFont(font)
        self.label_Ubi.setFrameShape(QFrame.Shape.Panel)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_Ubi)

        self.insUbi = QLineEdit(self.group)
        self.insUbi.setObjectName(u"insUbi")
        self.insUbi.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.insUbi)

        self.label_PJ_2 = QLabel(self.group)
        self.label_PJ_2.setObjectName(u"label_PJ_2")
        self.label_PJ_2.setFont(font)
        self.label_PJ_2.setFrameShape(QFrame.Shape.Panel)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_PJ_2)

        self.insTel = QLineEdit(self.group)
        self.insTel.setObjectName(u"insTel")
        self.insTel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.insTel)

        self.label_ND = QLabel(self.group)
        self.label_ND.setObjectName(u"label_ND")
        self.label_ND.setFont(font)
        self.label_ND.setFrameShape(QFrame.Shape.Panel)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_ND)

        self.insND = QLineEdit(self.group)
        self.insND.setObjectName(u"insND")
        self.insND.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.insND)

        self.label_ED = QLabel(self.group)
        self.label_ED.setObjectName(u"label_ED")
        self.label_ED.setFont(font)
        self.label_ED.setFrameShape(QFrame.Shape.Panel)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_ED)

        self.insED = QLineEdit(self.group)
        self.insED.setObjectName(u"insED")
        self.insED.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.insED)

        self.btnIngresar = QPushButton(self.group)
        self.btnIngresar.setObjectName(u"btnIngresar")
        self.btnIngresar.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.btnIngresar)

        self.btncancelar = QPushButton(self.group)
        self.btncancelar.setObjectName(u"btncancelar")
        self.btncancelar.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.btncancelar)


        self.verticalLayout.addWidget(self.group)

        QWidget.setTabOrder(self.insPJ, self.insFV)
        QWidget.setTabOrder(self.insFV, self.insDis)
        QWidget.setTabOrder(self.insDis, self.insUbi)
        QWidget.setTabOrder(self.insUbi, self.insTel)
        QWidget.setTabOrder(self.insTel, self.insND)
        QWidget.setTabOrder(self.insND, self.insED)
        QWidget.setTabOrder(self.insED, self.btnIngresar)
        QWidget.setTabOrder(self.btnIngresar, self.btncancelar)

        self.retranslateUi(Form_juntas)

        QMetaObject.connectSlotsByName(Form_juntas)
    # setupUi

    def retranslateUi(self, Form_juntas):
        Form_juntas.setWindowTitle(QCoreApplication.translate("Form_juntas", u"Registrar nueva Junta", None))
        self.group.setTitle("")
        self.label_PJ.setText(QCoreApplication.translate("Form_juntas", u"Personer\u00eda Jur\u00eddica", None))
        self.label_FV.setText(QCoreApplication.translate("Form_juntas", u"Fecha Vencimiento", None))
        self.label_Dis.setText(QCoreApplication.translate("Form_juntas", u"Distrito", None))
        self.label_Ubi.setText(QCoreApplication.translate("Form_juntas", u"Ubicaci\u00f3n", None))
        self.label_PJ_2.setText(QCoreApplication.translate("Form_juntas", u"Telefono", None))
        self.label_ND.setText(QCoreApplication.translate("Form_juntas", u"Nombre del Director", None))
        self.label_ED.setText(QCoreApplication.translate("Form_juntas", u"Email del Director", None))
        self.btnIngresar.setText(QCoreApplication.translate("Form_juntas", u"Ingresar Datos", None))
        self.btncancelar.setText(QCoreApplication.translate("Form_juntas", u"Cancelar", None))
    # retranslateUi
    def __init__(self):
        super(Ui_Form_juntas, self).__init__()
        self.setupUi(self)
