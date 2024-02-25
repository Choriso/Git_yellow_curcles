import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Желтые окружности")
        self.button.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(Qt.yellow))
        for circle in self.circles:
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
