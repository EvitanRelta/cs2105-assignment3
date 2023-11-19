# !/usr/bin/env python3
import os
import sys

from Cryptodome.Hash import SHA256


def generate_mac(key: bytes, data: bytes) -> bytes:
    h = SHA256.new(data)
    h.update(key)
    return h.digest()


if len(sys.argv) < 3:
    print("Usage: python3 ", os.path.basename(__file__), "key_file_name document_file_name")
    sys.exit()

key_file_name = sys.argv[1]
file_name = sys.argv[2]

# get the authentication key from the file
with open(key_file_name, "rb") as key_file:
    key = key_file.read()

# read the input file
with open(file_name, "rb") as file:
    file_content = file.read()

# First 32 bytes is the message authentication code
mac_from_file = file_content[:32]

# Use the remaining file content to generate the message authentication code
data = file_content[32:]
mac_generated = generate_mac(key, data)

if mac_from_file == mac_generated:
    print("yes")
else:
    print("no")
