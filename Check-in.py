import amino
    # If amino.py is not installed yet, do pip install amino.py

client = amino.Client() # Declares the Client

client.login(email="YOUR_EMAIL", password="YOUR_PASSWORD")
    # Enter your Credentials

subclients = client.sub_clients() 

for name, id in zip(subclients.name, subclients.comId):
    print(name, id)
    # Will print the community IDs additionally
    subclient = amino.SubClient(comId = id, profile=client.profile)
    subclient.check_in()
    # Check-in indefinetly
    subclient.lottery()
    # Can remove the lottery if you want to continue checking in indefinetly, the script will stop after it tries to attempt the lottery again


print('Total Coins: ' + client.get_wallet_info().totalCoinsFloat) # Will print your coins afterwards

# A simple Check-In all your communities script