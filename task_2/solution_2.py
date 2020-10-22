char_counter2 = 0
user_input = input()
for character in user_input:
  char_counter1 = 0
  for a in user_input:
    if a == character:
      char_counter1 = char_counter1 + 1
  if char_counter1 > char_counter2:
    char_counter2 = char_counter1
    most_frequent_character = character
print(most_frequent_character)
