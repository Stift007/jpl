import os
import subprocess

vars = {
        "STT_IN":1,
        "STT_OUT":0,
        "STT_PIPE":-1,
        "PS":"NO_VALUE_PUSHED"
        }

# ! StdIO Functionality

def printf(__str):
        print(__str)

def puts(__str):
    printf(__str)

def scanf(__prompt=""):
    return input(__prompt)

# File I/O

files = []

def fopen(fn, mode="r"):
    files.append(open(fn, mode.strip(" ")))

def fread(idx):
    return files[int(idx)].read()

def fwrite(idx, text):
    files[int(idx)].write(text)

def fclose(idx):
    files[int(idx)].close()
    files.pop(int(idx))

# Generally useful Procedures

def system(*s):
    r = subprocess.Popen(s, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    puts(r.decode())

def popen(*s):
    r = subprocess.Popen(s, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    return r

funcs = {
        "printf":printf,
        "puts":puts,
        "scanf":scanf,

        "fopen":fopen,
        "fread":fread,
        "fwrite":fwrite,
        "fclose":fclose,
        
        "system":system,
        "popen":popen,
        "env_v":os.getenv

        }
