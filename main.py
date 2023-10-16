from reportlab.platypus import SimpleDocTemplate, Image, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
import tkinter as tk
from PIL import Image as PILImage
from io import BytesIO
from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
# # from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
from reportlab.platypus import Image
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from reportlab.platypus import ListFlowable, ListItem
# from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from tabulate import tabulate
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import re
import time
import csv
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QShortcut, QWidget, QDesktopWidget, QFileDialog
from PyQt5.QtGui import QIcon, QKeySequence, QPixmap, QImage
from PyQt5.QtCore import QEvent, QObject, QTimer, Qt
import numpy as np
from mainwindow import Ui_MainWindow
from tkinter import *
from tkinter import colorchooser
from pyqtgraph import PlotWidget
import pyqtgraph.exporters as exporters
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QFileDialog
from PyQt5.QtCore import QStateMachine, QState, QPropertyAnimation
from PyQt5.QtCore import QDateTime, Qt
import io
from statistics import mean, stdev
import matplotlib.pyplot as plt
import pyqtgraph as pg
import pandas as pd
import pyqtgraph.exporters
from fpdf import FPDF

# class CheckableComboBox(QComboBox):
#     def __init__(self):
#         super().__init__()
#         self._changed = False

#         self.view().pressed.connect(self.handleItemPressed)

#     def setItemChecked(self, index, checked=False):
#         item = self.model().item(index, self.modelColumn()) # QStandardItem object

#         if checked:
#             item.setCheckState(Qt.Checked)
#         else:
#             item.setCheckState(Qt.Unchecked)

#     def handleItemPressed(self, index):
#         item = self.model().itemFromIndex(index)

#         if item.checkState() == Qt.Checked:
#             item.setCheckState(Qt.Unchecked)
#         else:
#             item.setCheckState(Qt.Checked)
#         self._changed = True


#     def hidePopup(self):
#         if not self._changed:
#             super().hidePopup()
#         self._changed = False

