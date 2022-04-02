from PyQt5.QtWidgets import QWidget


MENU_WIDTH = 200
PANEL_XPOS = 500
PANEL_YPOS = 300
TILE_SIZE = 50

class GameGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 10
        self.set_dimensions();
        self.show()

    def set_dimensions(self):
        self.width = TILE_SIZE*self.x + MENU_WIDTH
        self.height = TILE_SIZE*self.y
        self.setWindowTitle("Snake")
        self.setGeometry(PANEL_XPOS, PANEL_YPOS, self.width, self.height)