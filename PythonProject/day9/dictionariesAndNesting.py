#intitalize dictionary
program_dictionary = {
    "Bug":"An error in the program that prevents it from running",
    "Function": "Piece of code that you can call over and over again",
}

# retrieve from dictionary
print(program_dictionary["Bug"])

#add to dictionary
program_dictionary["Loop"] = "The action of iterating through something many times"
print(program_dictionary)


# <---- Nesting ---->
dictionary = {
    key : [list],
    key : {dict},
}