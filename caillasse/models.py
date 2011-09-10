from PyQt4.QtGui import QDialog

from velat.base import Expense, Person, Transfer

from .model_base import CaillasseModel
from .new_transfer_ui import Ui_new_transfer


class PersonsModel(CaillasseModel):
    def __init__(self, velat, parent=None):
        CaillasseModel.__init__(self, velat, Person.SECTIONS, parent)
        self._new_item_name = "this new person"
        self._new_item_title = "New person"

    def _backend_valider(self, name):
        person = None
        dial_msg = None
        proposition = None
        try:
            person = self._velat.add_person(name)
        except ValueError:
            dial_msg = "Error: name '%s' is already in use, try another" % name
            proposition = "%s bis" % name
        return person, dial_msg, proposition


class ExpensesModel(CaillasseModel):
    def __init__(self, velat, parent=None):
        CaillasseModel.__init__(self, velat, Expense.SECTIONS, parent)
        self._new_item_name = "this new expense"
        self._new_item_title = "New expense"

    def _backend_valider(self, name):
        expense = None
        dial_msg = None
        proposition = None
        try:
            expense = self._velat.add_expense(name)
        except ValueError:
            dial_msg = "Error: name '%s' is already in use, try another" % name
            proposition = "%s bis" % name
        return expense, dial_msg, proposition

class TransfersModel(CaillasseModel):
    def __init__(self, velat, parent=None):
        CaillasseModel.__init__(self, velat, Transfer.SECTIONS, parent)

    def _backend_valider(self, name):
        expense = None
        dial_msg = None
        proposition = None
        try:
            expense = self._velat.add_expense(name)
        except ValueError:
            dial_msg = "Error: name '%s' is already in use, try another" % name
            proposition = "%s bis" % name
        return expense, dial_msg, proposition

    def new_item(self, widget, persons_model):
        dialog = QDialog(widget)
        ui = Ui_new_transfer()
        ui.setupUi(dialog)
        combos = ui.combo_giver, ui.combo_receiver
        for combo in combos:
            combo.setModel(persons_model)
            # combo.setModelColumn(0)
        if not dialog.exec_():
            return

        giver, receiver = (self._velat.persons[combo.currentIndex()]
            for combo in combos)
        amount = ui.spin_amount.value()
        context = unicode(ui.text_context.toPlainText()).strip()

        transfer = self._velat.add_transfer(giver, receiver, amount, context)

        self._add_to_model(transfer)
