import collections

def remove_opposites(lst):
  i = 0
  while i < len(lst) - 2:
    if lst[i].upper() == lst[i + 1].upper() and (lst[i].isupper() and lst[i + 1].islower() or lst[i].islower() and lst[i + 1].isupper()):
        del lst[i]
        del lst[i]
    else:
        i += 1

def remove_all_opposites(polymer):
  length = len(polymer) + 1
  while len(polymer) < length:
    length = len(polymer)
    remove_opposites(polymer)
  return len(polymer)

# Part 1
f  = open("input.txt", "r")
content = f.read()
polymer = list(content)
print(remove_all_opposites(polymer))

# Part 2
polymer = list(content)
letters = list(set(content.upper()))
print(letters)

length_list = []
for l in letters:
  reduced_polymer = [i for i in polymer if i.upper() != l]
  length_list.append(remove_all_opposites(reduced_polymer))
print(min(length_list))