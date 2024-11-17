
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping(price_list,quantity_list):
    result=[]
    total_cost = 0 #  for key in price_list.keys(): variable name inside that for loop must be equal as variable inside price_list[key]
    for key in price_list.keys():
        if key in quantity_list:
            total_cost+=price_list[key]*quantity_list[key]   
            result.append(total_cost)
            

    print("total cost = ", total_cost)
    return total_cost

def check_for_myself():
    result=[]#try to declare explicitly .keys()
    for key in price_list.keys():
        print(key)
        result.append(key)
    return result


def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    print("cost of ", quantity, fruit, "=", cost)
    return cost


def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping(price_list,quantity_list)


if __name__ == "__main__":
    check_for_myself()