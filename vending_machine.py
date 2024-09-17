#!/usr/bin/env python3

import random

import paho.mqtt.client as mqtt

class VENDING_MACHINE(object):


    def __init__(self):
        """ Class constructor

        Attributes:
        posible_product: Items that can be chosen in vending machine.
        product: Name of product to be refilled.
        client: MQTT client.
        """
        self.posible_product = ['coke', 'jet', 'mm', 'takis', 'layslem', 'sponch', 'mmp', 'trident', 'snickers', 'lays', 'gummies', 'pepsi']
        self.product = product = [[random.choice(self.posible_product)]*5 for i in range(25)]
        self.client = mqtt.Client("00")
        self.client.connect("localhost")
        print("\n product: \n",self.product)




    def Refill(self,product_refill,quantity_refill, row, column):
        """ Method to refill the product in the machine.

        Params:
        quantity_refill: Quantity of product to be refilled.
        product_refill: Name of product to be refilled.
        row: Desired row to refill.
        column: Desired column to refill.
        """
        if self.product[row*5+column]==[]:
            # Fills the respective product stack, regarding the row and column values.
            self.product[row*5+column] = [product_refill for i in range(quantity_refill)]
            print("\n product: \n",self.product)
            self.client.publish("isaac/test","holi")
            return 1
        else:
            return 0  # Mosquito server notification of refill




    def Dispense(self, product_dispense):
        """ Dispense product from vending machine

        Params:
        product_dispense: Product to be dispense (only dispensing by one)
        """
        # Finds the memory locations where the product is located in the matrix.
        print("\n product: \n",self.product)
        matches = []
        print(matches)
        for i in range(len(self.product)):
            if (len(self.product[i]) > 0) and (self.product[i][0] == product_dispense):
                matches = matches+[i]
        print(matches)
        # Creates a list that will contain the quantity of each stack of product found.
        quatity_list = [0 for i in range(len(matches))]
        list = [0 for i in range(len(matches))]
        print("\n first list" , list , "\n")
        for i in range(len(matches)):
            print(i)
            list[i] = len(self.product[matches[i]])
        print("\n second list" , list, "\n")
        try:
            # Finds the product stack with minimum quantity
            m = min(i for i in list if i > 0)
            print("minimun: ",m)
            # Get the index of the minimun quantity of product, in  the list of product quantities.
            list_index = list.index(m)
            print("list index: ",list_index)
        except:
            print("failed")
        # Erase one product from the stack.
        del self.product[matches[list_index]][0]
        ## report to MOSQUITO SERVER
        print("Dispensing: "+ product_dispense)
        if len(matches) == 0 and self.product[matches[list_index]] == []:
            return 0
        else:
            return 1
