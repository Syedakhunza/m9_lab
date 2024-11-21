#syeda khunza fatima
#19th nov, 2024

#problem2, create a list called L that starts with the number 57 and 83 in it.

#this program demonstrates how to create and dynamically grow a list, which is essential in data manipulation tasks.

L = [57, 83]

counter = 0

while counter <= 10:
    L.append(counter)
    counter += 1

print(f"The list has {len(L)} elements.")
print(f"The third element in the list is {L[2]}.")


