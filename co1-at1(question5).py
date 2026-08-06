import re

pattern = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.(com|org|edu|in)$')

emails = [
    "john.doe123@gmail.com",
    "student01@yahoo.com",
    "abc@college.edu",
    "user@company.in",
    "wrongemail@",
    "test#gmail.com",
    "hello@gmail"
]

for email in emails:
    if pattern.fullmatch(email):
        print(email, "-> Valid")
    else:
        print(email, "-> Invalid")
