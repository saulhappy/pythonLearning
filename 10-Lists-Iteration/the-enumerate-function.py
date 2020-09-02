# heroes = ["superman", "wolverine", "capt. america"]

# for index, hero in enumerate(heroes, 1):
#     print(f"{hero} is number {index}")

for index, num in enumerate([1, 1, 2, 2, 5]):
    if index < num:
        continue

    print(num)
