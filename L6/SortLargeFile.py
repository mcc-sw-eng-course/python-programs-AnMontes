import csv
import os
from datetime import datetime


class SortLargeCsv:
    def __init__(self):
        self.data_array = []
        self.data_file_path_name = ""
        self.data_output_path_file_name = ""
        self.error = 0
        self.input_state = 0
        self.output_state = 0
        self.start_time = 0
        self.finish_time = 0
        self.elapsed_time = 0

    def set_input_data(self, file_path_name, delimit):
        if type(file_path_name) is str:
            self.data_file_path_name = file_path_name
        else:
            raise ValueError("Filename must be of type string.")

        if delimit not in [',', '\n', '\t']:
            raise ValueError("Delimiter must be supported.")

        if os.access(self.data_file_path_name, os.F_OK):
            if os.access(self.data_file_path_name, os.R_OK):
                print("File Exists and is readable")
            else:
                raise Exception("File isn't readable.")
        else:
            raise Exception("File doesn't exists.")

        with open(self.data_file_path_name) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=delimit)
            for row in read_csv:
                for index in row:
                    try:
                        self.data_array.append(float(index))
                    except ValueError:
                        self.error = 1
                        print("The selected delimiter is incorrect.")
        self.input_state = 1
        #print(self.data_array)

    def set_output_data(self, file_path_name, delimit):
        if self.input_state and not self.error:
            if type(file_path_name) is str:
                self.data_output_path_file_name = file_path_name.replace(".csv", "")
                self.delimit = delimit
                # with open(self.data_output_path_file_name + ".csv", mode='w') as csvwriter:
                #     csvwriter = csv.writer(csvwriter, delimiter=delimit)
                #     csvwriter.writerow(self.data_array)
            else:
                raise ValueError("Filename must be of type string.")
        else:
            raise Exception("set_input_data hasn't been executed.")

        self.output_state = 1

    def execute_merge_sort(self):
        if self.output_state and not self.error:
            self.start_time = datetime.now()
            result = self.merge_sort(self.data_array)
            self.finish_time = datetime.now()
            self.elapsed_time = self.finish_time - self.start_time
            with open(self.data_output_path_file_name + "_merge.csv", mode='w') as csvwriter:
                csvwriter = csv.writer(csvwriter, delimiter=self.delimit)
                csvwriter.writerow(result)
        else:
            raise Exception("set_output_data hasn't been executed.")

    def merge(self, left, right):
        result = []
        left_temp = 0
        right_temp = 0

        while left_temp < len(left) and right_temp < len(right):
            if left[left_temp] <= right[right_temp]:
                result.append(left[left_temp])
                left_temp += 1
            else:
                result.append(right[right_temp])
                right_temp += 1

        if left:
            result.extend(left[left_temp:])
        if right:
            result.extend(right[right_temp:])
        return result

    def merge_sort(self, m):
        if len(m) <= 1:
            return m

        middle = len(m) // 2
        left = m[:middle]
        right = m[middle:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)
        self.data_array = list(self.merge(left, right))
        return list(self.merge(left, right))

    def execute_heap_sort(self):
        if self.output_state and not self.error:
            self.start_time = datetime.now()
            result = self.heap_sort(self.data_array)
            self.finish_time = datetime.now()
            self.elapsed_time = self.finish_time - self.start_time
            with open(self.data_output_path_file_name + "_heap.csv", mode='w') as csvwriter:
                csvwriter = csv.writer(csvwriter, delimiter=self.delimit)
                csvwriter.writerow(result)
        else:
            raise Exception("set_output_data hasn't been executed.")

    def heap_sort(self, array):
        len_array = len(array)

        for i in range(len_array, -1, -1):  # Iteration from last element to first.
            self.heap(array, len_array, i)

        for i in range(len_array - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heap(array, i, 0)

        return array

    @staticmethod
    def heap(array, len_array, i):
        curr_largest = i
        left = 2 * curr_largest + 1
        right = 2 * curr_largest + 2

        # comparison between elements and root.
        if left < len_array and array[i] < array[left]:
            curr_largest = left

        if right < len_array and array[curr_largest] < array[right]:
            curr_largest = right

        # if largest changed, swap the elements.
        if curr_largest != i:
            array[i], array[curr_largest] = array[curr_largest], array[i]

            SortLargeCsv.heap(array, len_array, curr_largest)

    def execute_quick_sort(self):
        if self.output_state and not self.error:
            self.start_time = datetime.now()
            result = self.quick_sort(self.data_array)
            self.finish_time = datetime.now()
            self.elapsed_time = self.finish_time - self.start_time
            self.data_array = result
            with open(self.data_output_path_file_name + "_quick.csv", mode='w') as csvwriter:
                csvwriter = csv.writer(csvwriter, delimiter=self.delimit)
                csvwriter.writerow(result)
        else:
            raise Exception("set_output_data hasn't been executed.")

    def quick_sort(self,lista):
        menor = []
        igual = []
        mayor = []
        if len(lista)>0:
            pivot = lista[0]
            for i in lista:
                if i < pivot:
                    menor.append(i)
                if i == pivot:
                    igual.append(i)
                if i > pivot:
                    mayor.append(i)
            return self.quick_sort(menor) + igual + self.quick_sort(mayor)
        else:
            return lista

    def get_performance_data(self):
        list_data = [str(len(self.data_array)), str(self.elapsed_time), str(self.start_time), str(self.finish_time)]

        print("Number of elements processed: " + list_data[0])
        print("Time consumed: " + list_data[1])
        print("Start time: " + list_data[2])
        print("Ending time: " + list_data[3])

        return list_data


#sort_data = SortLargeCsv()
#sort_data.set_input_data("large_csv - copia.csv", ',')
#print(sort_data.data_array)
#sort_data.set_output_data("outputcsv.csv", ',')
#sort_data.execute_quick_sort()
#print(sort_data.data_array)
# print(sort_data.data_array)
#sort_data.set_output_data("outputcsv.csv", ',')          # Falta checar con .txt, .docx, etc...
# sort_data.execute_merge_sort()
#sort_data.execute_heap_sort()
#sort_data.get_performance_data()

