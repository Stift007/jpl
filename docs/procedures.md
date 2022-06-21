# Procedures

##### Table of contents:
[Declaration](#declaration)  
[Usage](#usage)

A Procedure is a set of coded instructions that tell a computer how to run a program or calculation.  

## Declaration
To start a Procedure, type `procedure <name>;`.  
Then, enter all your code and THEN end with `yield;`.  
Here's an example:  

```
using stdlib;
using string;

procedure hello;
printf("Enter your Name");
var :: name = strscn();
printf("Hello,");
print *, name;
yield;
```

## Usage
The best way to call Procedures is using `call <name>;`  
Howeer, if the "Procedure" returns a Value (Which makes it a function), you can also use it with `var ::`.  

`var :: name = strscn();`  
`call strscn();`
