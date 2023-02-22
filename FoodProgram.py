import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

# instalist = []
# order_total = 0
# dis = 0
# disperc = 0.2
# diff = 0

person1 = fc.customer(
    "570",
    "Danni Sellyar",
    "97 Mitchell Way Hewitt Texas 76712",
    "dsellyarft@gmpg.org",
    "254-555-9362",
    False,
)
person2 = fc.customer(
    "569",
    "Aubree Himsworth",
    "1172 Moulton Hill Waco Texas 76710",
    "ahimsworthfs@list-manage.com",
    "254-555-2273",
    True,
)


def main():
    instalist = []
    order_total = 0
    dis = 0
    disperc = 0.2
    diff = 0
    print()
    print(f"Customer Name: {person2.get_name()}")
    print(f"Phone: {person2.get_phone()}")
    for i in dict:
        instance = fc.transaction(dict[i][0], dict[i][1], dict[i][2], dict[i][3])
        if person2.get_customerid() == instance.get_customerid():
            if person2.get_member_status() == True:
                order_total += float(instance.get_cost())
                dis += float(instance.get_cost()) * disperc
                diff += order_total - dis
                instalist.append(f"Order Item: ${dict[i][1]}   Price: ${dict[i][2]}")
            else:
                order_total += instance.get_cost()
                instalist.append(f"Order Item: ${dict[i][1]}   Price: ${dict[i][2]}")

    for i in instalist:
        print(i)

    if person2.get_member_status() == False:
        print(f"Total Cost: ${order_total}")
    else:
        print(f"Total Cost: ${format(order_total, '.2f')}")
        print(f"Member Discount: ${format(dis, '.2f')}")
        print(f"Total Cost after Discount: ${format(diff, '.2f')}")


main()
