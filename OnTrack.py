# OnTrack is an interactive Python program that allows the user to keep track of their food consumption (option 1), physical activity (option 2), and water intake (option 3)
# the user can also check their logs throughout the day (option 4) and finally calculate their total at the end of the day (option 5)
# to learn more about the program, feel free to watch this demo video: https://youtu.be/ySRz24RFVrE

def main():
    # initialize dictionaries and list to store values that get inputted by user
    food = {}
    exercise = {}
    water = []
    
    print("Welcome to OnTrack - an easy way for you to stay on track with your health!")
    message()
    answer = int(input("Your response: "))
    
    while True:
        # display if user inputs invalid number
        while answer != 1 and answer != 2 and answer != 3 and answer != 4 and answer != 5:
            answer = int(input("Please type in a valid response: "))
        # track user's food intake
        while answer == 1:
            new_food = food_counter()
            food.update(new_food)
            message()
            answer = int(input("Your response: "))
        # track user's exercise activities
        while answer == 2:
            new_exercise = exercise_counter()
            exercise.update(new_exercise)
            message()
            answer = int(input("Your response: "))
        # track user's water intake
        while answer == 3:
            water.extend(water_counter())
            message()
            answer = int(input("Your response: "))
        # display user's inputted logs
        while answer == 4:
            food_sum = 0
            for value in food.values():
                food_sum += value
            exercise_sum = 0
            for value in exercise.values():
                exercise_sum += value
            water_sum = sum(water)
            progress(food_sum, exercise_sum, water_sum)
            message()
            answer = int(input("Your response: "))
        # display user's final calculations for the day
        if answer == 5:
            calculator_food(**food)
            calculator_exercise(**exercise)
            print("You had a total of " + str(sum(water)) + " glasses of water.")
            print("Thank you for using OnTrack. Make sure to come back tomorrow and track your health!")
            break

# display message explaining what each value represents in Python program
def message():
    print("Enter 1 to track your food.")
    print("Enter 2 to track your exercise.")
    print("Enter 3 to track your water intake.")
    print("Enter 4 to see your current progress.")
    print("Enter 5 to calculate your total for the day.")

# summarize user's inputted logs and display summary
def progress(food_sum, exercise_sum, water_sum):
    print("Currently, you have: ")
    print("Consumed a total of " + str(food_sum) + " calories.")
    print("Burnt a total of " + str(exercise_sum) + " calories.")
    print("Had a total of " + str(water_sum) + " glasses of water.")
    print()

# track user's food intake
def food_counter():
    food = {}
    answer = input("Enter name of food item: ")
    food[answer] = int(input("Enter number of calories: "))
    more = input("Noted! To add to your food intake, type 'Yes'. To go back, type 'Done': ")
    while True:
        while more != 'Yes' and more != 'Done':
            more = input("Please type in a valid response: ")
        while more == 'Yes':
            answer = input("Enter name of food item: ")
            food[answer] = int(input("Enter number of calories: "))
            more = input("Noted! To add to your food intake, type 'Yes'. To go back, type 'Done': ")
        if more == 'Done':
            return food

# track user's exercise activity
def exercise_counter():
    exercise = {}
    answer = input("Enter name of physical activity: ")
    exercise[answer] = int(input("Enter number of calories burned: "))
    more = input("Noted! To add to your  physical activities, type 'Yes'. To go back, type 'Done': ")
    while True:
        while more != 'Yes' and more != 'Done':
            more = input("Please type in a valid response: ")
        while more == 'Yes':
            answer = input("Enter name of physical activity: ")
            exercise[answer] = int(input("Enter number of calories burned: "))
            more = input("Noted! To add to your  physical activities, type 'Yes'. To go back, type 'Done': ")
        if more == 'Done':
            return exercise

# track user's water intake
def water_counter():
    water = []
    answer = int(input("Enter the number of glasses (8 ounces) of water that you had: "))
    water.append(answer)
    more = input("Noted! To add to your water intake, type 'Yes'. To go back, type 'Done': ")
    while True:
        while more != 'Yes' and more != 'Done':
            more = input("Please type in a valid response: ")
        while more == 'Yes':
            answer = int(input("Enter the number of glasses (8 ounces) of water that you had: "))
            water.append(answer)
            more = input("Noted! To add to your water intake, type 'Yes'. To go back, type 'Done': ")
        if more == 'Done':
            return water

# calculate user's total food intake
def calculator_food(**food):
    sum_food = 0
    for value in food.values():
        sum_food += value
    print("You consumed a total of " + str(sum_food) + " calories by having the following:")
    for food in food.keys():
        print(food)

# calculate user's total exercise activity
def calculator_exercise(**exercise):
    sum_exercise = 0
    for value in exercise.values():
        sum_exercise += value
    print("You burned a total of " + str(sum_exercise) + " calories by doing the following:")
    for exercise in exercise.keys():
        print(exercise)

if __name__ == '__main__':
    main()
