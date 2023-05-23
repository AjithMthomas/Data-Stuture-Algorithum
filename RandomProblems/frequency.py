# Sample array
my_array = [1, 2, 3, 2, 1, 3, 4, 5, 4, 1]

# Create an empty dictionary to store frequencies
frequency_dict = {}

# Iterate over the array
for element in my_array:
    # If element is already in the dictionary, increment its count
    if element in frequency_dict:
        frequency_dict[element] += 1
    # Otherwise, add the element to the dictionary with count 1
    else:
        frequency_dict[element] = 1

# Iterate over the dictionary and print the elements with their frequencies
for element, frequency in frequency_dict.items():
    print(f"Element: {element}, Frequency: {frequency}")
