import re

name = input("What's your name ? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
"""
lines 7-10 achieves the same purpose as lines 13-14
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
"""

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
