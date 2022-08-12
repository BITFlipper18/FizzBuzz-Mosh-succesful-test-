def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("FizzBuzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(input)


def enter_fizzbuzz_value():
    try:
        global value
        value = int(input("Please enter a FizzBuzz integer value: "))
    except TypeError:
        print("Only enter an integer value!!")
        enter_fizzbuzz_value()
    except ValueError:
        print("Only enter an integer value!!")
        enter_fizzbuzz_value()


print("\nHello, welcome to the FizzBuzz challenge!!!\n")
value = ""
enter_fizzbuzz_value()
fizz_buzz(value)



#imput divisable by 3 = string "Fizz"
#imput divisable by 5 = string "Buzz".
#imput divisable by 3 and 5 = string "FizzBuzz".
#imput not divisable by 3 or 5 = string "input".