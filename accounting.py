melon_cost = 1.00

# make a list of customers' data tuples / for reusable


def all_datas(filename):
    datas_list = []
    datas = open(filename)
    for data in datas:
        data = data.split('|')
        _, customer_name, melon_qty, paid = data
        paid = ''.join(list(paid)[:-1])

        datas_list.append((customer_name, melon_qty, paid))
    datas.close()

    return datas_list


# print over/underpaid customers' datas
for data in all_datas('customer-orders.txt'):
    customer, melon_qty, paid = data
    paid = float(paid)
    melon_qty = int(melon_qty)
    customer_expected = melon_qty * melon_cost

    over_paid_format = format((paid - customer_expected), '.2f')

    if customer_expected < paid:
        print(f'{customer} overpaid {over_paid_format}')
    elif customer_expected > paid:
        print(f'{customer} underpaid {(customer_expected - paid):.2f}')
