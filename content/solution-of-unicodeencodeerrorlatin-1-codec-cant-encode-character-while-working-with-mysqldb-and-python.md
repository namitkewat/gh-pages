Title: Solution of "UnicodeEncodeError:'latin-1' codec can't encode character ..." while working with MySQLdb and Python.
Date: 2012-03-28 18:07
Author: namitkewat
Category: General
Tags: mysql, mysqldb, python
Slug: solution-of-unicodeencodeerrorlatin-1-codec-cant-encode-character-while-working-with-mysqldb-and-python
Status: published

I got the error of "UnicodeEncodeError:'latin-1' codec can't encode
character ..." while i was inserting data into mysql with
MySQLdb/Python.

Below is the solution:

import MySQLdb as litefire  
conx = litefire.connect('127.0.0.1', 'root', '' , 'litefire2' );  
conx.set\_character\_set('utf8')  
conr=conx.cursor()  
conr.execute('SET NAMES utf8;')  
conr.execute('SET CHARACTER SET utf8;')  
conr.execute('SET character\_set\_connection=utf8;')

Enjoy,
