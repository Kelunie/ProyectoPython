# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'planesInversion.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_planInversion(QWidget):
    def setupUi(self, planInversion):
        if not planInversion.objectName():
            planInversion.setObjectName(u"planInversion")
        planInversion.resize(1034, 774)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        planInversion.setFont(font)
        self.table1 = QTableWidget(planInversion)
        if (self.table1.columnCount() < 1):
            self.table1.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.table1.rowCount() < 5):
            self.table1.setRowCount(5)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(255, 170, 0));
        self.table1.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(4, __qtablewidgetitem5)
        self.table1.setObjectName(u"table1")
        self.table1.setGeometry(QRect(10, 170, 991, 231))
        self.insMuni = QLineEdit(planInversion)
        self.insMuni.setObjectName(u"insMuni")
        self.insMuni.setEnabled(True)
        self.insMuni.setGeometry(QRect(10, 20, 511, 41))
        self.insMuni.setReadOnly(True)
        self.insSoli = QLineEdit(planInversion)
        self.insSoli.setObjectName(u"insSoli")
        self.insSoli.setGeometry(QRect(10, 60, 511, 41))
        self.insSoli.setReadOnly(True)
        self.insLey = QLineEdit(planInversion)
        self.insLey.setObjectName(u"insLey")
        self.insLey.setGeometry(QRect(10, 100, 511, 41))
        self.insLey.setReadOnly(True)
        self.table2 = QTableWidget(planInversion)
        if (self.table2.columnCount() < 6):
            self.table2.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.table2.setObjectName(u"table2")
        self.table2.setGeometry(QRect(10, 410, 991, 191))
        self.table2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.table2.horizontalHeader().setCascadingSectionResizes(False)
        self.table2.horizontalHeader().setDefaultSectionSize(200)
        self.table2.verticalHeader().setCascadingSectionResizes(False)
        self.table2.verticalHeader().setProperty("showSortIndicator", False)
        self.table2.verticalHeader().setStretchLastSection(False)
        self.btnopen = QPushButton(planInversion)
        self.btnopen.setObjectName(u"btnopen")
        self.btnopen.setGeometry(QRect(20, 620, 221, 71))
        self.btnload = QPushButton(planInversion)
        self.btnload.setObjectName(u"btnload")
        self.btnload.setGeometry(QRect(250, 620, 221, 71))
        self.btncloose = QPushButton(planInversion)
        self.btncloose.setObjectName(u"btncloose")
        self.btncloose.setGeometry(QRect(130, 700, 221, 71))
        self.label = QLabel(planInversion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(520, 610, 151, 41))
        self.instotal = QLineEdit(planInversion)
        self.instotal.setObjectName(u"instotal")
        self.instotal.setGeometry(QRect(680, 610, 321, 41))
        self.instotal.setReadOnly(True)

        self.retranslateUi(planInversion)

        QMetaObject.connectSlotsByName(planInversion)
    # setupUi

    def retranslateUi(self, planInversion):
        planInversion.setWindowTitle(QCoreApplication.translate("planInversion", u"Cargar Plan de inversion", None))
        ___qtablewidgetitem = self.table1.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("planInversion", u"Codigo Asignado", None));
        ___qtablewidgetitem1 = self.table1.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("planInversion", u"Instituci\u00f3n", None));
        ___qtablewidgetitem2 = self.table1.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("planInversion", u"Encargada", None));
        ___qtablewidgetitem3 = self.table1.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("planInversion", u"Periodo", None));
        ___qtablewidgetitem4 = self.table1.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("planInversion", u"Descripci\u00f3n del Proyecto", None));
        ___qtablewidgetitem5 = self.table2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("planInversion", u"Detalle", None));
        ___qtablewidgetitem6 = self.table2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("planInversion", u"Proveedor", None));
        ___qtablewidgetitem7 = self.table2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("planInversion", u"Proforma", None));
        ___qtablewidgetitem8 = self.table2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("planInversion", u"Cantidad", None));
        ___qtablewidgetitem9 = self.table2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("planInversion", u"Pre Unitario", None));
        ___qtablewidgetitem10 = self.table2.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("planInversion", u"Sutotal", None));
        self.btnopen.setText(QCoreApplication.translate("planInversion", u"Abrir Archivo Excel", None))
        self.btnload.setText(QCoreApplication.translate("planInversion", u"Cargar Informaci\u00f3n", None))
        self.btncloose.setText(QCoreApplication.translate("planInversion", u"Cerrar Ventana", None))
        self.label.setText(QCoreApplication.translate("planInversion", u"Total Inversi\u00f3n", None))
    # retranslateUi
    def __init__(self):
        super(Ui_planInversion, self).__init__()
        self.setupUi(self)
