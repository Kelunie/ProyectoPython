# import libraries
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QWidgetAction, QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTableWidget, \
    QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtGui import Qt
from datetime import datetime, date
from Conexion import ConexionMySQL
import mysql.connector

# import guis and libraries
from inter.MainWindow import Ui_MainWindow
from inter.juntas import *
from inter.instituciones import *
from inter.Hogar import *


# Mysql
def inJun(PJ, fecVen, dis, ubi, tele, dirNom, dirEmail):
    aux = "INSERT INTO Juntas (PJ, fechVen, distri, ubicacion, telefono, dirNom, dirEmail) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    datos = (PJ, fecVen, dis, ubi, tele, dirNom, dirEmail)
    #start conexion
    conexionMSQL = ConexionMySQL("192.168.100.100", "kelunie", "culep1711", "proyecto")
    conexionMSQL.conectar()

    cursor = conexionMSQL.conexion.cursor()
    try:
        # Ejecutar la consulta SQL
        cursor.execute(aux, datos)

        # Confirmar los cambios
        conexionMSQL.conexion.commit()

        print("Datos insertados correctamente en la tabla Juntas.")
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        # Deshacer la transacción en caso de error
        conexionMSQL.conexion.rollback()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexionMSQL.desconectar()


def ininst(nom, PJ, vigen, func, dis, ubi, tele, email, presidente, tesorero):
    try:
        # Establecer conexión
        conexionMSQL = ConexionMySQL("192.168.100.100", "kelunie", "culep1711", "proyecto")
        conexionMSQL.conectar()
        cursor = conexionMSQL.conexion.cursor()

        # Insertar datos de la Institución
        aux = "INSERT INTO Instituciones (nombre, personeriaJuridica, vigencia, funciones, distrito, ubicacion, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (nom, PJ, vigen, func, dis, ubi, tele, email)
        cursor.execute(aux, datos)

        # Recuperar el ID de la Institución
        auxconsult = "SELECT idInstitucion FROM Instituciones WHERE personeriaJuridica = %s"
        cursor.execute(auxconsult, (PJ,))
        id_institucion = cursor.fetchone()

        if id_institucion:
            # Insertar datos de la Junta Administrativa
            aux2 = "INSERT INTO JuntaAdministrativa (idInstitucion, presidente, tesorero) VALUES (%s, %s, %s)"
            datos2 = (id_institucion[0], presidente, tesorero)
            cursor.execute(aux2, datos2)

        # Confirmar los cambios
        conexionMSQL.conexion.commit()
        print("Datos insertados correctamente en las tablas Instituciones y JuntaAdministrativa.")

    except mysql.connector.Error as e:
        print(f"Error al insertar datos: {e}")
        # Deshacer la transacción en caso de error
        conexionMSQL.conexion.rollback()

    finally:
        # Cerrar cursor y conexión
        if cursor:
            cursor.close()
        if conexionMSQL:
            conexionMSQL.desconectar()


