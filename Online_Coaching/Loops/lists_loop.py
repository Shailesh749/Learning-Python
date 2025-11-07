countries = ['india', 'united states', 'australia', 'ireland', 'srilanka', 'iceland', 'cube', 'iran', 'poland']

# count all the countries which are starting with 'i'

# first method
# counter = 0
# for country in countries:
#    if country[0] == 'i':
#       counter = counter +1
# print(counter)





# second method
# counter = 0
# for country in countries:
#    if country.startswith('i'):
#       counter = counter +1
# print(counter)



# list all this countris which start with i as list
counter = 0
output = []
for country in countries:
   if country.startswith('i'):
      counter = counter +1
      output.append(country)
print(output)
