import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel


class Example(QWidget): #extend QWidget
    def __init__(self): #父类构造器
        super().__init__() #父级
        self.initUI()

    def initUI(self): #本类构造器
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls','Bck'  , '233', '233', '233', '233', '233', '233', '233', '233', '233']
        positions = [(i,j) for i in range(5) for j in range(4)]
        for positions, name in zip(positions,names):
            if name == '':
                continue
            Label = QLabel(name)
            grid.addWidget(Label,*positions)
        self.move(300,150)
        self.setWindowTitle("test")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())
# if __name__ == '__main__':
#     app = QApplication(sys.argv) #shell argv
#     w = QWidget()
#     w.resize(250,150) #weight height
#     w.move(300,300)
#     w.setWindowTitle('松田课表')
#     w.show()
#     sys.exit(app.exec_()) #_关键词

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(20, 10, 91, 101))
#         self.label.setObjectName("label")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "1,1,2"))
