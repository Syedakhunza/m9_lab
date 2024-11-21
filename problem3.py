#syeda khunza fatima
#19th, nov 2024

#problem3, Using a while loop, ask the user to enter a number. Append each entered number to a list and add them together. Continue asking for a number until the sum of the list of numbers is greater than 100.

#this program show us that the loop end when the sum exceeds to 100

numbers = []3

total_sum = 0

while total_sum <= 100:
    num = float(input("Enter a number: "))
    
    numbers.append(num)
    
    total_sum = sum(numbers)

print(f"The numbers entered are: {numbers}")
print(f"The total sum of the numbers is: {total_sum}")


