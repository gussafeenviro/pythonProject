def letter_check(word, letter):
  for character in word:
    if letter == character:
      return True
  return False

print(letter_check("Bashiruu", "q"))