def inhogar(nomb, personeria_juridica, tiempo_vigencia, distrito, ubicacion, telefono, correo, tipo_centro, valoracion_puntos,
            horario_atencion, poblacion_anual, fecha_entrega_plan, fecha_presentacion_informe, presidente, tesorero,
            banco, cuenta_corriente):
    try:
        # Establecer conexión
        conexionMSQL = ConexionMySQL("192.168.100.100", "kelunie", "culep1711", "proyecto")
        conexionMSQL.conectar()
        cursor = conexionMSQL.conexion.cursor()

        # Insertar datos del Hogar
        aux = "INSERT INTO Hogares (nombre, personeria_juridica, tiempo_vigencia, distrito, ubicacion, telefono, correo, tipo_centro, valoracion_puntos, horario_atencion, poblacion_anual, fecha_entrega_plan, fecha_presentacion_informe) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (
            nomb, personeria_juridica, tiempo_vigencia, distrito, ubicacion, telefono, correo, tipo_centro, valoracion_puntos,
            horario_atencion, poblacion_anual, fecha_entrega_plan, fecha_presentacion_informe)
        cursor.execute(aux, datos)

        # Recuperar el ID del Hogar
        consult = "SELECT id FROM Hogares WHERE `personeria_juridica` = %s"
        cursor.execute(consult, (personeria_juridica,))
        hogar_id = cursor.fetchone()

        if hogar_id:
            hogar_id = hogar_id[0]  # Convertir a un solo valor

            # Insertar datos de la Junta Directiva
            aux2 = "INSERT INTO JuntaDirectiva (hogar_id, presidente, tesorero) VALUES (%s, %s, %s)"
            datos2 = (hogar_id, presidente, tesorero)
            cursor.execute(aux2, datos2)


            # Insertar datos de las cuentas bancarias
            aux3 = "INSERT INTO CuentasBancarias (hogar_id, banco, cuenta_corriente) VALUES (%s, %s, %s)"
            datos_cuentas = (hogar_id, banco, cuenta_corriente)
            # Insertar datos de las cuentas bancarias
            print("Consulta SQL para cuentas bancarias:", aux3)
            print("Datos de cuentas bancarias:", datos_cuentas)
            cursor.execute(aux3, datos_cuentas)

        # Confirmar los cambios
        conexionMSQL.conexion.commit()
        print("Datos insertados correctamente en las tablas Hogares, JuntaDirectiva y CuentasBancarias.")

    except mysql.connector.Error as e:
        print(f"Error al insertar datos: {e}")
        # Deshacer la transacción en caso de error
        conexionMSQL.conexion.rollback()

    finally:
        # Cerrar cursor y conexión
        if cursor:
            cursor.close()
        if conexionMSQL:
            conexionMSQL.desconectar()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ndi = QMdiArea()
        self.setCentralWidget(self.ndi)

        self.subRJuntas = QMdiSubWindow()
        self.subRInstituciones = QMdiSubWindow()
        self.subRHogares = QMdiSubWindow()

        self.initMenu()

    def initMenu(self):
        # Conectar acciones del menú a funciones
        self.ui.actionJuntas.triggered.connect(self.abrirJuntas)
        self.ui.actionInstituciones.triggered.connect(self.abrirInstituciones)
        self.ui.actionHogares.triggered.connect(self.abrirHogares)
        self.ui.actionPlanes_Inversi_n.triggered.connect(self.abrirPlanesInversion)
        self.ui.actionInforme_Liquidaci_n.triggered.connect(self.abrirInformeLiquidacion)
        self.ui.actionSalir.triggered.connect(self.salir)

    # Funciones para abrir otras ventanas
    def abrirJuntas(self):
        self.RJuntas = Ui_Form_juntas()
        self.subRJuntas.setWidget(self.RJuntas)
        self.subRJuntas.setAttribute(Qt.WA_DeleteOnClose, False)
        self.ndi.addSubWindow(self.subRJuntas)
        self.RJuntas.btncancelar.clicked.connect(self.cerrarRJuntas)
        self.subRJuntas.setFixedSize(self.RJuntas.size())

        self.subRJuntas.show()
        self.RJuntas.btnIngresar.clicked.connect(self.ingresarJuntas)

    def ingresarJuntas(self):
        # Obtener los datos de los campos de entrada
        PJ = self.RJuntas.insPJ.text()
        fecVen = self.RJuntas.insFV.text()
        dis = self.RJuntas.insDis.text()
        ubi = self.RJuntas.insUbi.text()
        tele = int(self.RJuntas.insTel.text())
        dirNom = self.RJuntas.insED.text()
        dirEmail = self.RJuntas.insED.text()

        try:
            inJun(PJ, fecVen, dis, ubi, tele, dirNom, dirEmail)

            QMessageBox.information(self, "Éxito", "Los datos se han ingresado correctamente.")

            # clr all fields
            self.RJuntas.insPJ.setText("")
            self.RJuntas.insFV.setText("")
            self.RJuntas.insDis.setText("")
            self.RJuntas.insUbi.setText("")
            self.RJuntas.insND.setText("")
            self.RJuntas.insED.setText("")
            self.RJuntas.insTel.setText("")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al ingresar los datos: {str(e)}")

    def cerrarRJuntas(self):
        self.RJuntas.close()
        self.subRJuntas.hide()

    def cerrarRInstituciones(self):
        self.RInstituciones.close()
        self.subRInstituciones.hide()

    def cerrarRHogares(self):
        self.RHogares.close()
        self.subRHogares.hide()

    def abrirInstituciones(self):
        self.RInstituciones = Ui_instituciones()
        self.subRInstituciones.setWidget(self.RInstituciones)
        self.subRInstituciones.setAttribute(Qt.WA_DeleteOnClose, False)
        self.ndi.addSubWindow(self.subRInstituciones)
        self.RInstituciones.btncancelarins.clicked.connect(self.cerrarRInstituciones)
        self.subRInstituciones.setFixedSize(self.RInstituciones.size())

        self.subRInstituciones.show()
        self.RInstituciones.btningreins.clicked.connect(self.ingresarInstituciones)

    def ingresarInstituciones(self):
        nom = self.RInstituciones.innom.text()
        PJ = self.RInstituciones.inperju.text()
        vigen = self.RInstituciones.invige.text()
        func = self.RInstituciones.insfunciones.toPlainText()
        dis = self.RInstituciones.indis.text()
        ubi = self.RInstituciones.inubi.text()
        tele = int(self.RInstituciones.intel.text())
        email = self.RInstituciones.incorreo.text()
        presi = self.RInstituciones.inpresi.text()
        teso = self.RInstituciones.intesorero.text()

        try:
            ininst(nom, PJ, vigen, func, dis, ubi, tele, email, presi, teso)
            QMessageBox.information(self, "Éxito!", "Los datos se han ingresado correctamente.")

            # clr all fields
            self.RInstituciones.innom.setText("")
            self.RInstituciones.inperju.setText("")
            self.RInstituciones.invige.setText("")
            self.RInstituciones.insfunciones.setText("")
            self.RInstituciones.indis.setText("")
            self.RInstituciones.inubi.setText("")
            self.RInstituciones.intel.setText("")
            self.RInstituciones.incorreo.setText("")
            self.RInstituciones.inpresi.setText("")
            self.RInstituciones.intesorero.setText("")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al ingresar los datos: {str(e)}")

    def abrirHogares(self):
        self.RHogares = Ui_Hogar()
        self.subRHogares.setWidget(self.RHogares)
        self.subRHogares.setAttribute(Qt.WA_DeleteOnClose, False)
        self.ndi.addSubWindow(self.subRHogares)
        self.RHogares.btncancelar.clicked.connect(self.cerrarRHogares)
        self.subRHogares.setFixedSize(self.RHogares.size())

        self.subRHogares.show()
        self.RHogares.btningresar.clicked.connect(self.ingresarHogares)

    def ingresarHogares(self):
        nom = self.RHogares.insnomb.text()
        PJ = self.RHogares.insPJ.text()
        TV = self.RHogares.insTV.text()
        dis = self.RHogares.insdis.text()
        ubi = self.RHogares.insubi.text()
        tel = int(self.RHogares.instel.text())
        correo = self.RHogares.inscorreo.text()
        TC = self.RHogares.insTC.text()
        val = int(self.RHogares.insVP.text())
        HA = self.RHogares.insHA.text()
        PA = self.RHogares.insPA.text()
        FEP = self.RHogares.insFEP.text()
        FPI = self.RHogares.insFPI.text()
        pres = self.RHogares.inspresi.text()
        teso = self.RHogares.insteso.text()
        ban = self.RHogares.insbanco.text()
        CC = self.RHogares.insCC.text()

        try:
            inhogar(nom, PJ, TV, dis, ubi, tel, correo, TC, val, HA, PA, FEP, FPI, pres, teso, ban, CC)
            QMessageBox.information(self, "Éxito!", "Los datos se han ingresado Correctamente")

            # clr fields
            self.RHogares.insnomb.setText("")
            self.RHogares.insPJ.setText("")
            self.RHogares.insTV.setText("")
            self.RHogares.insdis.setText("")
            self.RHogares.insubi.setText("")
            self.RHogares.instel.setText("")
            self.RHogares.inscorreo.setText("")
            self.RHogares.insTC.setText("")
            self.RHogares.insVP.setText("")
            self.RHogares.insHA.setText("")
            self.RHogares.insPA.setText("")
            self.RHogares.insFEP.setText("")
            self.RHogares.insFPI.setText("")
            self.RHogares.inspresi.setText("")
            self.RHogares.insteso.setText("")
            self.RHogares.insbanco.setText("")
            self.RHogares.insCC.setText("")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al ingresar los datos: {str(e)}")

    def abrirPlanesInversion(self):
        # Lógica para abrir la ventana de Planes de Inversión
        pass

    def abrirInformeLiquidacion(self):
        # Lógica para abrir la ventana de Informe de Liquidación
        pass

    def salir(self):
        # Lógica para salir de la aplicación
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = MainWindow()
    ventana_principal.show()
    sys.exit(app.exec())
