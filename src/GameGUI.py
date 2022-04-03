from GameManager import *
from PyQt5.Qt import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget

MENU_WIDTH = 0
PANEL_XPOS = 500
PANEL_YPOS = 300
SIM_SPEED = 100
START_SIZE = 25
TILE_SIZE = 25

class GameGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.x = START_SIZE
        self.y = START_SIZE
        self.manager = GameManager(self.x, self.y)
        self.setDimensions()
        self.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(SIM_SPEED)

    def setDimensions(self):
        self.width = TILE_SIZE*self.x + MENU_WIDTH
        self.height = TILE_SIZE*self.y
        self.setWindowTitle("Snake")
        self.setGeometry(PANEL_XPOS, PANEL_YPOS, self.width, self.height)

    def paintEvent(self, event):
        qp = QPainter(self)
        for x in range (0, self.x):
            for y in range(0, self.y):
                if self.manager.snake.contains(x, y):
                    qp.fillRect(x*TILE_SIZE, y*TILE_SIZE,TILE_SIZE, TILE_SIZE, QColor('yellow'))
                elif (x, y) == self.manager.food:
                    qp.fillRect(x*TILE_SIZE, y*TILE_SIZE,TILE_SIZE, TILE_SIZE, QColor('blue'))
                elif (x % 2 == 1) ^ (y % 2 == 1):
                    qp.fillRect(x*TILE_SIZE, y*TILE_SIZE,TILE_SIZE, TILE_SIZE, QColor('dark green'))
                else:
                    qp.fillRect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE, QColor('green'))

    def keyPressEvent(self, e):
        if (e.key() == Qt.Key_W) or (e.key() == Qt.Key_Up):
            self.manager.direction = 'NORTH'
        elif (e.key() == Qt.Key_S) or (e.key() == Qt.Key_Down):
            self.manager.direction = 'SOUTH'
        elif (e.key() == Qt.Key_D) or (e.key() == Qt.Key_Right):
            self.manager.direction = 'EAST'
        elif (e.key() == Qt.Key_A) or (e.key() == Qt.Key_Left):
            self.manager.direction = 'WEST'

    def tick(self):
        self.manager.update()
        self.update()

