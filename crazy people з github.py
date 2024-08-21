from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

win = QWidget()
win.setWindowTitle('визначити переможця')
win.move(100, 100)
win.resize(400, 200)

button = QPushButton('Згенерувати')
text = QLabel('Натисніть,')
text = QLabel('Натисніть, щоб дізнатися переможця')
num = QLabel('?')

