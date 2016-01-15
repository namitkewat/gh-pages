Title: Solution of "Can't turn on Web sharing on Mac OSX LION!"
Date: 2012-02-05 13:22
Author: namitkewat
Category: General
Tags: Apache, mac os x, osx-lion, web sharing
Slug: solution-of-cant-turn-on-web-sharing-on-mac-osx-lion
Status: published

I have upgraded my macbook from snow leopard to lion. I have to test
some python-cgi, for that i want to use native apache that i shipped
with mac operating system. But when i click the checkbox to turn it on
it displays a dash in the checkbox, changes from 'Off' to 'starting...',
and the gray indicator turns orange. This lasts for about a second then
it turns off again.

I went on google to find some idea! After two days of research i didn't
get anything. I have decided to revert back to snow leapard due to such
frustration.

But then i got the solution.  
As you can see in the screenshot of my terminal;

When i did "sudo apachectl --help"  
it comes as follow:  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
dyld: Library not loaded: /usr/lib/libpq.5.dylib  
Referenced from: /usr/sbin/httpd  
Reason: image not found  
/usr/sbin/apachectl: line 90: 1338 Trace/BPT trap: 5 \$HTTPD \$ARGV  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

so i went inside of the /usr/sbin and executed httpd in terminal,from
here it become clear that "libpq.5.dylib" is not there. So i went inside
/usr/lib/ to see which one i have. I found that "libpq.5.3.dylib" is
there. And this is what i am looking for.

Even i have tried to replace it with back-up "libpq.5.dylib.backup", but
again it was not there. At-last i have created a symbolic link from
"/usr/lib/libpq.5.3.dylib" to "/usr/lib/libpq.5.dylib":

"sudo ln -s /usr/lib/libpq.5.3.dylib /usr/lib/libpq.5.dylib"

Now go back to System preferences -\> Sharing -\> click on the "Web
sharing"

After few tapping on the same location it turns on, and
"http://localhost/" displays "It Works!" :)

[![screenshot of
terminal.](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-05-at-12-30-30-pm.png "Screen Shot 2012-02-05 at 12.30.30 PM")](http://namitkewat.files.wordpress.com/2012/02/screen-shot-2012-02-05-at-12-30-30-pm.png)

Some useful links from where i got solution:

<https://discussions.apple.com/thread/3190598?start=0&tstart=0>

<http://www.jonathandean.com/2011/08/postgresql-8-4-on-mac-os-x-10-7-lion/>

<http://superuser.com/questions/352005/os-x-lion-web-sharing-cant-start>
