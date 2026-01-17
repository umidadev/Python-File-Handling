input_file = 'Input/numbers.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

numbers = content.split()
numbers = list(map(
    lambda num: int(num),
    numbers
))

print(numbers)