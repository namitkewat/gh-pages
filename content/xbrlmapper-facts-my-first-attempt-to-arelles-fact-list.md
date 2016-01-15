Title: xbrlMapper- "Facts": my first attempt to Arelle's Fact-List
Date: 2012-09-17 00:54
Author: namitkewat
Category: XBRL
Tags: arelle, python xbrl, xbrl instance facts, xbrlMapper
Slug: xbrlmapper-facts-my-first-attempt-to-arelles-fact-list
Status: published

I was just thinking that what i can do with my [xbrlMapper
module](http://namitkewat.wordpress.com/2012/08/16/xbrlmapper-pythonic-library-for-xbrlxml-analytics/ "xbrlMapper"),
so i thought lets try to make something  like arelle's fact-list(3rd and
last image of this post; 'www.arelle.org").

I have extended my present library; added new method "reportGen"; a
methods with returns dicts of instance document's facts; and i really
love dicts; specially after watching pycon-2010 talk on dict "[The
Mighty
Dictionary](http://blip.tv/pycon-us-videos-2009-2010-2011/pycon-2010-the-mighty-dictionary-55-3352147 "The Mighty Dictionary")".

See the snaps i am uploading to this post. Though the speed of process
is fast but i am not satisfied because if it now takes 2.5sec for one
xbrl package then how much time it will take for 20,000 xbrl
packages!!!!

You know when i have started working on this , it has taken 71 seconds
in first attempt(in evening of day one), it was like i am in stone-age
 \#\$@\#\^@%\#&.  
So i have decided to improve it, then 25 sec, 20 sec(7 PM.. .of day
one) then 35 sec- 40 sec(11 PM.. day 1).. .lollzz.. that evening was
very funny, all time it was moving around 30 seconds!!! and then
suddenly 9.5 sec(at 00:30AM of day2), and then 4.5 sec(aaa...5:30AM day
2), then finally its near 2-2.5 sec(..day 2..7:30AM.. then i left it
because i have to go to my office), but my intuition is telling me that
we can reduce it even further.

[gallery link="file" columns="2"]

Here in fist image; its snap-shot of Arelle's fact-list, in
second  shows amount of python code i have to write to achieve this, and
finally in last image... final output, its a sqlite db view in firefox
plugin.
