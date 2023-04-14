

import requests
import datetime
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox
from PyQt5.QtGui import QFont, QTextCursor


version = "1.2"
class ProxyList:
    def __init__(self, api_key, mode):
        self.api_key = api_key
        self.mode = mode
        self.url = f"https://api.proxylist.to/{mode}?key={api_key}"
        self.proxy_list = []

    def fetch_proxies(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.proxy_list = response.text.split("\n")


class ProxyToolGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.api_key = ""
        self.mode = ""
        self.proxy_list = []
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 340, 360)
        # Create labels and line edits for API key input
        api_key_label = QLabel("API Key:")
        self.api_key_line_edit = QLineEdit()

        # Create label and combo box for proxy type selection
        mode_label = QLabel("Proxy Type:")
        self.mode_combo_box = QComboBox()
        self.mode_combo_box.addItem("http")
        self.mode_combo_box.addItem("socks4")
        self.mode_combo_box.addItem("socks5")

        # Create generate button
        generate_button = QPushButton("Generate Proxies")
        generate_button.clicked.connect(self.generate_proxies)

        # Create text area to display generated proxies
        self.proxy_text_area = QTextEdit()
        self.proxy_text_area.setFont(QFont('Courier New'))



        a="""

     ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀▀▀▄   
    ▐ ▄▀   █ █   █  █  █         
      █▄▄▄▀  ▐   █  ▐  █    ▀▄▄  
      █   █      █     █     █ █ 
     ▄▀▄▄▄▀   ▄▀▀▀▀▀▄  ▐▀▄▄▄▄▀ ▐ 
    █    ▐   █       █ ▐         
    ▐        ▐       ▐
DC:BiG#0627
GitHub:github.com/ysf72byk
                    """
        self.proxy_text_area.insertPlainText(a)
        ##        self.proxy_text_area.insertPlainText("Coder :BiG\nGitHub:github.com/ysf72byk\nDC:BiG#0627")

        # Create vertical layout and add all widgets
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(api_key_label)
        hbox1.addWidget(self.api_key_line_edit)
        vbox.addLayout(hbox1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(mode_label)
        hbox2.addWidget(self.mode_combo_box)
        vbox.addLayout(hbox2)
        vbox.addWidget(generate_button)
        vbox.addWidget(self.proxy_text_area)

        self.setLayout(vbox)
        self.setWindowTitle('Proxy Scraper [v1.1]    by BiG')
        self.show()

    def generate_proxies(self):
        # Get API key and proxy type from user
        self.api_key = self.api_key_line_edit.text()
        self.mode = self.mode_combo_box.currentText()

        # Generate proxies using proxy tool code
        proxy_list = ProxyList(self.api_key, self.mode)
        proxy_list.fetch_proxies()
        self.proxy_list = proxy_list.proxy_list

        # Display generated proxies in text area
        if len(self.proxy_list) > 1:
            self.proxy_text_area.clear()
            self.proxy_text_area.insertPlainText(f"{self.mode.upper()} Proxies:\n")
            for proxy in self.proxy_list:
                self.proxy_text_area.insertPlainText(proxy + "\n")
        else:
            self.proxy_text_area.clear()
            self.proxy_text_area.insertPlainText(f"No {self.mode.upper()} Proxies found. Perhaps your API key ({self.api_key}) is incorrect\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProxyToolGUI()
    sys.exit(app.exec_())



