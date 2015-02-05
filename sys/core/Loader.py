# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")

import os

class Loader():

    def ui(self, module):
        return nano.pathify("app.view.").replace(".py","") + module + ".ui"

    def qml(self, module):
        return nano.pathify("app.view.").replace(".py","") + module + ".qml"
        
    def view(self,module):
        view = ""
        if(  os.path.isfile( nano.pathify("app.view." + module ) ) != True ):
            print "Error: View "+module+" not found"
        else:
            view = open( nano.pathify("app.view." + module ) ).read()
        
        return view    
             
    def model(self,module):
        if(  os.path.isfile( nano.pathify("app.model." + module ) ) != True ):
            print "Error: View "+module+" not found"
        else:
            include("app.model." + module )
            #eval( "self."+ module +" = "+ module +"()")
