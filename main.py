import os
import re
import time#IMPORTS
import csv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QFileDialog, QTableWidgetItem , QComboBox
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
import pyqtgraph as pg
import pandas as pd

class MyWindow(QMainWindow):  
    def __init__(self ):
        super(MyWindow , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        
        self.data_1 = {}
        self.data_line_1 = {}

        self.data_2 = {}
        self.data_line_2 = {}
        
        self.graph_1_signals = []

        self.ui.act_add_sig_viewer_1.triggered.connect(self.open_file_1)
        self.ui.act_add_sig_viewer_2.triggered.connect(self.open_file_2)
        
        self.selectid_file = None

        self.index_1 = 50
        self.index_2 = 50

        self.pen = pg.mkPen(color=(255, 0, 0))
        
        
        self.signals_grph_1 = []

        self.graph1 = PlotWidget(self.ui.centralwidget)
        self.graph1.setGeometry(30, 50, 770, 300)
        self.graph1.setObjectName("Channel1")
        self.graph1.setYRange(-2,2)

        self.graph2 = PlotWidget(self.ui.centralwidget)
        self.graph2.setGeometry(30, 410, 770, 300)
        self.graph2.setObjectName("Channel2")
        self.graph2.setYRange(-2,2)
        
        self.ui.btn_zoom_in_viewer_1.clicked.connect(self.zoom_in_graph_1)
        self.ui.btn_zoom_out_viewer_1.clicked.connect(self.zoom_out_graph_1)
        
        self.ui.btn_zoom_in_grpbox_viewer_1.clicked.connect(self.zoom_in_graph_1)
        self.ui.btn_zoom_out_grpbox_viewer_1.clicked.connect(self.zoom_out_graph_1)
        
        self.ui.btn_zoom_in_viewer_2.clicked.connect(self.zoom_in_graph_2)
        self.ui.btn_zoom_out_viewer_2.clicked.connect(self.zoom_out_graph_2)
        
        self.ui.btn_zoom_in_grpbox_viewer_2.clicked.connect(self.zoom_in_graph_2)
        self.ui.btn_zoom_out_grpbox_viewer_2.clicked.connect(self.zoom_out_graph_2)
        
        self.ui.btn_add_sig_viewer_1.clicked.connect(self.open_file_1)
        self.ui.btn_add_sig_viewer_2.clicked.connect(self.open_file_2)
        
        self.ui.btn_chng_colr_grpbox_viewer_1.clicked.connect(self.chng_clor_grph_1)
        
    def open_file_1(self):
            # Get file path
        file_path = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

        # Open file and retrieve data
        file = open(file_path[0])
        lines = file.readlines()

        # file_name = file_path[0]
        
        ###################
        file_name = os.path.basename(file_path[0][:-4])

        print(f"({file_name})")

        self.add_signal_to_combo_graph_1(file_name)
        
        
        signal = {
            "color" : "#FFFFFF" ,
            "name" : file_name, 
            "display" : True,
            "speed" : None, 
            "zoom" : None, 
        }
        
        self.graph_1_signals.append(signal)
        
                
        ###################
        self.data_1[file_name] = {}
        self.data_1[file_name]['x_values'] = np.array([x.split(",")[0] for x in lines],dtype=float)
        self.data_1[file_name]['y_values'] = np.array([y.split(",")[1].strip("/\n") for y in lines],dtype=float)
#------------------------------ i wanna return a color from the list ---------------------
        self.data_line_1[file_name] = self.graph1.plot()
        # self.data_line_1[file_name] = self.graph1.plot(pen = self.pen)
       
        self.timer_1 = QtCore.QTimer()
        self.timer_1.setInterval(50)
        self.timer_1.timeout.connect(self.update_plot_data_1)
        self.timer_1.start()  

    def update_plot_data_1(self):
        for signal in self.data_line_1:
            x_to_plot = self.data_1[signal]['x_values'][self.index_1 -50 :self.index_1]
            y_to_plot = self.data_1[signal]['y_values'][self.index_1 -50 :self.index_1]
            self.data_line_1[signal].setData(x_to_plot, y_to_plot)
        self.index_1 += 1

    def open_file_2(self):
        # Get file path
        file_path = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

        # Open file and retrieve data
        file = open(file_path[0])
        lines = file.readlines()

        # file_name = file_path[0]
        file_name = os.path.basename(file_path[0][:-4])

        print(f"({file_name})")

        self.add_signal_to_combo_graph_2(file_name)
        
        self.data_2[file_name] = {}
        self.data_2[file_name]['x_values'] = np.array([x.split(",")[0] for x in lines],dtype=float)
        self.data_2[file_name]['y_values'] = np.array([y.split(",")[1].strip("/\n") for y in lines],dtype=float)
        self.data_line_2[file_name] = self.graph2.plot()    
       
        self.timer_2 = QtCore.QTimer()
        self.timer_2.setInterval(50)
        self.timer_2.timeout.connect(self.update_plot_data_2)
        self.timer_2.start()  

    def update_plot_data_2(self):
        for signal in self.data_line_2:
            x_to_plot = self.data_2[signal]['x_values'][self.index_2 -50 :self.index_2]
            y_to_plot = self.data_2[signal]['y_values'][self.index_2 -50 :self.index_2]
            self.data_line_2[signal].setData(x_to_plot, y_to_plot)
        self.index_2 += 1
     
    def zoom_in_graph_1(self):
        self.graph1.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
    
    def zoom_out_graph_1(self):
        self.graph1.getViewBox().scaleBy((1.2, 1.2))

    def zoom_in_graph_2(self):
        self.graph2.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
    
    def zoom_out_graph_2(self):
        self.graph2.getViewBox().scaleBy((1.2, 1.2))

    def choose_signal_color_grph_1(self ):
        self.pen= colorchooser.askcolor()[1]
        
    def play(self):
        pass
    
    def pause():
        pass
    
    def faster(self):
        self.timer_1.setInterval(self.timer_1.interval() // 2)
        self.timer_2.setInterval(self.timer_2.interval() // 2)

        pass
    
    def slower(self):
        self.timer_1.setInterval(self.timer_1.interval() * 2)
        self.timer_2.setInterval(self.timer_2.interval() * 2)

        pass
    
    def move_up(self):
        pass
    
    def move_down(self):
        pass
    
    def add_signal_to_combo_graph_1(self , file_name):
        self.ui.comb_sig_colr_grpbox_viewer_1.addItem(file_name)
        self.ui.comb_rename_viewer_1.addItem(file_name)
        self.ui.comb_sig_disp_viewer_1.addItem(file_name)
    
    def add_signal_to_combo_graph_2(self , file_name):
        self.ui.comb_sig_colr_grpbox_viewer_2.addItem(file_name)
        self.ui.comb_rename_viewer_2.addItem(file_name)
        self.ui.comb_sig_disp_viewer_2.addItem(file_name)
        
    def link_graphs(self):
        pass
    
    def make_report(self):
        pass
    
    def chng_clor_grph_1(self):
        signal_txt = self.ui.comb_sig_colr_grpbox_viewer_1.currentText()
        for signal in self.graph_1_signals:
            if signal["name"] == signal_txt:
                signal["color"] =  self.pen= colorchooser.askcolor()[1]
                print(signal["color"])
                self.update_plot_data_2()
        
        
        
        
    
 



def main():
    app = QApplication(sys.argv)
    window = MyWindow() 
    # window.setWindowIcon(QIcon("C:/Users/Sara/Desktop/DSP_tasks/task1_DSP_sara/imgs/app_icon.png"))
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
