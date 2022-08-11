#nesting
captials = { 
    "france": "paris",
    "germany" : "berlin"
}

#nesting a list in a dictionary
#has one key with 3 values
travel_log = {
    "France": {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visited": 12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visited" : 5 },
    }
#^^
#challenge: change the france entry so that it contains another dictionary
#nested dictionary uses the ley cities_visited for the values you can keep the list of Paris Lille and Dijon

#nesting dictionary in a list
travel_log2 = {
    {
        "Country" : "France", 
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visited": 12
    },
    {
        "country" : "Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visited" : 5 },
    }


#nested list in a list
alpha = ["a", "b", "c", ["d", "e","f"]]

dicti =  {"dict" : {"rand" : [1,2,3],}}
#^^ dictionary that has a dictionary as a value
print(dicti)
#prints {'dict': {'rand': [1, 2, 3]}}
print(dicti["dict"])
#{'rand': [1, 2, 3]}
print(dicti["dict"]["rand"])
#prints 1,2,3