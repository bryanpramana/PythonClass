def main():
    list = []
    iteration=0

    def GetData():
        Values = int(input("How many values do you wish to process? : "))

        for x in range(0,Values):
            list.append(float(input("Enter a Value: ")))
        list.sort()
        return Values

    Values = GetData()
    print("The input values in sorted order")

    for x in list:
        print(x)
    def Variance(list,Values):
        average = sum(list)/Values
        sumvariance = 0

        for x in list:
            sumvariance += (x-average)**2
        variance = sumvariance/Values
        return variance
    variance = Variance(list,Values)
    def StandardDev(variance):
        deviation = variance**0.5
        return deviation
    deviation = StandardDev(variance)

    print("Variance: ",variance)
    print("Standard Deviatiion",deviation)
main()