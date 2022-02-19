from os import path
from invoke import task

@task(default=True)
def upload(c):
    if not path.exists("/media/nnyn/CIRCUITPY"):
        print("mount CIRCUITPY")
        return
    c.run("cp code.py keymap.py /media/nnyn/CIRCUITPY/")