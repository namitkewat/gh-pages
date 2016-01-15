Title: Super-charging Python code with C-Extensions or Cython
Date: 2012-12-16 02:17
Author: namitkewat
Category: XBRL
Tags: Cython, financial analytics, python, xbrl
Slug: super-charging-python-code-with-c-extensions-or-cython
Status: published

Regarding my previous
[post](http://namitkewat.wordpress.com/2012/11/20/large-scale-data-analytics-in-xbrl-using-python/ "post")
that was Financial Analytics in XBRL was in pure-python with little bit
'C' touch (because of my base xml parsing lib is cElementTree). It was
taking 20-21 mins to process 200 xbrl packages.

But thats not the end; I have optimized it with
[Cython](http://cython.org/ "Cython"). Its a C-extensions in python,
giving multiple folds increase in the performance.  
I have just converted my raw module to '.so' and then imported it as
usual; and i found 25% reduction in time. Its now near 14-15min for the
same data set of 200 xbrl fillings.

See the screen-shot which i have just taken; 

[![Image](http://namitkewat.files.wordpress.com/2012/12/screen-shot-2012-12-16-at-1-12-53-am.png?w=580)](http://namitkewat.files.wordpress.com/2012/12/screen-shot-2012-12-16-at-1-12-53-am.png)  
 

Here i have not implemented any type declaration or typed arguments; and
yet i got 25% reduction in overall time. So you can imagine what will
happen when i will implement those changes.  
Anyway; 'C' rocks!!!!!
