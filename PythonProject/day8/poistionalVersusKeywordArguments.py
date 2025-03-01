def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location} ?")

greet_with("John", "USA") # this is a positional argue=ment, the data needs to be entered properly or else it is printed wrong

greet_with("USA", "Jack")

greet_with(name = "Jack", location =  "USA") # keyword argument, specifically places everything where it needs to be