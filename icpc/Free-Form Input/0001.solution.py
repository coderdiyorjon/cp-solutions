from sys import stdin

for line in stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(",")
    numbers = (float(part.replace(" ", "")) for part in parts)
    total = sum(numbers)
    print(total)
