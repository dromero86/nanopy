# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")

class data(Model):
    def test_mysql(self):
        for row in self.db.query("SELECT id,nombre FROM hal_usuarios") :
			#echo a test
			print row.id, row.nombre
