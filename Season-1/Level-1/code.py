'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    gross = 0
    paid = 0

    for item in order.items:
        if item.type == 'payment':
            if isinstance(item.amount, (int, float)):
                gross += item.amount
        elif item.type == 'product':
            if item.amount < 0 or item.quantity < 0:
                return "Invalid product amount or quantity: %s, %s" % (item.amount, item.quantity)
            paid += item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type


    net = gross - paid
    net = round(net, 2)     #for floating point
    gross = round(gross, 2)

    if gross > 9999:
        return "Total amount payable for an order exceeded"
    elif net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id