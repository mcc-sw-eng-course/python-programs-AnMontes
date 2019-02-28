import csv
import os


class SortLargeCsv:
    def __init__(self):
        self.data_array = []
        self.data_file_path_name = ""
        self.data_output_path_file_name = ""
        self.error = 0
        self.input_state = 0
        self.output_state = 0

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
                with open(self.data_output_path_file_name + ".csv", mode='w') as csvwriter:
                    csvwriter = csv.writer(csvwriter, delimiter=delimit)
                    csvwriter.writerow(self.data_array)
            else:
                raise ValueError("Filename must be of type string.")
        else:
            raise Exception("set_input_data hasn't been executed.")

        self.output_state = 1

    def execute_merge_sort(self):
        if self.output_state and not self.error:
            pass
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


sort_data = SortLargeCsv()
print(sort_data.data_array)
sort_data.set_input_data("large_csv.csv", ',')
print(sort_data.data_array)
sort_data.merge_sort(sort_data.data_array)
print(sort_data.data_array)
sort_data.set_output_data("outputcsv.csv", ',')          # Falta checar con .txt, .docx, etc...
#print(sorted_list)

