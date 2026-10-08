#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

    

# reading the names file
with open(file= r"day24_Files, Directories and Paths - Mail Merge Project\Mail Merge Project\Input\Names\invited_names.txt") as names_file:
    names = names_file.read()
    #print(names)

# splitting the file and putting all names into a list
names_list = names.split("\n")

"""
for each name, open the template file and read it. 
replace the placeholder in the template with the name, save the result to a variable
create the letter file in the desired location
overwrite contents with the variable
"""
for name in names_list:
    with open(file= r"day24_Files, Directories and Paths - Mail Merge Project\Mail Merge Project\Input\Letters\starting_letter.txt") as template_file:
        template = template_file.read()
        template_changed = template.replace("[name]", name)
        with open(file= fr"day24_Files, Directories and Paths - Mail Merge Project\Mail Merge Project\Output\ReadyToSend\letter_for_{name}.txt", mode= "w") as letter_file:
            letter = letter_file.write(template_changed)
