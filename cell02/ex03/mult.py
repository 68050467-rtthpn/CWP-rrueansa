fnumber = int(input("Enter first number : \n"))
snumber = int(input("Enter second number : \n"))

sum = fnumber * snumber

match sum :
    case x if x > 0 :
        print(f"{fnumber} * {snumber} = {sum}")
        print("The result is positive.")
    case x if x < 0 :
        print(f"{fnumber} * {snumber} = {sum}")
        print("The result is negative.")
    case x if x == 0 :
        print(f"{fnumber} * {snumber} = {sum}")
        print("The result is negative and positive.")