from ma import ma
while True:
    ma30=ma(30)
    ma120=ma(120)
    sum=ma30-ma120
    if -6 <= sum <= 6:
        print("报警")
    else:
        print(sum)

