Title: automating calucation of decimal value from scale for xbrl fact
Date: 2012-07-28 22:22
Author: namitkewat
Category: XBRL
Slug: automating-calucation-of-decimal-value-from-scale-for-xbrl-fact
Status: published

Today in office or currently in office; (both are right...)

i am making python script that can automate calculation of decimal value
from scale for various cases of xbrl instance facts.

Here below, i am giving my current output.

**(scale, excel value) (decimal, instance value)**

**(None, '2345') ('INF', '2345')**  
**('3', '439.10') (-1, '439100')**  
**('-4', '1789000') (4, '178.9')**  
**('-3', '0.006') (6, '0.000006')**  
**('0', '3987') (0, '3987')**  
**('0', '0.0660') (4, '0.066')**  
**('2', '100') (-2, '10000')**  
**('2', '100.0') (-1, '10000')**  
**('2', '100.00') (0, '10000')**  
**('3', '100.660') (0, '100660')**  
**('6', '2.5') (-5, '2500000')**  
**('6', '2.50') (-4, '2500000')**  
**('6', '2.500') (-3, '2500000')**  
**('6', '2.540') (-3, '2540000')**  
**('-1', '0.1') (2, '0.01')**  
**('-2', '0.12') (4, '0.0012')**  
**('-3', '0.123') (6, '0.000123')**  
**('9', '10.5') (-8, '10500000000')**  
**('9', '105') (-9, '105000000000')**  
**('0', '0.02') (2, '0.02')**  
**(None, '0.02') ('INF', '0.02')**

 

Here in 1st tuple(bracket); 1st value is the scale i am applying on cell
value on excel, and that value is on 2nd position of this tuple.

and in second bracket(tuple), its what the heading of this post.

1st value of second tuple is its decimal value, while 2nd value is the
value which i will send in instance document.

Well here i have also tried on negative scales as well.

It will remove the headache for analyst to worry about decimals (or
"precision"; what Bowne guys have on their "Bowne tagger") ; he/she has
to concern only about the scale value of fact, if it has any scale then
apply it, program will intelligently calculate the decimal value, and if
no scale is applied then it will put "INF" as a decimal for all numeric
itemTypes.

But let me check on live files.  
If you find any mistake please feel free to inform me about that.

 
