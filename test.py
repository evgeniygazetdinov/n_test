
"""
Write a function with one parameter of type string, that returns a list containing the characters of the paramater. 
If a character in the string is a space or a digit greater than 5, remove them and do not include them in the array.

def str_to_list(param):
    # todo: write the logic
"""
import random 
import string

BASIC_LEN = 15

EXCEPT_NUMBERS = ['5', " "]

def check_five_or_space(symbol: str) -> bool:
    return False if symbol in EXCEPT_NUMBERS else True     

def str_to_list(param: str) -> list:
    return list(filter(check_five_or_space, param))

# test strings

def get_random_number():
    return random.randint(1, BASIC_LEN)

def generate_string() -> str:
    return "".join(random.choice(string.ascii_letters) for i in range(BASIC_LEN))

def get_random_wrong_char() -> str:
    index = random.randint(0, len(EXCEPT_NUMBERS) - 1)
    return EXCEPT_NUMBERS[index]

def get_place_for_insert(list_with_doubles):
    place_for_insert = get_random_number()
    random_value = place_for_insert
    if place_for_insert not in list_with_doubles:
        list_with_doubles.append(random_value)
        return random_value
    else:
        while random_value not in list_with_doubles:
            random_value = get_random_number()
    list_with_doubles.append(random_value)
    return random_value

def put_wrong_numbers_into_random_string(random_string: str) -> string:
    double_place = []
    quantity_wrong_digits = get_random_number()
    new_string = random_string
    for _ in range(quantity_wrong_digits):
        place_for_insert = get_place_for_insert(double_place)
        new_string = new_string[:place_for_insert] + get_random_wrong_char() + new_string[place_for_insert:]
    return new_string

def generate_string_with_five_or_space():
    random_string = generate_string()
    string_with_wrong_numbers = put_wrong_numbers_into_random_string(random_string)
    print(string_with_wrong_numbers)
    return string_with_wrong_numbers
        
if __name__ == "__main__":
    example = "5mysup erstring 5  "
    print(str_to_list(example))
    print(str_to_list(generate_string_with_five_or_space()))

