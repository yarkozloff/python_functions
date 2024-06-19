#otus_course -> OtusCourse
#PythonIsTheBest -> python_is_the_best
user_input = (input('Введите текст: '))


import re # module regular expression 
def snake_camel_cases(user_input):
    if '_' in user_input:
        temp_split = user_input.split("_")
        return ''.join([s.capitalize() for s in temp_split])
    else:
        temp_split = re.findall('[A-Z][^A-Z]*', user_input)
        return '_'.join([s.lower() for s in temp_split])
    
print(snake_camel_cases(user_input))

'''
First attempt convert upper to lower case and delimiter "_"

        temp_split = "".join([(" " + i if i.isupper() else i) for i in user_input]).strip().split()
        temp_result = ''.join([s[:1].lower() + s[1:] + '_' for s in temp_split])
        return temp_result[:-1] # hack
'''