#     def itemChecked(self, index):
#         item = self.model().item(index, self.modelColumn())
#         return item.checkState() == Qt.Checked


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
        
        
        self.signals_1 =[]
        self.signals_2 =[]

        self.ui.btn_add_sig_viewer_1.clicked.connect(self.upload_data_grph_1)   
        self.ui.btn_play_pasuse_viewer_1.clicked.connect(self.play_pause_grph_1)

        self.ui.btn_zoom_in_viewer_1.clicked.connect(self.zoom_in_grph_1)
        self.ui.btn_zoom_out_viewer_1.clicked.connect(self.zoom_out_grph_1)
       
        self.ui.btn_fast_viewer_1.clicked.connect(self.faster_grph_1)
        self.ui.btn_slow_viewer_1.clicked.connect(self.slower_grph_1)
        
        # self.ui.actionreport.triggered.connect(self.generate_report)
        
        self.ui.btn_clear_viewer_1.clicked.connect(self.clear_grph_1)
        
        
        self.ui.btn_chng_colr_grpbox_viewer_1.clicked.connect(self.change_sig_color_grph_1)
        self.ui.btn_move_viewer_1.clicked.connect(self.move_signal_from_grph_1)
        
        self.ui.act_add_sig_viewer_1.triggered.connect(self.upload_data_grph_1)
        

        self.ui.act_add_sig_viewer_2.triggered.connect(self.upload_data_grph_2)
        self.ui.btn_add_sig_viewer_2.clicked.connect(self.upload_data_grph_2)   
        # self.ui.btn_add_sig_viewer_2.clicked.connect(self.open_file_1)   
        self.ui.btn_play_pasuse_viewer_2.clicked.connect(self.play_pause_grph_2)

        self.ui.btn_zoom_in_viewer_2.clicked.connect(self.zoom_in_grph_2)
        self.ui.btn_zoom_out_viewer_2.clicked.connect(self.zoom_out_grph_2)
       
        self.ui.btn_fast_viewer_2.clicked.connect(self.faster_grph_2)
        self.ui.btn_slow_viewer_2.clicked.connect(self.slower_grph_2)
        
        self.ui.btn_move_viewer_2.clicked.connect(self.move_signal_from_grph_2)
        
        self.ui.btn_clear_viewer_2.clicked.connect(self.clear_grph_2)
        
        self.ui.btn_chng_colr_grpbox_viewer_2.clicked.connect(self.change_sig_color_grph_2)
        self.ui.chk_bx_sig_show_1.stateChanged.connect(self.show_hide_grph_1)
        self.ui.chk_bx_sig_show_2.stateChanged.connect(self.show_hide_grph_2)
        self.ui.chk_bx_sig_show_1.setChecked(True)
        self.ui.chk_bx_sig_show_2.setChecked(True)
        
        self.ui.btn_link_graphs.clicked.connect(self.link_graphs)
        
        self.ui.btn_srt_begin__viewer_1.clicked.connect(self.replay_1)
        self.ui.btn_srt_begin__viewer_2.clicked.connect(self.replay_2)
        
        
        self.ui.btn_play_pasuse_viewer_1.setToolTip("paly")
        self.ui.btn_play_pasuse_viewer_2.setToolTip("paly")
        
        self.ui.btn_fast_viewer_1.setToolTip("faster")
        self.ui.btn_slow_viewer_1.setToolTip("slower")

        self.ui.btn_slow_viewer_2.setToolTip("slower")
        self.ui.btn_slow_viewer_2.setToolTip("slower")
        
        self.ui.btn_srt_begin__viewer_1.setToolTip("replay")
        self.ui.btn_srt_begin__viewer_2.setToolTip("replay")
        
        self.ui.btn_zoom_in_viewer_1.setToolTip("zoom in")
        self.ui.btn_zoom_out_viewer_1.setToolTip("zoom out")
        
        self.ui.btn_zoom_in_viewer_2.setToolTip("zoom in")
        self.ui.btn_zoom_out_viewer_2.setToolTip("zoom out")
        
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
        
        
        self.islinked = False

        # shortcuts
        QShortcut(QKeySequence("Ctrl+p"), self).activated.connect(self.generate_report)
        QShortcut(QKeySequence("Ctrl+l"), self).activated.connect(self.link_graphs)
        QShortcut(QKeySequence("Ctrl+c"), self).activated.connect(self.clear_all)

        QShortcut(QKeySequence("Ctrl + +"), self).activated.connect(self.zoom_in_all)
        QShortcut(QKeySequence("Ctrl + -"), self).activated.connect(self.zoom_out_all)

        QShortcut(QKeySequence("Ctrl + ["), self).activated.connect(self.slow_all_graphs)
        QShortcut(QKeySequence("Ctrl + ]"), self).activated.connect(self.fast_all_graphs)

        self.ui.actionreport.triggered.connect(self.repo)
        # self.ui.actionreport.triggered.connect(self.create_pdf)
        # self.ui.actionreport.triggered.connect(self.capture_snapshot)
        # self.ui.actionreport.triggered.connect(self.captureGraphImage)

    def fast_all_graphs(self):
        self.faster_grph_1()
        self.faster_grph_2()

    def slow_all_graphs(self):
        self.slower_grph_1()
        self.slower_grph_2()
        
    def zoom_in_all(self):
        self.zoom_in_grph_1()
        self.zoom_in_grph_2()
        
    def zoom_out_all(self):
        self.zoom_out_grph_1()
        self.zoom_out_grph_2()
        
    def clear_all(self):
        self.clear_grph_2()
        self.clear_grph_1()

    def clear_grph_1(self):
        self.graph1.clear()
        self.timer_1.stop()
        icon = QtGui.QPixmap("play.png")
        self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
        self.signals_1.clear()
        self.updata_combo_bxs_grph_1()
        
        if self.islinked:
            self.clear_grph_2()
        
        # self.ui.comb_sig_apperance_viewer_1.clear()
        # self.ui.comb_sig_apperance_viewer_1.addItem("choose signal")
           
    def upload_data_grph_1(self):
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

        

        data = np.genfromtxt(file_path, delimiter = ',')
        x = data[:, 0].tolist()
        y = data[:, 1].tolist()
        file_name = os.path.basename(file_path[:-4])
        # print(f"({file_name})")

        
        signal = {
            "color" : "#ffffff" ,
            "name" : file_name, 
            "display" : True,
            "data" : data,
            "x" : x,
            "y" : y,
            "data_lines":[],
            "data_indices":[], 
            "idx" : None
        }
        
        # print(signal["x"])
        self.signals_1.append(signal)
        
        self.updata_combo_bxs_grph_1()

        # self.plot_signal_grph_1(signal)
        print(signal["color"])
        self.replay_1()
         
    def plot_signal_grph_1(self ) :
    
        for signal in self.signals_1:
            data_line = self.graph1.plotItem.plot(signal["x"], signal["y"], pen=signal["color"])
            # print(f'here{signal["color"]}')
            signal["data_lines"].append(data_line)
            signal["data_indices"].append(0)
            signal["idx"]=0
        self.graph1.plotItem.getViewBox().setAutoPan(x=True,y=True)
        # self.timer_1.setInterval()
        self.timer_1.timeout.connect(lambda:self.update_plot_data_grph_1(self.signals_1))
        self.timer_1.start()
        self.graph1.show()
        # self.graph1.setYRange(min(signal["y"]) , max(signal["y"]))
        self.graph1.setXRange(0 , 0.002*len(signal["data"]))

        icon = QtGui.QPixmap("pause.png")
        self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
       
    def update_plot_data_grph_1(self,signals):
        for signal in signals:
            for i in range(len(signal["data_lines"])):
                x = signal["x"][:signal["data_indices"][i]]
                y = signal["y"][:signal["data_indices"][i]]
                signal["data_indices"][i] += 10  # Update the index for this signal
                
                # if signal["data_indices"][0] > len(signal["x"]):
                    # signal["data_indices"][i] = 0  # Reset the index for this signal
                # if signal["x"][signal["data_indices"][i]] > 0.5:
                #     self.graph1.setLimits(xMin=min(x, default=0), xMax=max(x, default=0))  # Disable panning over x-limits
                
                self.graph1.setXRange(max(x, default=0) - 0.5, max(x, default=0))
                self.graph1.setYRange(min(signal["y"]), max(signal["y"]))

                signal["data_lines"][i].setData(x, y)
                
        # for i in range(len(signal["data_lines"])):
        #     x = signal["x"][:signal["data_indices"][i]]
        #     y = signal["y"][:signal["data_indices"][i]]
        #     signal["data_indices"][i] += 10  # Update the index for this signal
            
        #     if signal["data_indices"][i] > len(signal["x"]):
        #         signal["data_indices"][i] = 0  # Reset the index for this signal
        #     if signal["x"][signal["data_indices"][i]] > 0.5:
        #         self.graph1.setLimits(xMin=min(x, default=0), xMax=max(x, default=0))  # Disable panning over x-limits
            
        #     self.graph1.setXRange(max(x, default=0) - 0.5, max(x, default=0))
        #     self.graph1.setYRange(min(signal["y"]) , max(signal["y"]))

        #     signal["data_lines"][i].setData(x, y)

    def play_pause_grph_1(self):
        if self.timer_1.isActive():
            self.timer_1.stop()
            icon = QtGui.QPixmap("play.png")
            self.ui.btn_play_pasuse_viewer_1.setToolTip("paly")
            self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
        else:
            self.timer_1.start()
            icon = QtGui.QPixmap("pause.png")
            self.ui.btn_play_pasuse_viewer_1.setToolTip("pause")
            self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
        
        if self.islinked:
            self.play_pause_grph_2()

    def add_signal_to_combo_grph_1(self , file_name):
        self.ui.comb_sig_apperance_viewer_1.addItem(file_name)
        self.ui.comb_move_viewer_1.addItem(file_name)
               
    def zoom_out_grph_1(self):
        # Increase the visible range 
        self.graph1.getViewBox().scaleBy((1.2, 1.2))
        if self.islinked:
            self.zoom_out_grph_2()
       
    def zoom_in_grph_1(self):
         # Decrease the visible range 
        self.graph1.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
        if self.islinked:
            self.zoom_in_grph_2()            
            
    def faster_grph_1(self):
        # Decrease the timer interval to make updates faster
        self.timer_1.setInterval(self.timer_1.interval() // 2)
        
        if self.islinked :
            self.faster_grph_2()
    
    def slower_grph_1(self):
         # Increase the timer interval to make updates slower
        self.timer_1.setInterval(self.timer_1.interval() * 2)
        #  self.timer_2.setInterval(self.timer_2.interval() * 2)
        if self.islinked :
            self.slower_grph_2()

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
                    self.plot_signal_grph_2()
                    
    def updata_combo_bxs_grph_1(self):
        
        self.ui.comb_sig_apperance_viewer_1.clear()
        self.ui.comb_move_viewer_1.clear()

        self.ui.comb_sig_apperance_viewer_1.addItem("choose signal")
        self.ui.comb_move_viewer_1.addItem("choose signal")

        for signal in self.signals_1:
            self.ui.comb_sig_apperance_viewer_1.addItem(signal["name"])
            self.ui.comb_move_viewer_1.addItem(signal["name"])
                    
    def change_sig_color_grph_1(self):
        if self.ui.comb_sig_apperance_viewer_1.currentText() != "chose signal":
            signal_to_be_changed = self.ui.comb_sig_apperance_viewer_1.currentText()
            for signal in self.signals_1 :
                if signal["name"] == signal_to_be_changed:
                    signal["color"] = colorchooser.askcolor()[1]
            
                    for data_line in signal["data_lines"]:
                        data_line.setPen(signal["color"])   
           
    def show_hide_grph_1 (self):
        signal_to_show_hide = self.ui.comb_sig_apperance_viewer_1.currentText()
        for signal in self.signals_1 :
            if signal["name"] == signal_to_show_hide:
                if (self.ui.chk_bx_sig_show_1.isChecked()):
                    
                    for data_line in signal["data_lines"]:
                        data_line.setVisible(True) 
                            # signal["data_lines"].setVisiable()       
                            # self.current_signal_v1.data_line.setVisible(True)
                else:
                    for data_line in signal["data_lines"]:    # self.current_signal_v1.data_line.setVisible(False)
                        data_line.setVisible(False)
    
    def find_max_min_1(self):
        max_number = float('-inf')  # Start with negative infinity
        min_number = float('-inf')  # Start with negative infinity

# Iterate through the list of dictionaries
        for signal in self.signals_1:
            y_list = signal.get("y", [])  # Get the "x" list from the dictionary

            # Find the maximum number in the current "x" list
            if y_list:
                current_max = max(y_list)
                current_min = min(y_list)
                
                # Update the maximum number if the current maximum is greater
                if current_max > max_number:
                    max_number = current_max
                    
                if current_min < min_number:
                    min_number = current_min
                    
        return max_number , min_number                    
        # The variable max_number now contains the maximum number from all "x" lists
        # print("Maximum number:", max_number)

    def replay_1(self):
        self.graph1.clear()
        self.plot_signal_grph_1()
        if self.islinked:
            self.replay_2()

    def clear_grph_2(self):
        self.graph2.clear()
        self.timer_2.stop()
        icon = QtGui.QPixmap("play.png")
        self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))
        self.signals_2.clear()
        self.updata_combo_bxs_grph_2()




    def upload_data_grph_2(self):
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

        

        data = np.genfromtxt(file_path, delimiter = ',')
        x = data[:, 0].tolist()
        y = data[:, 1].tolist()
        file_name = os.path.basename(file_path[:-4])
        # print(f"({file_name})")

        
        signal = {
            "color" : "#ffffff" ,
            "name" : file_name, 
            "display" : True,
            "data" : data,
            "x" : x,
            "y" : y,
            "data_lines":[],
            "data_indices":[], 
            "idx" : None
        }
        
        # print(signal["x"])
        self.signals_2.append(signal)
        
        self.updata_combo_bxs_grph_2()

        # self.plot_signal_grph_2(signal)
        print(signal["color"])
        self.replay_2()
        
    def  plot_signal_grph_2(self ) :
    
        for signal in self.signals_2:
            data_line = self.graph2.plotItem.plot(signal["x"], signal["y"], pen=signal["color"])
            # print(f'here{signal["color"]}')
            signal["data_lines"].append(data_line)
            signal["data_indices"].append(0)
            signal["idx"]=0
             
            # self.graph2.setXRange(0 , 0.002*len(signal["data"]))
            #that was not here it was outside loop same for grph1
        self.graph2.plotItem.getViewBox().setAutoPan(x=True,y=True)
        # self.timer_2.setInterval()
        self.timer_2.timeout.connect(lambda:self.update_plot_data_grph_2(self.signals_2))
        self.timer_2.start()
        self.graph2.show()
        self.graph2.setYRange(min(signal["y"]) , max(signal["y"]))

        self.graph2.setXRange(0 , 0.002*len(signal["data"]))
        icon = QtGui.QPixmap("pause.png")
        self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))
       
    def update_plot_data_grph_2(self,signals):
        for signal in signals:
            for i in range(len(signal["data_lines"])):
                x = signal["x"][:signal["data_indices"][i]]
                y = signal["y"][:signal["data_indices"][i]]
                signal["data_indices"][i] += 10  # Update the index for this signal
                
                # if signal["data_indices"][i] > len(signal["x"]):
                #     signal["data_indices"][i] = 0  # Reset the index for this signal
                # if signal["x"][signal["data_indices"][i]] > 0.5:
                #     self.graph2.setLimits(xMin=min(x, default=0), xMax=max(x, default=0))  # Disable panning over x-limits
                
                self.graph2.setXRange(max(x, default=0) - 0.5, max(x, default=0))
                self.graph2.setYRange(min(signal["y"]), max(signal["y"]))

                signal["data_lines"][i].setData(x, y)
         
         
         
         
         
    # def update_plot_data_grph_2(self,signal):
                
    #     for i in range(len(signal["data_lines"])):
    #         x = signal["x"][:signal["data_indices"][i]]
    #         y = signal["y"][:signal["data_indices"][i]]
    #         signal["data_indices"][i] += 10  # Update the index for this signal
    #         if signal["data_indices"][i] > len(signal["x"]):
    #             signal["data_indices"][i] = 0  # Reset the index for this signal
    #         if signal["x"][signal["data_indices"][i]] > 0.5:
    #             self.graph2.setLimits(xMin=min(x, default=0), xMax=max(x, default=0))  # Disable panning over x-limits
            
    #         self.graph2.setXRange(max(x, default=0) - 0.5, max(x, default=0))
    #         self.graph2.setYRange(min(signal["y"]) , max(signal["y"]))
    #         signal["data_lines"][i].setData(x, y)


    def play_pause_grph_2(self):
        if self.timer_2.isActive():
            self.timer_2.stop()
            icon = QtGui.QPixmap("play.png")
            self.ui.btn_play_pasuse_viewer_2.setToolTip("paly")
            self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))
        else:
            self.timer_2.start()
            icon = QtGui.QPixmap("pause.png")
            self.ui.btn_play_pasuse_viewer_2.setToolTip("pause")
            self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))

    def add_signal_to_combo_grph_2(self , file_name):
        self.ui.comb_sig_apperance_viewer_2.addItem(file_name)
        self.ui.comb_move_viewer_2.addItem(file_name)
               
    def zoom_out_grph_2(self):
          # Increase the visible range 
        self.graph2.getViewBox().scaleBy((1.2, 1.2))
        if self.islinked:
            self.graph1.getViewBox().scaleBy((1.2, 1.2))
            
        #  self.graph2.getViewBox().scaleBy((1.2, 1.2))

    def zoom_in_grph_2(self):
         # Decrease the visible range 
        self.graph2.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
        if self.islinked:
            self.graph1.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
            
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
                        self.graph2.removeItem(data_line)
                        self.graph1.addItem(data_line)
                    
                    self.signals_1.append(signal)
                    self.signals_2.remove(signal)
                    self.updata_combo_bxs_grph_1()
                    self.updata_combo_bxs_grph_2()

    def updata_combo_bxs_grph_2(self):
        
        self.ui.comb_sig_apperance_viewer_2.clear()
        self.ui.comb_move_viewer_2.clear()

        self.ui.comb_sig_apperance_viewer_2.addItem("choose signal")
        self.ui.comb_move_viewer_2.addItem("choose signal")

        for signal in self.signals_2:
            self.ui.comb_sig_apperance_viewer_2.addItem(signal["name"])
            self.ui.comb_move_viewer_2.addItem(signal["name"])
    
    def change_sig_color_grph_2(self):
        if self.ui.comb_sig_apperance_viewer_2.currentText() != "chose signal":
            signal_to_be_changed = self.ui.comb_sig_apperance_viewer_2.currentText()
            for signal in self.signals_2 :
                if signal["name"] == signal_to_be_changed:
                    signal["color"] = colorchooser.askcolor()[1]
            
                    for data_line in signal["data_lines"]:
                        data_line.setPen(signal["color"])   
            
            # # signal["color"] = colorchooser.askcolor()[1]
            # print(signal_to_be_changed)
            # print(signal["color"])
    
    def show_hide_grph_2 (self):
        signal_to_show_hide = self.ui.comb_sig_apperance_viewer_2.currentText()
        for signal in self.signals_2 :
            if signal["name"] == signal_to_show_hide:
                if (self.ui.chk_bx_sig_show_2.isChecked()):
                                        
                    for data_line in signal["data_lines"]:
                        data_line.setVisible(True) 
                            # signal["data_lines"].setVisiable()       
                            # self.current_signal_v1.data_line.setVisible(True)
                else:
                    for data_line in signal["data_lines"]:    # self.current_signal_v1.data_line.setVisible(False)
                        data_line.setVisible(False)        
        
        
        
        

    def replay_2(self):
        self.graph2.clear()
        self.plot_signal_grph_2()
        
        
    def link_graphs(self):
        if  self.islinked == False:
            self.islinked = True
            self.ui.btn_link_graphs.setText("disable link graphs")
            self.ui.btn_srt_begin__viewer_2.setEnabled(False)
            self.ui.btn_slow_viewer_2.setEnabled(False)
            self.ui.btn_zoom_out_viewer_2.setEnabled(False)
            self.ui.btn_play_pasuse_viewer_2.setEnabled(False)
            self.ui.btn_play_pasuse_viewer_2.setEnabled(False)
            self.ui.btn_fast_viewer_2.setEnabled(False)
            self.ui.btn_zoom_in_viewer_2.setEnabled(False)
            self.timer_1.setInterval(100)
            self.timer_2.setInterval(100)
            print(self.timer_1.interval())
            print(self.timer_2.interval())
            
            self.replay_1()
            self.replay_2()
            
            # self.timer_1.setInterval(100) 
            # self.timer_2.setInterval(100) 
        else:
            self.ui.btn_link_graphs.setText("link graphs")
            self.ui.btn_srt_begin__viewer_2.setEnabled(True)
            self.ui.btn_slow_viewer_2.setEnabled(True)
            self.ui.btn_zoom_out_viewer_2.setEnabled(True)
            self.ui.btn_play_pasuse_viewer_2.setEnabled(True)
            self.ui.btn_play_pasuse_viewer_2.setEnabled(True)
            self.ui.btn_fast_viewer_2.setEnabled(True)
            self.ui.btn_zoom_in_viewer_2.setEnabled(True)
            self.islinked = False
    
    def captureGraphImage(self, ):
        # img_1 = self.graph1.
        data_items1 = self.graph1.getPlotItem().listDataItems()
       
        data_items2 = self.graph2.getPlotItem().listDataItems()
    
        if len(data_items1)> 0 :
            exporter = exporters.ImageExporter(self.graph1.scene())
        
            # Set the file suffix to specify the export type
            exporter.params.fileSuffix = 'png'

            # Set the filename
            export_filename = 'img1.png'

            # Export the graph to the specified filename
            exporter.export(export_filename)
        if len(data_items2)> 0 :
            exporter = exporters.ImageExporter(self.graph2.scene())
        
            # Set the file suffix to specify the export type
            exporter.params.fileSuffix = 'png'

            # Set the filename
            export_filename = 'img2.png'

            # Export the graph to the specified filename
            exporter.export(export_filename)

    def generate_report(self):
        # Prompt the user to choose a file path for saving the PDF
        pdf_file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF Report", "", "PDF Files (*.pdf)")
        stat1= self.cal_statistics(self.graph1)
        stat2= self.cal_statistics(self.graph2)
        table1 = tabulate(stat1, headers='Graph1 statistics', tablefmt='pretty')
        table2 = tabulate(stat2, headers='Graph2 statistics', tablefmt='pretty')
        if pdf_file_path:
            self.captureGraphImage()
            c = canvas.Canvas(pdf_file_path, pagesize=letter)  # Use the selected PDF file path

            # Add a header with the same file name as the PDF
            file_name = pdf_file_path.split("/")[-1].replace(".pdf", " ")
            # Set font and size for the title
            c.setFont("Helvetica-Bold", 24)
        
            # Get the text width of the title
            title_width = c.stringWidth(file_name, "Helvetica-Bold", 24)
        
            # Calculate the x-coordinate to center the title
            x_centered = (letter[0] - title_width) / 2
        
            # Draw the centered and larger title
            c.drawString(x_centered, 750, file_name)

            # Display the images in smaller sizes
            imag = ImageReader('img1.png')
            imag2 = ImageReader('img2.png')
            image_width = 500  # Set the width for the images
            image_height = 180  # Set the height for the images
            c.drawImage(imag, 50, 550, width=image_width, height=image_height)
            c.drawImage(imag2, 50, 350, width=image_width, height=image_height)

            c.save()
      
    def cal_statistics(self,graph):
        data_item = graph.getPlotItem().listDataItems()[0]  
        x_values, y_values = data_item.getData()

        mean_value = mean(y_values)
        std_deviation = stdev(y_values)
        duration = len(y_values)
        min_value = min(y_values)
        max_value = max(y_values)

        statistics = {
            'mean': mean_value,
            'std': std_deviation,
            'duration': duration,
            'min': min_value,
            'max': max_value
        }

        return statistics
        
    def gen_listpdf(self):
        pdf_file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF Report", "", "PDF Files (*.pdf)")
        doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
        elements=[]
        # Generate statistics tables
        stat1 = self.cal_statistics(self.graph1)
        stat2 = self.cal_statistics(self.graph2)
        # Define headers for the tables
        headers = ["Statistic", "Value"]

        # Convert the dictionaries into a list of (key, value) pairs
        data1 = list(stat1.items())
        data2 = list(stat2.items())

        # Use tabulate to format the tables
        table1 = tabulate(data1, headers, tablefmt='grid')
        table2 = tabulate(data2, headers, tablefmt='grid')

        # Create a Table for table1
        table1 = Table([table1.split('\n')], colWidths=[100, 200], style=[
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])
        elements.append(table1)

        # Create a Table for table2
        table2 = Table([table2.split('\n')], colWidths=[100, 200], style=[
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])
        elements.append(table2)
        # Build the PDF document
        doc.build(elements)

    def capture_snapshot(self):
        exporter = pg.exporters.ImageExporter(self.graph1.plotItem)
        exporter.parameters()['width'] = 100   # (note this also affects height parameter)

