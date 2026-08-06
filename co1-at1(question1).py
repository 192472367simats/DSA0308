import re

email = "john.doe123@gmail.com"
mobile = "+91-9876543210"
password = "P@ssw0rd123"
dob = "15/08/2004"
reg = "23AIML1056"

email_pattern = r'^[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.(com|org|edu|in)$'
mobile_pattern = r'^\+91-[6-9]\d{9}$'
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!*])\S{8,}$'
dob_pattern = r'^\d{2}/\d{2}/\d{4}$'
reg_pattern = r'^\d{2}[A-Z]{5}\d{4}$'

print("Email:", bool(re.fullmatch(email_pattern, email)))
print("Mobile:", bool(re.fullmatch(mobile_pattern, mobile)))
print("Password:", bool(re.fullmatch(password_pattern, password)))
print("Date of Birth:", bool(re.fullmatch(dob_pattern, dob)))
print("Register Number:", bool(re.fullmatch(reg_pattern, reg)))
