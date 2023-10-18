def max_num (num1, num2, num3):
    max_number = max(num1, num2, num3)
    return max_number

# Example
result = max_num(66, 18, 23)
print("The maximum number is", result)

def mult_list (numbers):
    #initializes result to 1 (the identity element for multiplication because it leaves the other elements unchanged) and then iterates through the numbers in the list
    result = 1
    for number in numbers:
        result *= number
    return result

# Example
new_list = [1, 2, 3, 4]
result = mult_list(new_list)
print("The result of multiplying all the listed numbers is:", result)

def rev_string(stringElements):
    reversed_stringElements = stringElements[::-1]
    return reversed_stringElements

# Example
new_string = "Hi, how are you?"
result = rev_string(new_string)
print(result)

def num_within(number, start, end):
    # Checks if the number is within the specified range (inclusive) by using a conditional expression to check if the number is greater than or equal to start and less than or equal to end
    return start <= number <= end

# Examples
result1 = num_within(3, 2, 4)
result2 = num_within(3, 1, 3)
result3 = num_within(10, 2, 5)

print(result1)  # True
print(result2)  # True
print(result3)  # False

def pascal(n):
    result = []
    for i in range(n):
        row = [1 if j == 0 or j == i else row[j - 1] + row[j] for j in range(i + 1)]
        result.append(row)
    
    for row in result:
        print(" ".join(map(str, row)))

# Example: Print the first row and first 5 rows of Pascal's triangle
pascal(1)
print()  #empty line for separation
pascal(5)
