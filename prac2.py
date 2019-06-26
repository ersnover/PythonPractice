#Fizz Buzz
#Enter a number, if divisible by 3, print FIZZ. if number divisible by 5, print "BUZZ". if BOTH, FIZZ BUZZ

num = int(input("Enter a number: "))

if num %3 == 0 and num %5 == 0:
    print("FIZZ BUZZ")
elif num %3 == 0:
    print("FIZZ")
elif num %5 == 0:
    print("BUZZ")