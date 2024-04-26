# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        self.actionJuntas = QAction(MainWindow)
        self.actionJuntas.setObjectName(u"actionJuntas")
        self.actionInstituciones = QAction(MainWindow)
        self.actionInstituciones.setObjectName(u"actionInstituciones")
        self.actionHogares = QAction(MainWindow)
        self.actionHogares.setObjectName(u"actionHogares")
        self.actionPlanes_Inversi_n = QAction(MainWindow)
        self.actionPlanes_Inversi_n.setObjectName(u"actionPlanes_Inversi_n")
        self.actionInforme_Liquidaci_n = QAction(MainWindow)
        self.actionInforme_Liquidaci_n.setObjectName(u"actionInforme_Liquidaci_n")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuRegistros = QMenu(self.menubar)
        self.menuRegistros.setObjectName(u"menuRegistros")
        self.menuExcells = QMenu(self.menubar)
        self.menuExcells.setObjectName(u"menuExcells")
        self.menuSalir = QMenu(self.menubar)
        self.menuSalir.setObjectName(u"menuSalir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuRegistros.menuAction())
        self.menubar.addAction(self.menuExcells.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())
        self.menuRegistros.addSeparator()
        self.menuRegistros.addAction(self.actionJuntas)
        self.menuRegistros.addSeparator()
        self.menuRegistros.addAction(self.actionInstituciones)
        self.menuRegistros.addSeparator()
        self.menuRegistros.addAction(self.actionHogares)
        self.menuRegistros.addSeparator()
        self.menuExcells.addSeparator()
        self.menuExcells.addAction(self.actionPlanes_Inversi_n)
        self.menuExcells.addSeparator()
        self.menuExcells.addAction(self.actionInforme_Liquidaci_n)
        self.menuExcells.addSeparator()
        self.menuSalir.addSeparator()
        self.menuSalir.addAction(self.actionSalir)
        self.menuSalir.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Proyecto", None))
        self.actionJuntas.setText(QCoreApplication.translate("MainWindow", u"Juntas", None))
        self.actionInstituciones.setText(QCoreApplication.translate("MainWindow", u"Instituciones", None))
        self.actionHogares.setText(QCoreApplication.translate("MainWindow", u"Hogares", None))
        self.actionPlanes_Inversi_n.setText(QCoreApplication.translate("MainWindow", u"Planes Inversi\u00f3n", None))
        self.actionInforme_Liquidaci_n.setText(QCoreApplication.translate("MainWindow", u"Informe Liquidaci\u00f3n", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.menuRegistros.setTitle(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.menuExcells.setTitle(QCoreApplication.translate("MainWindow", u"Excells", None))
        self.menuSalir.setTitle(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

