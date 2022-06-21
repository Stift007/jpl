# Reference

## StdMods
StdMods is located in \<jpl-compilaion-path\>/StdMods

### stdmods/stdlib.py
* (Procedure) printf(\_\_str) : Prints str to stdout  
* (Procedure) puts(s)         : Calls printf(s)  
* (Procedure) fopen(fn, mode) : Opens the File \<fn\> as \<mode\>, pushes it to array  
* (chr) fread(idx)            : Reads the \<idx\>th File opened  
* (Procedure) fwrite(idx, txt): Write \<txt\> to \<\idx\>th File opened  
* (Procedure) fclose(idx)     : Closes \<idx\>th File  
* (Procedure) system(\*s)     : Run `s` as a command and prints the output  
* (chr) popen(\*s)            : Like ~.system, but returns the output instead of printing  
* (chr) env\_v(key)	      : Returns the Environment Variable corresponding to \<key\>  

### stdmods/mat.py
* (varfloat) pi               : Approximate PI  
* (int) add(a,b)              : Returns a+b  
* (int) sub(a,b)              : Returns a-b  
* (int) mul(a,b)              : Returns a\*b  
* (int) div(a,b)              : Returns a/b  
* (float) sqrt(x)             : Return the Square Root of x  
* (float) root(x,y)           : Return the y'th root of x  

### stdmods/process.py
* (varint) argc               : Argument Count  
* (varray[chr]) argv	      : Arguments  
* (varchr) cwd                : Currently working directory  
* (vardate) date              : Date of running  
* (Procedure) load\_dotenv    : Load's a `.env`'s Content into the environment variables  
* (chr) getenv(key)           : Equivalent to stdlib's env\_v  
* (Procedure) cd(d)           : Change the Current Working directory to d  
* (NoReturn) exit(code)       : End JPL, yield \<code\>  

### stdmods/string.py
* (int) strcmp(a,b)           : Compare 2 Strings  
* (int) strlen(a)             : Returns the length of a String  
* (chr) strscn()              : Ask for a String from STDIn
