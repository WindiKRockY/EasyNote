from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_main_w

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_main_w()
        self.ui.setupUi(self)
        self.notes = {
            "First note":{
                "Text" : "It's first text ",
                "Tegs":[]
            }
        }
        self.ui.list_wid.addItems(self.notes)
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
