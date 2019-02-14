

class Directory:
    def __init__(self, name, address, phone, email):

        if "@" in email:
            self.directory = [
                {"name": str(name), "Address": str(address), "Phone": str(phone), "email": str(email)}
            ]
            # print(self.directory)
        else:
            raise ValueError("Enter a valid email address.")

    def add_record(self, name, address, phone, email):
        if name and address and phone and email:        # An empty variable can be checked as a boolean, if it
                                                        # is empty it will return 0
            if "@" in email:
                self.directory.append(
                    {"name": str(name), "Address": str(address), "Phone": str(phone), "email": str(email)}
                )
                # print(self.directory)
            else:
                raise ValueError("Enter a valid email address.")
        else:
            raise ValueError("An input is missing.")

    def save_record(self, filename):
        if type(filename) in [str]:
            with open(filename + ".txt", "w") as fobj:
                for x in self.directory:
                    fobj.write(str(x))
                    fobj.write("\n")
        else:
            raise TypeError("Filename must be a string.")

    def load_record(self, filename):
        if type(filename) in [str]:
            with open(filename + ".txt") as fobj:
                text = fobj.read()

            text = text.split('\n')
            text.pop(-1)
            text1 = []
            for x in range(len(text)):
                text1.append(eval(text[x]))

            # print(text1)

            self.directory = text1
            # print(self.directory)
            print("List loaded to the main object variable.")
        else:
            raise TypeError("filename must be of type string.")

    def search_from_record(self, pos, key):
        if type(key) in [str] and type(pos) in [int]:
            if key in ["name", "Address", "Phone", "email"]:
                # print(self.directxory)
                return self.directory[pos][key]
            else:
                raise ValueError("Key is not in the dictionary.")
        else:
            raise ValueError("An argument doesnt have a valid type.")


direct = Directory("Antonio", "Depa", "123245", "anmksd@hotmail.com")
Directory.add_record(direct, "BAA", "CASA ", "123", "a@")
Directory.load_record(direct, "test2")
# result = direct.search_from_record(0, "name")
# print(result)
