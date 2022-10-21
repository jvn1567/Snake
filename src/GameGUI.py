from GameManager import *
from PyQt5.Qt import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget

MENU_HEIGHT = 50
PANEL_XPOS = 500
PANEL_YPOS = 300
SIM_SPEED = 100
START_SIZE = 20
TILE_SIZE = 25

class GameGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.x = START_SIZE
        self.y = START_SIZE
        self.manager = GameManager(self.x, self.y)
        self.setDimensions()
        self.setMenu()
        self.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(SIM_SPEED)

    def setDimensions(self):
        self.width = TILE_SIZE*self.x
        self.height = TILE_SIZE*self.y + MENU_HEIGHT
        self.setWindowTitle("Snake")
        self.setGeometry(PANEL_XPOS, PANEL_YPOS, self.width, self.height)

    def setMenu(self):
        mainLayout = QVBoxLayout()
        spacer = QVBoxLayout()
        spacer.addStretch(1)
        menuLayout = QHBoxLayout()
        message = 'Welcome to Snake! Use WASD to move.'
        menuLayout.addWidget(QLabel(message))
        btnPause = QPushButton('Pause (E)', self)
        btnPause.clicked.connect(self.pause)
        menuLayout.addWidget(btnPause)
        btnReset = QPushButton('Reset (R)', self)
        btnReset.clicked.connect(self.reset)
        menuLayout.addWidget(btnReset)
        mainLayout.addLayout(spacer)
        mainLayout.addLayout(menuLayout)
        self.setLayout(mainLayout)

    def paintEvent(self, event):
        qp = QPainter(self)
        for x in range (0, self.x):
            for y in range(0, self.y):
                if self.manager.snake.contains(x, y):
                    color = QColor('yellow')
                    if self.manager.gameOver:
                        color = QColor('red')
                    qp.fillRect(x*TILE_SIZE, y*TILE_SIZE,TILE_SIZE, TILE_SIZE, color)
                elif (x, y) == self.manager.food:
                    qp.fillRect(x*TILE_SIZE, y*TILE_SIZE,TILE_SIZE, TILE_SIZE, QColor('blue'))
                elif (x % 2 == 1) ^ (y % 2 == 1):
                    qp.fillRect(x*TILE_SIZE, y*TILE_SIZE,TILE_SIZE, TILE_SIZE, QColor('dark green'))
                else:
                    qp.fillRect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE, QColor('green'))

    def keyPressEvent(self, e):
        if (e.key() == Qt.Key_E):
            self.pause()
        elif (e.key() == Qt.Key_R):
            self.reset()
        if not self.manager.paused:
            prev = self.manager.prevDirection
            if (e.key() == Qt.Key_W) and prev != 'SOUTH':
                self.manager.direction = 'NORTH'
            elif (e.key() == Qt.Key_S) and prev != 'NORTH':
                self.manager.direction = 'SOUTH'
            elif (e.key() == Qt.Key_D) and prev != 'WEST':
                self.manager.direction = 'EAST'
            elif (e.key() == Qt.Key_A) and prev != 'EAST':
                self.manager.direction = 'WEST'

    def pause(self):
        self.manager.paused = not self.manager.paused
        if self.manager.paused:
            self.timer.stop()
        else:
            self.timer.start(SIM_SPEED)

    def reset(self):
        self.manager.reset(self.x, self.y)
        self.update()


    def tick(self):
        if not self.manager.paused and not self.manager.gameOver:
            self.manager.update()
            self.update()

