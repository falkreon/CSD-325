# CSD 325
# Module 1.3: On the Wall + Flowchart
# Isaac Ellingson
# 10/25/2025


def bottles(initial_count: int):
    if (initial_count > 0):

        for bottles in range(initial_count, 0, -1):
            if (bottles == 1):
                print("1 bottle of beer on the wall, 1 bottle of beer.")
            else:
                print(str(bottles)+" bottles of beer on the wall, "+str(bottles)+" bottles of beer.")
            print("Take one down and pass it around, "+str(bottles - 1)+" bottle(s) of beer on the wall.")
            print()

    print("Time to buy more bottles of beer.")

start_count = int(input("Enter number of bottles: "))
bottles(start_count)
