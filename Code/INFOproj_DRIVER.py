#Jared Keklak INFO 762 Dr.Walters API Project

import sys

from PyQt6.QtWidgets import QApplication

from INFOproj_GUI import MainWindow
#Driver Python Script for INFO 762 project

##integrate custom API
##integrate cat classifier
##integrate cat identifier
##integrate youtube API

app = QApplication(sys.argv)
w = MainWindow()
app.exec()