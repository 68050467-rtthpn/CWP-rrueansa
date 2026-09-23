user_input = input("What you gotta say? : ")
while True:
    user_input = input("I got that. Anything else? : ")

    match user_input:
        case "STOP" :
            break