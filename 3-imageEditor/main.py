import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton,
                             QVBoxLayout, QHBoxLayout, QVBoxLayout, QComboBox, QListWidget, QFileDialog)
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image, ImageFilter, ImageEnhance


app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('PhotoQT')
main_window.resize(900, 700)

# All app widgets/objects
btn_folder = QPushButton('Folder')
file_list = QListWidget()

btn_left = QPushButton('Left')
btn_right = QPushButton('Right')
mirror = QPushButton('Mirror')
sharpness = QPushButton('Sharpen')
contrast = QPushButton('Contrast')
gray = QPushButton('B/W')
blur = QPushButton('Blur')
saturation = QPushButton('Color')

# Dropdown box
filter_box = QComboBox()
filter_box.addItem('Orijinal')
filter_box.addItem('Left')
filter_box.addItem('Right')
filter_box.addItem('Mirror')
filter_box.addItem('Sharpen')
filter_box.addItem('B/W')
filter_box.addItem('Color')
filter_box.addItem('Contrast')
filter_box.addItem('Blur')

# Picturebox
picturebox = QLabel("Image will appear here")

# Layouts
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(contrast)
col1.addWidget(gray)
col1.addWidget(blur)
col1.addWidget(saturation)

col2.addWidget(picturebox)

master_layout.addLayout(col1, 20)
master_layout.addLayout(col2, 80)

main_window.setLayout(master_layout)

# All App events
working_directory = ""


def filter_(files, extensions):
    """Filter files by extension"""
    wrk_files = []
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                wrk_files.append(file)

    return wrk_files


def getWorkingDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory()
    extensions = ['.jpg', '.png', '.jpeg', '.svg']
    filenames = filter_(os.listdir(working_directory), extensions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)


btn_folder.clicked.connect(getWorkingDirectory)

# Execute
main_window.show()
app.exec_()
