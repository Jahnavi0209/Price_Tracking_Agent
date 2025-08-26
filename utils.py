def clean_price(price_str):
    # import pdb; pdb.set_trace()
    # remove commas, currency symbols, spaces
    price_str = price_str.replace(",", "").replace("₹", "").strip()
    
    # If it ends with a dot, remove it (e.g., "61499." → "61499")
    if price_str.endswith("."):
        price_str = price_str[:-1]

    # If it has decimals (e.g., "61499.00"), take only integer part
    if "." in price_str:
        price_str = price_str.split(".")[0]
    return int(price_str)