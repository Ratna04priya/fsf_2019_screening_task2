import sys
from PyQt4 import QtGui, QtCore

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

        openFile = QtGui.QAction("&Open File", self)
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
        



        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(a)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)


        viewMenu = mainMenu.addMenu('&Edit')
        viewMenu.addAction(openEditor)

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
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)



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
