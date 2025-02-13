import re

def extract_reg_numbers():
    # UK registration number pattern
    pattern = r'[A-Z]{2}\d{2}\s?[A-Z]{3}|[A-Z]{2}\d{2}\s?[A-Z]{2,3}|[A-Z]{1,2}\d{1,4}\s?[A-Z]{3}'

    # Find all matches
    reg_numbers = re.findall(pattern, content)
    return reg_numbers

# Read the file
with open('TestData/car_input - V5.txt', 'r') as file:
    content = file.read()

