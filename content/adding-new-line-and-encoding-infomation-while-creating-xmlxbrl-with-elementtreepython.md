Title: Adding new line and encoding infomation while creating XML/XBRL with ElementTree/Python
Date: 2012-07-10 17:12
Author: namitkewat
Category: XBRL
Tags: elementTree, ElementTree/Python, encoding, new line, ProcessingInstruction, python, xbrl, xbrl creation
Slug: adding-new-line-and-encoding-infomation-while-creating-xmlxbrl-with-elementtreepython
Status: published

I am making xbrl files with python ElementTree/python module. But there
is a problem while creating an xbrl file. It writes it into a single
line, which creates confusion a lot.

So i have tried to modified the native ElementTree class which writes a
xml  part. In windows it is located at the
"**C:\\Python27\\Lib\\xml\\etree\\ElementTree.py**" . In this file there
is a function named as **"\_serialize\_xml**";  and i have hacked it a
little bit. I have added a "\\n" where angle bracket of xml element is
defined. Screenshot for that is given
below.[![\_serialize\_xml](http://namitkewat.files.wordpress.com/2012/07/xbrl1.jpg "adding new line in xml while creating xml with ElementTree/python")](http://namitkewat.files.wordpress.com/2012/07/xbrl1.jpg)

So i got my output xbrl as follows.

[![xbrl
output](http://namitkewat.files.wordpress.com/2012/07/xbrl2.jpg "xbrl output")](http://namitkewat.files.wordpress.com/2012/07/xbrl2.jpg)Here
you can see that now my python script makes xbrl package as i have
wanted from it.  
Anyway, rest is i want to add encoding information to it, how?

Below is the solution,

**    \>\>\>ins\_out=open(instant\_filename,'wb',1000)**  

**    \>\>\>ElementTree.ElementTree(top).write(ins\_out,encoding="ASCII")**  
**    \>\>\>ins\_out.close()**

here "instant\_filename" is the output filename (example;
"htwr-20121231.xml") while  "top" is the root element below which i have
created my xml/xbrl file. Just add value of encoding to the instance
method "write" of ElementTree.ElementTree
