Title: Solution of "Could not Find any X11 fonts, check that Font path is correct" while working with "R-statistics" and "Python-rpy2" on MAC LION 10.7.2
Date: 2012-02-13 21:00
Author: namitkewat
Category: General
Tags: bashrc, Could not Find any X11 fonts, python, R, R Foundation for Statistical Computing, rpy, rpy2 and python, X11, x11 fonts
Slug: solution-of-could-not-find-any-x11-fonts-check-that-font-path-is-correct-working-with-r-statistics-and-python-rpy2
Status: published

Such kind of error i got while i want to get some graphics using python
and rpy on Mac LION 10.7.2.  
After some google i got the solution, but that search was very tedious,
so i decided to simplified the whole procedure. Below is the solution
for that.

First check where our problem is located. When you give command like
'xeyes" in your terminal, it open eyes, that means X11 is there.  
Now in your "R" GUI or from your terminal interface give sample task,
it can be "plot(1,1)".  
Here i can see the same error which i am getting in python
intrepretor,  
its  
"Could not find any X11 fonts  
check that Font path is correct"

Then in your R, given another command like "sessionInfo()".  
You can see both of above command in pic given below.

[![](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-13-at-7-41-04-pm.png "Screen Shot 2012-02-13 at 7.41.04 PM")](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-13-at-7-41-04-pm.png)

In "sessionInfo()" you can see that in "Local" fonts are mentioned but
this list in incomplete.

So here we got the troubled part and by fixing this point our problem is
solved.

For that open "etc/bashrc" and add the following lines which is
mentioned below the line "Setting for the new UTF-8 terminal support in
Lion" as in pic below.  
These two lines are:  
export LC\_CTYPE=en\_US.UTF-8  
export LC\_ALL=en\_US.UTF-8

Save the changes, and restart it!

[![](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-13-at-7-42-05-pm.png "Screen Shot 2012-02-13 at 7.42.05 PM")](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-13-at-7-42-05-pm.png)

[![](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-13-at-7-41-45-pm.png "Screen Shot 2012-02-13 at 7.41.45 PM")](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-13-at-7-41-45-pm.png)

After new logging, give "sessionInfo()" command in your R, You can see
in missing fonts are there, and for simple ploting of "plot(1,1)" gives
desired output.

[![](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-13-at-8-51-51-pm.png "Screen Shot 2012-02-13 at 8.51.51 PM")](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-13-at-8-51-51-pm.png)