# save to file
        exporter.export('fileName.png')
        
        exporter = pg.exporters.ImageExporter(self.graph2.plotItem)
        exporter.parameters()['width'] = 100   # (note this also affects height parameter)

# save to file
        exporter.export('fileName2.png')
        # self.create_pdf()
        # Capture the snapshot from graph1
        # graph_view_1 = self.graph1.getViewBox()
        # size = graph_view_1.size().toSize()  # Convert QSizeF to QSize
        # pixmap = QPixmap(size)
        # graph_view_1.render(pixmap)

        # # Convert QPixmap to QImage
        # image = pixmap.toImage()

        # # Save the image to a file
        # image.save("img1.png")

    def create_title(day, pdf):
      # Unicode is not yet supported in the py3k version; use windows-1252 standard font
        pdf.set_font('Arial', '', 24)  
        pdf.ln(60)
        pdf.write(5, f"Covid Analytics Report")
        pdf.ln(10)
        pdf.set_font('Arial', '', 16)
        pdf.write(4, f'{day}')
        pdf.ln(5)

    def repo(self):
        pdf = FPDF() # A4 (210 by 297 mm)
        WIDTH = 210
        HEIGHT = 297

        # states = ['Massachusetts', 'New Hampshire']

        ''' First Page '''
        pdf.add_page()
        # pdf.image("fileName.png", 0, 0, WIDTH)
        # create_title(day, pdf)

        # plot_usa_case_map("./tmp/usa_cases.png", day=day)
        # prev_days = 250
        # plot_states(states, days=prev_days, filename="./tmp/cases.png", end_date=day)
        # plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths.png", end_date=day)

        pdf.image("fileName.png", 5, 10, 190)
        pdf.image("fileName2.png", 5, 140, 195) 
        
        pdf.output( "tut.pdf", "F")
        
        
        
        
        
    def create_pdf(self ):
        # Open a file dialog to select where to save the PDF
        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")

        if file_path:
            # Create a root window for PIL
            tk.Tk().withdraw()

            doc = SimpleDocTemplate(file_path, pagesize=letter)

            image_paths = ['fileName.png', 'fileName2.png']  # Replace with your image paths

            story = []

            for image_path in image_paths:
                with open(image_path, 'rb') as image_file:
                    img_data = image_file.read()
                    img = ImageReader(BytesIO(img_data))
                    c = canvas.Canvas(file_path, pagesize=letter)
                    c.drawImage(img, 100, 100, width=400, height=400)
                    c.showPage()
                    

            doc.build(story)

