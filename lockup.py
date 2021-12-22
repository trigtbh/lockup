import os, sys, subprocess
import base64
import tkinter
from tkinter import messagebox
import json
import random
import platform
import shutil
import shlex
import hashlib

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/="

encryption_key = "change/me/to/whatever/you/want"


root = tkinter.Tk()
#root.withdraw()

class PasswordWindow:
    def __init__(self, ransom=False):

        self.password = ""
        self.master = root
        title = "Password Input"
        if ransom:
            title = "Decrypt files"
        self.master.title(title)
        
        if ransom:
            tkinter.Label(self.master, text="Your files have been encrypted!\nIf you want to decrypt the files, pay $500 USD worth of BTC or ETH to the address in the readme.txt file on your desktop.").pack()

        self.e1 = tkinter.Entry(self.master, show="*")
        self.e1.pack(padx=10, pady=10)

        self.button = tkinter.Button(self.master,
                                     text="Enter",
                                     command=self.getpw)
        self.button.pack(padx=10, pady=10)

        self.master.bind("<Control-q>", self.quit)
        self.master.bind("<Control-w>", self.quit)
        self.master.bind("<Return>", self.getpw2)

        self.master.mainloop()
        #self.master.destroy()

    def quit(self, event):
        self.master.destroy()
        exit()

    def getpw2(self, event):
        self.getpw()
        #self.master.destroy()

    def getpw(self):
        text = self.e1.get()
        if text == "":
            return self.master.destroy()
        self.password = text
        self.master.destroy()

def clear():
    plt = platform.system()
    if plt == "Linux" or plt == "Darwin":
        os.system("clear")
    elif plt == "Windows":
        os.system("cls")
    else:
        pass

def encrypt(string):
    encoded = base64.b64encode(string.encode("utf-8"))
    
    encoded = str(encoded, "utf-8")
    newstr = ""
    index = 0
    for c in encoded:
        ci = alphabet.index(c)
        ki = alphabet.index(encryption_key[index])
        new = (ci + ki) % len(alphabet)
        newstr = newstr + alphabet[new]
        index = (index + 1) % len(encryption_key)
    return newstr

def decrypt(encoded):
    index = 0
    newstr = ""
    for c in encoded:
        ci = alphabet.index(c)
        ki = alphabet.index(encryption_key[index])
        new = ci - ki
        newstr = newstr + alphabet[new]
        index = (index + 1) % len(encryption_key)
    return str(base64.b64decode(newstr.encode("utf-8")), "utf-8")

def exit1(trail):
    """Runs a completely different command."""
    os.system(trail)

def exit2():
    """Displays a fake fatal error."""
    root = tkinter.Tk()
    root.withdraw()
    code = random.randint(-673, 897)
    if platform.system() != "Darwin":
        messagebox.showerror(title="Fatal Error", message="A fatal error was encountered while trying to run the program.\n\nError code: -705")
    else:
        subprocess.check_output("""osascript -e 'set theDialogText to "A fatal error was encountered while trying to run the program.\n\nError code: -705"
display dialog theDialogText with title "Fatal Error" with icon stop'""", shell=True)

def exit3():
    """Shuts down the system. Use with caution."""
    if sys.platform == "darwin":
        subprocess.check_output("shutdown /s /t 1")
    else:
        subprocess.check_output("shutdown now", shell=True)

def exit4(command):
    """Completely removes parent of target program. Use with EXTREME caution."""
    executable = shlex.split(command)[0]
    if os.path.isfile(executable):
        shutil.rmtree(os.path.dirname(os.path.realpath(executable)))

if len(sys.argv) == 2:
    params = json.loads(decrypt(sys.argv[1]))
    try:
        exitfunc = eval("exit" + params["exit"])
    except NameError:
        raise AssertionError
    win = PasswordWindow(ransom=params["ransom"])
    if hashlib.sha256(win.password.encode("utf-8")).hexdigest() == params["password"]:
        subprocess.run(params["command"])
    else:
        if params["exit"] == "4":
            exitfunc(params["command"])
        elif params["exit"] == "1":
            exitfunc(params["trail"])
        else:
            exitfunc()

elif len(sys.argv) == 1:
    params = {}
    clear()
    params["command"] = input("Enter the command you want to lock: ")
    params["password"] = hashlib.sha256(input("Enter the password to lock this command with: ").encode("utf-8")).hexdigest()
    
    
    
    clear()
    params["ransom"] = input("Would you like to mask the program as a fake ransomware virus (y/N)? ").lower().strip().startswith("y")
    clear()
    print("Enter the number for the corresponding exit function you want to use.\nThe exit function only runs when an incorrect password is given to the program.")
    x = 1
    valid = []
    while True:
        try:
            f = eval("exit" + str(x))
            print("\t" + str(x) + ": " + f.__doc__)
            
        except NameError:
            break
        else:
            valid.append(str(x))
            x += 1
    e = input("\nEnter the exit function number: ").strip()
    if e.isnumeric():
        if e in valid:
            params["exit"] = e
            if e == "1":
                params["trail"] = input("Fake command to run upon failure: ")
            clear()
            print(encrypt(json.dumps(params)))