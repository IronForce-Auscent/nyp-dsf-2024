def sgd_to_usd(amt): 
    exchange_rate = 0.73
    return amt * exchange_rate

def sgd_to_eur(amt): 
    exchange_rate = 0.63
    return amt * exchange_rate

to_convert = input("Enter the currency to convert to (EUR, USD): ").upper()
amt_to_convert = float(input("Enter the currency to convert from (SGD): "))
if to_convert not in ["USD", "EUR"]:
    print(f"Invalid currency. We are not able to convert from SGD to {to_convert}.")
else:
    if to_convert == "USD": 
        print(f"{amt_to_convert} SGD is {sgd_to_usd(amt_to_convert)} USD.")
    else:
        print(f"{amt_to_convert} SGD is {sgd_to_eur(amt_to_convert)} EUR.")