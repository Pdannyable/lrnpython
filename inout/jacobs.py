children = []

with open("children.csv") as file:
    for line in file:
        name, gender, mother, position = line.rstrip().split(",")
        child = {"name": name, "gender": gender, "mother": mother, "position": position}
        children.append(child)
# line 6 achieves same thing as ln 11-15
"""
        child = {}
        child["name"] = name
        child["gender"] = gender
        child["mother"] = mother
        child["position"] = position
"""
def get_name(child):
    return child["name"]

for child in sorted(children, key=get_name, reverse=False):
        print(f"{child['name']} was Jacob's {child['gender']} {child['mother']}'s {child['position']} child")