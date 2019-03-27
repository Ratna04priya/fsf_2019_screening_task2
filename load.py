#from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt4 import QtCore, QtGui
Qt = QtCore.Qt
import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


# if __name__ == '__main__':
#     application = QtGui.QApplication(sys.argv)
#     view = QtGui.QTableView()
#     filePath = getOpenFileName('Open file','*.csv')
    
#     file=pd.read_csv(filePath)
#     model = PandasModel()
#     view.setModel(model)

#     view.show()
#     sys.exit(application.exec_())




# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(662, 512)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.verticalLayout = QtWidgets.QVBoxLayout()
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit.setObjectName("lineEdit")
#         self.verticalLayout.addWidget(self.lineEdit)
#         self.tableView = QtWidgets.QTableView(self.centralwidget)
#         self.tableView.setObjectName("tableView")
#         self.verticalLayout.addWidget(self.tableView)
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setObjectName("pushButton")
#         self.verticalLayout.addWidget(self.pushButton)
#         self.horizontalLayout.addLayout(self.verticalLayout)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.pushButton.setText(_translate("MainWindow", "PushButton"))


#         self.pushButton.clicked.connect(self.btn_clk)

#         MainWindow.show()

#     def btn_clk(self):
#         path = self.lineEdit.text()
#         df = pd.read_csv(path)
#         model = PandasModel(df)
#         self.tableView.setModel(model)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())