import random
import csv

random_array = [random.randint(1, 1001) / 10]
number_elements = 1000000
for x in range(number_elements - 1):
    random_array.append(random.randint(1, 1001) / 10)

with open('large_csv.csv', mode='w') as large_file:
    large_file = csv.writer(large_file, delimiter=',')

    large_file.writerow(random_array)

print("Length of array: " + str(len(random_array)))
