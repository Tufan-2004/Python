celsius=int(input("Enter celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in fahrenheit:",fahrenheit)
if celsius<10:
    print("Whether it's cold")
elif 10>=celsius and celsius<25:
    print("Whether it's warm")
else:
    print("Whether it's hot")
