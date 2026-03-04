import random


def get_numbers_ticket(min_num, max_num, quantity):
    if quantity > (max_num - min_num + 1):
        return None
    else:
        unique_numbers = set()
        while len(unique_numbers) < quantity:
            unique_numbers.add(random.randint(min_num,max_num))
            return list(unique_numbers)