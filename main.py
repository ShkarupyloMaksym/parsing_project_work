import work_ua
from PyQt5 import QtCore, QtGui, QtWidgets
from Screen_forms.main_window_new import QMainWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())