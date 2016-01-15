Title: XBRLFINAPP: XBRL financial analytics Platform - beta1.0 release
Date: 2013-03-11 11:14
Author: namitkewat
Category: XBRL
Tags: financial analysis, python, xbrl, xbrl analytics, xbrl fin app, xbrl financial analysis, xbrl finapp, xbrlfinapp
Slug: xbrlfinapp-beta1-0-release
Status: published

Hello friends,  
New updated
[xbrlfinapp](http://xbrlfinapp.pythonanywhere.com/ "XBRLFINAPP")has been
released.

Now It has more capabilities and more dynamic nature. So its going to be
fun; and i am sure you will enjoy analysis of xbrl financial data.

Visit xbrlfinapp at: <http://xbrlfinapp.pythonanywhere.com/>

[![xbrl financial analysis home
page](http://namitkewat.files.wordpress.com/2013/03/welcome.png)](http://namitkewat.files.wordpress.com/2013/03/welcome.png)

Some important updates are:

-   **Formula Design:** Now user can design custom formulas. For that
    they need to enter id of those xbrl elements. There are two types of
    formulas(type1 and type2). type1 formulas accepts xbrl elements in
    form of list/array of their ids. while type2 formulas are based on
    type1 formulas where you can write simple arithmetic formulas based
    on previously designed type1 formulas
-   **login system:** User has to register and login to get started with
    the app
-   **Makeover of app**: website's look and feel has been update to make
    user comfortable with the site

Most important of them are formula building. User can build their
formulas.  In mathematics; formulas are as simple as: x=3,y=2,z=x+y;

Like this; user can write their own financial formulas.

For example:

lets download sample xbrl: [NUVASIVE INC's 2012,
10-K](http://www.sec.gov/Archives/edgar/data/1142596/000144530513000348/0001445305-13-000348-xbrl.zip "NUVASIVE INC's' 2012-10-K"),
and upload this at xbrlfinapp.

UGT has xbrl element '*us-gaap\_AssetsCurrent*' for Current Assets(or in
simple manner, just assume, if x=30). So lets we first create type1
formula of this by giving it a name and in input list.

[![current asset's type1
formula](http://namitkewat.files.wordpress.com/2013/03/assets_frm.png)](http://namitkewat.files.wordpress.com/2013/03/assets_frm.png)

Similarly for current liabilities we have element
'*us-gaap\_LiabilitiesCurrent*', and we will create type1 formula(or in
simple manner, just assume, if y=20) for it as:

[![liabilities type1
formula](http://namitkewat.files.wordpress.com/2013/03/lia_frm.png)](http://namitkewat.files.wordpress.com/2013/03/lia_frm.png)

So output of this operation at xbrlfinapp will be something like(if you
have upload valid sec filled xbrl package) :

[![assets n
lia](http://namitkewat.files.wordpress.com/2013/03/assets-n-lia.png)](http://namitkewat.files.wordpress.com/2013/03/assets-n-lia.png)

All that was for type1 formulas. Now type2. Say we want to find out
working capital; then formula for it in general is current assets -
current liabilities. So in XBRLFINAPP we can write such mathematical
equations in type2 formulas.

Create type2 formula of working capital as:

[![working capital's type2
formula](http://namitkewat.files.wordpress.com/2013/03/wc_frm.png)](http://namitkewat.files.wordpress.com/2013/03/wc_frm.png)

We have just wrote "currentAssets - currnetlia" as a input and give it a
name 'workingCapital'(as simple as "z=x-y"). So output of this operation
will be:

[![wc](http://namitkewat.files.wordpress.com/2013/03/wc.png)](http://namitkewat.files.wordpress.com/2013/03/wc.png)

Similarly type2 formula of current ratio can we written as:

[![current ratio's type2
formula](http://namitkewat.files.wordpress.com/2013/03/currentratio_frm.png)](http://namitkewat.files.wordpress.com/2013/03/currentratio_frm.png)

and its result will be:

[![currentratio](http://namitkewat.files.wordpress.com/2013/03/currentratio.png)](http://namitkewat.files.wordpress.com/2013/03/currentratio.png)

By this way; user is allowed to use "+","-" and "/" operator with "(" or
")" for writing equations.

**Note:**

-   type1 formulas will contain array or list of ids of xbrl
    elements(separated by comma) which you want to add. and these
    elements must have same item type. If user has added different item
    type elements; nothing will happen. you can also add ids of
    extension elements.
-   type2 formulas will contain previously formulated type1 and type2
    formulas.
-   And you can't delete type1 or type2 formulas which are used in
    formulas which were created after it.
-   You can't modify the name or alias of formula after creating it. To
    modify it first delete it and then create it again with new name or
    alias.

### **One of the most important feature of xbrlfinapp is; its intelligent element discovery.**

XBRLFINAPP is intelligent in terms of finding element. For example if
the first xbrl element of input array of type1 formula is not present in
instance then it will find its part; and return the total. for example;
in this filling lets find "cash and cash equivalents". But it is not
present. So xbrlfinapp will search for its component and will return
total of them(by resolving itemtype, balance type, context, unit, period
in background), and if additional xbrl elements has been added as input;
then rest of that type1 array will be added into this total if they are
the not part of first element. Part means: are they duplicate or they
are part of cash or cash equivalents. It means if user has created
extension then we can  add extensions here.

[![cash equ type1
formula](http://namitkewat.files.wordpress.com/2013/03/cashequ_frm.png)](http://namitkewat.files.wordpress.com/2013/03/cashequ_frm.png)

Output of this is:

[![cashequ](http://namitkewat.files.wordpress.com/2013/03/cashequ.png)](http://namitkewat.files.wordpress.com/2013/03/cashequ.png)

Here; output has 4 values because XBRLFINAPP with search for element in
complete filling. Also; look at the filtered elements list; it has two
elements; and when you look at the balance sheet; here they are:

[![Screen shot 2013-03-12 at 11.18.59
PM](http://namitkewat.files.wordpress.com/2013/03/screen-shot-2013-03-12-at-11-18-59-pm.png)](http://namitkewat.files.wordpress.com/2013/03/screen-shot-2013-03-12-at-11-18-59-pm.png)

**Such type of issue was the most challenging part for me; For example;
hardest question were:**

**1. how will you calculate current ratio if filler has not provided
current assets's tag?**

**2. How will calculate Net Income if filler hasn't tagged it??**

*But now;  this question has been resolved by xbrlfinapp :)*

So my formulas are now constant for all companies. I don't require to
change them for companies to companies.

For more register and login
[xbrlfinapp](http://xbrlfinapp.pythonanywhere.com/ "XBRLFINAPP"); you
will receive 35 formulas by defaults. you can learn from them how to
create formulas based on these formulas.

Anyways; friends if you face any query/error/bug; please email me about
that at "namitkewat@gmail.com".
