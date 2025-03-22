text = """
ORIGIN
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""

# print(text[2].islower())
# print(filter(str.islower, text))

#print(list(filter(str.islower, text)))
# print("".join(list(filter(str.islower, text))))

cleaned_text = ''.join(filter(str.islower, text))
print(cleaned_text)
assert(len(cleaned_text) == 110)

# Save the cleaned text to preproinsulin-seq-clean.txt
with open('preproinsulin-seq-clean.txt', 'w') as f:
    f.write(cleaned_text)
    
# Part 1: Characters 1–24
part1 = cleaned_text[0:24]
assert(len(part1) == 24)
with open('lsinsulin-seq-clean.txt', 'w') as f:
    f.write(part1)    
    
# Part 2: Characters 25–54
part2 = cleaned_text[24:54]
print(part2)
assert(len(part2) == 30)
with open('binsulin-seq-clean.txt', 'w') as f:
    f.write(part2)
    
# Part 3: Characters 55 - 89
part3 = cleaned_text[54:89]
print(part3)
assert(len(part3) == 35)
with open('cinsulin-seq-clean.txt', 'w') as f:
    f.write(part3)      
    
# Part 4: Characters 90–110
part4 = cleaned_text[89:110]
print(part4)
assert(len(part4) == 21)
with open('ainsulin-seq-clean.txt', 'w') as f:
    f.write(part4)
    