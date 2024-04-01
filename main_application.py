from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUiType
from file_handling import get_files, delete_file
from files_order import move_file_up, move_file_down
from encrypt import hide_or_show_password
from exec import merger
from info_dialog import info_btn_clicked

gui, _ = loadUiType("gui.ui")


class PyPDFMerger(QMainWindow, gui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.initializing()
        self.actions_triggered()
        self.buttons_clicked()
        self.tabs_change()

    def initializing(self):
        self.tabWidget.tabBar().setVisible(False)
        self.hidePasswordButton.hide()
        self.progressBar.hide()

    def buttons_clicked(self):
        self.addPDFButton.clicked.connect(lambda: get_files(self.PDFList))
        self.deletePDFButton.clicked.connect(lambda: delete_file(self.PDFList))
        self.hidePasswordButton.clicked.connect(lambda: hide_or_show_password(self.passwordInput))
        self.showPasswordButton.clicked.connect(lambda: hide_or_show_password(self.passwordInput))
        self.upPDFButton.clicked.connect(lambda: move_file_up(self.PDFList))
        self.downPDFButton.clicked.connect(lambda: move_file_down(self.PDFList))
        self.executeButton.clicked.connect(lambda: merger(self))

    def actions_triggered(self):
        self.actionInfo.triggered.connect(info_btn_clicked)

    def tabs_change(self):
        self.actionMerger.triggered.connect(lambda e: self.tabWidget.setCurrentIndex(0))
        self.actionSpeech.triggered.connect(lambda e: self.tabWidget.setCurrentIndex(1))
