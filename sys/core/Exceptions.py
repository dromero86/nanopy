# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")

import os

class Exceptions(Exception): 
    
    def show_error(self,heading, message, template = 'error_general', status_code = 500):
        message = ( "\n".join(message) if( isinstance(message, list) ) else message )
        filestream = open( nano.pathify("app.errors."+template) ).read()
        filestream = filestream.replace("{message}",message )
        filestream = filestream.replace("{heading}",heading )
        return filestream
        
    def show_python_error(self,severity, message, filepath, line):
        filestream = open( nano.pathify("app.errors.error_python") ).read()
        filestream = filestream.replace("{severity}",severity )
        filestream = filestream.replace("{message}",message )
        filestream = filestream.replace("{filepath}",filepath )
        filestream = filestream.replace("{line}",line )
        return filestream
        
    def show_404(self,page=''):
        heading = "404 "+page+" Not Found"
        message = "The page you requested ( "+page+" ) was not found."
        print self.show_error(heading, message, 'error_404', 404)
