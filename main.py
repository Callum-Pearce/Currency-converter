import forex_python.converter as Converter

def convert_currency(amount, from_currenncy :  str, to_currency: str):
    exchange_rate = Converter.get_rate(
        base_cur = from_currenncy,
        dest_cur = to_currency
    )
    converted_amount = amount * exchange_rate
    return converted_amount

current_currency         = input("current currency: ").upper()
current_currency_amount = float(input("current ammount: "))
desired_currency         = input("desired currency: ").upper()

result = convert_currency(
    amount          = current_currency_amount,
    from_currenncy  = current_currency,
    to_currency     = desired_currency
)
print(f"{current_currency_amount:.2f} {current_currency} is equal to {result:.2f} {desired_currency}")
 