import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from Emp import load_employee_data, calculate_age, filter_employees_born_in_2001, \
    export_top_3_oldest_employees, filter_employees_with_tester_role, count_employees_by_role
from Ui import Ui_MainWindow


class EmployeeExt(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.df = load_employee_data()

        self.df['Age'] = self.df['Dob'].apply(calculate_age)

        self.actionExit.triggered.connect(self.close)
        self.btnShowAll.clicked.connect(self.show_all)
        self.btnBorn2001.clicked.connect(self.show_born_2001)
        self.btnOldest.clicked.connect(self.show_oldest)
        self.btnTesters.clicked.connect(self.show_testers)
        self.btnRoleCount.clicked.connect(self.show_role_count)

        self.show_all()

    def showWindow(self):
        self.show()

    def show_all(self):
        self.display_dataframe(self.df)
        self.statusbar.showMessage(f"Showing all {len(self.df)} employees")

    def show_born_2001(self):
        born_in_2001 = filter_employees_born_in_2001(self.df)
        self.display_dataframe(born_in_2001)
        self.statusbar.showMessage(f"Showing {len(born_in_2001)} employees born in 2001")

    def show_oldest(self):
        oldest_employees = export_top_3_oldest_employees(self.df)
        self.display_dataframe(oldest_employees)
        self.statusbar.showMessage("Showing top 3 oldest employees")

    def show_testers(self):
        testers = filter_employees_with_tester_role(self.df)
        self.display_dataframe(testers)
        self.statusbar.showMessage(f"Showing {len(testers)} employees with Tester role")

    def show_role_count(self):
        role_counts = count_employees_by_role(self.df)
        self.display_dataframe(role_counts)
        self.statusbar.showMessage("Showing employee count by role")

    def display_dataframe(self, df):
        if df is None or df.empty:
            QMessageBox.information(self, "Information", "No data to display.")
            return

        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        rows, cols = df.shape
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)

        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        for row in range(rows):
            for col in range(cols):
                value = str(df.iloc[row, col])
                item = QTableWidgetItem(value)
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.resizeColumnsToContents()