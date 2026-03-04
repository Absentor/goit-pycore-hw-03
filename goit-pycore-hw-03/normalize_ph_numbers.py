import re


def normalize_ph_numbers(phone_number):
    digits = re.sub(r"\D", "", phone_number)

    if digits.startswith("380"):
        return "+" + digits

    if digits.startswith("0"):
        return "+38" + digits

    return "+" + digits