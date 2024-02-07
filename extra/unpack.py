"""USE OF UNPACKING"""


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
"""Coins here is in a list form"""


kotos = {"galleons": 100, "sickles": 50, "knuts": 25}
"""Kotos here is in a dictionary form"""


print(total(*coins), "Knuts")
"""introduction of * before the word 'coins' unpacks the list"""
print(total(**kotos), "Knuts")
"""introduction of double ** before the word 'kotos' unpacks the dictionary"""
