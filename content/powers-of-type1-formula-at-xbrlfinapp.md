Title: Powers of type1 Formula at xbrlfinapp
Date: 2013-03-13 17:23
Author: namitkewat
Category: XBRL
Tags: type1 xbrlfinapp formula, xbrl, xbrl analytics, xbrlfinapp
Slug: powers-of-type1-formula-at-xbrlfinapp
Status: published

In this post i am going to explain type1 formula/array in details.

type1 formula/array is the most important, fundamental building block of
[xbrlfinapp](http://xbrlfinapp.pythonanywhere.com/).

It represent an xbrl element in terms of array.

To understand this; lets take an example:

Suppose we want to calculate "Total Assets" and in US GAAP taxonomy its
id is "us-gaap\_Assets". So now we will find this xbrl element in our
concerned xbrl filling. And if filler has tagged values with this xbrl
element, then we will fetch that value and will use that value according
to our need.

Anyways, This is the easiest part!

Now hardest part: How to calculate "Total Assets" is filler hasn't
provided?

So the solution is: Lets find out its part/components and return the
total of all and call this total as our "Total Assets".

This concept has been implemented in type1 array.

type1 array is considering first element as a primary element and rest
in the list as a component of it.

Its algorithm will first search for 1st element of input array in the
filling.

If it is there then simply take its values, and move to next elements in
the list and will add into the values of the first element  if it is not
the element wise duplicate of first or is not the part or component of
it according to US GAAP taxonomy(with resolving context, unit, item
type, balance type).

And if it is not there; then its algorithm will search for the
components of "Total Assets", and will sum them all, without any
repetitions(means if current assets is there and its parts are also
there; then algorithm will take current assets and forgot its part).
After this algorithm will move to the next element of input array and
will do the same for it and its returning value will be added to its
previous one(with resolving everything: balance type, unit, item type).

When the iteration is over; type1 array will take the properties of
first element and assign that to the final result.

Do you think that at this point our work is over? and we got what we
have asked for?

My answer is: No

Up-to this, we have done nothing for extensions. But type1 array allows
you to add them. Extensions are not algorithmically checked for part and
its sub-part. They are filling specific. So you can add them in type1
array. algorithm will just add if it finds it to the final sum.

This was the main reason to use id's of xbrl element. Because one
extension's id will differ from id other filler's. So if it is there
then it will add in its final sum or will forgot it and move to the
other element.

By this way; you can add huge list of elements as formula/array where
1st element will be the US-GAAP's xbrl element and others are from
different fillings. If that id is present; then it will added otherwise
forgot it and more to next element of input array.

Lets take real life example. I am going to consider
[filling](http://www.sec.gov/Archives/edgar/data/1142596/000144530513000348/0001445305-13-000348-xbrl.zip)
that we have used in our previous
[post](http://namitkewat.wordpress.com/2013/03/11/xbrlfinapp-beta1-0-release/ "post"):

Its "Total Assets" is:

[![array2](http://namitkewat.files.wordpress.com/2013/03/array2.jpg)](http://namitkewat.files.wordpress.com/2013/03/array2.jpg)And
when we have added multiple elements which are part of Total Assets, in
that also the result is same as "Total Assets". type1 knows how to avoid
duplicate and how to avoid sub components.

[![array1](http://namitkewat.files.wordpress.com/2013/03/array1.jpg)](http://namitkewat.files.wordpress.com/2013/03/array1.jpg)

Similarly we can test "Total Assets" and "Liabilities and Stockholders
Equity's" total. If both are equal then returning total will be zero,
because one is debit and other is credit and when we represent these two
as a one; then both will eliminate each other and result will be
zero.[![array3](http://namitkewat.files.wordpress.com/2013/03/array3.jpg)](http://namitkewat.files.wordpress.com/2013/03/array3.jpg)

In same way; We can find "Debt"
as:[![array4](http://namitkewat.files.wordpress.com/2013/03/array4.jpg)](http://namitkewat.files.wordpress.com/2013/03/array4.jpg)

Above you can see that the debt's component: short term and long term
are not present; so will return its components.

In same way "Revenues" can be find. Here xbrl element for revenues
"us-gaap\_Revenues" is not provided by the filler, so its component are:
*us-gaap\_InterestExpense,* *us-gaap\_SalesRevenueNet* were filtered by
the app and its result
is:[![array5](http://namitkewat.files.wordpress.com/2013/03/array5.jpg)](http://namitkewat.files.wordpress.com/2013/03/array5.jpg)
