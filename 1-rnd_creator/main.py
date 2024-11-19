from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

from utils.rnd_num_crtr import generate_random_word

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Random Number Generator')
main_window.resize(300, 200)

# Objects/Widgets
title = QLabel('Random Keywords')
text1 = QLabel('?')
text2 = QLabel('?')
text3 = QLabel('?')


button1 = QPushButton('Click Me!')
button2 = QPushButton('Click Me!')
button3 = QPushButton('Click Me!')

# Frame Layout
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Functions


def update_label1(result):
    text1.setText(result)


def update_label2(result):
    text2.setText(result)


def update_label3(result):
    text3.setText(result)


# Events
button1.clicked.connect(lambda: update_label1(generate_random_word()))
button2.clicked.connect(lambda: update_label2(generate_random_word()))
button3.clicked.connect(lambda: update_label3(generate_random_word()))

# Execute the application
main_window.show()
app.exec_()
