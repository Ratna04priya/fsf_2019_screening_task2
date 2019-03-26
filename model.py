import sys
from PyQt4 import QtGui, QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(400, 500, 600, 500)
        self.setWindowTitle("Text Editor")
        self.setWindowIcon(QtGui.QIcon('editor.png'))
        

        a = QtGui.QAction("&New Project",self)
        a.setShortcut("Ctrl+N")
        a.setStatusTip('Wanna add new project')
        a.triggered.connect(self.editor)
        #a.triggered.connect(self.close_application)

        openFile = QtGui.QAction("&Load", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
            

        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Source')
        openEditor.triggered.connect(self.editor)

        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)


        d =  QtGui.QAction("&Exit",self)
        d.setShortcut("Ctrl+Q")
        d.setStatusTip('Wanna leave the App')
        d.triggered.connect(self.close_application)

        p =  QtGui.QAction("&Plot", self)
        p.setShortcut("Ctrl+P")
        p.setStatusTip('Plot')
        p.triggered.connect(self.plot)

        



        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(a)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)


        viewMenu = mainMenu.addMenu('&Edit')
        viewMenu.addAction(openEditor)

        plotmenu= mainMenu.addMenu('&Plot')
        plotmenu.addAction(p)

        exit = mainMenu.addMenu('&Exit')
        exit.addAction(d)

        self.home()

        self.show()

    def home(self):

        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(100,100)

        self.toolBar = self.addToolBar("C")
    



    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self,
                                                    'CSV File',
                                                   '/home/ratna/Documents/GUI_p/csvfiles','*.csv')
        file=pd.read_csv(name)
        #self.tableView.setModel(file)
        print(file)

        file = open(name,'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def plot(self):
        name = QtGui.QFileDialog.getOpenFileName(self,
                                                    'CSV File',
                                                   '/home/ratna/Documents/GUI_p/csvfiles','*.csv')
        file=pd.read_csv(name)
        
        print(file)
        print(file.columns)

        text1, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter first column:')
        text2, oku = QInputDialog.getText(self, 'Text Input Dialog', 'Enter second column:')
        print(text1)
        print(text2)
        # df = pd.DataFrame(file)
        # plt.scatter(df['text1'])
      
        plt.figure(num=1, figsize=(8, 6))
        plt.title('Plot 1', size=14)
        plt.xlabel('x-axis', size=14)
        plt.ylabel('y-axis', size=14)
        plt.plot(file['Phone'], file['School'])
        plt.hist(file['City'])
        #plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
        plt.legend(loc='upper left')
        plt.savefig('plot1.png', format='png')
        plt.show()


    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(100,100)




    def close_application(self):
        choice = QtGui.QMessageBox.question(self,'Extract!',"Want to Quit?",QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print("Okay! Importing you out !")
            sys.exit()

        else:
            pass



def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
