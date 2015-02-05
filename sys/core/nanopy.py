# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")

import os

include("sys.core.Exceptions")

try:

    include("sys.core.Common")
    include("app.config.constants")
 
#set timeout - gui not relevant

#benchmark start  - mas adelante

#start hooks - post desarrollo

#pre system
    include("sys.core.Model")
#utf8 start

#uri core start

#router core start
    include("sys.core.Router")
    router = Router()
    _dir = router.fetch_directory()
    _cls = router.fetch_class()
    _mtd = router.fetch_method()

#output core start

#cache core start

#security core start

#lang core start

#load controller class

    include("sys.core.Controller") 

#analize request controller
# 1 - check file exist
# 2 - check class
# 3 - check method
# 4 - manage 404 errors 
    if(  os.path.isfile( nano.pathify("app.controller." + _cls ) ) != True ):
        print "Error 404 -  default contoller not found"
    else:
        include("app.controller." + _cls )

    NN = eval( _cls+"()")

    getattr(NN, _mtd)()

#load pre-controller class

#callback controller class

#benchmark end

#database close
except Exceptions as e:
    print e.show_error("A error in nanopy", "raise error in nano", 'error_general', 500)
