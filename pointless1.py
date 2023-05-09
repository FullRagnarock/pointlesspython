import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%I:%M:%S %p")

print("Current time is: ", formatted_time)

print('hello lets do some math')
i = 0
while(i<=100):
    print(i , " Squared is " , i**2 ,i," Cubed is ", i**3)
    print("the current time is ",formatted_time)
    i= i + 1
    