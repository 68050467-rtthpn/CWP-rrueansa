password_input = input()

match password_input:
    case "python is awesome":
        print("ACCESS GRANTED")
    case _:
        print("ACCESS DENIED")
