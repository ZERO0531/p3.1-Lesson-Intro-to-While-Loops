# 1. What does n += 1 do? Remove it and see what happens. (Then put it back.) ctrl + c may come in handy. 
# If I remove n += 1, the loop will run indefinitely because n will always be 0.

# 2. Change the code so that the loop repeats ten times instead of five.
print("Type in a message, and I'll display it ten times.")
message = input("Message: ")
print()
n = 0
while n < 10:
    print(f"{n + 1}. {message}")
    n += 1

# 3. See if you can change the code so that the message still prints ten times, but the numbers in front count by tens, like so:
print("Type in a message, and I'll display it ten times.")
message = input("Message: ")
print()

n = 0
while n < 10:
print(f"{(n + 1) * 10}. {message}")
n += 1

# 4. Change the code so that it asks the person how many times to display the message. Then, print it that many times. Still count by tens.
message = input("Type in a message: ")
num_times = int(input("How many times? "))

for i in range(1, num_times + 1):
    print(f"{i * 10}. {message}")
