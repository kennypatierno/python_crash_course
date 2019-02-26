hello_world = "HeLLo, WoRld"

print(hello_world)
print(hello_world.title() + " in Title Case")
print(hello_world.upper() + " in UPPER")
print(hello_world.lower() + " in lower")

print("ADDING WHITESPACES")

white_space = "\n\t\tDOUBLE TAB COLA\n\t\t\t packed with new lines and tabs\n"
print(white_space)

hello_world_note = "Hey World,\n\n\tWant to go for a spin?\n\nBest Regards,\n\nKenny\n"

print(hello_world_note)
print("REMOVING WHITESPACES")
# rstrip, lstrip, strip
fourth_message = "extra spaces to right    "
print(fourth_message+"SEE THERE'S SPACE")
print(fourth_message.rstrip()+"SEE THERE'S NO SPACE")
print(fourth_message+"SEE THERE'S SPACE AGAIN")
#remove space and reassign variable
fourth_message = fourth_message.rstrip()
print(fourth_message+"SEE THERE'S NO SPACE AGAIN\n")

#int to string concat function
final_score = 100
name = "Kenny P"
print(name + " received a " + str(final_score) + "%")

import this
