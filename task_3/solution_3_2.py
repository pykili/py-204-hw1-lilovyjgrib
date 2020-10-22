alphabet = ''
all_input = ''
for a in 'a'*10:
  user_input = input()
  all_input = all_input + user_input
for letter in all_input:
  if letter not in alphabet:
    alphabet = alphabet + letter
print(alphabet)
