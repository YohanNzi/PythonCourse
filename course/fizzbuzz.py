def fizzbuzz(number: int) -> None:
    i = 1
    while i <= number:
        if i % 3 == 0 or i % 5 == 0:
            if (i % 3 == 0) and (i % 5 == 0):
                print("Fizz Buzz")
            elif i % 3 == 0:
                print("Fizz ")
            else:
                print("Buzz ")
        else:
            print (i)
        i += 1



fizzbuzz(16)