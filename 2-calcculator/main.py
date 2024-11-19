from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QVBoxLayout)

app = QApplication([])
# Main window
main_window = QWidget()
main_window.setWindowTitle('Calculator App')
main_window.resize(250, 300)


def button_clicked():
    button = app.sender()
    text = button.text()

    if text == '=':
        try:
            result = eval(text_box.text())
            text_box.setText(str(result))
            text_box.setFocus()
        except ZeroDivisionError:
            text_box.setText('Error: Division by zero')
            text_box.setFocus()

    else:
        text_box.setText(text_box.text() + text)
        text_box.setFocus()


# Objects/Widgets
text_box = QLineEdit()
grid = QGridLayout()

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

clear = QPushButton('C')
clear.clicked.connect(lambda: text_box.setText(''))
delete = QPushButton('<-')
delete.clicked.connect(lambda: text_box.backspace())

row = 0
col = 0
for button in buttons:
    button_obj = QPushButton(button)
    button_obj.clicked.connect(button_clicked)
    grid.addWidget(button_obj, row, col)
    col += 1
    if col == 4:
        col = 0
        row += 1

# Design the calculator layout
main_layout = QVBoxLayout()
main_layout.addWidget(text_box)
main_layout.addLayout(grid)

button_rows = QHBoxLayout()
button_rows.addWidget(clear)
button_rows.addWidget(delete)


main_layout.addLayout(button_rows)

main_window.setLayout(main_layout)

# Execute app
main_window.show()
app.exec_()
