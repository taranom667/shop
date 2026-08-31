import re

pattern = re.compile(r'^\\+?[1-9][0-9]{7,14}$')

phone_numbers = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123.456.7890",
        "+1 123-456-7890",
        "1 123-456-7890"
    ]


def validate_phone_number(value):

    def validate_phone_number(phone_number):
        if pattern.match(phone_number):
            return True
        else:
            return False