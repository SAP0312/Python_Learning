def collatz(input):
    number = int(input)
   # if number == 1:
    while(number !=1):
     if number % 2 == 0:
            number = number / 2
            print(str(number) + "\n")
            continue
     else:
        number = number * 3 + 1
        print(str(number) + "\n")
        continue
value = input("Please enter a integer \n")
collatz(value)
print("There you go it's 1")