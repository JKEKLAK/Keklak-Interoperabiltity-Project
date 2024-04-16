#Jared Keklak INFO 762 Dr.Walters API Project
#basic GUI class, meant to provide easy access to functions of the app, extremely unfinished.
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QLineEdit, QPlainTextEdit
import INFOproj_GLOBALS as G

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(G.window_title)

        self.setFixedWidth(G.window_width)
        self.setFixedHeight(G.window_height)

        # Create textbox
        textbox = QPlainTextEdit(self)
        textbox.move(G.main_window_textbox_x, G.main_window_textbox_y)
        textbox.resize(G.main_window_textbox_size1, G.main_window_textbox_size2)
        textbox.setReadOnly(True)

        widget = QWidget()

        ID_Cat = QPushButton(widget)
        ID_Cat.setText("ID Cat")
        ID_Cat.move(G.button_x_position, G.button_y_position+32)
        ID_Cat.clicked.connect(id_cat_button_clicked)

        Get_Cat_Facts = QPushButton(widget)
        Get_Cat_Facts.setText("Get Cat Facts")
        Get_Cat_Facts.move(G.button_x_position, G.button_y_position+64)
        Get_Cat_Facts.clicked.connect(get_cat_facts_button_clicked)

        Get_Youtube_Videos = QPushButton(widget)
        Get_Youtube_Videos.setText("Search Youtube")
        Get_Youtube_Videos.move(G.button_x_position, G.button_y_position+96)
        Get_Youtube_Videos.clicked.connect(get_youtube_videos_clicked)


        self.setCentralWidget(widget)
        #self.setCentralWidget(console)
        self.show()



def id_cat_button_clicked(textbox):
    print("id cat button was clicked")


def get_cat_facts_button_clicked():
    print("get cat facts button was clicked")

def get_youtube_videos_clicked():
    print("youtube video button was clicked")

