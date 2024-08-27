# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p_change.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 661, 831))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.dispense = QtWidgets.QWidget()
        self.dispense.setObjectName("dispense")
        self.trident_button = QtWidgets.QPushButton(self.dispense)
        self.trident_button.setGeometry(QtCore.QRect(270, 390, 131, 131))
        self.trident_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.trident_button.setAutoFillBackground(False)
        self.trident_button.setStyleSheet("border-image: url(:/resource/img/trident_straw.jpeg);")
        self.trident_button.setText("")
        self.trident_button.setFlat(False)
        self.trident_button.setObjectName("trident_button")
        self.coke_button = QtWidgets.QPushButton(self.dispense)
        self.coke_button.setGeometry(QtCore.QRect(100, 90, 131, 131))
        self.coke_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.coke_button.setAutoFillBackground(False)
        self.coke_button.setStyleSheet("border-image: url(:/resource/img/coke.jpeg);")
        self.coke_button.setText("")
        self.coke_button.setFlat(False)
        self.coke_button.setObjectName("coke_button")
        self.sponch_button = QtWidgets.QPushButton(self.dispense)
        self.sponch_button.setGeometry(QtCore.QRect(440, 240, 131, 131))
        self.sponch_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sponch_button.setAutoFillBackground(False)
        self.sponch_button.setStyleSheet("border-image: url(:/resource/img/sponch.jpeg);")
        self.sponch_button.setText("")
        self.sponch_button.setFlat(False)
        self.sponch_button.setObjectName("sponch_button")
        self.mmp_button = QtWidgets.QPushButton(self.dispense)
        self.mmp_button.setGeometry(QtCore.QRect(100, 390, 131, 131))
        self.mmp_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mmp_button.setAutoFillBackground(False)
        self.mmp_button.setStyleSheet("border-image: url(:/resource/img/mm_p.jpg);")
        self.mmp_button.setText("")
        self.mmp_button.setFlat(False)
        self.mmp_button.setObjectName("mmp_button")
        self.pepsi_button = QtWidgets.QPushButton(self.dispense)
        self.pepsi_button.setGeometry(QtCore.QRect(440, 540, 131, 131))
        self.pepsi_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pepsi_button.setAutoFillBackground(False)
        self.pepsi_button.setStyleSheet("border-image: url(:/resource/img/pepsi.jpg);")
        self.pepsi_button.setText("")
        self.pepsi_button.setFlat(False)
        self.pepsi_button.setObjectName("pepsi_button")
        self.jet_button = QtWidgets.QPushButton(self.dispense)
        self.jet_button.setGeometry(QtCore.QRect(270, 90, 131, 131))
        self.jet_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.jet_button.setAutoFillBackground(False)
        self.jet_button.setStyleSheet("border-image: url(:/resource/img/jet.jpeg);")
        self.jet_button.setText("")
        self.jet_button.setFlat(False)
        self.jet_button.setObjectName("jet_button")
        self.layslem_button = QtWidgets.QPushButton(self.dispense)
        self.layslem_button.setGeometry(QtCore.QRect(270, 240, 131, 131))
        self.layslem_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.layslem_button.setAutoFillBackground(False)
        self.layslem_button.setStyleSheet("border-image: url(:/resource/img/lays_lem.jpeg);")
        self.layslem_button.setText("")
        self.layslem_button.setFlat(False)
        self.layslem_button.setObjectName("layslem_button")
        self.takis_button = QtWidgets.QPushButton(self.dispense)
        self.takis_button.setGeometry(QtCore.QRect(100, 240, 131, 131))
        self.takis_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.takis_button.setAutoFillBackground(False)
        self.takis_button.setStyleSheet("border-image: url(:/resource/img/takis.jpg);")
        self.takis_button.setText("")
        self.takis_button.setFlat(False)
        self.takis_button.setObjectName("takis_button")
        self.label_4 = QtWidgets.QLabel(self.dispense)
        self.label_4.setGeometry(QtCore.QRect(140, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily("AlmendraSmallCaps")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(46, 52, 54)")
        self.label_4.setObjectName("label_4")
        self.lays_button = QtWidgets.QPushButton(self.dispense)
        self.lays_button.setGeometry(QtCore.QRect(100, 540, 131, 131))
        self.lays_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lays_button.setAutoFillBackground(False)
        self.lays_button.setStyleSheet("border-image: url(:/resource/img/lays.jpeg);")
        self.lays_button.setText("")
        self.lays_button.setFlat(False)
        self.lays_button.setObjectName("lays_button")
        self.mm_button = QtWidgets.QPushButton(self.dispense)
        self.mm_button.setGeometry(QtCore.QRect(440, 90, 131, 131))
        self.mm_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mm_button.setAutoFillBackground(False)
        self.mm_button.setStyleSheet("border-image: url(:/resource/img/mm.jpg);")
        self.mm_button.setText("")
        self.mm_button.setFlat(False)
        self.mm_button.setObjectName("mm_button")
        self.gummies_button = QtWidgets.QPushButton(self.dispense)
        self.gummies_button.setGeometry(QtCore.QRect(270, 540, 131, 131))
        self.gummies_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gummies_button.setAutoFillBackground(False)
        self.gummies_button.setStyleSheet("border-image: url(:/resource/img/gomitas.jpg);")
        self.gummies_button.setText("")
        self.gummies_button.setFlat(False)
        self.gummies_button.setObjectName("gummies_button")
        self.snickers_button = QtWidgets.QPushButton(self.dispense)
        self.snickers_button.setGeometry(QtCore.QRect(440, 390, 131, 131))
        self.snickers_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.snickers_button.setAutoFillBackground(False)
        self.snickers_button.setStyleSheet("border-image: url(:/resource/img/snickers.jpeg);")
        self.snickers_button.setText("")
        self.snickers_button.setFlat(False)
        self.snickers_button.setObjectName("snickers_button")
        self.refill_button = QtWidgets.QPushButton(self.dispense)
        self.refill_button.setGeometry(QtCore.QRect(290, 730, 111, 51))
        self.refill_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.refill_button.setObjectName("refill_button")
        self.stackedWidget.addWidget(self.dispense)
        self.congrats = QtWidgets.QWidget()
        self.congrats.setObjectName("congrats")
        self.label_5 = QtWidgets.QLabel(self.congrats)
        self.label_5.setGeometry(QtCore.QRect(70, 330, 531, 41))
        font = QtGui.QFont()
        font.setFamily("AlmendraSmallCaps")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(46, 52, 54)")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.congrats)
        self.no_product = QtWidgets.QWidget()
        self.no_product.setObjectName("no_product")
        self.label_17 = QtWidgets.QLabel(self.no_product)
        self.label_17.setGeometry(QtCore.QRect(140, 330, 421, 41))
        font = QtGui.QFont()
        font.setFamily("AlmendraSmallCaps")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(46, 52, 54)")
        self.label_17.setObjectName("label_17")
        self.stackedWidget.addWidget(self.no_product)
        self.refill = QtWidgets.QWidget()
        self.refill.setObjectName("refill")
        self.refill_jet_button = QtWidgets.QPushButton(self.refill)
        self.refill_jet_button.setGeometry(QtCore.QRect(270, 90, 131, 131))
        self.refill_jet_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_jet_button.setAutoFillBackground(False)
        self.refill_jet_button.setStyleSheet("border-image: url(:/resource/img/jet.jpeg);")
        self.refill_jet_button.setText("")
        self.refill_jet_button.setFlat(False)
        self.refill_jet_button.setObjectName("refill_jet_button")
        self.refill_coke_button = QtWidgets.QPushButton(self.refill)
        self.refill_coke_button.setGeometry(QtCore.QRect(100, 90, 131, 131))
        self.refill_coke_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_coke_button.setAutoFillBackground(False)
        self.refill_coke_button.setStyleSheet("border-image: url(:/resource/img/coke.jpeg);")
        self.refill_coke_button.setText("")
        self.refill_coke_button.setFlat(False)
        self.refill_coke_button.setObjectName("refill_coke_button")
        self.refill_trident_button = QtWidgets.QPushButton(self.refill)
        self.refill_trident_button.setGeometry(QtCore.QRect(270, 390, 131, 131))
        self.refill_trident_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_trident_button.setAutoFillBackground(False)
        self.refill_trident_button.setStyleSheet("border-image: url(:/resource/img/trident_straw.jpeg);")
        self.refill_trident_button.setText("")
        self.refill_trident_button.setFlat(False)
        self.refill_trident_button.setObjectName("refill_trident_button")
        self.spinBox = QtWidgets.QSpinBox(self.refill)
        self.spinBox.setGeometry(QtCore.QRect(440, 720, 81, 26))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5)
        self.spinBox.setObjectName("spinBox")
        self.refill_mmp_button = QtWidgets.QPushButton(self.refill)
        self.refill_mmp_button.setGeometry(QtCore.QRect(100, 390, 131, 131))
        self.refill_mmp_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_mmp_button.setAutoFillBackground(False)
        self.refill_mmp_button.setStyleSheet("border-image: url(:/resource/img/mm_p.jpg);")
        self.refill_mmp_button.setText("")
        self.refill_mmp_button.setFlat(False)
        self.refill_mmp_button.setObjectName("refill_mmp_button")
        self.refill_layslem_button = QtWidgets.QPushButton(self.refill)
        self.refill_layslem_button.setGeometry(QtCore.QRect(270, 240, 131, 131))
        self.refill_layslem_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_layslem_button.setAutoFillBackground(False)
        self.refill_layslem_button.setStyleSheet("border-image: url(:/resource/img/lays_lem.jpeg);")
        self.refill_layslem_button.setText("")
        self.refill_layslem_button.setFlat(False)
        self.refill_layslem_button.setObjectName("refill_layslem_button")
        self.refill_gummies_button = QtWidgets.QPushButton(self.refill)
        self.refill_gummies_button.setGeometry(QtCore.QRect(270, 540, 131, 131))
        self.refill_gummies_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_gummies_button.setAutoFillBackground(False)
        self.refill_gummies_button.setStyleSheet("border-image: url(:/resource/img/gomitas.jpg);")
        self.refill_gummies_button.setText("")
        self.refill_gummies_button.setFlat(False)
        self.refill_gummies_button.setObjectName("refill_gummies_button")
        self.refill_mm_button = QtWidgets.QPushButton(self.refill)
        self.refill_mm_button.setGeometry(QtCore.QRect(440, 90, 131, 131))
        self.refill_mm_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_mm_button.setAutoFillBackground(False)
        self.refill_mm_button.setStyleSheet("border-image: url(:/resource/img/mm.jpg);")
        self.refill_mm_button.setText("")
        self.refill_mm_button.setFlat(False)
        self.refill_mm_button.setObjectName("refill_mm_button")
        self.label_2 = QtWidgets.QLabel(self.refill)
        self.label_2.setGeometry(QtCore.QRect(70, 710, 341, 41))
        font = QtGui.QFont()
        font.setFamily("AlmendraSmallCaps")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(46, 52, 54)")
        self.label_2.setObjectName("label_2")
        self.refill_lays_button = QtWidgets.QPushButton(self.refill)
        self.refill_lays_button.setGeometry(QtCore.QRect(100, 540, 131, 131))
        self.refill_lays_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_lays_button.setAutoFillBackground(False)
        self.refill_lays_button.setStyleSheet("border-image: url(:/resource/img/lays.jpeg);")
        self.refill_lays_button.setText("")
        self.refill_lays_button.setFlat(False)
        self.refill_lays_button.setObjectName("refill_lays_button")
        self.refill_sponch_button = QtWidgets.QPushButton(self.refill)
        self.refill_sponch_button.setGeometry(QtCore.QRect(440, 240, 131, 131))
        self.refill_sponch_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_sponch_button.setAutoFillBackground(False)
        self.refill_sponch_button.setStyleSheet("border-image: url(:/resource/img/sponch.jpeg);")
        self.refill_sponch_button.setText("")
        self.refill_sponch_button.setFlat(False)
        self.refill_sponch_button.setObjectName("refill_sponch_button")
        self.refill_takis_button = QtWidgets.QPushButton(self.refill)
        self.refill_takis_button.setGeometry(QtCore.QRect(100, 240, 131, 131))
        self.refill_takis_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_takis_button.setAutoFillBackground(False)
        self.refill_takis_button.setStyleSheet("border-image: url(:/resource/img/takis.jpg);")
        self.refill_takis_button.setText("")
        self.refill_takis_button.setFlat(False)
        self.refill_takis_button.setObjectName("refill_takis_button")
        self.refill_snickers_button = QtWidgets.QPushButton(self.refill)
        self.refill_snickers_button.setGeometry(QtCore.QRect(440, 390, 131, 131))
        self.refill_snickers_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_snickers_button.setAutoFillBackground(False)
        self.refill_snickers_button.setStyleSheet("border-image: url(:/resource/img/snickers.jpeg);")
        self.refill_snickers_button.setText("")
        self.refill_snickers_button.setFlat(False)
        self.refill_snickers_button.setObjectName("refill_snickers_button")
        self.refill_pepsi_button = QtWidgets.QPushButton(self.refill)
        self.refill_pepsi_button.setGeometry(QtCore.QRect(440, 540, 131, 131))
        self.refill_pepsi_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refill_pepsi_button.setAutoFillBackground(False)
        self.refill_pepsi_button.setStyleSheet("border-image: url(:/resource/img/pepsi.jpg);")
        self.refill_pepsi_button.setText("")
        self.refill_pepsi_button.setFlat(False)
        self.refill_pepsi_button.setObjectName("refill_pepsi_button")
        self.label = QtWidgets.QLabel(self.refill)
        self.label.setGeometry(QtCore.QRect(90, 20, 491, 41))
        font = QtGui.QFont()
        font.setFamily("AlmendraSmallCaps")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(46, 52, 54)")
        self.label.setObjectName("label")
        self.dispense_button = QtWidgets.QPushButton(self.refill)
        self.dispense_button.setGeometry(QtCore.QRect(40, 780, 91, 31))
        self.dispense_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.dispense_button.setObjectName("dispense_button")
        self.stackedWidget.addWidget(self.refill)
        self.position = QtWidgets.QWidget()
        self.position.setObjectName("position")
        self.E3_button = QtWidgets.QPushButton(self.position)
        self.E3_button.setGeometry(QtCore.QRect(310, 500, 91, 51))
        self.E3_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.E3_button.setText("")
        self.E3_button.setObjectName("E3_button")
        self.A5_button = QtWidgets.QPushButton(self.position)
        self.A5_button.setGeometry(QtCore.QRect(490, 300, 91, 51))
        self.A5_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.A5_button.setText("")
        self.A5_button.setObjectName("A5_button")
        self.C5_button = QtWidgets.QPushButton(self.position)
        self.C5_button.setGeometry(QtCore.QRect(490, 400, 91, 51))
        self.C5_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.C5_button.setText("")
        self.C5_button.setObjectName("C5_button")
        self.label_13 = QtWidgets.QLabel(self.position)
        self.label_13.setGeometry(QtCore.QRect(90, 470, 16, 17))
        self.label_13.setObjectName("label_13")
        self.E2_button = QtWidgets.QPushButton(self.position)
        self.E2_button.setGeometry(QtCore.QRect(220, 500, 91, 51))
        self.E2_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.E2_button.setText("")
        self.E2_button.setObjectName("E2_button")
        self.A4_button = QtWidgets.QPushButton(self.position)
        self.A4_button.setGeometry(QtCore.QRect(400, 300, 91, 51))
        self.A4_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.A4_button.setText("")
        self.A4_button.setObjectName("A4_button")
        self.B4_button = QtWidgets.QPushButton(self.position)
        self.B4_button.setGeometry(QtCore.QRect(400, 350, 91, 51))
        self.B4_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.B4_button.setText("")
        self.B4_button.setObjectName("B4_button")
        self.label_7 = QtWidgets.QLabel(self.position)
        self.label_7.setGeometry(QtCore.QRect(260, 270, 16, 17))
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.position)
        self.label_12.setGeometry(QtCore.QRect(90, 370, 16, 17))
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.position)
        self.label_9.setGeometry(QtCore.QRect(440, 270, 16, 17))
        self.label_9.setObjectName("label_9")
        self.D3_button = QtWidgets.QPushButton(self.position)
        self.D3_button.setGeometry(QtCore.QRect(310, 450, 91, 51))
        self.D3_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.D3_button.setText("")
        self.D3_button.setObjectName("D3_button")
        self.E5_button = QtWidgets.QPushButton(self.position)
        self.E5_button.setGeometry(QtCore.QRect(490, 500, 91, 51))
        self.E5_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.E5_button.setText("")
        self.E5_button.setObjectName("E5_button")
        self.label_3 = QtWidgets.QLabel(self.position)
        self.label_3.setGeometry(QtCore.QRect(130, 170, 441, 41))
        font = QtGui.QFont()
        font.setFamily("AlmendraSmallCaps")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(46, 52, 54)")
        self.label_3.setObjectName("label_3")
        self.C4_button = QtWidgets.QPushButton(self.position)
        self.C4_button.setGeometry(QtCore.QRect(400, 400, 91, 51))
        self.C4_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.C4_button.setText("")
        self.C4_button.setObjectName("C4_button")
        self.D4_button = QtWidgets.QPushButton(self.position)
        self.D4_button.setGeometry(QtCore.QRect(400, 450, 91, 51))
        self.D4_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.D4_button.setText("")
        self.D4_button.setObjectName("D4_button")
        self.D2_button = QtWidgets.QPushButton(self.position)
        self.D2_button.setGeometry(QtCore.QRect(220, 450, 91, 51))
        self.D2_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.D2_button.setText("")
        self.D2_button.setObjectName("D2_button")
        self.C3_button = QtWidgets.QPushButton(self.position)
        self.C3_button.setGeometry(QtCore.QRect(310, 400, 91, 51))
        self.C3_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.C3_button.setText("")
        self.C3_button.setObjectName("C3_button")
        self.B3_button = QtWidgets.QPushButton(self.position)
        self.B3_button.setGeometry(QtCore.QRect(310, 350, 91, 51))
        self.B3_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.B3_button.setText("")
        self.B3_button.setObjectName("B3_button")
        self.A1_button = QtWidgets.QPushButton(self.position)
        self.A1_button.setGeometry(QtCore.QRect(130, 300, 91, 51))
        self.A1_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.A1_button.setText("")
        self.A1_button.setObjectName("A1_button")
        self.label_6 = QtWidgets.QLabel(self.position)
        self.label_6.setGeometry(QtCore.QRect(170, 270, 16, 17))
        self.label_6.setObjectName("label_6")
        self.E4_button = QtWidgets.QPushButton(self.position)
        self.E4_button.setGeometry(QtCore.QRect(400, 500, 91, 51))
        self.E4_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.E4_button.setText("")
        self.E4_button.setObjectName("E4_button")
        self.D1_button = QtWidgets.QPushButton(self.position)
        self.D1_button.setGeometry(QtCore.QRect(130, 450, 91, 51))
        self.D1_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.D1_button.setText("")
        self.D1_button.setObjectName("D1_button")
        self.E1_button = QtWidgets.QPushButton(self.position)
        self.E1_button.setGeometry(QtCore.QRect(130, 500, 91, 51))
        self.E1_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.E1_button.setText("")
        self.E1_button.setObjectName("E1_button")
        self.label_10 = QtWidgets.QLabel(self.position)
        self.label_10.setGeometry(QtCore.QRect(530, 270, 16, 17))
        self.label_10.setObjectName("label_10")
        self.B2_button = QtWidgets.QPushButton(self.position)
        self.B2_button.setGeometry(QtCore.QRect(220, 350, 91, 51))
        self.B2_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.B2_button.setText("")
        self.B2_button.setObjectName("B2_button")
        self.label_15 = QtWidgets.QLabel(self.position)
        self.label_15.setGeometry(QtCore.QRect(90, 520, 16, 17))
        self.label_15.setObjectName("label_15")
        self.B1_button = QtWidgets.QPushButton(self.position)
        self.B1_button.setGeometry(QtCore.QRect(130, 350, 91, 51))
        self.B1_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.B1_button.setText("")
        self.B1_button.setObjectName("B1_button")
        self.A3_button = QtWidgets.QPushButton(self.position)
        self.A3_button.setGeometry(QtCore.QRect(310, 300, 91, 51))
        self.A3_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.A3_button.setText("")
        self.A3_button.setObjectName("A3_button")
        self.label_8 = QtWidgets.QLabel(self.position)
        self.label_8.setGeometry(QtCore.QRect(350, 270, 16, 17))
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.position)
        self.label_14.setGeometry(QtCore.QRect(90, 420, 16, 17))
        self.label_14.setObjectName("label_14")
        self.A2_button = QtWidgets.QPushButton(self.position)
        self.A2_button.setGeometry(QtCore.QRect(220, 300, 91, 51))
        self.A2_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.A2_button.setText("")
        self.A2_button.setObjectName("A2_button")
        self.C2_button = QtWidgets.QPushButton(self.position)
        self.C2_button.setGeometry(QtCore.QRect(220, 400, 91, 51))
        self.C2_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.C2_button.setText("")
        self.C2_button.setObjectName("C2_button")
        self.B5_button = QtWidgets.QPushButton(self.position)
        self.B5_button.setGeometry(QtCore.QRect(490, 350, 91, 51))
        self.B5_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.B5_button.setText("")
        self.B5_button.setObjectName("B5_button")
        self.C1_button = QtWidgets.QPushButton(self.position)
        self.C1_button.setGeometry(QtCore.QRect(130, 400, 91, 51))
        self.C1_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.C1_button.setText("")
        self.C1_button.setObjectName("C1_button")
        self.label_11 = QtWidgets.QLabel(self.position)
        self.label_11.setGeometry(QtCore.QRect(90, 320, 16, 17))
        self.label_11.setObjectName("label_11")
        self.D5_button = QtWidgets.QPushButton(self.position)
        self.D5_button.setGeometry(QtCore.QRect(490, 450, 91, 51))
        self.D5_button.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.D5_button.setText("")
        self.D5_button.setObjectName("D5_button")
        self.back_button = QtWidgets.QPushButton(self.position)
        self.back_button.setGeometry(QtCore.QRect(70, 720, 91, 31))
        self.back_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.back_button.setObjectName("back_button")
        self.stackedWidget.addWidget(self.position)
        self.stack_refilled = QtWidgets.QWidget()
        self.stack_refilled.setObjectName("stack_refilled")
        self.label_16 = QtWidgets.QLabel(self.stack_refilled)
        self.label_16.setGeometry(QtCore.QRect(200, 320, 291, 41))
        font = QtGui.QFont()
        font.setFamily("AlmendraSmallCaps")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(46, 52, 54)")
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.stack_refilled)
        self.stack_not_empty = QtWidgets.QWidget()
        self.stack_not_empty.setObjectName("stack_not_empty")
        self.label_18 = QtWidgets.QLabel(self.stack_not_empty)
        self.label_18.setGeometry(QtCore.QRect(200, 320, 321, 41))
        font = QtGui.QFont()
        font.setFamily("AlmendraSmallCaps")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(46, 52, 54)")
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.stack_not_empty)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vending Machine"))
        self.label_4.setText(_translate("MainWindow", "CHOOSE  YOUR  PRODUCT"))
        self.refill_button.setText(_translate("MainWindow", "REFILL A STACK"))
        self.label_5.setText(_translate("MainWindow", "THANKS  FOR  YOUR  PURCHASE!!"))
        self.label_17.setText(_translate("MainWindow", "PRODUCT  NO  AVAILABLE!!"))
        self.label_2.setText(_translate("MainWindow", "CHOOSE  PRODUCT QUANTITY"))
        self.label.setText(_translate("MainWindow", "CHOOSE  PRODUCT TO CHANGE"))
        self.dispense_button.setText(_translate("MainWindow", "DISPENSE"))
        self.label_13.setText(_translate("MainWindow", "D"))
        self.label_7.setText(_translate("MainWindow", "2"))
        self.label_12.setText(_translate("MainWindow", "B"))
        self.label_9.setText(_translate("MainWindow", "4"))
        self.label_3.setText(_translate("MainWindow", "CHOOSE  STACK  TO  CHANGE"))
        self.label_6.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "5"))
        self.label_15.setText(_translate("MainWindow", "E"))
        self.label_8.setText(_translate("MainWindow", "3"))
        self.label_14.setText(_translate("MainWindow", "C"))
        self.label_11.setText(_translate("MainWindow", "A"))
        self.back_button.setText(_translate("MainWindow", "BACK"))
        self.label_16.setText(_translate("MainWindow", "STACK   REFILLED!!"))
        self.label_18.setText(_translate("MainWindow", "STACK  NOT EMPTY!!"))
import resource
