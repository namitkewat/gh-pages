Title: working with pypm/python in internet proxy on windows
Date: 2012-04-11 10:40
Author: namitkewat
Category: General
Tags: easy_install, internet proxy, pypm, python, windows
Slug: working-with-pypmpython-in-internet-proxy-on-windows
Status: published

Well guys,

Currently I am working on PC in my company's development center.Its an
Windows XP. This place is highly secured, you need to get all proxy
setting for your internet use.

I want to install few python packages with pypm, but in DOS prompt it is
not allowing me to do that.

So after little bit of google, i got the solution as below:

-**set HTTP\_PROXY=domain\\username:password@myproxy:myproxyport**

**example: set
http\_proxy=IND\\namit.kewat:xl123456@192.168.180.150:8880**

after that.. .pypm works fine!!!
