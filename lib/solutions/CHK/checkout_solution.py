def checkout(skus):
    """In a normal supermarket, things are identified using Stock Keeping Units, or SKUs.
In our store, we'll use individual letters of the alphabet (A, B, C, and so on).
Our goods are priced individually. In addition, some items are multi-priced: buy n of them, and they'll cost you y pounds.
For example, item A might cost 50 pounds individually, but this week we have a special offer:
 buy three As and they'll cost you 130."""
    skus = skus.split()
    total_sum = 0
    store_skus = {"A": 50, "B": 30, "C": 20, "D": 15}
    skus_discount = {"A": {
        "min_prod": 3,
        "rate": 130 / 150},
        "B": {
            "min_prod": 2,
            "rate": 45 / 50}
    }
    for sku in skus:
        if sku is not store_skus:
            total_sum = -1
            break
        if sku[0].is
    return -1


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


