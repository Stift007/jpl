import sys
import importlib
import os

stdpath = [
    os.getcwd(),
    os.path.dirname(os.path.abspath(__file__))+"/stdmods"
]

funcs = {}

vars = {
    "NULL": None
}


def open_file(fp):
    d = open(fp, 'r').read()
    d = d.replace("\n","")
    d = d.split(";")
    return d

def parse(contents):
    
    global vars
    global funcs
    for i in contents:
        if i.startswith("!"):continue        
        if i[0:8].lower() == "print *,":
            text = i.replace("print *,","")
            quotes = []
            spaces = []
            for j in range(len(text)):
                if text[j] == "\"":
                    quotes.append(j)
                if text[j] == " ":
                    spaces.append(j)
            try:
                print(text[quotes[0]+1:quotes[1]])
            except IndexError:
                fn = text
                if "(" in fn: 
                    if "()" in fn:
                        fn = fn.replace("()","")
                        resargs = []
                    else:
                        fn, args = fn.split("(")
                        args = args[:-1]
                        args = args.split(",")
                        resargs = []
                        for arg in args:
                            quotes = []
                            spaces = []
                            
                            for j in range(len(arg)):
                                if arg[j] == "\"":
                                    quotes.append(j)
                                if arg[j] == " ":
                                    spaces.append(j)
                            try:
                                resargs.append(arg[quotes[0]+1:quotes[1]])
                            except IndexError:
                                resargs.append(vars[arg[len(arg)-len(arg.lstrip()):]])

                        print(funcs[fn](*resargs))
                else:
                    print(vars[text[len(text)-len(text.lstrip()):]])

        elif i[0:2] == "do":
            amt = i.replace("do ","")

            ret_idx = -1
            for j in range(len(contents[contents.index(i):])):
                
                if contents[j] == "yield":
                    ret_idx = j
                    break
            code = []

            
            start = contents.index(i)
            
            
            for j in contents[start:ret_idx]:    
                contents.pop(contents.index(j))      
                if not j.startswith("procedure"):
                    code.append(j)
                
            for j in contents[:start]:
                if j.startswith("using"):
                    code.append(j)
            
            code.reverse()
            for _ in range(int(amt)): parse(code)
            
        elif i[0:2] == "if":
            
            ret_idx = -1
            for j in range(len(contents[contents.index(i):])):
                
                if contents[j] == "fi":
                    ret_idx = j-1
                    break
            code = []

            cond = i.replace("if ","")
            start = contents.index(i)
            
            lside, rside = cond.split("==")
            lside = lside.lstrip().rstrip()
            rside = rside.rstrip().lstrip()

            if not "\"" in lside:
                try:
                    c1 = int(lside)
                except:
                    if "(" in lside:
                        fn = lside
                        if "()" in fn:
                            fn = fn.replace("()","")
                            resargs = []
                        else:
                            fn, args = fn.split("(")
                            args = args[:-1]
                            args = args.split(",")
                            resargs = []
                            for arg in args:
                                quotes = []
                                spaces = []
                                
                                for j in range(len(arg)):
                                    if arg[j] == "\"":
                                        quotes.append(j)
                                    if arg[j] == " ":
                                        spaces.append(j)
                                try:
                                    resargs.append(arg[quotes[0]+1:quotes[1]])
                                except IndexError:
                                    resargs.append(vars[arg[len(arg)-len(arg.lstrip()):]])

                        c1  = funcs[fn](*resargs)
                    else:
                        c1 = vars[lside]
            else:
                text = lside
                quotes = []
                spaces = []
                for j in range(len(text)):
                    if text[j] == "\"":
                        quotes.append(j)
                    if text[j] == " ":
                        spaces.append(j)
                
                c1 = (text[quotes[0]+1:quotes[1]])
            if not "\"" in rside:
                try:
                    c2 = int(rside)
                except:
                    if "(" in rside:
                        fn = rside
                        if "()" in fn:
                            fn = fn.replace("()","")
                            resargs = []
                        else:
                            fn, args = fn.split("(")
                            args = args[:-1]
                            args = args.split(",")
                            resargs = []
                            for arg in args:
                                quotes = []
                                spaces = []
                                
                                for j in range(len(arg)):
                                    if arg[j] == "\"":
                                        quotes.append(j)
                                    if arg[j] == " ":
                                        spaces.append(j)
                                try:
                                    resargs.append(arg[quotes[0]+1:quotes[1]])
                                except IndexError:
                                    resargs.append(vars[arg[len(arg)-len(arg.lstrip()):]])

                        c2  = funcs[fn](*resargs)
                    else:
                        c2 = vars[lside]
            
            else:
                text = rside            
                quotes = []
                spaces = []
                for j in range(len(text)):
                    if text[j] == "\"":
                        quotes.append(j)
                    if text[j] == " ":
                        spaces.append(j)
                
                c2 = (text[quotes[0]+1:quotes[1]])
            for j in contents[start+1:ret_idx]:    
                contents.pop(contents.index(j))
                code.append(j)
        
            for j in contents[:start]:
                if j.startswith("using"):
                    code.append(j)
            
            code.reverse()
            
            if c1 == c2: parse(set(code))

        elif i[0:9] == "procedure":
            ret_idx = -1
            for j in range(len(contents[contents.index(i):])):
                
                if contents[j] == "yield":
                    ret_idx = j
                    break
            code = []

            proc_name = i.replace("procedure ","")
            start = contents.index(i)
            
            for j in contents[start:ret_idx]:    
                contents.pop(contents.index(j))
                
                if not j.startswith("procedure"):
                    code.append(j)
        
            for j in contents[:start]:
                if j.startswith("using"):
                    code.append(j)
            
            code.reverse()
            funcs[proc_name] = lambda *a: parse(code)
            funcs[proc_name]() 
            ##parse(code)

        elif i[0:4] == "call":
            fn = i.replace("call ","")
            if "()" in fn:
                fn = fn.replace("()","")
                resargs = []
            else:
                fn, args = fn.split("(")
                args = args[:-1]
                args = args.split(",")
                resargs = []
                for arg in args:
                    quotes = []
                    spaces = []
                    
                    for j in range(len(arg)):
                        if arg[j] == "\"":
                            quotes.append(j)
                        if arg[j] == " ":
                            spaces.append(j)
                    try:
                        resargs.append(arg[quotes[0]+1:quotes[1]])
                    except IndexError:
                        if arg[len(arg)-len(arg.lstrip()):] in vars: 
                            resargs.append(vars[arg[len(arg)-len(arg.lstrip()):]])
                        else:
                            resargs.append(int(arg[len(arg)-len(arg.lstrip()):]))

                funcs[fn](*resargs)

        elif i[0:9].lower() == "tprint *,":
            text = i.replace("tprint *,","")
            quotes = []
            spaces = []
            for j in range(len(text)):
                if text[j] == "\"":
                    quotes.append(j)
                if text[j] == " ":
                    spaces.append(j)
            try:
                print(type(text[quotes[0]+1:quotes[1]]))
            except IndexError:
                print(type(vars[text[len(text)-len(text.lstrip()):]]))

        if i[0:8].lower() == "objfound":
            text = i.replace("objfound","")
            quotes = []
            spaces = []
            for j in range(len(text)):
                if text[j] == "\"":
                    quotes.append(j)
                if text[j] == " ":
                    spaces.append(j)
            try:
                text[quotes[0]+1:quotes[1]]
                print("null")
            except IndexError:
                print(text[len(text)-len(text.lstrip()):] in vars or text[len(text)-len(text.lstrip()):] in funcs)

        elif i[0:6].lower() == "var ::":
            var = i.replace("var ::","")
            typedef = "str"
            try:
                firstquote = var.index("\"")
            except:
                
                if "(" in var: 
                    typedef = "fn"
                else:
                    typedef = "int"
            eq = var.index("=")
            varname = var[:eq].replace(" ","")
            if typedef == "str":
                varvalue = var[firstquote+1:-1]
                vars[varname] = varvalue
            elif typedef == "int":
                varvalue = var[eq+1:].replace(" ","")
                vars[varname] = int(varvalue)
            elif typedef == "fn":
                    fn = var[eq+1:].replace(" ","")
                    if "()" in fn:
                        fn = fn.replace("()","")
                        resargs = []
                    else:
                        fn, args = fn.split("(")
                        args = args[:-1]
                        args = args.split(",")
                        resargs = []
                        for arg in args:
                            quotes = []
                            spaces = []
                            
                            for j in range(len(arg)):
                                if arg[j] == "\"":
                                    quotes.append(j)
                                if arg[j] == " ":
                                    spaces.append(j)
                            try:
                                resargs.append(arg[quotes[0]+1:quotes[1]])
                            except IndexError:
                                
                                if arg[len(arg)-len(arg.lstrip()):] in vars: 
                                    resargs.append(vars[arg[len(arg)-len(arg.lstrip()):]])
                                else:
                                    resargs.append(int(arg[len(arg)-len(arg.lstrip()):]))

                        vars[varname] = funcs[fn](*resargs)
            typedef = "str"

        elif i[0:6].lower() == "int ::":
            var = i.replace("int ::","")
            typedef = "int"
            eq = var.index("=")
            varname = var[:eq].replace(" ","")
                        
            varvalue = var[eq+1:].replace(" ","")
            print(varname, str(varvalue))
            vars[varname] = int(varvalue)
            typedef = "str"


        elif i[0:6].lower() == "chr ::":
            var = i.replace("chr ::","")
            typedef = "str"
            try:
                firstquote = var.index("\"")
            except:
                typedef = "int"
            eq = var.index("=")
            varname = var[:eq].replace(" ","")
            if typedef == "str":
                varvalue = var[firstquote+1:-1]
                vars[varname] = varvalue
            elif typedef == "int":
                varvalue = var[eq+1:].replace(" ","")
                vars[varname] = int(varvalue)
            typedef = "str"

        
        elif i[0:5] == "using":
            module = i.replace("using ","")
            for i in stdpath:
                if os.path.exists(f'{i}/{module}.jpl'):
                    parse(open_file(f'{i}/{module}.jpl'))
                elif os.path.exists(f'{i}/{module}.py'):
                    sys.path.insert(0, i)
                    curvar = vars.copy()
                    PPM_Vars = importlib.import_module(module).vars
                    PPM_Funcs = importlib.import_module(module).funcs
                    vars = {**curvar, **PPM_Vars}
                    funcs = {**funcs, **PPM_Funcs}
                    break



def run():  
    data = open_file(sys.argv[1])
    parse(data)


if __name__ == "__main__":
    run()
