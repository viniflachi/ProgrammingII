try:
    gross = float(input("Enter gross salary: "))

    if gross < 1000:
        tax = 0.10
    elif gross < 2000:
        tax = 0.12
    elif gross < 4000:
        tax = 0.14
    else:
        tax = 0.18

    net = gross * (1 - tax)
    print("Net salary:", net)

except ValueError:
    print("Please enter a valid number.")

