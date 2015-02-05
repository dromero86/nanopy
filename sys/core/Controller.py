# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")

class Controller():
    
    instance = None
    
    def __init__(self):
        
        self.instance = self
        
        include("sys.core.Loader")
        self.load = Loader()
        
    
    def get_instance(self):
        
        return self.instance    

#GLOBAL FUNCTION
get_instance = Controller.get_instance
