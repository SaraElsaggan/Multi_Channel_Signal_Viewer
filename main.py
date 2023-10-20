from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from tabulate import tabulate
from PyQt5 import QtCore, QtGui
import os
import sys
from PyQt5.QtWidgets import QInputDialog ,  QMessageBox ,  QApplication, QMainWindow, QShortcut, QFileDialog
from PyQt5.QtGui import QIcon, QKeySequence
import numpy as np
from mainwindow import Ui_MainWindow
from tkinter import *
from tkinter import colorchooser
import pyqtgraph.exporters as exporters
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QFileDialog
from statistics import mean, stdev
import matplotlib.pyplot as plt
import pyqtgraph as pg
from fpdf import FPDF



class MyWindow(QMainWindow):  
    
    def __init__(self ):
        super(MyWindow , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        self.ui.btn_rename_sig_1.clicked.connect(self.rename_grph_1)        
        self.ui.btn_rename_sig_2.clicked.connect(self.rename_grph_2)        
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
        
        
        self.ui.btn_clear_viewer_1.clicked.connect(self.clear_grph_1)
        
        
        self.ui.btn_chng_colr_grpbox_viewer_1.clicked.connect(self.change_sig_color_grph_1)
        self.ui.btn_move_viewer_1.clicked.connect(self.move_signal_from_grph_1)
        
        self.ui.act_add_sig_viewer_1.triggered.connect(self.upload_data_grph_1)
        

        self.ui.act_add_sig_viewer_2.triggered.connect(self.upload_data_grph_2)
        self.ui.btn_add_sig_viewer_2.clicked.connect(self.upload_data_grph_2)   
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
        self.counter_1 = 1
        self.counter_2 = 1

        QShortcut(QKeySequence("Ctrl+p"), self).activated.connect(self.report)
        QShortcut(QKeySequence("Ctrl+l"), self).activated.connect(self.link_graphs)
        QShortcut(QKeySequence("Ctrl+c"), self).activated.connect(self.clear_all)

        QShortcut(QKeySequence("Ctrl++"), self).activated.connect(self.zoom_in_all)
        QShortcut(QKeySequence("Ctrl+-"), self).activated.connect(self.zoom_out_all)

        QShortcut(QKeySequence("Ctrl+["), self).activated.connect(self.slow_all_graphs)
        QShortcut(QKeySequence("Ctrl+]"), self).activated.connect(self.fast_all_graphs)

        self.ui.btn_snap_grph_1.clicked.connect(self.capture_snapshot_1)
        self.ui.btn_snap_grph_2.clicked.connect(self.capture_snapshot_2)
        self.ui.btn_repo.clicked.connect(self.report)
        # self.ui.btn_report_grph_2.clicked.connect(self.report_grph_2)
        self.ui.actionreport.triggered.connect(self.report)
        
        self.snapshots_1 = []
        self.snapshots_2 = []

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
        self.ui.graphicsView.clear()
        self.timer_1.stop()
        icon = QtGui.QPixmap("play.png")
        self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
        self.signals_1.clear()
        self.updata_combo_bxs_grph_1()
        
        if self.islinked:
            self.clear_grph_2()
        
           
    def upload_data_grph_1(self):
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

        

        data = np.genfromtxt(file_path, delimiter = ',')
        x = data[:, 0].tolist()
        y = data[:, 1].tolist()
        file_name = os.path.basename(file_path[:-4])

        
        signal = {
            "color" : "#ffffff" ,
            "name" : file_name, 
            "display" : True,
            "data" : data,
            "x" : x,
            "y" : y,
            "data_lines":[],
            "data_indices":[], 
        }
        
        self.signals_1.append(signal)
        
        self.updata_combo_bxs_grph_1()

        print(signal["color"])
        self.replay_1()
         
    def plot_signal_grph_1(self ) :
        p = 0
        for signal in self.signals_1:
            data_line = self.ui.graphicsView.plotItem.plot( pen=signal["color"])
            signal["data_lines"].append(data_line)
            signal["data_indices"].append(0)
        p += 20
        self.legend_1 = pg.LegendItem((10, 10), offset=(40 ,  p ))
        self.legend_1.setParentItem(self.ui.graphicsView.getPlotItem())
        self.legend_1.addItem(data_line, signal["name"])
        self.ui.graphicsView.plotItem.getViewBox().setAutoPan(x=True,y=True)
        self.timer_1.timeout.connect(lambda:self.update_plot_data_grph_1(self.signals_1))
        self.timer_1.start()
        max_y , min_y = self.find_max_min_y_grph_1()
        self.ui.graphicsView.plotItem.vb.setLimits(xMin=0, xMax=max(signal["x"]), yMin=min_y-.5, yMax=max_y+.5)
        self.ui.graphicsView.setXRange(0 , 0.002*len(signal["data"]))

        
        icon = QtGui.QPixmap("pause.png")
        self.ui.btn_play_pasuse_viewer_1.setIcon(QtGui.QIcon(icon))
        
        self.ui.graphicsView.show()
        
    def find_max_min_y_grph_1(self):
        max_y = float('-inf')  
        min_y = float('inf')   

        for signal in self.signals_1 :
            if "y" in signal and signal["y"]:
                max_y = max(max_y, max(signal["y"]))
                min_y = min(min_y, min(signal["y"]))

        return max_y, min_y
    
    
    def update_plot_data_grph_1(self,signals):
        for signal in signals:
            for i in range(len(signal["data_lines"])):
                x = signal["x"][:signal["data_indices"][i]]
                y = signal["y"][:signal["data_indices"][i]]
                signal["data_indices"][i] += 5 # Update the index for this signal
                signal["data_lines"][i].setData(x, y)
                
    def find_max_min_1(self):

        max_number = float('-inf')  # Start with negative infinity
        min_number = float('-inf')  # Start with negative infinity

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
      

    def rename_grph_1(self):
        old_name = self.ui.combo_rename_grph_1.currentText()
        new_name, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your text:')
        
        if ok:
            for signal in self.signals_1:
                if signal["name"] == old_name:
                    signal["name"] = new_name
            self.updata_combo_bxs_grph_1()            
        else:
            pass

    def rename_grph_2(self):
        old_name = self.ui.combo_rename_grph_2.currentText()
        new_name, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your text:')
        
        if ok:
            for signal in self.signals_2:
                if signal["name"] == old_name:
                    signal["name"] = new_name
            self.updata_combo_bxs_grph_2()            
        else:
            pass
        
                
            


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
       
        self.ui.graphicsView.getViewBox().scaleBy((1.2, 1.2))
        set 
        if self.islinked:
            self.zoom_out_grph_2()
       
    def zoom_in_grph_1(self):
         # Decrease the visible range 
        self.ui.graphicsView.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
        if self.islinked:
            self.zoom_in_grph_2()            
            
    def faster_grph_1(self):
        self.timer_1.setInterval(self.timer_1.interval() // 2)
        
        if self.islinked :
            self.faster_grph_2()
    
    def slower_grph_1(self):
        self.timer_1.setInterval(self.timer_1.interval() * 2)
        if self.islinked :
            self.slower_grph_2()

    
    def move_signal_from_grph_1(self):
            signal_to_move = self.ui.comb_move_viewer_1.currentText()
            for signal in self.signals_1:
                if signal["name"] == signal_to_move:
                    for data_line in signal["data_lines"]:
                        self.ui.graphicsView.removeItem(data_line)
                        self.ui.graphicsView_2.addItem(data_line)
                    
                    self.signals_2.append(signal)
                    self.signals_1.remove(signal)
                    self.updata_combo_bxs_grph_1()
                    self.updata_combo_bxs_grph_2()
                    self.plot_signal_grph_2()
                    
    def updata_combo_bxs_grph_1(self):
        
        self.ui.comb_sig_apperance_viewer_1.clear()
        self.ui.comb_move_viewer_1.clear()
        self.ui.combo_rename_grph_1.clear()
        
        reversed_signals = self.signals_1[::-1]

        for signal in reversed_signals:
            self.ui.comb_sig_apperance_viewer_1.addItem( signal["name"])
            self.ui.comb_move_viewer_1.addItem( signal["name"])
            self.ui.combo_rename_grph_1.addItem( signal["name"])
        
    def change_sig_color_grph_1(self):
        color = colorchooser.askcolor()[1]
        if color[1]:
    
            signal_to_be_changed = self.ui.comb_sig_apperance_viewer_1.currentText()
            for signal in self.signals_1 :
                if signal["name"] == signal_to_be_changed:
                    signal["color"] = color
            
                    for data_line in signal["data_lines"]:
                        data_line.setPen(signal["color"])   
        
    def show_hide_grph_1 (self):
        signal_to_show_hide = self.ui.comb_sig_apperance_viewer_1.currentText()
        for signal in self.signals_1 :
            if signal["name"] == signal_to_show_hide:
                if (self.ui.chk_bx_sig_show_1.isChecked()):
                    
                    for data_line in signal["data_lines"]:
                        data_line.setVisible(True) 
                else:
                    for data_line in signal["data_lines"]:    # self.current_signal_v1.data_line.setVisible(False)
                        data_line.setVisible(False)
    
                   

    def replay_1(self):
        self.ui.graphicsView.clear()
        self.plot_signal_grph_1()
        if self.islinked:
            self.replay_2()

    def clear_grph_2(self):
        self.ui.graphicsView_2.clear()
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

        
        signal = {
            "color" : "#ffffff" ,
            "name" : file_name, 
            "display" : True,
            "data" : data,
            "x" : x,
            "y" : y,
            "data_lines":[],
            "data_indices":[], 
        }
        
        self.signals_2.append(signal)
        
        self.updata_combo_bxs_grph_2()

        print(signal["color"])
        self.replay_2()
        
    def  plot_signal_grph_2(self ) :
    
        for signal in self.signals_2:
            data_line = self.ui.graphicsView_2.plotItem.plot( pen=signal["color"])
            signal["data_lines"].append(data_line)
            signal["data_indices"].append(0)
        self.ui.graphicsView_2.plotItem.getViewBox().setAutoPan(x=True,y=True)
        self.timer_2.timeout.connect(lambda:self.update_plot_data_grph_2(self.signals_2))
        self.timer_2.start()
        self.ui.graphicsView_2.show()
        max_y , min_y = self.find_max_min_y_grph_2()
        self.ui.graphicsView_2.plotItem.vb.setLimits(xMin=min(signal["x"]), xMax=max(signal["x"]), yMin=min_y, yMax=max_y)
        self.ui.graphicsView_2.setXRange(0 , 0.002*len(signal["data"]))


        
        icon = QtGui.QPixmap("pause.png")
        self.ui.btn_play_pasuse_viewer_2.setIcon(QtGui.QIcon(icon))
       
    def update_plot_data_grph_2(self,signals):
        for signal in signals:
            for i in range(len(signal["data_lines"])):
                x = signal["x"][:signal["data_indices"][i]]
                y = signal["y"][:signal["data_indices"][i]]
                signal["data_indices"][i] += 5 # Update the index for this signal
                signal["data_lines"][i].setData(x, y)
         
    
    def find_max_min_y_grph_2(self):
        max_y = float('-inf')  
        min_y = float('inf')   

        for signal in self.signals_2 :
            if "y" in signal and signal["y"]:
                max_y = max(max_y, max(signal["y"]))
                min_y = min(min_y, min(signal["y"]))

        return max_y, min_y
    
         
         
         

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
        self.ui.graphicsView_2.getViewBox().scaleBy((1.2, 1.2))
        if self.islinked:
            self.ui.graphicsView.getViewBox().scaleBy((1.2, 1.2))
            

    def zoom_in_grph_2(self):
        self.ui.graphicsView_2.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
        if self.islinked:
            self.ui.graphicsView.getViewBox().scaleBy((1 / 1.2, 1 / 1.2))
            
    
    def faster_grph_2(self):
        self.timer_2.setInterval(self.timer_2.interval() // 2)
    
    def slower_grph_2(self):
         self.timer_2.setInterval(self.timer_2.interval() * 2)

 
    def move_signal_from_grph_2(self):
            signal_to_move = self.ui.comb_move_viewer_2.currentText()
            for signal in self.signals_2:
                if signal["name"] == signal_to_move:
                    for data_line in signal["data_lines"]:
                        self.ui.graphicsView_2.removeItem(data_line)
                        self.ui.graphicsView.addItem(data_line)
                    
                    self.signals_1.append(signal)
                    self.signals_2.remove(signal)
                    self.updata_combo_bxs_grph_1()
                    self.updata_combo_bxs_grph_2()

    def updata_combo_bxs_grph_2(self):
        
        self.ui.comb_sig_apperance_viewer_2.clear()
        self.ui.comb_move_viewer_2.clear()
        self.ui.combo_rename_grph_2.clear()
        
        reversed_signals = self.signals_2[::-1]

        for signal in reversed_signals:
            self.ui.comb_sig_apperance_viewer_2.addItem(signal["name"])
            self.ui.comb_move_viewer_2.addItem(signal["name"])
            self.ui.combo_rename_grph_2.addItem(signal["name"])
    
    def change_sig_color_grph_2(self):
        color = colorchooser.askcolor()[1]
        if color[1]:
    
            signal_to_be_changed = self.ui.comb_sig_apperance_viewer_2.currentText()
            for signal in self.signals_2 :
                if signal["name"] == signal_to_be_changed:
                    signal["color"] = color
            
                    for data_line in signal["data_lines"]:
                        data_line.setPen(signal["color"])   
            
    
    def show_hide_grph_2 (self):
        signal_to_show_hide = self.ui.comb_sig_apperance_viewer_2.currentText()
        for signal in self.signals_2 :
            if signal["name"] == signal_to_show_hide:
                if (self.ui.chk_bx_sig_show_2.isChecked()):
                                        
                    for data_line in signal["data_lines"]:
                        data_line.setVisible(True) 
                else:
                    for data_line in signal["data_lines"]:    # self.current_signal_v1.data_line.setVisible(False)
                        data_line.setVisible(False)        
        
        
        
    

    def replay_2(self):
        self.ui.graphicsView_2.clear()
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
        
            self.replay_1()
            
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
    
   
    def cal_statistics_1(self):
        statistics_list = []

        for signal in self.signals_1:
            data_item = self.ui.graphicsView.getPlotItem().listDataItems()[0]  
            x_values, y_values = data_item.getData()

            mean_value = round(mean(y_values), 2)
            std_deviation = round(stdev(y_values), 2)
            duration = round(len(y_values), 2)
            min_value = round(min(y_values), 2)
            max_value = round(max(y_values), 2)

            statistics = {
                "signal" : signal["name"],
                'mean': mean_value,
                'std': std_deviation,
                'duration': duration,
                'min': min_value,
                'max': max_value
            }

            statistics_list.append(statistics)

        return statistics_list
        
    def cal_statistics_2(self):
        data_item = self.ui.graphicsView_2.getPlotItem().listDataItems()[0]  
        x_values, y_values = data_item.getData()

        mean_value = mean(y_values)
        std_deviation = stdev(y_values)
        duration = len(y_values)
        min_value = min(y_values)
        max_value = max(y_values)

        statistics = {
            'mean':round( mean_value , 2),
            'std':round( std_deviation , 2),
            'duration':round( duration , 2),
            'min':round( min_value , 2),
            'max':round( max_value , 2)
        }

        return statistics

   
            
    def capture_snapshot_1(self):
        exporter = exporters.ImageExporter(self.ui.graphicsView.plotItem)
        exporter.parameters()['width'] = self.ui.graphicsView.width()    
        exporter.parameters()['height'] = self.ui.graphicsView.height()   
        img1_path = f"grah1_snap_{self.counter_1}.png"
        exporter.export(img1_path)
        self.snapshots_1.append(img1_path)
        self.counter_1 += 1 
        self.ui.btn_repo.setEnabled(True)
        
        
        
    def capture_snapshot_2(self):
        exporter = exporters.ImageExporter(self.ui.graphicsView_2.plotItem)
        exporter.parameters()['width'] = self.ui.graphicsView_2.width()  
        exporter.parameters()['height'] = self.ui.graphicsView_2.height() 
        img2_path = f"grah2_snap_{self.counter_2}.png"
        exporter.export(img2_path)
        self.snapshots_2.append(img2_path)
        self.counter_2 += 1 
        self.ui.btn_repo.setEnabled(True)
        
    

    def report(self ):    
        file_path, _ = QFileDialog.getSaveFileName(None, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)")
        pdf = FPDF()
        
        for snap in self.snapshots_1:
            
            pdf.add_page()
            pdf.image(snap, 5, 10, 190)
            os.remove(snap)
            self.snapshots_1.remove(snap)
        
            table_x = 5
            table_y = 100
            
            data_dict1  = self.cal_statistics_1()
            
            pdf.set_xy(table_x, table_y)
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, "Data Table 1", ln=True, align="C")
            pdf.ln(10)
            col_widths = [60, 25, 25, 25, 25, 25]
            headers = ["Signals", "mean", "max", "min", "std", "duration"]
            for header in headers:
                pdf.cell(col_widths[headers.index(header)], 10, header, border=1)
            pdf.ln()

            # Create the table rows with 7 rows
            for data in data_dict1:
                pdf.cell(col_widths[0], 10, data["signal"], border=1)
                pdf.cell(col_widths[1], 10, str(data['mean']), border=1)
                pdf.cell(col_widths[2], 10, str(data['max']), border=1)
                pdf.cell(col_widths[3], 10, str(data['min']), border=1)
                pdf.cell(col_widths[4], 10, str(data['std']), border=1)
                pdf.cell(col_widths[5], 10, str(data['duration']), border=1)
                pdf.ln()

            # for key, value in data_dict1.items():
            #     pdf.cell(100, 10, str(key), border=1)
            #     pdf.cell(0, 10, str(value), border=1)
            #     pdf.ln()

                
                
        for snap in self.snapshots_2:
                
            pdf.add_page()
            pdf.image(snap, 5, 10, 190)
            os.remove(snap)
            self.snapshots_2.remove(snap)
        
            table_x = 5
            table_y = 100
            
            data_dict2  = self.cal_statistics_2()
            pdf.set_xy(table_x, table_y)
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, "Data Table 2", ln=True, align="C")
            pdf.ln(10)

            for key, value in data_dict2.items():
                pdf.cell(100, 10, str(key), border=1)
                pdf.cell(0, 10, str(value), border=1)
                pdf.ln()
        
        pdf.output( file_path, "F")
        self.ui.btn_repo.setEnabled(False)
    
  
def main():
    app = QApplication(sys.argv)
    window = MyWindow() 
    window.setWindowIcon(QIcon("C:/Users/Sara/Desktop/DSP_tasks/sara_multi_channel_signal_viewer/imgs/app_icon.png"))
    window.setWindowTitle("signal viewer")
    window.showMaximized()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
