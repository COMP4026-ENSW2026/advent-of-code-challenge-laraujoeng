def CaloriesElf():
    i = 1
    caloriesSum = []

    print("Day %s" % i)
    while (i <= 5):
        calories = input("Calories:")
        if (calories.strip() == ""):
            i += 1
            print("Day %s" % i)
        else:
            caloriesSum[i] = int(calories) + caloriesSum[i]

    print( caloriesSum)

CaloriesElf()



