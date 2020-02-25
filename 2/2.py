import collections
        
def contains_value(d, s):
    c = 0
    for v in d.values():
        if s == v:
            return True
    return False
    
d = collections.defaultdict(int)
f = open("input.txt", "r")
content = f.readlines()

count_two = 0
count_three = 0
for line in content:
    for char in line:
        d[char] += 1
    count_two += contains_value(d, 2)
    count_three += contains_value(d, 3)
    d.clear()
        
print(count_two * count_three)
