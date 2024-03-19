from seven_api.SevenApi import SevenApi

client = SevenApi("InsertYourSuperSecretApiKeyFromSeven")
balance = client.balance.retrieve()
print(balance)
