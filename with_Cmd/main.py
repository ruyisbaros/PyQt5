import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtGui import QFont, QIcon


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TesT APP")
        self.setGeometry(300, 300, 400, 300)

        # Layout
        self.setLayout(QVBoxLayout())
        my_label = QLabel("Welcome to TesT App!")
        my_label.setFont(QFont("Arial", 16))
        my_entry = QLineEdit()
        my_entry.setPlaceholderText("Enter Something...")
        my_entry.setFixedWidth(200)
        my_entry.setObjectName("name")
        my_button = QPushButton("Submit")
        my_button.setStyleSheet(
            "QPushButton {font-weight: bold; padding: 10px 20px; background-color: #333; color: #fff; border: none;} QPushButton:hover {background-color: #666;}"
        )
        my_button.setCursor(Qt.PointingHandCursor)

        self.layout().addWidget(my_label, alignment=Qt.AlignCenter)
        self.layout().addWidget(my_entry, alignment=Qt.AlignCenter)
        self.layout().addWidget(my_button, alignment=Qt.AlignCenter)

        self.show()


app = QApplication([])
mw = MainWindow()
app.exec_()
