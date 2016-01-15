Title: Using list, set and dict as a key in python dict
Date: 2013-04-15 17:44
Author: namitkewat
Category: General
Tags: python, python dict, python hashable dict, python hashable list, python hashable set, python list, python set
Slug: using-list-set-and-dict-as-a-key-in-python-dict
Status: draft

Python dict allows immutable types as a dictionary keys.

From the python
[docs](http://docs.python.org/2/reference/datamodel.html#the-standard-type-hierarchy "docs"):

*The only types of values not acceptable as keys are values containing
lists or dictionaries or other mutable types that are compared by value
rather than by object identity, the reason being that the efficient
implementation of dictionaries requires a key’s hash value to remain
constant.*

it means if we try to set list, set or dict(which are mutable types) as
a dict key.. . we will get error as:

[sourcecode language="python" wraplines="false" collapse="false"]  
In [1]: lst=[1,2,3,4]  
In [2]: a={lst:'my name is namit'}  
---------------------------------------------------------------------------  
TypeError Traceback (most recent call last)  
\<ipython-input-2-fa474d946338\> in \<module\>()  
----\> 1 a={lst:'my name is namit'}  
TypeError: unhashable type: 'list'  
[/sourcecode]

So the solution is lets add a \_\_hash\_\_ magic method to make it
immutable by providing a unique hash value.

### Hashable python list

[sourcecode language="python" wraplines="false" collapse="false"]  
class hashablelist(list):  
insnum=0  
def \_\_init\_\_(self, initial=[]):  
super(hashablelist, self).\_\_init\_\_(initial)  
self.hashval=hashablelist.insnum  
hashablelist.insnum+=1  
def \_\_hash\_\_(self):  
return self.hashval

lst=[1,2,3,4]  
lst2=hashablelist(lst)  
a={lst2:'my name is namit'}  
print a  
print a[lst2]  
print lst2  
print hashablelist.insnum  
print lst2==lst  
[/sourcecode]

output of above will be:

[sourcecode language="python" wraplines="false" collapse="false"]  
{[1, 2, 3, 4]: 'my name is namit'}  
my name is namit  
[1, 2, 3, 4]  
1  
True  
[/sourcecode]

As you have seen above that by this we can use python lists as a dict
keys; and this will be very helpful in many areas.

Similarly for dict we can do it as:

### Hashable python dict

[sourcecode language="python" wraplines="false" collapse="false"]  
class hashabledict(dict):  
insnum=0  
def \_\_init\_\_(self,initial={}):  
super(hashabledict,self).\_\_init\_\_(initial)  
self.hashval=hashabledict.insnum  
hashabledict.insnum+=1  
def \_\_hash\_\_(self):  
return self.hashval

dct={'name':'namit'}  
dct2=hashabledict(dct)  
a={dct2:"voila"}  
print a  
print a[dct2]  
print hashabledict.insnum  
print dct2==dct  
[/sourcecode]

output of above will be:

[sourcecode language="python" wraplines="false" collapse="false"]  
{{'name': 'namit'}: 'voila'}  
voila  
1  
True  
[/sourcecode]

and python sets as:

### Hashable python set

[sourcecode language="python" wraplines="false" collapse="false"]  
class hashableset(set):  
insnum=0  
def \_\_init\_\_(self,initial=set()):  
\#\#hashableset.\_\_name\_\_='set'  
super(hashableset,self).\_\_init\_\_(initial)  
self.hashval=hashableset.insnum  
hashableset.insnum+=1  
def \_\_hash\_\_(self):  
return self.hashval

cet2=hashableset(cet)  
a={cet2:"my name is namit"}  
print a  
print a[cet2]  
print cet==cet2  
[/sourcecode]

its output will be:

[sourcecode language="python" wraplines="false" collapse="false"]  
{set([2, 3, 4, 5]): 'my name is namit'}  
my name is namit  
True  
[/sourcecode]

For more you can download my ipython notebook from
[here](https://docs.google.com/file/d/0B_1SHAnqrt8TWHVuRmVydVlTQVU/edit?usp=sharing "here").
