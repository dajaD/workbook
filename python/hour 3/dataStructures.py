import random

#working with lists
state1 = "Deleware"
state2 = "illinois"

#list called usa with all the states in order when they joined the union
usa = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut',
 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia',
  'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 
  'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois',
   'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida',
    'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon',
     'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 
     'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho',
      'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska',
       'Hawaii']

#working with index###
#prints out the len() of the list
print(len(usa))

#shows that the index starts at 0, by printing the 49th element in the list
print(usa[49])

print()

#prints error "index out of range"
print(usa[50])

#prints out the value of the index 0 in list usa
#prints pennsylvania
print(usa[1])

#change value in the list at index 1
usa[1] = 'changesMade'

#prints the new list with the changes made above
print(usa)

#appending to the already created list
usa.append("newAddition")

#prints the new list with the append
print(usa)
#prints the last value which should be "newAddition"
print(usa[-1])