num = int(input("Enter the number less than 25 : "))

if num > 25 :
    print("Error")
else :
    for i in range(num , 26) :
        print(f"Inside the loop, my variable is {i}")
