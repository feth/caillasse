from PyQt4.QtCore import QObject, Qt, SIGNAL, pyqtSignal
from PyQt4.QtGui import QAction, QMainWindow

from velat import Velat

from .main_window_ui import Ui_caillasse
from .models import PersonsModel


def _connect(source, target):
    if isinstance(source, QAction):
        return QObject.connect(source, SIGNAL('triggered()'), target)
    assert False, "unhandled type %s" % type(source)


class Caillasse(QMainWindow, Ui_caillasse):

    new_person = pyqtSignal(name="new_person")

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self._file = None
        self._velat = None
        self._all_persons_model = None
        self._expenses_model = None

        _connect(self.actionNew, self._new)
        _connect(self.actionSave, self._save)
        _connect(self.actionSave_copy, self._save_as)
        _connect(self.actionNew_person, self._new_person)
        _connect(self.actionNew_expense, self._new_expense)

        self._new()

    def _new(self):
        self._file = None
        self._velat = Velat()
        self._all_persons_model = PersonsModel(self._velat, self)
        self.all_persons.setModel(self._all_persons_model)

    def _save(self):
        print "save"
        if self._file is None:
            return self.save_as()

    def _save_as(self):
        print "save as"
    
    def _new_person(self):
        self._all_persons_model.new_person(self)

    def _new_expense(self):
        self._all_persons_model.new_person(self)
