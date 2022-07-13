import os
import sys
from os import path
from invoke import task
import detect

mount_dir = "/media/" + os.environ["USER"] + "/CIRCUITPY"
if detect.osx:
    mount_dir = "/Volumes/CIRCUITPY"

keymap_path = os.environ.get("KEYMAP_PATH", "./keymap.py")
backup_keymap_path = os.environ.get("BACKUP_KEYMAP_PATH", "./backup_keymap.py")

@task
def mount_linux(c):
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

@task
def mount_mac(c):
    if not path.exists(mount_dir):
        c.run(f"sudo mkdir -p {mount_dir}")

    device_name = ""
    print(f"{mount_dir}/lib")
    if path.exists(f"{mount_dir}/lib"):
        return

    l = c.run("diskutil list", hide=True).stdout
    for line in l.strip().split("\n"):
        if line.count("CIRCUITPY") == 0:
            continue
        device_name = line.split(" ")[-1]
    if not device_name:
        print("cannot found CIRCUITPY disk")
        sys.exit(1)
    c.run(f"sudo mount -t msdos /dev/{device_name} /Volumes/CIRCUITPY")

@task
def mount(c):
    if detect.osx:
        mount_mac(c)
    elif detect.linux:
        mount_linux(c)
    else:
        print("cannot mount CIRCUITPY")
        sys.exit(1)

@task
def umount(c):
    c.run(f"sudo umount {mount_dir}")

@task(default=True)
def upload(c):
    if detect.osx:
        mount_mac(c)
    elif detect.linux:
        mount_linux(c)

    c.run(f"cp code.py {keymap_path} {mount_dir}")
    c.run(f"cp code.py {mount_dir}")
    c.run(f"cp {keymap_path} {mount_dir}/keymap.py")
    c.run(f"cp {backup_keymap_path} {mount_dir}/backup_keymap.py")
    c.run("sync")

    umount(c)

@task
def console(c):
    if detect.linux :
        c.run("minicom -D /dev/ttyACM0")
    if detect.mac :
        usb_devices = c.run("ls /dev/tty.usbmodem*", hide=True).stdout.strip().split("\n")
        if len(usb_devices) > 1 or len(usb_devices) == 0:
            print("cannot determine CIRCUITPY console", usb_devices)
        else:
            usb = usb_devices[0].strip()
            print(f"command:")
            print(f"screen {usb} 115200")

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