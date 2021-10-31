# Author: Zachary Burleson
# Title: Hello World
# Date: 10/30/2021
# Description: Displays "Hello World!" and waits for the user to press
#       the enter key before the program terminates.

# initialize variable used to print message
hello = "Hello World!"
count = 5

# prints a message multiple times
def print_many_times(message, times):
    for _ in range(times):
        print(message)

# print message once
print(hello)
print("\n\n")

# print message many times
print_many_times(hello, count)
print("\n\n")

# print every letter in message on new line
for x in hello:
    print("\t" + x + "\n")

input("\nPress enter to exit.")
