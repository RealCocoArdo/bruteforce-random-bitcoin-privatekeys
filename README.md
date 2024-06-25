<h1>Bruteforce random private keys<h1>

<h2>Disclaimer</h2>

<b>This code could be illegal in your country.<b> Do not download it, if thats the case<br>
I take no responsibilitiy for abusing my code for a bad purpose.

<h2>How it works</h2>

1. It takes a random input, for example common names or passwords
2. Then it uses sha256 to create a private Key of it (how it was done in the old days)
3. It creates a Bitcoin adresses of that private key
4. It checks on mempool.space if there is or was money on that adress
5. It stores a .txt file of Succesfull and allready looted private keys

<h2>Requirements </h2>

* Latest Python version
* Pip installed

<h2>Start the program</h2>

1. Download the code
2. Open your terminal or cmd
3. Navigate to the folder where you stored the programm with `cd folderName` and `cd ..`
4. Install required packages via pip
5. Start the file with the random input method of your choice
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
6. Or start the file with a counting up input method
```
py "count up.py"
```

<h2>Ressources</h2>

<a href="https://learnmeabitcoin.com/tools/sha256/?string=%23BTC&multiple=1" taget="_blank">Sha256 calculator</a>

| Seconds | Minutes | Hours |
|---------|---------|------|
| 60 | 1 | |
| 300 | 5 | |
| 600 | 10 | |
| 3600 | 60 | 1 |
| 18000 | 300 | 5 |
| 86400 | 1440 | 24 |
