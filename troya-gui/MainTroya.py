import sys
from PyQt5 import QtWidgets
from UIClass import Ui_MainWindow, Ui_Dialog
import Terminal_Connector
import funcLogTrace, funcPrintTsoBrowse, funcPrintTsoListing, funcPrintTroyaM, funcPrintTsoTordump, funcDelAURF, funcFindDurf, funcTest

global terminal


class Login(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.sessionName = 0
        self.sessionSelected = False
        self.setupUiD(self)
        self.comboBox.currentIndexChanged.connect(self.selection_change)
        self.listWidget.itemClicked.connect(self.show_session_list)
        self.listWidget.setVisible(False)
        self.label.setVisible(False)
        self.buttonBox.accepted.connect(self.handle_connection)
        self.buttonBox.rejected.connect(self.reject)

    def show_session_list(self):
        for item in self.listWidget.selectedItems():
            self.sessionName = item.text()
            self.sessionSelected = True

    def selection_change(self):
        self.listWidget.setVisible(False)
        self.label.setVisible(False)
        self.listWidget.clear()
        if self.comboBox.currentText() == "TERMINAL":
            self.listWidget.setVisible(True)
            self.label.setVisible(True)
#            print("TERMINAL SELECTED")
            global terminal
            terminal = Terminal_Connector.TerminalConnector()
            sessionList = terminal.get_session_list()
            for item in range(0, len(sessionList)):
                self.listWidget.addItem(sessionList[item])
        elif self.comboBox.currentText() == "TCP-IP":
            pass
#            print("TCP-IP SELECTED")

    def handle_connection(self):
        if self.sessionSelected:
            terminal.connect_session(self.sessionName)
            QtWidgets.QMessageBox.information(self, 'Terminal Connection', self.sessionName + " connected ")
            self.accept()
        elif self.comboBox.currentText() == "TCP-IP":
            QtWidgets.QMessageBox.information(self, '  TCP-IP  ', 'UNDER CONSTRUCTION')
        else:
            QtWidgets.QMessageBox.critical(self, '  Error  ', 'Invalid Selection')

    def reject(self):
        sys.exit(Login.exec_())


class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        self.textBrowser.setText(terminal.troya_entry("<GETSCREEN>"))
        self.pushButton.clicked.connect(self.send_troya_entry)
        self.pushButton.setShortcut("Return")
        self.pushButton1.clicked.connect(self.execute_macro)
        self.actionexit.triggered.connect(self.close)

    def send_troya_entry(self):
        self.textBrowser.textCursor()
        if self.lineEdit.text() != "":
            self.textBrowser.setText(terminal.troya_entry(self.lineEdit.text()))
            # self.textBrowser.setText(terminal.troya_entry("<GETSCREEN>"))
        else:
            self.textBrowser.setText(terminal.troya_entry("<ENTER>"))
        self.lineEdit.clear()

    def execute_macro(self):
        text = self.comboBox1.currentText()
        if text == "Trace Log":
            funcLogTrace.main(terminal)
        elif text == "PrintTSO_Browse":
            funcPrintTsoBrowse.main(terminal)
        elif text == "PrintTSO_Listing":
            funcPrintTsoListing.main(terminal)
        elif text == "PrintTroya_M":
            funcPrintTroyaM.main(terminal)
        elif text == "PrintTSO_Tordump":
            funcPrintTsoTordump.main(terminal)
        elif text == "Delete DURF":
            funcDelAURF.main(terminal, mainGui)
        elif text == "Delete Empty AURF":
            funcFindDurf.main(terminal, mainGui)
        elif text == "TEST":
            funcTest.main(terminal)


if __name__ == "__main__":
    UIClass = QtWidgets.QApplication(sys.argv)
    Login = Login()
    Login.exec_()
    mainGui = MainUi()
    mainGui.show()
    sys.exit(UIClass.exec_())