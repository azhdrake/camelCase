user_input = input('Give me a sentence: ')
words = user_input.split(' ')

lower_list = [word.capitalize() for word in words]
lower_list[0] = str(lower_list[0]).lower()

new_string = ''

for word in lower_list:
    new_string += str(word)

print(new_string)