# Save the input in this variable
ticket = int(input())

# Add up the digits for each half
half1 = (ticket % 10)
ticket //= 10
half1 += (ticket % 10)
ticket //= 10
half1 += (ticket % 10)
ticket //= 10

half2 = (ticket % 10)
ticket //= 10
half2 += (ticket % 10)
ticket //= 10
half2 += (ticket % 10)

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
