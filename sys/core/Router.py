# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")

class Router:
    
    dir = ''
    cls = 'index'
    mtd = 'index'
    
    def fetch_directory(self):
        return self.dir
    
    def fetch_class(self):
        return self.cls
    
    def fetch_method(self):
        return self.mtd
