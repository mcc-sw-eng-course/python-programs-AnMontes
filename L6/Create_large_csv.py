import random
import csv

random_array = [random.randint(1, 1001) / 10]
# random_array[0] = random.randint(1, 1001) / 10
for x in range(2999999):
    random_array.append(random.randint(1, 1001) / 10)

with open('large_csv.csv', mode='w') as large_file:
    large_file = csv.writer(large_file, delimiter=',')

    large_file.writerow(random_array)

print(len(random_array))

