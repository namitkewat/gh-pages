Title: installing python3.3 on Ubuntu
Date: 2014-01-14 02:02
Author: namitkewat
Category: General
Slug: installing-python3-3-on-ubuntu
Status: published

my system is ubuntu 12.04 at Digital Ocean, and i am going to install
python3.3 and pip3.3

here are few simple steps with which you can do so!

\$ apt-get install python-software-properties  
\$ add-apt-repository ppa:fkrull/deadsnakes  
\$ apt-get update  
\$ apt-get install python3.3  
\$ curl http://python-distribute.org/distribute\_setup.py | python3.3  
\$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py |
python3.3

and yes. . don't forget to apply "sudo" above!!!

enjoy. .. 
