from PyQt4.QtCore import QObject, Qt, SIGNAL, pyqtSignal
from PyQt4.QtGui import QAction, QMainWindow, QMessageBox

from velat import Velat

from .main_window_ui import Ui_caillasse
from .models import ExpensesModel, PersonsModel, TransfersModel 


def _connect(source, target):
    if isinstance(source, QAction):
        return QObject.connect(source, SIGNAL('triggered()'), target)
    assert False, "unhandled type %s" % type(source)


class Caillasse(QMainWindow, Ui_caillasse):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self._file = None
        self._velat = None
        self._all_persons_model = None
        self._all_expenses_model = None
        self._all_transfers_model = None

        _connect(self.actionNew, self._new)
        _connect(self.actionSave, self._save)
        _connect(self.actionSave_copy, self._save_as)
        _connect(self.actionNew_person, self._new_person)
        _connect(self.actionNew_expense, self._new_expense)
        _connect(self.actionNew_transfer, self._new_transfer)

        self._new()

    def _new(self):
        self._file = None
        self._velat = Velat()
        self._all_persons_model = PersonsModel(self._velat, self)
        self.all_persons.setModel(self._all_persons_model)
        self._all_expenses_model = ExpensesModel(self._velat, self)
        self.all_expenses.setModel(self._all_expenses_model)
        self._all_transfers_model = TransfersModel(self._velat, self)
        self.all_transfers.setModel(self._all_transfers_model)

    def _save(self):
        print "save"
        if self._file is None:
            return self.save_as()

    def _save_as(self):
        print "save as"
    
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
