input_file = 'Input/students.txt'
input_file_obj = open(input_file)

content = input_file_obj.read()
input_file_obj.close()

students = content.split()

name = input('ism kiriting: ')

if name in students:
    result = f"{name} faylda mavjud"
else:
    result = f"{name} faylda mavjud emas"

print(result)

output_file = 'Output/output18.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(result)
output_file_obj.close()