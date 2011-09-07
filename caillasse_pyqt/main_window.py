from PyQt4.QtCore import SIGNAL, pyqtSignal
from PyQt4.QtGui import QInputDialog, QMainWindow, QMessageBox, QStandardItem,\
        QStandardItemModel

from velat import Velat

from .main_window_ui import Ui_caillasse


def _person_item(person):
    return QStandardItem(person.name)


class Caillasse(QMainWindow, Ui_caillasse):

    new_person = pyqtSignal(name="new_person")

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self._file = None
        self._velat = None

        self._persons_model = QStandardItemModel(self)
        self.all_persons.setModel(self._persons_model)

        self._activities_model = QStandardItemModel(self)
        self.all_activities.setModel(self._persons_model)

        self.connect(self.actionNew, SIGNAL('triggered()'), self._new)
        self.connect(self.actionSave, SIGNAL('triggered()'), self._save)
        self.connect(self.actionSave_copy, SIGNAL('triggered()'), self._save_as)
        self.connect(self.actionNew_person, SIGNAL('triggered()'), self._new_person)
        self.connect(self, SIGNAL("new_person"), self._new_person)

        self._new()

    def _new(self):
        self._file = None
        self._persons_model.reset()
        self._activities_model.reset()
        self._velat = Velat()

    def _save(self):
        print "save"
        if self._file is None:
            return self.save_as()

    def _save_as(self):
        print "save as"
    
    def _get_name(self):
        name, ok = QInputDialog.getText(self, "New person", "Name this person")
        if not ok:
            return name, False, False
        name = unicode(name).strip()
        if not name:
            return name, False, True
        return name, True, False

    def _new_person(self):
        loop = True
        while loop:
            name, cont, loop = self._get_name()
        print name
        if not cont:
            return
        try:
            person = self._velat.add_person(name)
        except ValueError, err:
            #FIXME: use a velatexception
            QMessageBox.warning(self, "Error", "Name %s is already in use, "
                    "try another" % name)
            #FIXME: ue pyqtSignal
            self.emit(SIGNAL("new_person"))
            return
        item = _person_item(person)
        self._persons_model.appendRow(item)
