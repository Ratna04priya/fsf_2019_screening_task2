from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os, sys
import csv
import pandas as pd
import numpy as np
from scipy.interpolate import spline
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from sklearn.decomposition import FastICA
from scipy.interpolate import make_interp_spline, BSpline
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


class PrettyWidget(QtGui.QWidget):
    
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(100,200, 1000, 600)
        self.center()
        self.setWindowTitle('Loading the Files & Plotting ')     
        
        #Grid Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
                    
        #Canvas and Toolbar
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)     
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 2,0,1,2)
        grid.addWidget(self.toolbar, 1,0,1,2)

        #Empty 5x5 Table
        self.table = QtGui.QTableWidget(self)
        self.table.setRowCount(13)
        self.table.setColumnCount(13)
        grid.addWidget(self.table, 3,0,1,2)
        
        #Import CSV Button
        btn1 = QtGui.QPushButton('Import CSV', self)
        btn1.resize(btn1.sizeHint()) 
        btn1.clicked.connect(self.getCSV)
        grid.addWidget(btn1, 0,0)
        
        #Plot scatter Button
        btn2 = QtGui.QPushButton('Plot Point', self)
        btn2.resize(btn2.sizeHint())    
        btn2.clicked.connect(self.plotscatter)
        grid.addWidget(btn2, 0,1)
        
        #Plot line
        btn3 = QtGui.QPushButton('Plot Line', self)
        btn3.resize(btn3.sizeHint())    
        btn3.clicked.connect(self.plotline)
        grid.addWidget(btn3, 0,2)

        #plot Smooth
        btn4 = QtGui.QPushButton('Plot Smooth', self)
        btn4.resize(btn4.sizeHint())    
        btn4.clicked.connect(self.plotsmooth)
        grid.addWidget(btn4, 0,3)
    
        self.show()
    
    
    def getCSV(self):
        filePath = QtGui.QFileDialog.getOpenFileName(self, 'Open File','*.csv')
        fileHandle = open(filePath, 'r')
        # line = fileHandle.readline()[:-1].split(',')
        # for n, val in enumerate(line):
        #     newitem = QtGui.QTableWidgetItem(val)
        #     self.table.setItem(0, n, newitem)
        # self.table.resizeColumnsToContents()
        # self.table.resizeRowsToContents()    
        df = pd.read_csv(filePath)
       


        #reader = csv.reader(fileHandle,delimiter = ",")
        #data = list(reader)
        #print(data)
        row_count = df.shape[0]

        #i = 0

        line1 = fileHandle.readline()[:-1].split(',')
        for n, val in enumerate(line1):
            newitem = QtGui.QTableWidgetItem(val)
            self.table.setItem(0, n, newitem)
        
        
        for i in range(1,row_count):
            #print(i)
            #line = fileHandle.readline()[:-1].split(',')
        #print(df)
        #print(line)


            line = df.values[i]
            for n, val in enumerate(line):
                newitem = QtGui.QTableWidgetItem(val)
                print(val)
                self.table.setItem(i, n, newitem)
            i=+1
        
        
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()    
    
    
    def plotline(self):
        
        col1, ok = QtGui.QInputDialog.getInt(self, 'Text Input Dialog', 'Enter numbers of column 1:')
    
        col2, oku = QtGui.QInputDialog.getInt(self, 'Text Input Dialog', 'Enter the column 2:')
            
        y = []
        for n in range(10):
            try:
                y.append(float(self.table.item(n, col1).text()))
            except:
                y.append(np.nan)
        plt.cla()
        ax = self.figure.add_subplot(111)
        ax.plot(y, 'r.-')
        ax.set_title('Line Plot')
        self.canvas.draw()

        x = []
        for n in range(10):
            try:
                x.append(float(self.table.item(n, col2).text()))
            except:
                x.append(np.nan)
        plt.cla()
        ax = self.figure.add_subplot(111)
        ax.plot(x,y, 'r.-')
        ax.set_title('Line Plot')
        self.canvas.draw()
        

    def plotsmooth(self):
            col1, ok = QtGui.QInputDialog.getInt(self, 'Text Input Dialog', 'Enter numbers of column 1:')
    
            col2, oku = QtGui.QInputDialog.getInt(self, 'Text Input Dialog', 'Enter the column 2:')
         
            y = []
            for n in range(10):
                try:
                    y.append(float(self.table.item(n, col1).text()))
                except:
                    y.append(np.nan)
            

            y = np.linspace(max(y),min(y),500) 

            x = []
            for n in range(10):
                try:
                    x.append(float(self.table.item(n, col2).text()))
                except:
                    y.append(np.nan)
            plt.cla()

            x = np.linspace(max(x),min(x),500) 

            #s = np.cos(y)

            ax = self.figure.add_subplot(111)
            plt.plot (x,y)
        
            ax.set_title('Smooth Line Plot')
            self.canvas.draw()


    def plotscatter(self):
        col1, ok = QtGui.QInputDialog.getInt(self, 'Text Input Dialog', 'Enter numbers of column 1:')
    
        col2, oku = QtGui.QInputDialog.getInt(self, 'Text Input Dialog', 'Enter the column 2:')
         
        x = []
        for n in range(9):
            try:
                x.append(float(self.table.item(n, col1).text()))
            except:
                x.append(np.nan)
        
       
        y = []
        for n in range(9):
            try:
                y.append(float(self.table.item(n, col2).text()))
            except:
                y.append(np.nan)
        plt.cla()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y,'o',c='purple')
        ax.set_title('Point Plot')
        self.canvas.draw()
    
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    
        
def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()
