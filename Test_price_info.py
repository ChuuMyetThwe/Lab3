import price_info as price
def test_total_cost_shopping():
    test_result = 46.75
    result = price.total_cost_shopping()

    assert (result == test_result)

def test_cost_of_fruit():
    input = 'orange'
    quantity = 2
    test_result = 2.80

    result = price.cost_of_fruits(input, quantity)

    assert (result == test_result)