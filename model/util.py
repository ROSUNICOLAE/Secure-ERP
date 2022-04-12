import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    id = []
    for char in range(number_of_small_letters):
        id.append(random.choice(string.ascii_lowercase))
    for char in range(number_of_capital_letters):
        id.append(random.choice(string.ascii_uppercase))
    for char in range(number_of_digits):
        id.append(random.choice(string.digits))
    for char in range(number_of_special_chars):
        id.append(random.choice(allowed_special_chars))
    random.shuffle(id)        

    return "".join(id)
