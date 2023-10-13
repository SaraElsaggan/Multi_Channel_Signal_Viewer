from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import re
import time#IMPORTS
import csv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QPushButton,  QWidget, QDesktopWidget, QFileDialog, QTableWidgetItem , QComboBox
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import QEvent, QObject, QTimer, Qt
from PyQt5 import QtCore
import numpy as np
from mainwindow import Ui_MainWindow
from tkinter import *
from tkinter import colorchooser
from pyqtgraph import PlotWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget , QDesktopWidget , QFileDialog
from PyQt5.QtCore import QStateMachine, QState, QPropertyAnimation
from PyQt5.QtCore import QDateTime, Qt

import pyqtgraph as pg
import pandas as pd

class CheckableComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self._changed = False

        self.view().pressed.connect(self.handleItemPressed)

    def setItemChecked(self, index, checked=False):
        item = self.model().item(index, self.modelColumn()) # QStandardItem object

        if checked:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)

        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self._changed = True


    def hidePopup(self):
        if not self._changed:
            super().hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == Qt.Checked



class MyWindow(QMainWindow):  
    
    def __init__(self ):
        super(MyWindow , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        
        self.graph1 = PlotWidget(self.ui.centralwidget)
        self.graph1.setGeometry(30, 50, 770, 300)
        self.graph1.setObjectName("Channel1")
        self.graph1.setYRange(-2,2)
        
        self.graph2 = PlotWidget(self.ui.centralwidget)
        self.graph2.setGeometry(30, 400, 770, 300)
        self.graph2.setObjectName("Channel1")
        self.graph2.setYRange(-2,2)

        self.timer_1 = QtCore.QTimer()
        self.timer_1.setInterval(100) 

        self.timer_2 = QtCore.QTimer()
        self.timer_2.setInterval(100) 
        
        # self.data_lines = []
        # self.data_indices = []
        self.signals_1 =[]
        self.signals_2 =[]

        self.ui.btn_add_sig_viewer_1.clicked.connect(self.upload_data_grph_1)   
        # self.ui.btn_add_sig_viewer_1.clicked.connect(self.open_file_1)   
        self.ui.btn_play_pasuse_viewer_1.clicked.connect(self.play_pause_grph_1)

        self.ui.btn_zoom_in_viewer_1.clicked.connect(self.zoom_in_grph_1)
        self.ui.btn_zoom_out_viewer_1.clicked.connect(self.zoom_out_grph_1)
       
        self.ui.btn_fast_viewer_1.clicked.connect(self.faster_grph_1)
        self.ui.btn_slow_viewer_1.clicked.connect(self.slower_grph_1)
        
        self.ui.actionreport.triggered.connect(self.generate_report)
        
        self.ui.btn_clear_viewer_1.clicked.connect(self.clear_grph_1)
        
        self.ui.btn_slow_grpbox_viewer_1.clicked.connect(self.slower_grph_1)
        self.ui.btn_fast_grpbox_viewer_1.clicked.connect(self.faster_grph_1)
        
        self.ui.btn_chng_colr_grpbox_viewer_1.clicked.connect(self.change_sig_color_grph_1)
        self.ui.btn_move_viewer_1.clicked.connect(self.move_signal_from_grph_1)
        # self.ui.btn_entr_name_viewer_1.clicked.connect(self.signal_rename_grph_1)

        

        self.ui.btn_add_sig_viewer_2.clicked.connect(self.upload_data_grph_2)   
        # self.ui.btn_add_sig_viewer_2.clicked.connect(self.open_file_1)   
        self.ui.btn_play_pasuse_viewer_2.clicked.connect(self.play_pause_grph_2)

        self.ui.btn_zoom_in_viewer_2.clicked.connect(self.zoom_in_grph_2)
        self.ui.btn_zoom_out_viewer_2.clicked.connect(self.zoom_out_grph_2)
       
        self.ui.btn_fast_viewer_2.clicked.connect(self.faster_grph_2)
        self.ui.btn_slow_viewer_2.clicked.connect(self.slower_grph_2)
        
        
        self.ui.btn_clear_viewer_2.clicked.connect(self.clear_grph_2)
        
        self.ui.btn_chng_colr_grpbox_viewer_2.clicked.connect(self.change_sig_color_grph_2)
        # self.ui.btn_entr_name_viewer_2.clicked.connect(self.signal_rename_grph_2)
        
        self.i_1 = 1
        self.flag_1 = False
        self.data_1 = {}
        self.data_line_1 = {}
        
        
        self.selectid_file = None
        self.end = 0
        self.start = 0 
        self.index_1 = 50
        self.index_2 = 50
        self.second_value_1 = 0
        self.second_value_2 = 0

        self.pen = pg.mkPen(color=(255, 0, 0))



    def clear_grph_1(self):
        self.graph1.clear()
        self.timer_1.stop()
        icon = QtGui.QPixmap("play.png")
        self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
        self.signals_1.clear()
        # self.ui.comb_rename_viewer_1.clear()
        self.ui.comb_sig_colr_grpbox_viewer_1.clear()
        self.ui.comb_sig_disp_viewer_1.clear()
           
    def upload_data_grph_1(self):
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")
        # print(file_path)
        # if file_path:

        color =  colorchooser.askcolor()[1]
        print(color)

        # self.data = pd.read_csv(file_path)
        data = np.genfromtxt(file_path, delimiter = ',')
        x1 = data[:, 0].tolist()
        y1 = data[:, 1].tolist()
        # print(x1)
        file_name = os.path.basename(file_path[:-4])

        print(f"({file_name})")

        self.add_signal_to_combo_grph_1(file_name)
        
        
        signal = {
            "color" : color ,
            "name" : file_name, 
            "display" : True,
            "data" : data,
            "x1" : x1,
            "y1" : y1,
            "data_lines":[],
            "data_indices":[], 
            "idx1" : None
        }
        
        # print(signal["x1"])
        self.signals_1.append(signal)
        # print(self.signals_1)
        for i_signal in self.signals_1:
            if i_signal["name"] == file_name:
                signal = i_signal
        # signal = [signal for signal in  self                                                  .signals if signal["name"] == file_name]
        # self.plot_signal([signal for signal in self.signals_1 if signal["name"] == file_name])
        # self.plot_signal(file_name)
        self.plot_signal_grph_1(signal)
        print(signal["color"])
        # print([signal["color"] for signal in self.signals_1 if signal["name"] == file_name])
        
        # print(self.x1)
        # print(self.y1)
         
    def plot_signal_grph_1(self , signal ) :
    # def plot_signal(self , file_name ) :
    #     for i_signal in self.signals_1:
    #         if i_signal["name"] == file_name:
    #             signal = i_signal
        data_line = self.graph1.plotItem.plot(signal["x1"], signal["y1"], pen=signal["color"])
        # print(f'here{signal["color"]}')
        signal["data_lines"].append(data_line)
        signal["data_indices"].append(0)
        signal["idx1"]=0
        self.graph1.plotItem.getViewBox().setAutoPan(x=True,y=True)
        # self.timer_1.setInterval()
        self.timer_1.timeout.connect(lambda:self.update_plot_data_grph_1(signal))
        # self.timer_1.timeout.connect(lambda:self.update_plot_data(file_name))
        self.timer_1.start()
        self.graph1.show()
        self.graph1.setXRange(0,0.002*len(signal["data"]))

        icon = QtGui.QPixmap("pause.png")
        self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
       
    def update_plot_data_grph_1(self,signal):
    # def update_plot_data(self,file_name):

        # for i_signal in self.signals_1:
        #     if i_signal["name"] == file_name:
        #         signal = i_signal
                
        for i in range(len(signal["data_lines"])):
            x = signal["x1"][:signal["data_indices"][i]]
            y = signal["y1"][:signal["data_indices"][i]]
            signal["data_indices"][i] += 10  # Update the index for this signal
            if signal["data_indices"][i] > len(signal["x1"]):
                signal["data_indices"][i] = 0  # Reset the index for this signal
            if signal["x1"][signal["data_indices"][i]] > 0.5:
                self.graph1.setLimits(xMin=min(x, default=0), xMax=max(x, default=0))  # Disable panning over x-limits
            self.graph1.plotItem.setXRange(max(x, default=0) - 0.5, max(x, default=0))
            signal["data_lines"][i].setData(x, y)

    def play_pause_grph_1(self):
        if self.timer_1.isActive():
            self.timer_1.stop()
            icon = QtGui.QPixmap("play.png")
            self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
        else:
            self.timer_1.start()
            icon = QtGui.QPixmap("pause.png")
            self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))

    def add_signal_to_combo_grph_1(self , file_name):
        self.ui.comb_sig_colr_grpbox_viewer_1.addItem(file_name)
        self.ui.comb_move_viewer_1.addItem(file_name)
        self.ui.comb_sig_disp_viewer_1.addItem(file_name)
                
    def zoom_out_grph_1(self):
          # Increase the visible range 
         self.graph1.getViewBox().scaleBy((1.2, 1.2))
        #  self.graph2.getViewBox().scaleBy((1.2, 1.2))

    def zoom_in_grph_1(self):
         # Decrease the visible range 
         self.graph1.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
        #  self.graph2.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
    
    def faster_grph_1(self):
         # Decrease the timer interval to make updates faster
        self.timer_1.setInterval(self.timer_1.interval() // 2)
        # self.timer_2.setInterval(self.timer_2.interval() // 2)
    
    def slower_grph_1(self):
         # Increase the timer interval to make updates slower
         self.timer_1.setInterval(self.timer_1.interval() * 2)
        #  self.timer_2.setInterval(self.timer_2.interval() * 2)

    def open_file_1(self):
        # Get file path
        file_path = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

        # Open file and retrieve data
        file = open(file_path[0])
        lines = file.readlines()


        file_name = file_path[0].split("/")[-1][:-4]
        print(file_name)
        self.data_1[file_name] = {}
        self.data_1[file_name]['x_values'] = np.array([x.split(",")[0] for x in lines],dtype=float)
        self.data_1[file_name]['y_values'] = np.array([y.split(",")[1].strip("/\n") for y in lines],dtype=float)

        self.data_line_1[file_name] = self.graph1.plot()
        if(len(self.data_line_1) > self.i_1):
            self.i_1+=1
            self.flag_1 =True
           
        first_value = self.data_1[file_name]['x_values'][0]
        
        self.second_value_1 = self.data_1[file_name]['x_values'][1]
        self.second_value_1 = self.second_value_1 - first_value 

        self.end = self.second_value_1 * 100
        
        color =  colorchooser.askcolor()[1]
        print(color)

        signal = {
            "color" : color ,
            "name" : file_name, 
            "display" : True,
        }
        
        self.signals_1.append(signal)
        self.add_signal_to_combo_grph_1(file_name)
        # print(self.signals_1)



        # self.timer_1 = QtCore.QTimer()
        # self.timer_1.setInterval(50)
        self.timer_1.timeout.connect(self.update_plot_data_1)
        self.timer_1.start()  

    def update_plot_data_1(self):
        if(self.flag_1 == True):
            self.index_1 = 50
            self.start  = 0
            self.end  = self.second_value_1 * 100
            self.flag_1 = False

            
        for signal in self.data_line_1:
            x_to_plot = self.data_1[signal]['x_values'][:self.index_1]
            y_to_plot = self.data_1[signal]['y_values'][:self.index_1]
            self.data_line_1[signal].setData(x_to_plot, y_to_plot)

        self.index_1 += 1
        self.start = self.start + self.second_value_1
        self.end = self.end + self.second_value_1
        
        self.graph1.setXRange(self.start ,self.end)

    def change_sig_color_grph_1(self):
        if self.ui.comb_sig_colr_grpbox_viewer_1.currentText() != "chose signal":
            signal_to_be_changed = self.ui.comb_sig_colr_grpbox_viewer_1.currentText()
            for signal in self.signals_1 :
                if signal["name"] == signal_to_be_changed:
                    signal["color"] = colorchooser.askcolor()[1]
            
                    for data_line in signal["data_lines"]:
                        data_line.setPen(signal["color"])   
           
    def move_signal_from_grph_1(self):
        if self.ui.comb_move_viewer_1.currentText != "choose signal":
            signal_to_move = self.ui.comb_move_viewer_1.currentText()
            for signal in self.signals_1:
                if signal["name"] == signal_to_move:
                    for data_line in signal["data_lines"]:
                        self.graph1.removeItem(data_line)
                        self.graph2.addItem(data_line)
                    
                    self.signals_2.append(signal)
                    self.signals_1.remove(signal)
                    self.updata_combo_bxs_grph_1()
                    self.updata_combo_bxs_grph_2()
                    
    def updata_combo_bxs_grph_1(self):
        
        self.ui.comb_sig_colr_grpbox_viewer_1.clear()
        self.ui.comb_move_viewer_1.clear()
        self.ui.comb_sig_disp_viewer_1.clear()

        for signal in self.signals_1:
            self.ui.comb_sig_colr_grpbox_viewer_1.addItem(signal["name"])
            self.ui.comb_move_viewer_1.addItem(signal["name"])
            self.ui.comb_sig_disp_viewer_1.addItem(signal["name"])

    



    def clear_grph_2(self):
        self.graph1.clear()
        self.timer_2.stop()
        icon = QtGui.QPixmap("play.png")
        self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))
        self.signals_2.clear()
        # self.ui.comb_rename_viewer_2.clear()
        self.ui.comb_sig_colr_grpbox_viewer_2.clear()
        self.ui.comb_sig_disp_viewer_2.clear()
           
    def upload_data_grph_2(self):
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")
        # print(file_path)
        # if file_path:

        color =  colorchooser.askcolor()[1]
        print(color)

        # self.data = pd.read_csv(file_path)
        data = np.genfromtxt(file_path, delimiter = ',')
        x1 = data[:, 0].tolist()
        y1 = data[:, 1].tolist()
        # print(x1)
        file_name = os.path.basename(file_path[:-4])

        print(f"({file_name})")

        self.add_signal_to_combo_grph_2(file_name)
        
        
        signal = {
            "color" : color ,
            "name" : file_name, 
            "display" : True,
            "data" : data,
            "x1" : x1,
            "y1" : y1,
            "data_lines":[],
            "data_indices":[], 
            "idx1" : None
        }
        
        # print(signal["x1"])
        self.signals_1.append(signal)
        # print(self.signals_1)
        for i_signal in self.signals_1:
            if i_signal["name"] == file_name:
                signal = i_signal
        # signal = [signal for signal in  self                                                  .signals if signal["name"] == file_name]
        # self.plot_signal([signal for signal in self.signals_1 if signal["name"] == file_name])
        # self.plot_signal(file_name)
        self.plot_signal_grph_2(signal)
        print(signal["color"])
        # print([signal["color"] for signal in self.signals_1 if signal["name"] == file_name])
        
        # print(self.x1)
        # print(self.y1)
         
    def plot_signal_grph_2(self , signal ) :
    # def plot_signal(self , file_name ) :
    #     for i_signal in self.signals_1:
    #         if i_signal["name"] == file_name:
    #             signal = i_signal
        data_line = self.graph2.plotItem.plot(signal["x1"], signal["y1"], pen=signal["color"])
        # print(f'here{signal["color"]}')
        signal["data_lines"].append(data_line)
        signal["data_indices"].append(0)
        signal["idx1"]=0
        self.graph2.plotItem.getViewBox().setAutoPan(x=True,y=True)
        # self.timer_2.setInterval()
        self.timer_2.timeout.connect(lambda:self.update_plot_data_grph_2(signal))
        # self.timer_2.timeout.connect(lambda:self.update_plot_data(file_name))
        self.timer_2.start()
        self.graph2.show()
        self.graph2.setXRange(0,0.002*len(signal["data"]))

        icon = QtGui.QPixmap("pause.png")
        self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))
       
    def update_plot_data_grph_2(self,signal):
    # def update_plot_data(self,file_name):

        # for i_signal in self.signals_1:
        #     if i_signal["name"] == file_name:
        #         signal = i_signal
                
        for i in range(len(signal["data_lines"])):
            x = signal["x1"][:signal["data_indices"][i]]
            y = signal["y1"][:signal["data_indices"][i]]
            signal["data_indices"][i] += 10  # Update the index for this signal
            if signal["data_indices"][i] > len(signal["x1"]):
                signal["data_indices"][i] = 0  # Reset the index for this signal
            if signal["x1"][signal["data_indices"][i]] > 0.5:
                self.graph2.setLimits(xMin=min(x, default=0), xMax=max(x, default=0))  # Disable panning over x-limits
            self.graph2.plotItem.setXRange(max(x, default=0) - 0.5, max(x, default=0))
            signal["data_lines"][i].setData(x, y)

    def play_pause_grph_2(self):
        if self.timer_2.isActive():
            self.timer_2.stop()
            icon = QtGui.QPixmap("play.png")
            self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))
        else:
            self.timer_2.start()
            icon = QtGui.QPixmap("pause.png")
            self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))

    def add_signal_to_combo_grph_2(self , file_name):
        self.ui.comb_sig_colr_grpbox_viewer_2.addItem(file_name)
        # self.ui.comb_rename_viewer_2.addItem(file_name)
        self.ui.comb_sig_disp_viewer_2.addItem(file_name)
                
    def zoom_out_grph_2(self):
          # Increase the visible range 
         self.graph2.getViewBox().scaleBy((1.2, 1.2))
        #  self.graph2.getViewBox().scaleBy((1.2, 1.2))

    def zoom_in_grph_2(self):
         # Decrease the visible range 
         self.graph2.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
        #  self.graph2.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
    
    def faster_grph_2(self):
         # Decrease the timer interval to make updates faster
        self.timer_2.setInterval(self.timer_2.interval() // 2)
        # self.timer_2.setInterval(self.timer_2.interval() // 2)
    
    def slower_grph_2(self):
         # Increase the timer interval to make updates slower
         self.timer_2.setInterval(self.timer_2.interval() * 2)
        #  self.timer_2.setInterval(self.timer_2.interval() * 2)

    def open_file_2(self):
        # Get file path
        file_path = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

        # Open file and retrieve data
        file = open(file_path[0])
        lines = file.readlines()


        file_name = file_path[0].split("/")[-1][:-4]
        print(file_name)
        self.data_2[file_name] = {}
        self.data_2[file_name]['x_values'] = np.array([x.split(",")[0] for x in lines],dtype=float)
        self.data_2[file_name]['y_values'] = np.array([y.split(",")[1].strip("/\n") for y in lines],dtype=float)

        self.data_line_2[file_name] = self.graph2.plot()
        if(len(self.data_line_2) > self.i_2):
            self.i_2+=1
            self.flag_2 =True
           
        first_value = self.data_2[file_name]['x_values'][0]
        
        self.second_value_2 = self.data_2[file_name]['x_values'][1]
        self.second_value_2 = self.second_value_2 - first_value 

        self.end = self.second_value_2 * 100
        
        color =  colorchooser.askcolor()[1]
        print(color)

        signal = {
            "color" : color ,
            "name" : file_name, 
            "display" : True,
        }
        
        self.signals_1.append(signal)
        self.add_signal_to_combo_grph_2(file_name)
        # print(self.signals_1)



        # self.timer_2 = QtCore.QTimer()
        # self.timer_2.setInterval(50)
        self.timer_2.timeout.connect(self.update_plot_data_2)
        self.timer_2.start()  

    def update_plot_data_2(self):
        if(self.flag_2 == True):
            self.index_2 = 50
            self.start  = 0
            self.end  = self.second_value_2 * 100
            self.flag_2 = False

            
        for signal in self.data_line_2:
            x_to_plot = self.data_2[signal]['x_values'][:self.index_2]
            y_to_plot = self.data_2[signal]['y_values'][:self.index_2]
            self.data_line_2[signal].setData(x_to_plot, y_to_plot)

        self.index_2 += 1
        self.start = self.start + self.second_value_2
        self.end = self.end + self.second_value_2
        
        self.graph2.setXRange(self.start ,self.end)

    def move_signal_from_grph_2(self):
        if self.ui.comb_move_viewer_2.currentText != "choose signal":
            signal_to_move = self.ui.comb_move_viewer_2.currentText()
            for signal in self.signals_2:
                if signal["name"] == signal_to_move:
                    for data_line in signal["data_lines"]:
                        self.graph1.removeItem(data_line)
                        self.graph2.addItem(data_line)
                    
                    self.signals_2.append(signal)
                    self.signals_2.remove(signal)
                    self.updata_combo_bxs_grph_1()
                    self.updata_combo_bxs_grph_2()
                    

    def updata_combo_bxs_grph_2(self):
        
        self.ui.comb_sig_colr_grpbox_viewer_2.clear()
        self.ui.comb_move_viewer_2.clear()
        self.ui.comb_sig_disp_viewer_2.clear()

        for signal in self.signals_2:
            self.ui.comb_sig_colr_grpbox_viewer_2.addItem(signal["name"])
            self.ui.comb_move_viewer_2.addItem(signal["name"])
            self.ui.comb_sig_disp_viewer_2.addItem(signal["name"])

    
    # def signal_rename_grph_2(self):
    #     if self.ui.comb_sig_colr_grpbox_viewer_2.currentText() != "chose signal":
    #         old_name = self.ui.comb_rename_viewer_2.currentText()
    #         new_name = input("Enter a signal name: ")
    #         for signal in self.signals_1 :
    #                 if signal["name"] == old_name:
    #                     signal["name"] = new_name
    #                     # self.update_sig_name_in_combo(old_name , signal)
    
    # def update_sig_name_in_combo_grph_1(self , old_name , signal):
    #     # for index in range(self.ui.comb_rename_viewer_1.count()):
    #         if self.ui.comb_rename_viewer_1.itemText(index) == old_name:
    #             self.ui.comb_rename_viewer_1.setItemText(index,signal["name"] )
        
       
       
       
       
            

    def change_sig_color_grph_2(self):
        if self.ui.comb_sig_colr_grpbox_viewer_1.currentText() != "chose signal":
            signal_to_be_changed = self.ui.comb_sig_colr_grpbox_viewer_1.currentText()
            for signal in self.signals_1 :
                if signal["name"] == signal_to_be_changed:
                    signal["color"] = colorchooser.askcolor()[1]
            
                    for data_line in signal["data_lines"]:
                        data_line.setPen(signal["color"])   
            
            # # signal["color"] = colorchooser.askcolor()[1]
            # print(signal_to_be_changed)
            # print(signal["color"])
   
    def generate_report(self):
        # Create a file dialog to choose the signals to include in the report
        selected_signals, _ = QFileDialog.getOpenFileNames(self, "Select Signals for Report", "", "CSV Files (*.csv)")
        
        if selected_signals:
            # Create a dictionary to hold selected signal data
            selected_data = {}

            # Open and read the selected CSV files
            for file_path in selected_signals:
                file = open(file_path)
                lines = file.readlines()
                file_name = file_path
                selected_data[file_name] = {}
                selected_data[file_name]['x_values'] = np.array([x.split(",")[0] for x in lines], dtype=float)
                selected_data[file_name]['y_values'] = np.array([y.split(",")[1].strip("/\n") for y in lines], dtype=float)

            # Generate the PDF report with statistics
            # You can customize the report generation code based on your requirements
            # For example, create a title, add statistics for each selected signal, etc.
            # Finally, call export_to_pdf to save the report
            self.data_1 = selected_data
            # self.export_to_pdf()


    # def export_to_pdf(self):
    #     # Get a file path for saving the PDF
    #     pdf_file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF Report", "", "PDF Files (*.pdf)")
        
    #     if pdf_file_path:
    #         # Create a PDF document
    #         doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)

    #         # Create story elements for the report content
    #         styles = getSampleStyleSheet()
    #         story = []
    #         title = "Signal Data Report"
    #         story.append(Paragraph(title, styles["Title"]))
    #         story.append(Spacer(1, 12))

    #         # Add content to the PDF report
    #         for signal_name, signal_data in self.data_1.items():
    #             signal_statistics = f"Statistics for Signal: {signal_name}"
    #             story.append(Paragraph(signal_statistics, styles["Heading2"]))
                
    #             # Calculate statistics (mean, std, max, min, duration) for the signal data
    #             signal_values = signal_data['y_values']
    #             # mean_value = mean(signal_values)
    #             # std_deviation = stdev(signal_values)
    #             max_value = max(signal_values)
    #             min_value = min(signal_values)
    #             duration = len(signal_values)  # Duration can be the length of the data
                
    #             statistics_text = (
    #                 # f"Mean: {mean_value:.2f}<br/>"
    #                 # f"Standard Deviation (STD): {std_deviation:.2f}<br/>"
    #                 f"Maximum Value: {max_value:.2f}<br/>"
    #                 f"Minimum Value: {min_value:.2f}<br/>"
    #                 f"Duration: {duration} data points"
    #             )
                
    #             story.append(Paragraph(statistics_text, styles["Normal"]))
    #             story.append(Spacer(1, 12))

    #         # Build the PDF document
    #         doc.build(story)

'''   
#------------------------------------------------  
        self.i_1 = 1
        self.flag_1 = False
        self.data_1 = {}
        self.data_line_1 = {}

        # self.i_2 = 1
        # self.flag_2 = False
        # self.data_2 = {}
        # self.data_line_2 = {}

       
        
        self.ui.act_add_sig_viewer_1.triggered.connect(self.open_file_1)
       
       
        self.selectid_file = None
        self.end = 0
        self.start = 0 
        self.index_1 = 50
        self.index_2 = 50
        self.second_value_1 = 0
        self.second_value_2 = 0

        self.pen = pg.mkPen(color=(255, 0, 0))


        self.graph2 = PlotWidget(self.ui.centralwidget)
        self.graph2.setGeometry(10, 349, 750, 300)
        self.graph2.setObjectName("Channel2")
        self.graph2.setYRange(-2,2)

    





'''
#---------------------------------------------------  
'''
        #         self.data_1 = {}
#         self.data_line_1 = {}

#         self.data_2 = {}
#         self.data_line_2 = {}
        
#         self.graph_1_signals = []

        # self.ui.act_add_sig_viewer_1.triggered.connect(self.open_file)
        
#         self.selectid_file = None

#         self.index_1 = 50
#         self.index_2 = 50

#         self.pen = pg.mkPen(color=(255, 0, 0))
        
        
#         self.signals_1_grph_1 = []

        # self.graph1 = PlotWidget(self.ui.centralwidget)
        # self.graph1.setGeometry(30, 50, 770, 300)
        # self.graph1.setObjectName("Channel1")
        # self.graph1.setYRange(-2,2)

        # self.timer = QTimer()
        # self.timer_1.timeout.connect(self.load_data)
        # self.timer_1.start(500)
        # self.graph1.show()
        
    # def update(self):
    #     data = pd.read_csv("C:/Users/Sara/Desktop/ECG.csv")
    #     data = np.random.random(100)
    #     # x = data.iloc[:, 0] # Replace 'x_column' with the actual column name containing X-axis data
    #     # y = data.iloc[:, 1] # Replace 'x_column' with the actual column name containing X-axis data
    #     self.graph1.plotItem.clear()
    #     # y = data[: , 1]  # Replace 'y_column' with the actual column name containing Y-axis data

    #     # Plot the data
    #     # self.graph1.plotItem.plot(x, y)
    #     self.graph1.plotItem.plot(data)
        
    # def load_data(self):
    #     x = []
    #     y = []

    #     with open("C:/Users/Sara/Desktop/ECG.csv", 'r') as file:
    #         reader = csv.reader(file , delimiter='\t')
    #         for row in reader:
    #             if len(row) == 2:
    #                 x.append(float(row[0]))
    #                 y.append(float(row[1]))
    #     # Set the data for the plot
    #     self.graph1.setData(x = x, y = y)

    # def open_file(self):
        # file =QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","(*.csv) ")
        # if file :
        #     print(f"selected file :{file}")
            
                
                
                
                
#         self.ui.btn_zoom_in_viewer_1.clicked.connect(self.zoom_in_graph_1)
#         self.ui.btn_zoom_out_viewer_1.clicked.connect(self.zoom_out_graph_1)
        
#         self.ui.btn_zoom_in_grpbox_viewer_1.clicked.connect(self.zoom_in_graph_1)
#         self.ui.btn_zoom_out_grpbox_viewer_1.clicked.connect(self.zoom_out_graph_1)
        
#         self.ui.btn_zoom_in_viewer_2.clicked.connect(self.zoom_in_graph_2)
#         self.ui.btn_zoom_out_viewer_2.clicked.connect(self.zoom_out_graph_2)
        
#         self.ui.btn_zoom_in_grpbox_viewer_2.clicked.connect(self.zoom_in_graph_2)
#         self.ui.btn_zoom_out_grpbox_viewer_2.clicked.connect(self.zoom_out_graph_2)
        
#         self.ui.btn_add_sig_viewer_1.clicked.connect(self.open_file_1)
#         self.ui.btn_add_sig_viewer_2.clicked.connect(self.open_file_2)
        
#         self.ui.btn_chng_colr_grpbox_viewer_1.clicked.connect(self.chng_clor_grph_1)
        
#     def open_file_1(self):
#             # Get file path
#         file_path = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

#         # Open file and retrieve data
#         file = open(file_path[0])
#         lines = file.readlines()

#         # file_name = file_path[0]
        
#         ###################
#         file_name = os.path.basename(file_path[0][:-4])

#         print(f"({file_name})")

#         self.add_signal_to_combo_graph_1(file_name)
        
        
#         signal = {
#             "color" : "#FFFFFF" ,
#             "name" : file_name, 
#             "display" : True,
#         }
        
#         self.graph_1_signals.append(signal)
        
                
#         ###################
#         self.data_1[file_name] = {}
#         self.data_1[file_name]['x_values'] = np.array([x.split(",")[0] for x in lines],dtype=float)
#         self.data_1[file_name]['y_values'] = np.array([y.split(",")[1].strip("/\n") for y in lines],dtype=float)
# #------------------------------ i wanna return a color from the list ---------------------
#         self.data_line_1[file_name] = self.graph1.plot()
#         # self.data_line_1[file_name] = self.graph1.plot(pen = self.pen)
       
#         self.timer_1 = QtCore.QTimer()
#         self.timer_1.setInterval(50)
#         self.timer_1.timeout.connect(self.update_plot_data_1)
#         self.timer_1.start()  

#     def update_plot_data_1(self):
#         for signal in self.data_line_1:
#             x_to_plot = self.data_1[signal]['x_values'][self.index_1 -50 :self.index_1]
#             y_to_plot = self.data_1[signal]['y_values'][self.index_1 -50 :self.index_1]
#             self.data_line_1[signal].setData(x_to_plot, y_to_plot)
#         self.index_1 += 1

#     def open_file_2(self):
#         # Get file path
#         file_path = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

#         # Open file and retrieve data
#         file = open(file_path[0])
#         lines = file.readlines()

#         # file_name = file_path[0]
#         file_name = os.path.basename(file_path[0][:-4])

#         print(f"({file_name})")

#         self.add_signal_to_combo_graph_2(file_name)
        
#         self.data_2[file_name] = {}
#         self.data_2[file_name]['x_values'] = np.array([x.split(",")[0] for x in lines],dtype=float)
#         self.data_2[file_name]['y_values'] = np.array([y.split(",")[1].strip("/\n") for y in lines],dtype=float)
#         self.data_line_2[file_name] = self.graph2.plot()    
       
#         self.timer_2 = QtCore.QTimer()
#         self.timer_2.setInterval(50)
#         self.timer_2.timeout.connect(self.update_plot_data_2)
#         self.timer_2.start()  

#     def update_plot_data_2(self):
#         for signal in self.data_line_2:
#             x_to_plot = self.data_2[signal]['x_values'][self.index_2 -50 :self.index_2]
#             y_to_plot = self.data_2[signal]['y_values'][self.index_2 -50 :self.index_2]
#             self.data_line_2[signal].setData(x_to_plot, y_to_plot)
#         self.index_2 += 1
     
#     def zoom_in_graph_1(self):
#         self.graph1.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
    
#     def zoom_out_graph_1(self):
#         self.graph1.getViewBox().scaleBy((1.2, 1.2))

#     def zoom_in_graph_2(self):
#         self.graph2.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
    
#     def zoom_out_graph_2(self):
#         self.graph2.getViewBox().scaleBy((1.2, 1.2))

#     def choose_signal_color_grph_1(self ):
#         self.pen= colorchooser.askcolor()[1]
        
    
#     def faster(self):
#         self.timer_1.setInterval(self.timer_1.interval() // 2)
#         self.timer_2.setInterval(self.timer_2.interval() // 2)

#         pass
    
#     def slower(self):
#         self.timer_1.setInterval(self.timer_1.interval() * 2)
#         self.timer_2.setInterval(self.timer_2.interval() * 2)

#         pass
    
#     def move_up(self):
#         pass
    
#     def move_down(self):
#         pass
    
#     def add_signal_to_combo_graph_1(self , file_name):
#         self.ui.comb_sig_colr_grpbox_viewer_1.addItem(file_name)
#         self.ui.comb_rename_viewer_1.addItem(file_name)
#         self.ui.comb_sig_disp_viewer_1.addItem(file_name)
    
#     def add_signal_to_combo_graph_2(self , file_name):
#         self.ui.comb_sig_colr_grpbox_viewer_2.addItem(file_name)
#         self.ui.comb_rename_viewer_2.addItem(file_name)
#         self.ui.comb_sig_disp_viewer_2.addItem(file_name)
        
#     def link_graphs(self):
#         pass
    
#     def make_report(self):
#         pass
    
#     def chng_clor_grph_1(self):
#         signal_txt = self.ui.comb_sig_colr_grpbox_viewer_1.currentText()
#         for signal in self.graph_1_signals:
#             if signal["name"] == signal_txt:
#                 signal["color"] =  self.pen= colorchooser.askcolor()[1]
#                 print(signal["color"])
#                 self.update_plot_data_2()
'''
       
       
       
        
        
        
    
 



def main():
    app = QApplication(sys.argv)
    window = MyWindow() 
    # window.setWindowIcon(QIcon("C:/Users/Sara/Desktop/DSP_tasks/task1_DSP_sara/imgs/app_icon.png"))
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
