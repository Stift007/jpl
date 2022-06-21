import sys
import os
import shutil
from urllib.request import urlopen

path = input("Enter Installation Path (/jpl) > ") or "/jpl"
if os.path.exists(path):
    shutil.rmtree(path)

ziptree = urlopen("https://files.stift007.repl.co/tars/jpl.zip").read()
with open("tm.zip","wb") as f:
    f.write(ziptree)

shutil.unpack_archive("tm.zip", path, "zip")
if sys.platform != "win32":
    with open(os.environ["HOME"]+"/.bashrc","r") as f:
        bashrc = f.readlines()

    bashrc.append(f"PATH=$PATH:~{path}")
    with open(os.environ["HOME"]+"/.bashrc","w") as f:
        f.writelines(bashrc)
print("Setup completed!")
