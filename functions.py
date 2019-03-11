# Make a function to determine if a number is odd or even

def odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Given a list return the unique names in the list

def unique_names(list_of_names):
    unique_bois = list(set(list_of_names))
    return unique_bois


# Make a function that determines if a word is a palindrome

def palindrome_detector(string):
    reverse_string = string[::-1]
    if reverse_string == string:
        return "This is a palidrome"
    else:
        return "This is not a palindrome"

print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7,8]))
print(unique_names(['john', 'john', 'john', 'brenda', 'brendee', 'brenda']))
print(palindrome_detector('racecar'))
print(palindrome_detector('not'))
