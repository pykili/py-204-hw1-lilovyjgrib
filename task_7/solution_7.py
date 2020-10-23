#я уже понял что решение не соответствует условию((
word = input()
rev_word = ''
l = len(word)
while l > 0:
    rev_word = rev_word + word[l - 1]
    l = l - 1
is_palindrom = rev_word == word
print(is_palindrom)
