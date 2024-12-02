try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise ValueError("Number is negative.")
    print(f"The number is: {number}")
except ValueError as e:
    print(e)
