import os
import sys
from os import path
from invoke import task

mount_dir = "/media/nnyn/CIRCUITPY"

def mount(c):

    if not path.exists(mount_dir):
        c.run(f"sudo mkdir -p {mount_dir}")

    device_path = ""
    if not path.exists(f"{mount_dir}/lib"):
        l = c.run("lsblk -p -r -o NAME,SIZE", hide=True).stdout
        for line in l.strip().split("\n"):
            name, size = line.split(" ")
            if name.endswith("1") and size == "1M":
                device_path = name
                break
        if not device_path:
            print("cannot find usb")
            sys.exit(1)
        c.run(f"sudo mount {device_path} {mount_dir} -o umask=000")

def umount(c):
    c.run(f"sudo umount {mount_dir}")

@task(default=True)
def upload(c):
    mount(c)

    c.run(f"cp code.py keymap.py {mount_dir}")
    c.run("sync")

    umount(c)

@task
def console(c):
    c.run("minicom -D /dev/ttyACM0")

@task
def compile_kmk(c):
    cwd = os.getcwd()
    kmk_dir = f"{cwd}/libs/kmk_firmware"
    paths = f"{kmk_dir}/bin:" + os.environ["PATH"]
    with c.cd(kmk_dir):
        c.run("rm -rf ./.compiled")
        c.run(f"make compile", env={"PATH": paths})

    mount(c)
    c.run(f"rm -rf {mount_dir}/lib/kmk_firmware")
    c.run(f"cp -r {kmk_dir}/.compiled/kmk {mount_dir}/lib")
    c.run("sync")
    umount(c)