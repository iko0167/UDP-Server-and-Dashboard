import socket
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QLineEdit, QPushButton

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.line_edit = QLineEdit(self)
        self.line_edit.move(0, 0)
        self.send_button = QPushButton("Send", self)
        self.send_button.move(0, 30)
        self.send_button.clicked.connect(self.send_message)

    def send_message(self):
        message = self.line_edit.text().encode()
        self.client.sendto(message, ("127.0.0.1", 20001))
        self.line_edit.clear()

app = QApplication(sys.argv)
window = ClientWindow()
window.show()
sys.exit(app.exec_())