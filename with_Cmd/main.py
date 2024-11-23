import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QFont, QIcon


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TesT APP")
        self.setGeometry(300, 300, 400, 300)

        # Layout
        self.setLayout(qtw.QVBoxLayout())
        my_label = qtw.QLabel("Pick something from the list below!")
        my_label.setFont(QFont("Arial", 16))
        # Add item to layout
        self.layout().addWidget(my_label, alignment=Qt.AlignCenter)

        """ my_entry = qtw.QLineEdit()
        my_entry.setPlaceholderText("Enter Something...")
        my_entry.setFixedWidth(200)
        my_entry.setObjectName("name")
        # Add item to layout
        self.layout().addWidget(my_entry, alignment=Qt.AlignCenter) """
        """ cmb_box = qtw.QComboBox(self, editable=True,
                                insertPolicy=qtw.QCheckBox.insertAction)
        cmb_box.addItem("Doner", "something")
        cmb_box.addItem("Pide", 2)
        cmb_box.addItem("Lahmacun", 3)
        cmb_box.addItem("Çorba")
        cmb_box.addItem("Ayran")
        cmb_box.addItem("Sütlaç")
        cmb_box.addItem("Köfte")
        cmb_box.addItems(["one", "two"])
        cmb_box.setStyleSheet("QComboBox {width:200px;}")
        # Add item to layout
        self.layout().addWidget(cmb_box, alignment=Qt.AlignCenter) """
        """ spn_box = qtw.QSpinBox(
            self, value=10, maximum=100, minimum=0, singleStep=5, prefix="#", suffix=" Order")
        spn_box.setFont(QFont("Helvetica", 15))
        spn_box.setStyleSheet("QSpinBox {width:200px;}")
        # Add item to layout
        self.layout().addWidget(spn_box, alignment=Qt.AlignCenter) """
        text_box = qtw.QTextEdit(
            self, lineWrapColumnOrWidth=50, placeholderText="This is a text box")

        self.layout().addWidget(text_box, alignment=Qt.AlignCenter)
        my_button = qtw.QPushButton("Submit", clicked=lambda: press_it())
        my_button.setStyleSheet(
            "QPushButton {font-weight: bold; padding: 10px 20px; background-color: #333; color: #fff; border: none; border-radius:5px} QPushButton:hover {background-color: #666;}"
        )
        my_button.setCursor(Qt.PointingHandCursor)
        # Add item to layout
        self.layout().addWidget(my_button, alignment=Qt.AlignCenter)

        self.show()

        """ def press_it():
            # cmb_box.currentData(), cmb_box.currentIndex() etc can be selected
            my_label.setText(f"You picked {cmb_box.currentText()}")"""
        """ def press_it():
            # cmb_box.currentData(), cmb_box.currentIndex() etc can be selected
            my_label.setText(f"You picked {spn_box.value()}") """

        def press_it():
            # cmb_box.currentData(), cmb_box.currentIndex() etc can be selected
            my_label.setText(f"You picked {text_box.toPlainText()}")


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
