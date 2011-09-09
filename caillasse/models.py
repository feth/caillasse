from PyQt4.QtCore import Qt
from PyQt4.QtGui import QInputDialog, QStandardItem, QStandardItemModel

from velat.base import Person


class PersonItem(QStandardItem):
    def __init__(self, person, column):
        if column == 0:
            text = person.name
        elif column == 1:
            text = person.information
        elif column == 2:
            text = str(person.totalowed)
        elif column == 3:
            text = str(person.totalpaid)
        else:
            raise ValueError(str(column))
        QStandardItem.__init__(self, text)

        self._person = person
        self._column = column

    def setData(self, value, role):
        if role == Qt.EditRole:
            text = unicode(value.toString()).strip()
            if self._column == 0:
                # FIXME: can lead to duplicate names
                self._person.name = text
            if self._column == 1:
                self._person.information = text
        return QStandardItem.setData(self, value, role)

    
class PersonsModel(QStandardItemModel):
    def __init__(self, velat, parent=None):
        QStandardItemModel.__init__(self, parent)
        self.setHorizontalHeaderLabels(Person.SECTIONS)
        self._velat = velat
        self._persons = velat.persons

    def new_person(self, widget):
        """
        widget: needed to display question in front of it
        """
        loop_ok = False
        dial_msg = None
        proposition = ""

        while not loop_ok:

            if not dial_msg:
                dial_msg = "Enter a name for a new person"
            
            name, dial_ok = QInputDialog.getText(widget, "New person", dial_msg,
                    text=proposition)

            if not dial_ok:
                # user cancelled
                return

            name = unicode(name).strip()

            if not name:
                dial_msg = "Please enter a valid name (empty values are refused)"
                proposition = ""
                continue

            try:
                person = self._velat.add_person(name)
            except ValueError:
                dial_msg = "Error: name '%s' is already in use, try another" % name
                proposition = "%s bis" % name
                continue
            loop_ok = True
        # take person in account in this model
        row = list(PersonItem(person, index) 
            for index, value in enumerate(Person.SECTIONS))
        self.appendRow(row)


class ExpenseItem(QStandardItem):
    def __init__(self, expense, column):
        if column == 0:
            text = expense.name
        QStandardItem.__init__(self, text)
