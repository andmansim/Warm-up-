def bitcointoeuros(monto_bitcoin, valor_bitcoin_euros):
    euros_value = monto_bitcoin * valor_bitcoin_euros
    return euros_value
Bitcoin_value_euros = 25000
Bitcoin_amount = 1 
result = bitcointoeuros (Bitcoin_value_euros,Bitcoin_amount)


if result < 30000:
        print("¡Warning!, yours bitcoins are coming down")
else:
        print("All correct")

 