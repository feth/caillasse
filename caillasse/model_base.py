from PyQt4.QtCore import Qt
from PyQt4.QtGui import QInputDialog, QStandardItem, QStandardItemModel


class CaillasseItem(QStandardItem):
    def __init__(self, thing, column, editable):
        QStandardItem.__init__(self, str(thing.get_by_col(column)))
        self._column = column
        self._editable = editable
        self._thing = thing

    def setData(self, value, role):
        if role == Qt.EditRole:
            text = unicode(value.toString()).strip()
            self._thing.set_by_col(self._column, text)
        return QStandardItem.setData(self, value, role)

    def flags(self):
        if self._editable:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        return Qt.ItemIsEnabled


class CaillasseModel(QStandardItemModel):
    def __init__(self, velat, sections, parent=None):
        QStandardItemModel.__init__(self, parent)
        self.setHorizontalHeaderLabels([value[0] for value in sections])
        self._velat = velat
        self._sections = sections
        self._new_item_name = "this new item"
        self._new_item_title = "New item"

    def new_item(self, widget):
        loop_ok = False
        dial_msg = None
        proposition = ""

        while not loop_ok:

            if not dial_msg:
                dial_msg = "Enter a name for %s" % self._new_item_name
            
            name, dial_ok = QInputDialog.getText(widget, self._new_item_title, 
                    dial_msg, text=proposition)

            if not dial_ok:
                # user cancelled
                return

            name = unicode(name).strip()

            if not name:
                dial_msg = "Please enter a valid name (empty values are refused)"
                proposition = ""
                continue

            item, dial_msg, proposition = self._backend_valider(name)

            if item:
                loop_ok = True

        self._add_to_model(item)

    def _add_to_model(self, item):
        # take item in account in this model
        row = list(CaillasseItem(item, index, value[1]) # value[1]: editable? bool
            for index, value in enumerate(self._sections))
        self.appendRow(row)

    def _backend_valider(self, name):
        """
        return item , dial_msg, proposition
        if item is None, dial_msg and proposition are strings used to ask user again.
        """
        raise NotImplementedError("Please implement _backend_valider() that must"
        "interact with the backend or implement _new_item")

    def flags(self, index):
        return self.itemFromIndex(index).flags()