# Rest of your class definition and code







            
            # doc = SimpleDocTemplate(file_path, pagesize=letter)

            # image_paths = ['image1.png', 'image2.png']  # Replace with your image paths

            # story = []

            # for image_path in image_paths:
            #     im = Image(image_path, width=3.5 * inch, height=3.5 * inch)  # Adjust the size as needed
            #     table_data = [['Table Cell 1', 'Table Cell 2'], ['Table Cell 3', 'Table Cell 4']]  # Replace with your table data

            #     data = []
            #     data.append([im, Table(table_data)])
            #     tbl_style = TableStyle([
            #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            #         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
            #     ])
            #     data[0][1].setStyle(tbl_style)

            #     story.append(data)
            #     story.append(PageBreak())

            # doc.build(story)

    
    
    
    
    
    
    def generate_pdf(file_path, statistics, graphs, custom_dict):
        doc = SimpleDocTemplate(file_path, pagesize=letter)
        story = []

        # Title
        title_style = getSampleStyleSheet()['Title']
        title = Paragraph("Your PDF Title", title_style)
        story.append(title)

        # Statistics
        stats_style = getSampleStyleSheet()['Normal']
        stats = Paragraph(statistics, stats_style)
        story.append(stats)

        # Dictionary
        dict_style = getSampleStyleSheet()['Normal']
        dict_list = ListFlowable(
            [ListItem(Paragraph(f"{key}: {value}", dict_style)) for key, value in custom_dict.items()],
            bulletType='bullet',
            bulletFontSize=10,
            bulletIndent=10,
        )
        story.append(dict_list)

        # Images from graphs
        pdf_pages = PdfPages(file_path)
        for graph in graphs:
            fig = plt.figure()
            plt.imshow(graph)
            pdf_pages.savefig(fig)
        pdf_pages.close()

        # Add images to the PDF
        for i in range(len(graphs)):
            image = Image(file_path, width=6 * inch, height=4 * inch)
            story.append(image)

        doc.build(story)

        return file_path

def main():
    app = QApplication(sys.argv)
    window = MyWindow() 
    window.setWindowIcon(QIcon("C:/Users/Sara/Desktop/DSP_tasks/sara_multi_channel_signal_viewer/imgs/app_icon.png"))
    window.setWindowTitle("signal viewer")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
