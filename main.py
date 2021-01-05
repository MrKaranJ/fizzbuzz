def fizzBuzz(n, a, b):
    '''
    Takes input 'n' for the number of FizzBuzz numbers to 
    be generated and the bases 'a' and 'b'.

    USAGE:

    fizzBuzz(3, 3, 5)

    OUTPUT:
    3 Fizz
    5 Buzz
    6 Fizz
    '''
    # Keep track and the number to be checked and the successful hits
    number = 0
    count = 0
    # Loop until the required number of numbers are generated
    while count < n:
        number = number + 1
        # Checking the conditions
        if number % a == 0 and number % b == 0:
            print(number, "Fizz Buzz")
            count = count + 1
        elif number % a == 0:
            print(number, "Fizz")
            count = count + 1
        elif number % b == 0 :
            print(number, "Buzz")
            count = count + 1
        else:
            continue

# Testing the algorithm
n = int(input("Enter number of FizzBuzz numbers (N) required: "))

fizzBuzz(10, 3, 5)