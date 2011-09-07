from PyQt4.QtGui import QMainWindow, QStandardItemModel

from .main_window_ui import Ui_caillasse


class Caillasse(QMainWindow, Ui_caillasse):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self._persons_model = QStandardItemModel(self)
        self.all_persons.setModel(self._persons_model)

        self._activities_model = QStandardItemModel(self)
        self.all_activities.setModel(self._persons_model)

    
