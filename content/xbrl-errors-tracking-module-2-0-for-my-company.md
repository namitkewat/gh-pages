Title: XBRL Errors Tracking module 2.0 for my company
Date: 2012-05-16 11:38
Author: namitkewat
Category: XBRL
Tags: python-cgi, sqlite, xbrl errors
Slug: xbrl-errors-tracking-module-2-0-for-my-company
Status: published

I have updated my Errors tracking module. Its now "2.0"

It is Python-CGI working under Apache server. I have developed it in
spare time while working with Research and Development team at my
company [Aptara](http://www.aptaracorp.com "Aptara Corp").

In my previous release it was accepting only instance document every
time for all three test. Analyst have to upload instance document again
and again. It was time consuming and gives load on network and on server
too.

So in i have replace them all with single zip upload. Now analyst have
to upload xbrl zip package. Zipped XBRL package is relatively small in
size(about 1/10th of extracted content), so it will decrease the load on
network.

In back-end i am using SQLite database. SQlite is tiny, server-less
database. Few high-level SQL queries are not present in SQLite, but if i
require those functionality, then i am using python to solve them (Like
List-comprehensions).

Requirement of such tool is that, in my company we using
"<https://examiner.rrd.com>"  to find errors from XBRL package. But few
errors that are not tracked by it, but needed to be removed. So analyst
has to remove them for higher quality of xbrl package. On an average it
took 2-3 hrs to check such errors. But all such errors are make
available to analyst  in just matter of seconds with use of my tool.

[gallery link="file" columns="2"]

Here test 4 and test 5 are new. In test 4 we are finding elements whose
negated and signage needs to be checked. In test 4 it is showing those
elements from instance which are negative and doesn't have negated label
as pereferredLabel in presentation linkbase. So as you can see in
snap-shot it finds that element's value, its balance from company
schema/or from US-GAAP taxonomy (while confirming if is from 2009, 2011
or from 2012 UGT), its preferred label as well as its weight from
calculation linkbase.

In test 5, we are interested in checking various period type elements
and their value in instance.

-   xbrli:dateItemType
-   us-types:dateStringItemType
-   xbrli:dateTimeItemType
-   xbrli:durationItemType
-   us-types:durationStringItemType
-   xbrli:gDayItemType
-   xbrli:gMonthDayItemType
-   xbrli:gMonthItemType
-   xbrli:gYearItemType
-   xbrli:gYearMonthItemType
-   xbrli:timeItemType

So this is it.

This tool is working in all three production facilities (New Delhi,
Trivendrum, Pune).

Monthly statistics:

-   total hits is about 10000-30000
-   4000-8000 number of files uploaded
-   total size of files after extraction is 8GB+
-   total number of systems in intranet are about 300
-   total Time saving 1000hrs-2000hrs (Assumption: if it saves 2 hrs per
    file)

In the end; SQLite is great.

After seeing it working under such large work load, it creates a great
respect for this tiny database. That's why, i want to tell: "If i am not
using MongoDB then i am sure, i will using SQLite"
