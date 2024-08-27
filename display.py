#!/usr/bin/env python3

import sys
import time
sys.path.append(".")

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

from vending_machine import VENDING_MACHINE
from p_change import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.product_refill = ''
        self.quantity_refill = 0
        self.row = 0
        self.column = 0
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.vm = VENDING_MACHINE()

        self.ui.stackedWidget.setCurrentWidget(self.ui.dispense)

        # Dispense screen buttons
        self.ui.refill_button.clicked.connect(self.Show_Refill)
        self.ui.coke_button.clicked.connect(self.Show_Coke)
        self.ui.jet_button.clicked.connect(self.Show_Jet)
        self.ui.mm_button.clicked.connect(self.Show_Mm)
        self.ui.takis_button.clicked.connect(self.Show_Takis)
        self.ui.layslem_button.clicked.connect(self.Show_Layslem)
        self.ui.sponch_button.clicked.connect(self.Show_Sponch)
        self.ui.mmp_button.clicked.connect(self.Show_Mmp)
        self.ui.trident_button.clicked.connect(self.Show_Trident)
        self.ui.snickers_button.clicked.connect(self.Show_Snickers)
        self.ui.lays_button.clicked.connect(self.Show_Lays)
        self.ui.gummies_button.clicked.connect(self.Show_Gummies)
        self.ui.pepsi_button.clicked.connect(self.Show_Pepsi)

        # Refill screen buttons
        self.ui.dispense_button.clicked.connect(self.Show_Dispense)
        self.ui.refill_coke_button.clicked.connect(self.Show_Refill_Coke)
        self.ui.refill_jet_button.clicked.connect(self.Show_Refill_Jet)
        self.ui.refill_mm_button.clicked.connect(self.Show_Refill_Mm)
        self.ui.refill_takis_button.clicked.connect(self.Show_Refill_Takis)
        self.ui.refill_layslem_button.clicked.connect(self.Show_Refill_Layslem)
        self.ui.refill_sponch_button.clicked.connect(self.Show_Refill_Sponch)
        self.ui.refill_mmp_button.clicked.connect(self.Show_Refill_Mmp)
        self.ui.refill_trident_button.clicked.connect(self.Show_Refill_Trident)
        self.ui.refill_snickers_button.clicked.connect(self.Show_Refill_Snickers)
        self.ui.refill_lays_button.clicked.connect(self.Show_Refill_Lays)
        self.ui.refill_gummies_button.clicked.connect(self.Show_Refill_Gummies)
        self.ui.refill_pepsi_button.clicked.connect(self.Show_Refill_Pepsi)

        # Position buttons
        self.ui.back_button.clicked.connect(self.Show_Back)
        self.ui.A1_button.clicked.connect(self.Show_A1)
        self.ui.A2_button.clicked.connect(self.Show_A2)
        self.ui.A3_button.clicked.connect(self.Show_A3)
        self.ui.A4_button.clicked.connect(self.Show_A4)
        self.ui.A5_button.clicked.connect(self.Show_A5)
        self.ui.B1_button.clicked.connect(self.Show_B1)
        self.ui.B2_button.clicked.connect(self.Show_B2)
        self.ui.B3_button.clicked.connect(self.Show_B3)
        self.ui.B4_button.clicked.connect(self.Show_B4)
        self.ui.B5_button.clicked.connect(self.Show_B5)
        self.ui.C1_button.clicked.connect(self.Show_C1)
        self.ui.C2_button.clicked.connect(self.Show_C2)
        self.ui.C3_button.clicked.connect(self.Show_C3)
        self.ui.C4_button.clicked.connect(self.Show_C4)
        self.ui.C5_button.clicked.connect(self.Show_C5)
        self.ui.D1_button.clicked.connect(self.Show_D1)
        self.ui.D2_button.clicked.connect(self.Show_D2)
        self.ui.D3_button.clicked.connect(self.Show_D3)
        self.ui.D4_button.clicked.connect(self.Show_D4)
        self.ui.D5_button.clicked.connect(self.Show_D5)
        self.ui.E1_button.clicked.connect(self.Show_E1)
        self.ui.E2_button.clicked.connect(self.Show_E2)
        self.ui.E3_button.clicked.connect(self.Show_E3)
        self.ui.E4_button.clicked.connect(self.Show_E4)
        self.ui.E5_button.clicked.connect(self.Show_E5)



        # Dispense screen buttons response
    def Show_Refill(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.refill)
    def Show_Coke(self):
        self.ui.coke_button.hide()

        if self.vm.Dispense('coke'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))


    def Show_Jet(self):
        self.ui.coke_button.show()

        if self.vm.Dispense('jet'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Mm(self):

        if self.vm.Dispense('mm'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Takis(self):

        if self.vm.Dispense('takis'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Layslem(self):

        if self.vm.Dispense('layslem'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Sponch(self):

        if self.vm.Dispense('sponch'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Mmp(self):

        if self.vm.Dispense('mmp'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Trident(self):

        if self.vm.Dispense('trident'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Snickers(self):

        if self.vm.Dispense('snickers'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Lays(self):

        if self.vm.Dispense('lays'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Gummies(self):

        if self.vm.Dispense('gummies'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))

    def Show_Pepsi(self):

        if self.vm.Dispense('pepsi'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.congrats)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.no_product)

        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))


        # Refill screen buttons
    def Show_Dispense(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dispense)
    def Show_Refill_Coke(self):
        self.product_refill = 'coke'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Jet(self):
        self.product_refill = 'jet'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Mm (self):
        self.product_refill = 'mm'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Takis(self):
        self.product_refill = 'takis'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Layslem(self):
        self.product_refill = 'layslem'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Sponch(self):
        self.product_refill = 'sponch'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Mmp(self):
        self.product_refill = 'mmp'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Trident(self):
        self.product_refill = 'trident'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Snickers(self):
        self.product_refill = 'snickers'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Lays(self):
        self.product_refill = 'lays'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Gummies(self):
        self.product_refill = 'gummies'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)
    def Show_Refill_Pepsi(self):
        self.product_refill = 'pepsi'
        self.quantity_refill = self.ui.spinBox.value()
        self.ui.stackedWidget.setCurrentWidget(self.ui.position)



        # Position buttons
    def Show_Back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.refill)
    def Show_A1(self):
        self.row=0
        self.column=0
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_A2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=0
        self.column=1
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_A3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=0
        self.column=2
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_A4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=0
        self.column=3
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_A5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=0
        self.column=4
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_B1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=1
        self.column=0
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_B2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=1
        self.column=1
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_B3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=1
        self.column=2
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_B4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=1
        self.column=3
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_B5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=1
        self.column=4
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_C1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=2
        self.column=0
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_C2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=2
        self.column=1
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_C3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=2
        self.column=2
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_C4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=2
        self.column=3
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_C5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=2
        self.column=4
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_D1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=3
        self.column=0
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_D2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=3
        self.column=1
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_D3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=3
        self.column=2
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_D4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=3
        self.column=3
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_D5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=3
        self.column=4
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_E1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=4
        self.column=0
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_E2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=4
        self.column=1
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_E3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=4
        self.column=2
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_E4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=4
        self.column=3
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
    def Show_E5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        self.row=4
        self.column=4
        print("\n product refill: ",self.product_refill)
        print("\n quantity refill : ",self.quantity_refill)
        print("\n row : ",self.row)
        print("\n col : ",self.column)

        empty = self.vm.Refill(self.product_refill, self.quantity_refill, self.row, self.column)

        if empty:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_refilled)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.stack_not_empty)

        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dispense))
        
    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
