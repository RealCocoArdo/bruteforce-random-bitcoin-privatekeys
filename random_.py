import requests
import bitcoin
import time
import random
import string

while True:
    # generates a random key of length 5
    # random_key = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
    random_key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
    print(random_key)
    time.sleep(1.2)
    private_key = bitcoin.sha256(random_key)
    pub_key = bitcoin.privkey_to_pubkey(private_key)
    address = bitcoin.pubkey_to_address(pub_key)

    # Check if the address has any coins on it using the mempool.space API
    url = f"https://mempool.space/api/address/{address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")

    balance_sats = (data['chain_stats'])['funded_txo_sum'] - (data['chain_stats'])['spent_txo_sum']
    balance = format(balance_sats * 0.00000001, '.8f')
    funded_sats = (data['chain_stats'])['funded_txo_sum']
    funded = format(funded_sats * 0.00000001, '.8f')

    # Store Wallets with coins on it
    if data['chain_stats']['funded_txo_sum'] > data['chain_stats']['spent_txo_sum']:
        print('\n Succesfully created Wallet file \n')
        i = 1
        while True:
            try:
                fp = open('Succesfully found Wallets/urandom/' + str(funded) + ' Bitcoin (' + str(i) + ').txt', 'x')
                fp.write('Bitcoin Wallet Backup \n \n')
                fp.write('Your private key is: \n' + private_key + '\n \n')
                fp.write('Your public key is: \n' + pub_key + '\n \n')
                fp.write('Your adress is: \n' + address + '\n \n')
                fp.write('The random key was: \n' + random_key + '\n \n')
                fp.write('The balance is: \n' + str(balance) + ' Bitcoin \n \n')
                fp.close()
                break
            except IOError as e:
                i += 1        
    else:
        print('Empty Wallet')

    # Store allready looted wallets
    if data['chain_stats']['funded_txo_sum'] > 0:
        print('\n Created looted Wallet file \n')
        i = 1
        while True:
            try:
                fp = open('Allready looted Wallets/urandom/' + str(funded) + ' Bitcoin (' + str(i) + ').txt', 'x')
                fp.write('Bitcoin Wallet Backup \n \n \n')
                fp.write('Your private key is: \n' + private_key + '\n \n')
                fp.write('Your public key is: \n' + pub_key + '\n \n')
                fp.write('Your adress is: \n' + address + '\n \n')
                fp.write('The random key was: \n' + random_key + '\n \n')
                fp.write('The funded balance was: \n' + str(funded) + ' Bitcoin \n \n')
                fp.close()
                break
            except IOError as e:
                i += 1
