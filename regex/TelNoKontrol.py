import re

phone_pattern = r"^\d{3}-\d{3}-\d{4}$"

phone_numbers = ["123-456-7890", "555-abc-1234", "12-345-6789", "987-654-3210"]

for phone_number in phone_numbers:
    if re.match(phone_pattern, phone_number):
        print(f"{phone_number} geçerli bir telefon numarasıdır.")
    else:
        print(f"{phone_number} geçerli bir telefon numarası değildir.")
