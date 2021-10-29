investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000
invest = investment_in_bitcoin*bitcoin_to_usd
print(invest)

if invest < 30000:
    print("you don´t have enough money")
else:
    print("¡Congratulations!, you are millionaire")