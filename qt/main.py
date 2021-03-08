import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('calculator')
        self.setLayout(qtw.QVBoxLayout())
        btn1 = qtw.QPushButton('test')
        self.layout().addWidget(btn1)

        self.keypad()
        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
