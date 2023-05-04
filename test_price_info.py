import price_info as price

def test_total_cost_shopping():
 result=0

 test=46.75
 result=price.total_cost_shopping()
 assert (result == test)
def test_cost_of_fruit():
