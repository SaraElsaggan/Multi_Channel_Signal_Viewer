#IMPORTS
#--------------------------
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget , QDesktopWidget , QFileDialog
from PyQt5.QtGui import QIcon 
import matplotlib.pyplot as plt
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mainwindow import Ui_MainWindow

from matplotlib.animation import FuncAnimation
from pyqtgraph import PlotWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget , QDesktopWidget , QFileDialog
from PyQt5.QtCore import QStateMachine, QState, QPropertyAnimation
import pyqtgraph as pg
import pandas as pd
# from PyQt5 import QtWidgets, QtCore,QtGui,uic
# from pyqtgraph import PlotWidget, plot
# from mainwindow import Ui_MainWindow
# import matplotlib.pyplot as plot
# from random import randint
# from threading import Timer
# from scipy import signal
# import pyqtgraph as pg
# import pandas as pd
# import numpy as np 
# import pathlib 
# import sys  # We need sys so that we can pass argv to QApplication
# import os
# import csv
# import pyautogui
# from PIL import Image






class MyWindow(QMainWindow):  #this means is we're gonna take all of the properties that cue main window has and we're gonna use them in my window
    def __init__(self):
        super(MyWindow , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionchannel_1.triggered.connect(self.open_file)
        
        
        # self.ui.tab_12 = 
        # self.ui.tab_12.

        
        self.selectid_file = None

        self.graph1 = PlotWidget(self.ui.centralwidget)
        self.graph1.setGeometry(10, 10, 750, 300)
        self.graph1.setObjectName("Channel1")
        
        self.graph1 = PlotWidget(self.ui.centralwidget)
        self.graph1.setGeometry(10, 349, 750, 300)
        self.graph1.setObjectName("Channel2")
        
        # self.signal_ch3_3 = pg.GraphicsLayoutWidget(self.ui.centralwidget)
        # self.signal_ch3_3.setGeometry(QtCore.QRect(20, 390, 750, 300))
        # self.signal_ch3_3.setObjectName("signal_ch3_3")
        # # self.graph1 = self.signal_ch3_2.addPlot()
        # self.graph2 = PlotWidget(self.signal_ch3_3)
        # # self.graph2.setGeometry(10, 350, 750, 400)
        # # self.graph2.setObjectName("Channel2")



        # self.ui.graph2 = PlotWidget(self.ui.graphicsView)
        # self.ui.graph2.setGeometry(QtCore.QRect(10, 30, 750, 300))
        # self.ui.graph2.setObjectName("Channel1")
        
        # self.ui.play_pause_btn_ch3.clicked.connect(self.toggle_play_pause)


    def open_file(self):
        file = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","(*.csv) ")
        if file :
            print(f"selected file :{file}")
            # self.selectid_file = file
            # signal = pd.read_csv(file)
            # file = file[0]
            # print (signal.head())
    
    
    def zoom_in(self):
        pass

    def out(self):
        pass
    
    def choose_signal_color(self):
        pass

    def play(self):
        pass
    
    def pause():
        pass
    
    def faster(self):
        pass
    
    def slower(self):
        pass
    
    def move_up(self):
        pass
    
    def move_down(self):
        pass
    
    def add_signal_tab_to_data_window(self):
        pass
    
    def add_signal_row_to_prop_window(self):
        pass
    
    
    def link_graphs(self):
        pass
    
    
    # def channel1 (self,data):
    #     self.ui.signal_ch3.setBackground('w')
    #     self.data_line1 =self.ui.signal_ch3.plot( self.x1,self.y1,pen=self.pen1)
    #     self.ui.signal_ch3.plotItem.setLimits(xMin =0, xMax=12 , yMin =-0.6, yMax=0.6)
    #     self.idx1=0
    #     self.ui.signal_ch3.plotItem.getViewBox().setAutoPan(x=True,y=True)
    #     self.timer1.setInterval(20)
    #     self.timer1.timeout.connect(lambda:self.update_plot_data1(self.data_line1,data))
    #     self.timer1.start()
    #     self.ui.signal_ch3.show()
    #     self.ui.signal_ch3.setXRange(0,0.002*len(data))
    
    # def read_data1(self,fname):
    #     path = fname[0]
    #     if fname[1] == "(*.csv)":
    #        self.data1 = np.genfromtxt(path, delimiter = ' ')
    #        self.x1= self.data1[: , 0]
    #        self.y1 =self.data1[: , 1] 
    #        self.x1= list(self.x1[:])
    #        self.y1= list(self.y1[:])
    #        self.channel1(self.data1)
    
            
    # def load1(self):
    #     options =  QFileDialog.Options()
    #     fname = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
    #                     "(*.csv) ", options=options)

    #     if(fname[0]!=''): 
    #         self.read_data1(fname) 
    #     else:
    #         pass 
    
    def open_file(self):
        
        file = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")

        if file:
            print(f"Selected file: {file}")

# def toggle_play_pause(self):
#         if self.machine.configuration() == [self.play_state]:
#             self.machine.postEvent(QStateMachine.SignalEvent(self.play_pause_button.clicked))
#             self.play_animation.start()
#         else:
#             self.machine.postEvent(QStateMachine.SignalEvent(self.play_pause_button.clicked))
#             self.pause_animation.start()




def main():
    app = QApplication(sys.argv)
    window = MyWindow() 
    # window.setWindowIcon(QIcon("C:/Users/Sara/Desktop/DSP_tasks/task1_DSP_sara/imgs/app_icon.png"))
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
