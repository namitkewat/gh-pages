Title: Processing files larger than RAM in python
Date: 2012-09-11 17:27
Author: namitkewat
Category: General
Tags: large files, mongo-db log reading, python, reading files larger than RAM in python
Slug: processing-files-larger-than-ram-in-python
Status: published

I got a log file of 131 GB from Mongo-DB that has been collected in last
6 months. So I just thought lets calculate the number of lines.

Here files size is greater than RAM, so after searching over internet; i
got solution on http://stackoverflow.com.

I have modified it a little bit! But work is
done.[![](http://namitkewat.files.wordpress.com/2012/09/131gb_logfile_code.jpg "python code for raeding 131GB logfile")](http://namitkewat.files.wordpress.com/2012/09/131gb_logfile_code.jpg)[![](http://namitkewat.files.wordpress.com/2012/09/131gb_output.jpg "131GB_output")](http://namitkewat.files.wordpress.com/2012/09/131gb_output.jpg)

It took around 75 min. and total number of lines was around 2.1 Billion.
