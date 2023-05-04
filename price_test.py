import price_info as price

def test_total_cost_shopping():
 result=0
 test=46.75
 result=price.total_cost_shopping()
 assert (result == test)
def test_cost_of_fruit():
    result = 0

    quantity=15
    test = 12.0
    result = price.cost_of_fruits('apple', 10)
    assert (result == test)
