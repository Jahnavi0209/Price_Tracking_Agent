from typing import Tuple, Optional
from amazon_agent import amazon_price
from flipkart_agent import flipkart_price

def compare_prices(amazon_url: str, flipkart_url: str) -> Tuple[str, Optional[int], dict, dict]:
    """
    Return (decision, best_price, amazon_result, flipkart_result)
    decision ∈ {"amazon", "flipkart", "tie", "unknown"}
    """
    a = amazon_price(amazon_url)
    f = flipkart_price(flipkart_url)

    if a["ok"] and f["ok"]:
        if a["price"] < f["price"]:
            return ("amazon", a["price"], a, f)
        elif f["price"] < a["price"]:
            return ("flipkart", f["price"], a, f)
        else:
            return ("tie", a["price"], a, f)

    if a["ok"]:
        return ("amazon", a["price"], a, f)
    if f["ok"]:
        return ("flipkart", f["price"], a, f)

    return ("unknown", None, a, f)
