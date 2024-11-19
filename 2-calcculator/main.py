from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QVBoxLayout)


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator App')
        self.resize(250, 300)

        # Objects/Widgets
        self.text_box = QLineEdit()
        self.grid = QGridLayout()

        # Buttons
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]
        row = 0
        col = 0
        for button in self.buttons:
            button_obj = QPushButton(button)
            button_obj.clicked.connect(self.button_clicked)
            self.grid.addWidget(button_obj, row, col)
            col += 1
            if col == 4:
                col = 0
                row += 1

        self.clear = QPushButton('C')
        self.clear.clicked.connect(lambda: self.text_box.setText(''))
        self.delete = QPushButton('<-')
        self.delete.clicked.connect(lambda: self.text_box.backspace())

        # Design the calculator layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_box)
        main_layout.addLayout(self.grid)

        button_rows = QHBoxLayout()
        button_rows.addWidget(self.clear)
        button_rows.addWidget(self.delete)

        main_layout.addLayout(button_rows)

        self.setLayout(main_layout)

    def button_clicked(self):
        button = app.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.text_box.text())
                self.text_box.setText(str(result))
                self.text_box.setFocus()
            except ZeroDivisionError:
                self.text_box.setText('Error: Division by zero')
                self.text_box.setFocus()

        else:
            self.text_box.setText(self.text_box.text() + text)
            self.text_box.setFocus()


# Execute app
if __name__ == '__main__':
    app = QApplication([])
    main_window = CalculatorApp()
    main_window.show()
    app.exec_()
