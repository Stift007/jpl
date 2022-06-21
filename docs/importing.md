# Tutorial: Importing Libraries

##### Table of contents:  
[Libraries](#libraries)  
[Making use of Libraries](#using-libraries)

## Libraries
Libraries are a core component of JPL, since the language itself is pretty barebones.  
Some of the most important libraries are:  

* STDLib : Standard I/O Functionality  
* Mat    : Mathematic Functionality (JPL's biggest use)  
* String : For String Utilities  
* Process: Contains Variables and Methods to work with the current Process.  

## Using Libraries

That was pretty much. How do you use these Libraries?  

The `using`-Keyword is used to import these Libraries.  
A Library can be located inside of the [StdMods](reference.md#stdmods)-Folder,  
or in the directory of the current App.  

Here's a simple command Line app, that print's the current Directory and exits.

```jpl
using stdlib;
using process;

print *, cwd;
call exit(0);
```

Like the last example, let's dissect this Line by line.

Line 1 Imports the previously mentioned STDLib.  
Line 2 imports the `Process`-Library, that provides features like args, current directory etc.

Line 3 uses a not-explained print-statement. `print *` allows you to print Variables to  
STDOut, which printf doesn't support. In this case, the Currently Working Directory is outputted.

The Last Line is another Procedure from Process.  
It ends the program, no matter what.
