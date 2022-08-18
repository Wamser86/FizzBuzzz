for lst in range(1,21):

    if lst % 3 == 0 and lst % 5 == 0:
        print("FizzBuzz!")

    elif lst % 3 == 0:
       print("Fizz!")

    elif lst % 5 == 0:
        print("Buzz!")

    else:
        print(lst)
