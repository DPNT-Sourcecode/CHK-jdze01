def checkout(skus):
    """In a normal supermarket, things are identified using Stock Keeping Units, or SKUs.
In our store, we'll use individual letters of the alphabet (A, B, C, and so on).
Our goods are priced individually. In addition, some items are multi-priced: buy n of them, and they'll cost you y pounds.
For example, item A might cost 50 pounds individually, but this week we have a special offer:
 buy three As and they'll cost you 130."""
    def get_char_from_str(string):
        return "".join([i for i in string if not i.isdigit()])
    skus = skus.split()
    total_sum = 0
    store_skus = {"A": 50, "B": 30, "C": 20, "D": 15}
    skus_discount = {"A": {
        "min_prod": 3,
        "rate": 130 / 150},
        "B": {
            "min_prod": 2,
            "rate": 45 / 60}
    }
    for sku in skus:
        if type(sku) is not str or get_char_from_str(sku) not in store_skus.keys():
            total_sum = -1
            break
        elif sku[0].isdigit():
            sku_str = get_char_from_str(sku)
            num = int(sku[:len(sku_str)])
            total_sum = total_sum + \
                        ((num // skus_discount[sku_str]["min_prod"]) * store_skus[sku_str] * skus_discount[sku_str]["rate"]) + \
                        ((num % skus_discount[sku_str]["min_prod"]) * store_skus[sku_str])
        else:
            total_sum = total_sum + store_skus[sku]

    return total_sum


"""
Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+"""
