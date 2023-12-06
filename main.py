"""Python currency converter"""
import forex_python.converter as Converter

def convert_currency(amount, from_currenncy : str, to_currency: str):
    """
    Converts an amouynt from one currency to another using the forex_python library
    
    Parameter:
    - amount (float): The amount to be converted.
    - from_currecy (str): The code of the source currency.
    - to_currency (str): The code of the target currency.

    Returns:
    - float : the converted amount.
    """
    exchange_rate = Converter.get_rate(base_cur = from_currenncy,dest_cur = to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == "__main__":
    # get user imput for the current currency, amount, and desired currency.
    current_currency        = input("current currency: ").upper()
    current_currency_amount = float(input("current ammount: "))
    desired_currency        = input("desired currency: ").upper()

    # perform the currency conversion.
    result = convert_currency(
        amount          = current_currency_amount,
        from_currenncy  = current_currency,
        to_currency     = desired_currency
    )

    # display the result to the user.
    current = f"{current_currency_amount:.2f} {current_currency}"
    desired = f"{result:.2f} {desired_currency}"
    print(f"{current} is equal to {desired}")
