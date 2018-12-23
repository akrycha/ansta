from decimal import Decimal


def list_generator():
    end = Decimal(2.0)
    decimal_list = []
    while end <= Decimal(5.5):
        decimal_list.append(end)
        end += Decimal(0.5)
    print(decimal_list)


list_generator()
