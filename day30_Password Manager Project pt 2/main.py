
# File not found

# with open("file.txt") as file:
#     file.read()

# Key error

# a_dictionary = {"key" : "value"}
# value = a_dictionary["non-existent key"]

# Index error

# fruit_list = ["apple", "banana", "orange"]
# fruit = fruit_list[3]

# Type error
# text = "abc"
# print(text + 5)



# Trying to use the Try, Except, Else, Finally

try: #try running these statements
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["haghgds"])
except FileNotFoundError: # if you run into the exception, do this
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message: # if you run into the exception, do this
    print(f"The key {error_message} does not exist")
else: # if try block was run without any exceptions, do this
    content = file.read()
    print(content)
finally: # whether or not the try block ran with or without exceptions, do this
    file.close()
    print("File was closed")
