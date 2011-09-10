import os.path

from PyQt4.QtCore import QObject, QSettings, SIGNAL
from PyQt4.QtGui import QAction, QFileDialog, QMainWindow, QMessageBox, QWidget

from velat import Velat, velat

from .main_window_ui import Ui_caillasse
from .models import ExpensesModel, PersonsModel, TransfersModel 
from .statusbar_ui import Ui_statusbar 


def _connect(source, target):
    if isinstance(source, QAction):
        return QObject.connect(source, SIGNAL('triggered()'), target)
    assert False, "unhandled type %s" % type(source)


_FILE_FILTER = "caillasse files (*.caillasse)"

class Caillasse(QMainWindow, Ui_caillasse):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self._settings = QSettings("Free software", "Caillasse", self)

        statusbar = QWidget(self)
        self.ui_bar = Ui_statusbar()
        self.ui_bar.setupUi(statusbar)
        self.statusBar().addPermanentWidget(statusbar)

        self._file = ""
        self._velat = None

        self._all_expenses_model = ExpensesModel(self._velat, self)
        self.all_expenses.setModel(self._all_expenses_model)
        self._all_persons_model = PersonsModel(self._velat, self)

        self.all_persons.setModel(self._all_persons_model)
        self._all_transfers_model = TransfersModel(self._velat, self)
        self.all_transfers.setModel(self._all_transfers_model)

        _connect(self.actionNew, self._new)
        _connect(self.actionLoad, self._load)
        _connect(self.actionSave, self._save)
        _connect(self.actionSave_copy, self._save_as)
        _connect(self.actionNew_person, self._new_person)
        _connect(self.actionNew_expense, self._new_expense)
        _connect(self.actionNew_transfer, self._new_transfer)

        self._new()

    def _new(self):
        self._file = ""
        self._velat = Velat()
        self._load_velat()

    def _load(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", 
                os.path.split(self._file)[0], _FILE_FILTER)
        if not filename:
            return
        self._velat = velat.load(filename)
        self._load_velat()
        self._file = filename

    def _load_velat(self):
        self._all_persons_model.load(self._velat, self._velat.persons)
        self._all_expenses_model.load(self._velat, self._velat.expenses)
        self._all_transfers_model.load(self._velat, self._velat.transfers)

    def _save(self):
        if not self._file:
            return self._save_as()
        self._velat.save(self._file)


    def _save_as(self):
        filename = QFileDialog.getSaveFileName(self, "Save as...", self._file, 
                _FILE_FILTER)
        if not filename:
            return
        self._velat.save(filename)
        self._file = filename
    
    def _new_person(self):
        self.tabs.setCurrentIndex(0)
        self._all_persons_model.new_item(self)

    def _new_expense(self):
        self.tabs.setCurrentIndex(1)
        self._all_expenses_model.new_item(self)

    def _new_transfer(self):
        if not self._velat.persons:
            QMessageBox.warning(self, "New transfer", "Please create persons "
                    "before transfers between them")
            return
        self.tabs.setCurrentIndex(2)
        self._all_transfers_model.new_item(self, self._all_persons_model)
