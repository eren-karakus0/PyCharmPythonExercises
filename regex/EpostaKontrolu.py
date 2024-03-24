import re

email_pattern = r"^[a-zA-Z0-9._%+-?]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

emails = ["?user@example.com", "user123@gmail", "invalid.email", "another_user@mail.co.uk"]

for email in emails:
    if re.match(email_pattern, email):
        print(f"{email} geçerli bir e-posta adresidir.")
    else:
        print(f"{email} geçerli bir e-posta adresi değildir.")
