#vendingpy
#  Python/MQTT Vending Machine


## Content

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Software Architecture](#sw_arch)
   1. [Graphical Interface Configuration Module](#gicm)
   2. [Vending Machine Module](#vmm)
   3. [Graphical Interface Module](#gim)
4. [Execution](#execution)


## Introduction
This repository contains a project to simulate a prototype of a vending machine system. It consists of an user-interactive LCD screen, which presents different products to be purchased by the user and dispensed by the machine. 

The system is connected via the Internet to a server that is notified of every purchase made, and every time a product ran out of the machine. 

## Requirements
+ Git
+ Minicom
+ Python 3+
+ python3-pyqt5
+ mosquitto
+ mosquitto-clients
+ python3-pip
+ "paho-mqtt<2.0.0"
+ python-etcd

## Software Architecture
On this occasion, an architecture like the one shown in Figure 1 was implemented. In it you can see 3 large modules, which contain the main elements of the software. Such modules have the following functionality:

![Software Architecture](/img/Architecture_SW.jpg "Software Architecture")

### Graphical Interface Configuration Module: 
This module is responsible for defining the dimensions, appearance and general properties of the windows, buttons and all the elements that make up the graphical interface.

### Vending Machine Module: 
This module is responsible for the actions of dispensing a product from the vending machine, refilling a stack of product, defining the initial content of the vending machine and defining the products that can be added. 
garnish and dispense. On the other hand, this module is also responsible for connecting to the MQTT server, as well as sending messages to it.

### Graphical Interface Module: 
This module is responsible for managing all the interactions of the graphical interface. Defines the actions to be taken when a button is pressed or when a particular situation occurs. It is, in general, responsible for generating the application experience, using the elements of the graphical interface.

![App flow](/img/App_GUI.jpg "App Flow")

## Execution
In a bash terminal run following command:
```bash
mosquitto_sub -h localhost -t host/vm
```
In a new terminal, go to the src folder and run the following command:
```bash
python3 display.py
```

