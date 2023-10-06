#IMPORTS
#--------------------------
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget , QDesktopWidget
from PyQt5.QtGui import QIcon 
import matplotlib.pyplot as plt
# from PyQt5.QtCore import QTimer
# import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mainwindow import Ui_MainWindow




class MyWindow(QMainWindow):  #this means is we're gonna take all of the properties that cue main window has and we're gonna use them in my window
    def __init__(self):
        super(MyWindow , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        # self.setWindowTitle("Signal Viewer") 
        # self.setGeometry(0 , 0 , QApplication.desktop().screenGeometry().width() ,  QApplication.desktop().screenGeometry().height())
        # self.setGeometry( 0 , 0 , 1500 , 2000)
        # self.setFullScreen()

def main():
    app = QApplication(sys.argv)
    window = MyWindow() 
    # window.setWindowIcon(QIcon("C:/Users/Sara/Desktop/DSP_tasks/task1_DSP_sara/imgs/app_icon.png"))
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
