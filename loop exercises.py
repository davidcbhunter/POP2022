import random
# create a loop that counts
# from 0 to 100
for x in range(101):
    print(x)


# create a loop that multiplies the numbers from 1 to 20
answer = 1
for x in range(1,21):
    answer *= x
print(answer)

# create a loop that adds random numbers to a list
random_list = []
count = random.randint(25,120)
for x in range(count):
    #get another random number
    num = random.randint(1,100)
    random_list.append(num)

print(random_list)
# use a loop that finds the largest number, the smallest number,
# and the average of the list
average = 0
largest = random_list[0]
smallest = random_list[0]
for x in random_list:
    average += x
    # compare largest to ???
    if x > largest:
        largest = x
    # compare smallest to ???
    if x < smallest:
        smallest = x

average /= len(random_list) # count
print(average)
print(largest)
print(smallest)
