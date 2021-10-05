# Write a python program which will keep adding a stream of numbers added by the user. The adding stops as soon as user presses 'q' key in the keyboard

sum = 0
my_list = []

while (True):
    userInput = input("Enter the price or press q to quit: \n")
    if(userInput != "q"):
        my_list.append(float(userInput))
        sum = sum + float(userInput)
        print(f"Your order total so far {sum}")
    else:
        print(f"Your sum is {sum}")
        print("Thanks for useing out Calculator.")
        print("Price of individual items: \n")
        for item in my_list:
            print(f"{my_list.index(item) + 1}. {item}")
        break
