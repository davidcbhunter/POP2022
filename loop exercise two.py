li = ["abc", "xyz", "1234", "Mr. Hunter", "S"]

for x in li:
    if len(x) > 5:
        break
    print(x)

a = []

b = [1,2,3,4,5,6,7,8,9,10,20,24,30,32,35,40,42]

for x in b:
    if x % 8 == 0:
        continue
    else:
        a.append(x)

print(a)


#DNA!!

dna = ["A","T","T","C","G","A"]

# make a function to combine the nucleic acids
# into one string

def Combine(dna_list):
    dna_string = ""
    for x in dna_list:
        dna_string += x
    return dna_string

d = Combine(dna)
print(d)
print(type(d))

#check if the string contains "ATTACAG"

