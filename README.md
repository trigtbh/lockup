# Lock-Up
## Basic password protection for running programs

This program adds (or attempts to add) an extra layer of security to prevent unwanted people from running programs on your computer

---
## Requirements

- Python 3 (preferably 3.6 or higher)
- Tkinter installed for Python 3
- Standard package library for Python 3 (if for some reason it isn't already included)
---
## Usage
1. Ensure [Git is installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your computer. Open up a terminal, and type `git clone https://github.com/TriG-Tbh/lockup.git` to download the files. Once they're downloaded, type `cd lockup` to enter the folder they were installed to.

2. Open `lockup.py`. On line 14, edit `encryption_key` to be whatever string you want (as long as all of its characters are in `alphabet`). You don't need to remember this, as it helps encrypt and decrypt content generated by the program. However, you **should** make sure it is kept secure.

3. Run `python3 lockup.py` (or `python lockup.py` if your Python 3 command is called `python`). It will ask you for a few inputs:
    
    - `Command`: the command that you want to protect. This will be executed as if it were entered into a terminal in your [home folder](https://en.wikipedia.org/wiki/Home_directory#Default_home_directory_per_operating_system).
    - `Password`: the password that protects the command. This can be set to a different string for every protected command you create, so **it's important that you remember specifically what passwords correspond to what commands**.
    - `Ransom`: if you want an extra layer of security, saying yes to this prompt will mask the password input window to make it look like ransomware, to try and throw off unwanted access.
    - `Exit Function`: what the program should do if an incorrect password is given. This can range from a fake fatal error message to completely shutting down the system. Use whatever function best suits the content you're protecting.
    - `Trail`: if you selected that you want to run a second command if an incorrect password is entered, this field is where you enter that. For example, if an incorrect password is given, you might want to open `firefox.exe` to try and throw people off.

    Once all fields are given, the program will generate a long string of *seemingly* random characters. Keep this, as it's what will make the script open your command.

4. Run `python3 lockup.py [string of characters from step 3]`. If all goes well, the script should ask for your password, and run the command you set it to run.

---

## Taking it further

There's a couple of things you can do once you have an encrypted command. You can:

- Save the entire command created in step 4 to a shortcut for easy access
- [Obfuscate](https://pyob.oxyry.com) `lockup.py` to make it harder to read
- Hide both the target program and `lockup.py` so they're much more difficult to find 
- Use [Pyinstaller](https://www.pyinstaller.org) to convert it to a standard executable file and make it seem less suspicious
- Combine all of the above to make it as difficult as possible for other people to access your programs

---

## Issues

If there are somehow any issues with the code, use the [Issues tab](https://github.com/TriG-Tbh/lockup/issues) to report them.

If you want to submit changes, use the [Pull requests tab](https://github.com/TriG-Tbh/lockup/issues).

---

## License

This project is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT).

Full license text can be found in `LICENSE.txt`.