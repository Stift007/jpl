import os
import sys
import datetime

def load_dotenv(env_path=None):
    if not env_path:
        with open(os.getcwd()+"/.env","r") as f:
            datas = f.readlines()
    else:
        with open(env_path) as f:
            datas = f.readlines()
    for d in datas:
            k, v = d.split("=")
            os.environ[k] = v

vars = {
        "argc":len(sys.argv),
        "argv":sys.argv,
        "cwd":os.getcwd(),

        "date":datetime.datetime.now(),

}

funcs = {
        "load_dotenv":load_dotenv,
        "getenv":os.getenv,
        "exit":sys.exit,
        "cd":os.chdir

}
