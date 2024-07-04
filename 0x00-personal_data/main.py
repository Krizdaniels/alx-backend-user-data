#!/usr/bin/env python3
"""
Main file
"""
import logging
from filtered_logger import (
    RedactingFormatter,
    filter_datum,
    get_db,
    get_logger,
    PII_FIELDS
)
from encrypt_password import hash_password, is_valid

fields = ["password", "date_of_birth"]
messages = [
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;"
    "date_of_birth=12/12/1986;",
    "name=bob;email=bob@dylan.com;password=bobbycool;"
    "date_of_birth=03/04/1993;"
]

# Redacting sensitive data in messages
for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

# Logging example with RedactingFormatter
message = (
    "name=Bob;email=bob@dylan.com;ssn=000-123-0000;"
    "password=bobby2019;"
)
log_record = logging.LogRecord(
    "my_logger", logging.INFO, None, None, message, None, None
)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))
# Printing logger return type annotation
get_logger_instance = get_logger()
print(get_logger_instance.__class__.__name__)  # Check logger type (optional)

# Printing PII_FIELDS length
print(f"PII_FIELDS: {len(PII_FIELDS)}")

# Database operations
try:
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        print(row[0])
    cursor.close()
    db.close()
except Exception as e:
    print(f"Error fetching data: {e}")

# Password hashing example
password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(f"Hashed Password: {encrypted_password}")
print(f"Verify Hashed Password: {hash_password(password)}")
print(f"Password Validation: {is_valid(encrypted_password, password)}")
