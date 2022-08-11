# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

# final_dictionary = starting_dictionary["c"] = 7
# print(starting_dictionary)

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
# dict["c"] = [1,2,3]
# print(dict[1])

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }
# print(order["main"][2][0])
#^^ accessses the value with key 2, [0] gets the first item from the list

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))