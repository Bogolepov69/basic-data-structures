# 1st program
result = 9**0.5 * 5
print(result)

# 2nd program
result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)

# 3rd program
expression1 = 2 * 2 + 2
expression2 = 2 * (2 + 2)
print(expression1)
print(expression2)
print(expression1 == expression2)  # Output: False

# 4th program
string_number = '123.456'
float_number = float(string_number)
shifted_number = float_number * 10
integer_part = int(shifted_number)
first_digit_after_decimal = integer_part % 10
print(first_digit_after_decimal)