

class Statistics:
    def __init__(self, i_numbers):
        self.i_numbers = i_numbers
        self.len_array = len(i_numbers)
        self.sum1 = 0
        self.std_dev1 = 0
        self.error = 0.00001
        self.median1 = 0
        i_numbers1 = 0
        index_lower = 0
        index_upper = 1
        decrease = 0
        self.median1 = self.len_array / 2

        for element in self.i_numbers:
            self.sum1 += element

        self.mean1 = self.sum1 / self.len_array

        # Sort array. Insertion Method.
        while index_lower < self.len_array - 1:
            while self.i_numbers[index_lower - decrease] > self.i_numbers[index_upper - decrease]:
                i_numbers1 = self.i_numbers[index_upper - decrease]
                self.i_numbers[index_upper - decrease] = self.i_numbers[index_lower - decrease]
                self.i_numbers[index_lower - decrease] = i_numbers1
                decrease += 1
                if index_lower - decrease < 0:
                    break

            index_lower += 1
            index_upper += 1
            decrease = 0

    def mean(self):

        return self.mean1

    def std_dev(self):

        for element in self.i_numbers:
            self.std_dev1 += (element - self.mean1) * (element - self.mean1)

        self.std_dev1 = self.std_dev1 / (self.len_array - 1)

        """ By the Babylonian Method """

        s = self.std_dev1
        x = self.std_dev1
        while s - x/s > self.error:
            s = (s + x/s) / 2

        self.std_dev1 = s

        return round(self.std_dev1, 5)

    def median(self):

        if self.median1 > int(self.median1):
            return self.i_numbers[int(self.median1)]
        else:
            return (self.i_numbers[int(self.median1 - 1)] + self.i_numbers[int(self.median1)]) / 2

    def n_quartil(self, n):
        quartil1 = self.median1 / 2
        quartil3 = (self.median1 / 2) + self.median1
        if n == 1:
            if quartil1 > int(quartil1):
                return self.i_numbers[int(quartil1)]
            else:
                return (self.i_numbers[int(quartil1 - 1)] + self.i_numbers[int(quartil1)]) / 2
        elif n == 2:
            return self.median()
        elif n == 3:
            if quartil3 > int(quartil3):
                return self.i_numbers[int(quartil3)]
            else:
                return (self.i_numbers[int(quartil3 - 1)] + self.i_numbers[int(quartil3)]) / 2
        else:
            return "Not a valid input"

    def n_percentil(self, n):
        p = (n * self.len_array) / 100
        p = int(round(p))

        return self.i_numbers[p - 1]


# i_numbers = [7, 8, 5.8, 2, 4.3, 4, 6, 3, 1.5, 8, 10]

# obj_statistics = Statistics(i_numbers)


# print("Sorted array: " + str(obj_statistics.i_numbers))
# print("Number of elements: " + str(obj_statistics.len_array))
# print("")
# print("Mean: " + str(obj_statistics.mean()))
# print("SD: " + str(obj_statistics.std_dev()))
# print("Median: " + str(obj_statistics.median()))
# print("")
# print("1-quartil: " + str(obj_statistics.n_quartil(1)))
# print("2-quartil: " + str(obj_statistics.n_quartil(2)))
# print("3-quartil: " + str(obj_statistics.n_quartil(3)))
# print("")
#
# print("98-percentil: " + str(obj_statistics.n_percentil(98)))



print("Hola")