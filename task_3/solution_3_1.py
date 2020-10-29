alphabet = ''
user_input = input()
for letter in user_input:
    if letter not in alphabet:
        alphabet = alphabet + letter
print(alphabet)
