import socket
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.client.bind(("127.0.0.1", 20001))
        self.client.setblocking(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.receive_message)
        self.timer.start(100)
    
    def receive_message(self):
        try:
            message, address = self.client.recvfrom(1024)
            self.text_edit.append(message.decode())
        except:
            pass

app = QApplication(sys.argv)
window = ClientWindow()
window.show()
sys.exit(app.exec_())
ğ