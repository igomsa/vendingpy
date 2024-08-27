#!/usr/bin/env python3
#
import random

import paho.mqtt.client as mqtt

class VENDING_MACHINE(object):
    ############################################################
    def __init__(self):
        self.posible_product = ['coke', 'jet', 'mm', 'takis', 'layslem', 'sponch', 'mmp', 'trident', 'snickers', 'lays', 'gummies', 'pepsi']

        self.product = product = [[random.choice(self.posible_product)]*5 for i in range(25)]

        self.client = mqtt.Client("00")
        self.client.connect("64.227.111.82", port=1884, keepalive=60, bind_address="")


        print("\n product: \n",self.product)
    ############################################################



    ############################################################
        """
        Refill()
        Method to refill the product in the machine.

        Params:
        quantity_refill: Quantity of product to be refilled.
        product_refill: Name of product to be refilled.
        """
    def Refill(self,product_refill,quantity_refill, row, column):

        if self.product[row*5+column]==[]:
            # Fills the respective product stack, regarding the row and column values.
            self.product[row*5+column] = [product_refill for i in range(quantity_refill)]

            print("\n product: \n",self.product)

            self.client.publish("isaac/test","holi")

            return 1

        else:
            return 0


        # Mosquito server notification of refill
     ############################################################



    ############################################################
        """
        Dispense()
        Method to dispense product from vending machine

        Params:
        product_dispense: Product to be dispense (only dispense by one)
        """
    def Dispense(self, product_dispense):
        # Finds the memory locations where the product is located in the matrix.
        print("\n product: \n",self.product)

        matches = []
        print(matches)
        for i in range(len(self.product)):
            if (len(self.product[i]) > 0) and (self.product[i][0] == product_dispense):
                matches = matches+[i]

        print(matches)

        #if matches != []:

        # Creates a list that will contain the quantity of each stack of product found.
        quatity_list = [0 for i in range(len(matches))]

        list = [0 for i in range(len(matches))]

        print("\n primera lista" , list , "\n")

        for i in range(len(matches)):
            print(i)
            list[i] = len(self.product[matches[i]])

        print("\n segunda lista" , list, "\n")

        try:
            # Finds the product stack with minimum quantity
            m = min(i for i in list if i > 0)
            print("minimun: ",m)

            # Get the index of the minimun quantity of product, in  the list of product quantities.
            list_index = list.index(m)
            print("list index: ",list_index)
        except:
            print("fallé")

        # Erase one product from the stack.
        del self.product[matches[list_index]][0]
        ## report to MOSQUITO SERVER
        print("Se dispensó: "+ product_dispense)

        if len(matches) == 0 and self.product[matches[list_index]] == []:
            return 0
        else:
            return 1


    ############################################################
