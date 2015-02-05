# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")

#Sample using pyside as front-end
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView

class index(Controller):

    def index(self):   
        # Create Qt application and the QDeclarative view
        app = QApplication(sys.argv)
        view = QDeclarativeView() 
        # Create an URL to the QML file
        url = QUrl(self.load.qml('vista'))
        # Set the QML file and show
        view.setSource(url)
        view.show()
        app.exec_()
        
