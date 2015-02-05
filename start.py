# -*- coding: utf-8 -*-
import os
import sys
import platform
import subprocess

"""
	Path -> 3 goal modes
    * SO compat
    * easy learning
    * easy writting
     
	2 - string notation path|to|file.py
	3 - array  ["path","to","file.py"]
	4 - seudo java import 
"""

class Nano:
    version = "1.0.0"
    python_version  = "2.7"
    file = ""
    dir  = ""
    so   = ""
    env  = "dev" #choose dev|test|prod 
    slash= "\\" 
    sysd = "sys"
    appd = "app"
    
    EXT  = ".py"
    BASE = ""
    
    include_stack = [] 
    
    def pathify(self, path):
        path = path.replace(self.sysd,self.SYSPATH) 
        path = path.replace(self.appd,self.APPPATH) 
        path = path.replace('.',self.slash) + self.EXT
        return path
     
    def include(self, path ):
        if( isinstance(path, str) ):
            path = self.pathify(path)
            
        filename = ( self.slash.join(path) if isinstance(path, list) else path )
        
        if os.path.exists(filename): 
            self.include_stack.append(filename) 
            execfile(filename,globals())  #, , locals() 
            

    def build(self):
        self.file = os.path.abspath(__file__)
        self.dir  = os.getcwd()
        self.so   = platform.system()
        self.BASEPATH = self.dir
        self.APPPATH  = self.dir + self.slash + self.appd
        self.SYSPATH  = self.dir + self.slash + self.sysd
        self.include_stack.append(self.file)

nano = Nano()
nano.build()

#Global function include
include = nano.include
pathify = nano.pathify

if __name__ == '__main__':
    include("sys.core.nanopy") 

#print "\n - ".join(nano.include_stack)
