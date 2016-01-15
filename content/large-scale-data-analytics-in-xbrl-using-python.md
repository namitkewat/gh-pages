Title: Large scale data analytics in XBRL using python
Date: 2012-11-20 23:52
Author: namitkewat
Category: XBRL
Tags: financial ratios, python, python xbrl, sec fillings, xbrl analytics
Slug: large-scale-data-analytics-in-xbrl-using-python
Status: published

Hello all,

Just now i am completing my 8 months old experiment. It was to develop
something with use of XBRL which can reduce the dependency on financial
information which are processed by 3rd party.

I mean that the current dependency on Yahoo finance/Bloomberg/Google
Finance/9W search/i-metrix\_edgar-online/.. . etc for the financial
information should not be there.

I am working as financial analyst doing XBRL tagging/verification/QC of
financial information.

I thought if we can tag this information then we can use it for
analytics purpose.

So lets build it. And now its almost done. I have just run my program on
200 companies and it took only 20-25 min to analyze them.  
You can see the output in the link given below. Its for 200 SEC's
filling. (Not for entire quater; because it took me 3 hours to download
them and just 20-25min to analyze them).

[Download 200 filling's
analysed Data](https://docs.google.com/open?id=0B_1SHAnqrt8TMHdxMG1oVmstNTA "Download 200 filling's data")

I am covering 21 main financial ratios; and around 20-21 financial
facts.

Ratios are also covered for dimension's case.  
For example company "OPLINK COMMUNICATIONS INC (0001022225)"'s "Fixed
turnover ratio" for "UnitedStatesMember" is "10.7756" while
"ChinaMember" has "1.2279" for period of 2011-07-04/2012-07-01.

You can see the how much detail can be pulled out if XBRL document is
well formed.

There was a time when it was taking more than 3 hours for 10% of current
task. And at present it was just 20-25 mins on my Intel core2 duo/2GB
RAM. Even then my instinct tells me that it can go down further.

Well to do that; i am really thankful of "Python". It was great
experience for me. Entire coding was done in python only.  
I hope what python has given in field of Genome sequencing/Astronomy/
and Physics will be repeated in finance as well.

Scope of such program is in big data centers to small investors; like
stock-exchange,financial information site like google-finance where
authorities has to perform custom/personalized calculations on the
financial data; also end user like you and me.

If you have more formulas to include that can be easily calculated from
XBRL then please mention it as a comment below;

For more detailed study download this text file which contains the
analysis of Google's and 3M's filling by my program: [Google and
3M](https://docs.google.com/open?id=0B_1SHAnqrt8TV0llSTFrelZmUk0 "Google and 3M")

Any query regarding my development; then email me at
"namitkewat@gmail.com"

and any suggestion for current work??
