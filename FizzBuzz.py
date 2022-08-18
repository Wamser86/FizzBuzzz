def test():
    try:
        while True:
            try:
                user_min = int(input("Please enter min : "))
                break
            except ValueError:
                print("Try again")

        while True:
            try:
                user_max = int(input("Please enter max: "))
                if user_max <= user_min:
                    print("Please enter a number greater than", str(user_min))
                    continue
                break
            except ValueError:
                print("Try again")

        for lst in range(user_min, user_max + 1):

            if lst % 3 == 0 and lst % 5 == 0:
                print("FizzBuzz!")

            elif lst % 3 == 0:
                print("Fizz!")

            elif lst % 5 == 0:
                print("Buzz!")

            else:
                print(lst)

    finally:
        while True:

            check = input("Do you want to start over?"
                          " Press Y to start over. Or N to quit!")
            if check.upper() == "Y":
                test()
            elif check.upper() != "N":
                print("Press Y or N")
                continue
            else:
                print("See you soon!")
                quit()


test()