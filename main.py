import sys

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic, QtGui
import random


class Circle(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        x = random.randint(0, 450)
        y = random.randint(0, 390)
        d = random.randint(20, 100)
        self.circles.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(255, 255, 0)))
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0), 1))

        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())