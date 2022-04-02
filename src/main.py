import sys
from GameGUI import GameGUI
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GameGUI()
    sys.exit(app.exec_())