# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")

import os

def isset(variable):
    ret = variable in locals() or variable in globals()
    print variable, ret
    return ret

def is_python(version='2.7.5'):
    ret = False
    current= str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])
    print version,current
    if(version == current): 
        ret = True
    else:
        Sver = version.split('.') 
        if( int(sys.version_info[0]) <= int(Sver[0]) ): #major or equal 
            if( int(sys.version_info[1]) <= int(Sver[1]) ): #major or equal 
                if( int(sys.version_info[2]) <= int(Sver[2]) ): #major or equal
                   ret = True
    return ret

def show_error(message, status_code = 500, heading = 'An Error Was Encountered'):
    e = Exceptions()
    e.show_error(heading, message, 'error_general', status_code);
