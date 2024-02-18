import json
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
        self.ui.list_wid.itemClicked.connect(self.show_note)
        self.ui.savenote_btn.clicked.connect(self.save_note)

    def show_note(self):
        name = self.ui.list_wid.selectedItems()[0].text()
        self.ui.findnote_btn.setText(name)
        self.ui.note_wid.setText(self.notes[name]["Text"])


    def save_note(self):
        self.notes[self.ui.findnote_btn.text()]= self.ui.note_wid.toPlainText()
        with open("notes.json","w",encoding="utf-8") as file:
            json.dump(self.notes, file)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
