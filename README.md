# Bruteforce random private keys

## Disclaimer !
<details>
<summary>see more</summary>

<b>This code could be illegal in your country.</b> Do not download it, if thats the case<br>
I take no responsibilitiy for abusing my code for a bad purpose.

</details>


## How it works
<details>
<summary>see more</summary>

1. It takes a random input, for example common names or passwords
2. Then it uses sha256 to create a private key of it (how it was done in the old days)
3. It creates a Bitcoin adress of that private key
4. It checks on <a target="blank" href="https://mempool.space">mempool.space</a> if there is or was money on that adress
5. It stores a .txt file of Succesfull and allready looted private keys

</details>


## Requirements
<details>
<summary>see more</summary>

* Latest <a target="blank" href="https://www.python.org/">Python</a> version
* Pip installed (should be installed with python)

</details>


## Start the program on Windows
<details>
<summary>see more</summary>

1. <a traget="blank" href="https://github.com/RealCocoArdo/bruteforce-random-bitcoin-privatekeys/archive/refs/heads/main.zip">Download</a> or clone the code
2. Open your terminal or cmd
3. Navigate to the folder where you stored the programm with `cd folderName` and `cd ..`
4. Install required packages via pip
```
pip install requests bitcoin time itertools random string wonderwords
```
5. Start the program with the random input method of your choice
```
py random_.py
```
```
py random_names.py
```
```
py random_passwords.py
```
```
py random_stopwords.py
```
```
py random_word.py
```
6. Or start the program with a counting up input method
```
py "count up.py"
```

</details>


## Start the program on Linux, like Fedora/ Ubuntu
<details>
<summary>see more</summary>

1. <a traget="blank" href="https://github.com/RealCocoArdo/bruteforce-random-bitcoin-privatekeys/archive/refs/heads/main.zip">Download</a> or clone the code
2. Open your terminal
3. Navigate to the folder where you stored the programm with `cd folderName` and `cd ..`
4. Install required packages via pip
```
pip install requests bitcoin time itertools random string wonderwords
```
5. Start the program
<br> Run one of the program files located at `/bruteforce-random-bitcoin-privatekeys-main/Linux/`
<br> You might need the change the properties of the .sh file by right clicking it and change it to "executable program"
<br> Then right click it and run it. Or open your terminal an bash the file
<br><br>

### If the start doesnt work you can start the .py -files directly:
<details>
<summary>see more</summary>

1. Open your terminal
2. Navigate to the folder where you stored the programm with `cd folderName` and `cd ..`
3. Start the program with the random input method of your choice
```
py random_.py
```
```
py random_names.py
```
```
py random_passwords.py
```
```
py random_stopwords.py
```
```
py random_word.py
```
4. Or start the program with a counting up input method
```
py "count up.py"
```

</details>

### Add the program to your application list as .desktop file:
<details>
<summary>see more</summary>

1. Open the `/Linux` folder.
2. Use a texteditor to edit a program you like to add. For example the `countup.sh` file.
3. Change the relative path `../"count up.py"` of the file to your actual path. This depends on where yoo stored your file.
It should look somethink like this: <br> `python3 /home/username/Documents/bruteforce-random-bitcoin-privatekeys-main/"count up.py"`
4. Save the file and close it.
5. Open the the .py file of the programm you like to add with a Texteditor. In my example the `count up.py` file
6. Change the line that looks like this:
```
fp = open('Succesfully found Wallets/countup/' + str(funded) + ' Bitcoin (' + str(i) + ').txt', 'x')
```
<br> This line is responsible for storeing the files of found wallets.
<br> You need the change the relative path again to your actual path. It might look like this then 
<br> `fp = open('/home/username/Documents/bruteforce-random-bitcoin-privatekeys-main/Succesfully found Wallets/countup/' + str`...
<br> Do the same for the line that looks like this:
```
fp = open('Allready looted Wallets/countup/' + str(funded) + ' Bitcoin (' + str(i) + ').txt', 'x')
```

7. Save the file and close it.
8. Open `/home/.local/share/applications/` | This might be diffrent depending on the Operating System you are using. I used Fedora.
9. Create a new file named `YourAppName.desktop`
10. Write the following text into that file:
```
[Desktop Entry]
Name=YourAppName
Keywords=Bruteforce;Bitcoin;
Categories=Development;IDE;
Exec=/home/username/Documents/bruteforce-random-bitcoin-privatekeys-main/Linux/countup.sh
Icon=/home/image.png
Type=Application
StartupNotify=true
```

11. Change the paths to your paths. Save and close.
12. Done

</details>
</details>

## Ressources

* <a href="https://learnmeabitcoin.com/tools/sha256/?string=%23BTC&multiple=1" taget="_blank">Sha256 calculator</a>
* <a target="blank" href="https://bfr.sate.tools">Check your adresses on diffrent forks of Bitcoin</a>