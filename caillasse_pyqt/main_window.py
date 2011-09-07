from PyQt4.QtGui import QMainWindow

from .ui_wrapper import ui_wrapper
from .main_window_ui import Ui_caillasse


WINDOW = ui_wrapper("Caillasse", Ui_caillasse, QMainWindow)
