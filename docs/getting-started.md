# Tutorial: Getting started

##### Table of contents:  
[Prerequisites](#prerequisites)  
[Write some code](#write-some-code)  
[Write more code](#write-more-code)

## Prerequisites

* A Bit of Programming experience (JPL isn't self-explanatory)  
* A Text Editor (We recommend sublime or VSCode)  
* Python 3.6+

## Write some code

The time has come! We'll get started with a simple "Hello, World!" Script.  

In your text editor, create a file like "main.jpl"
```
!jpl version=1 charset=utf8;
using stdlib;

printf("Hello, World!");
```

Now, what does this do? Let's go through this, Line by Line  

The first line isn't required or important, it just helps when sending your File around,  
so people know what version of JPL you were using.

The Second Line (using stdlib) imports a Module called "STDLib" (Standard Library).  
STDLib contains functions for simple I/O Operations, like printing Text.  
It also supports File writing, but we'll get there later.  

The Third Line refers to the - in stdlib defined - procedure "PrintF", which prints  
text to the Screen. There's other ways to do that, but printf is the most efficient.

## Write MORE Code!
That was a simple introduction, behold what other things JPL has in store!
