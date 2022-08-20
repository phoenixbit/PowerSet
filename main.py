# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


n = int(input("Enter number of objects"))
i = -1
power = ""

def powerSetPrinter(i,n,power):
    # Use a breakpoint in the code line below to debug your script.
    if i == n:
        return
    print(power)

    for p in range(i+1,n):
        power += chr(p+65)
        powerSetPrinter(p,n,power)
        power =power.replace(power[len(power)-1],"")
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    powerSetPrinter(i,n,power)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
