# Form implementation generated from reading ui file 'C:\Users\Nicolee\Coding\TechnicalProgramming\Chapter6\BonusTask\Ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnShowAll = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnShowAll.setObjectName("btnShowAll")
        self.horizontalLayout.addWidget(self.btnShowAll)
        self.btnBorn2001 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBorn2001.setObjectName("btnBorn2001")
        self.horizontalLayout.addWidget(self.btnBorn2001)
        self.btnOldest = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnOldest.setObjectName("btnOldest")
        self.horizontalLayout.addWidget(self.btnOldest)
        self.btnTesters = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTesters.setObjectName("btnTesters")
        self.horizontalLayout.addWidget(self.btnTesters)
        self.btnRoleCount = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRoleCount.setObjectName("btnRoleCount")
        self.horizontalLayout.addWidget(self.btnRoleCount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Data Viewer"))
        self.btnShowAll.setText(_translate("MainWindow", "Show All"))
        self.btnBorn2001.setText(_translate("MainWindow", "Born in 2001"))
        self.btnOldest.setText(_translate("MainWindow", "Top 3 Oldest"))
        self.btnTesters.setText(_translate("MainWindow", "Show Testers"))
        self.btnRoleCount.setText(_translate("MainWindow", "Count by Role"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
