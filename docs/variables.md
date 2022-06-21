# Tutorial: Variables

##### Table of contents:  
[Declaration](#declaration)  
[Usage](#usage)

In programming, a variable is a value that can change, depending on conditions or on information passed to the program.

## Declaration
A Variable can be either:  
* declared by its type (chr, int) or  
* using the `var`-Type (Which is a non-fixed Type)  
Declaration looks like this:

`type :: name = value`.  

So, for example:
```jpl
var :: hello = "Hey, there";
int :: MyAge = 15;
chr :: MyName = "Jane";
```

## Usage
Variables can be used in Procedure Calls (Like MAT's calculations) or on certain keywords.

These Keywords are:  
* `print *, var_name;` : Print the Variable's Content.  
* `tprint *, var_name` : Print the Variable's Type.  
* `objfound var_name`  : Check if var\_name is referring to an existing Variable
