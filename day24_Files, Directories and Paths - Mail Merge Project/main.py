
# READING THE FILE
# using the keyword "with" will make the computer automatically close the file 
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# OVERWRITING THE FILE
# by default, mode is "r", meaning read. Changing mode to "w" allows us to read
# this will overwrite all text currently in the file
# if the system can't find the file, it will create one itself
with open("new_file.txt", mode = "w") as file:
    file.write("New text.")

# APPENDING THE FILE
# Changing mode to "a" allows us to append
with open("my_file.txt", mode = "a") as file:
    file.write("\nNew text.")
