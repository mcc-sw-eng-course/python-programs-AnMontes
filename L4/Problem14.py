

class MyPowerClass:
    def __init__(self):
        self.classList = []

    def add_item(self, item):
        if type(item) in [int, float]:
            self.classList.append(item)
        else:
            raise TypeError("The type of the argument is not a float or integer.")

    def remove_item(self, pos):
        if type(pos) in [int]:
            if 1 <= pos < len(self.classList) + 1:
                self.classList.pop(pos - 1)
            else:
                raise ValueError("The index cannot be lower than 1 or grater than the length of the array.")
        else:
            raise TypeError("The type of the index is not an integer.")

    def sort_list(self):
        index_lower = 0
        index_upper = 1
        decrease = 0

        while index_lower < len(self.classList) - 1:
            while self.classList[index_lower - decrease] > self.classList[index_upper - decrease]:
                class_list1 = self.classList[index_upper - decrease]
                self.classList[index_upper - decrease] = self.classList[index_lower - decrease]
                self.classList[index_lower - decrease] = class_list1
                decrease += 1
                if index_lower - decrease < 0:
                    break

            index_lower += 1
            index_upper += 1
            decrease = 0

    def l_merge(self, array2):
        array1 = []
        for x in array2:
            if type(x) not in [int, float]:
                raise ValueError("An element or more is not an integer or float.")

        for x in array2:
            array1.append(x)

        for x in self.classList:
            array1.append(x)

        self.classList = array1

    def r_merge(self, array2):
        for x in array2:
            if type(x) not in [int, float]:
                raise ValueError("An element or more is not an integer or float.")

        for x in array2:
            self.classList.append(x)

    def save_to_text_file(self, filename):
        with open(filename + ".txt", "w") as fobj:
            for x in self.classList:
                fobj.write(str(x))
                fobj.write("\n")

    @staticmethod
    def read_from_text_file(filename):
        with open(filename + ".txt") as fobj:
            text = fobj.read()

        text2 = text.split('\n')
        text2.pop(-1)
        text3 = []

        for x in range(len(text2)):
            if "." in text2[x]:
                text3.append(float(text2[x]))
            else:
                text3.append(int(text2[x]))

        return text3


array = MyPowerClass()
array.add_item(5)
array.add_item(2.2)
array.add_item(4)
array.add_item(4)
array.add_item(1)
array.add_item(8)
array.add_item(4.5)
array.remove_item(1)
array.sort_list()
array.l_merge([6, 7, 4, 9])
array.r_merge([1, 1, 1, 1])
array.save_to_text_file("test1")
read = array.read_from_text_file("test1")

#print(read)
