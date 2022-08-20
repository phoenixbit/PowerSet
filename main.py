

#n is number of objects
n = int(input("Enter number of objects"))
i = -1
power = ""
#power is the variable to print out the power set

#function to output the power set of a given number of objects
def powerSetPrinter(i,n,power):

    if i == n:
        return
    print(power)

    for p in range(i+1,n):
        power += chr(p+65)
        powerSetPrinter(p,n,power)
        power =power.replace(power[len(power)-1],"")
    return



if __name__ == '__main__':
    powerSetPrinter(i,n,power)


