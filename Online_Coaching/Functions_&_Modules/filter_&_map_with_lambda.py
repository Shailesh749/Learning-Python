# filter(function, sequence)

# seq = [1, 2, 3, 4]

# odd = lambda x: True if x % 2 != 0 else False

# filtered_output = filter(odd, seq)
# print(filtered_output)
# print(f" Odd number in the above sequence are: {list(filtered_output)}")






# seq = [1, 2, 3, 4]

# filtered_output = filter(lambda x: True if x % 2 != 0 else False, seq)
# print(filtered_output)
# print(f" Odd number in the above sequence are: {list(filtered_output)}")





# seq = [1, 2, 3, 4]

# maped_output = map(lambda x: True if x % 2 != 0 else False, seq)
# print(maped_output)
# print(f" map output are: {list(maped_output)}")





seq = [1, 2, 3, 4]

maped_output = map(lambda x: x ** 2, seq)
print(maped_output)
print(f" map output are: {list(maped_output)}")