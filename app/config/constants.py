# -*- coding: utf-8 -*- 
import sys

if( ( 'nano' in globals() ) == False ):  sys.exit("No direct script access allowed")
 
FILE_READ_MODE = 0644
FILE_WRITE_MODE= 0666
DIR_READ_MODE  = 0755
DIR_WRITE_MODE = 0777

FOPEN_READ								='rb' 
FOPEN_READ_WRITE						='r+b' 
FOPEN_WRITE_CREATE_DESTRUCTIVE			='wb' # truncates existing file data, use with care
FOPEN_READ_WRITE_CREATE_DESTRUCTIVE		='w+b'# truncates existing file data, use with care
FOPEN_WRITE_CREATE						='ab' 
FOPEN_READ_WRITE_CREATE					='a+b' 
FOPEN_WRITE_CREATE_STRICT				='xb' 
FOPEN_READ_WRITE_CREATE_STRICT			='x+b'

APP_NAME = 'Nanopy'



