import price_info as price
def test_total_cost_shopping():
    test_case=price.cost_of_fruits('orange',2)
    expected_value=2.80
    assert test_case==expected_value

def test_cost_of_fruit():
    price_list={'orange' : 2, 'apple': 5}
    quantity_list={'orange': 4, 'apple' : 5}
    test_case=price.total_cost_shopping(price_list,quantity_list)
    expected_value=33
    assert test_case==expected_value