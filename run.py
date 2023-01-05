import time

class Records:
    def __init__(self,packageName,customerName,numberOfPax,packageCost):
        self.packageName = packageName
        self.customerName = customerName
        self.numberOfPax = numberOfPax
        self.packageCost = packageCost

def recordsData():
    Colin = Records("Lapis", "Colin", 2, 364)
    Anthony = Records("Opal", "Anthony", 7, 135)
    Iggy = Records("Sapphire", "Iggy", 8, 144)
    Daphne = Records("Amethyst", "Daphne", 1, 546)
    Hyacinth = Records("Jade", "Hyacinth", 6, 654)
    Francesca = Records("Amber", "Francesca", 3, 324)
    Gregory = Records("Pearl", "Gregory", 4, 545)
    Benedict = Records("Emerald", "Benedict", 4, 473)
    Eloise = Records("Quartz", "Eloise", 9, 345)
    James = Records("Ruby", "James", 1, 435)
    return [Anthony, Benedict, Colin, Daphne, Eloise, Francesca, Gregory, Hyacinth, Iggy, James]

def displayAll(user):
    print("\n----------- All Records ----------- ")
    for c, i in enumerate(user):
        print(str(c+1)+". Package name: "+str(i.packageName)+", Customer name: "+str(i.customerName)+", Number of pax: "+str(i.numberOfPax)+", Package cost per pax: $"+str(i.packageCost))

def bubbleSort(user):
    print("\n---------- Bubble Sort by Customer Name ----------")
    theSeq = [i.customerName.lower() for i in user]
    n = len(theSeq)
    for i in range(n-1,0,-1):
        for j in range(i):
            if (theSeq[j] > theSeq[j+1]):
                tmp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j+1] = tmp
    for c, j in enumerate(theSeq):
        for i in user:
            if i.customerName.lower() == j:
                print(str(c+1)+". Customer Name: "+str(i.customerName)+", Package Name: "+str(i.packageName)+", Number Of Pax: "+str(i.numberOfPax)+", Package Cost Per Pax: $"+str(i.packageCost))

def selectionSort(customer):
    print("\n---------- Selection Sort by Package Name ----------")
    theSeq = [i.packageName.lower() for i in customer]
    n = len(theSeq)
    for i in range(n - 1):
        smallNdx = i
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    for c, j in enumerate(theSeq):
        for i in customer:
            if i.packageName.lower() == j:
                print(str(c+1)+". Package Name: "+str(i.packageName)+", Customer Name: "+str(i.customerName)+", Number Of Pax: "+str(i.numberOfPax)+", Package Cost Per Pax: $"+str(i.packageCost))

def insertionSort(customer):
    print("\n---------- Insertion Sort by Package Cost ----------")
    theSeq = [i.packageCost for i in customer]
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos-1]
            pos -= 1
        theSeq[pos] = value
    for c, j in enumerate(theSeq):
        for i in customer:
            if i.packageCost == j:
                print(str(c+1)+") Package Cost Per Pax: $"+str(i.packageCost)+", Package Name: "+str(i.packageName)+", Customer Name: "+str(i.customerName)+", Number Of Pax: "+str(i.numberOfPax))

def editCustomerName(user, current):
    new = input("Enter the new customer name: ")
    if new != "":
        user[current].customerName = new
        print("Customer Name has been updated.")

def editPackageName(user, current):
    new = input("Enter the new package name: ")
    if new != "":
        user[current].packageName = new
        print("Package Name has been updated.")

def editNumberOfPax(user, current):
    while True:
        try:
            new = input("Enter the new number of pax: ")
            if new == "":
                break
            else:
                new = int(new)
                user[current].numberOfPax = new
                print("Number of Pax has been updated.")
                break
        except ValueError:
            print("Value error! Please enter a number!")

def editPackageCost(user, current):
    while True:
        try:
            new = input("Enter the new package cost: ")
            if new == "":
                break
            else:
                new = int(new)
                user[current].packageCost = new
                print("Package Cost has been updated.")
                break
        except ValueError:
            print("Value error! Please enter a number!")

def listRecords(user):
    global y
    print("\n---------- List Records Range ----------")
    while True:
        try:
            x = input("Enter start range (press return to return to menu): $")
            if x != "":
                y = input("Enter stop range (press return to return to menu): $")
                if y == "":
                    break
                x, y = int(x), int(y)
                if y <= x:
                    raise Exception("Error!")
                break
            else:
                break
        except ValueError:
            print("Error! Please enter a number!")
        except:
            print("Error! Stop Range cannot be greater than or equal to Start Range.")
    theSeq = [i.packageCost for i in user if i.packageCost >= x and i.packageCost <= y]
    finalSeq = [i for j in sorted(theSeq) for i in user if i.packageCost == j]
    if len(finalSeq) == 0:
        print("Range has no data.")
    else:
        for c, i in enumerate(finalSeq):
            print(str(c + 1) + ". Package name: " + str(i.packageName) + ", Customer name: " + str(
                i.customerName) + ", Number of pax: " + str(i.numberOfPax) + ", Package cost per pax: $" + str(
                i.packageCost))

def linearSearch(user):
    print("\n---------- Linear Search by Customer Name ----------")
    name = input("Enter customer name (press return to return to menu): ")
    if name != "":
        current = -1
        n = len(user)
        for i in range(n):
            if user[i].customerName.lower() == name.lower():
                current = i
        if current == -1:
            print(f"Customer {name} is not found!")
        else:
            print(f"\nCustomer {name} found!")
            print("Customer name: "+str(user[current].customerName)+", Package name: " + str(user[current].packageName) +
                  ", Number of pax: "+str(user[current].numberOfPax) +
                  ", Package cost per pax: $" + str(user[current].packageCost))
            print("Select one to update: ")
            print(f"1. Customer name \n2. Package name \n3. Number of pax \n4. Package cost per pax")
            while True:
                try:
                    selection = input("Enter a number between 1-4 (press return to return to menu): ")
                    if selection == "":
                        break
                    selection = int(selection)
                    if selection < 1 or selection > 4:
                        print("Error! Please enter a number between 1-4.")
                    if selection == 1:
                        editCustomerName(user, current)
                    elif selection == 2:
                        editPackageName(user, current)
                    elif selection == 3:
                        editNumberOfPax(user, current)
                    elif selection == 4:
                        editPackageCost(user, current)
                    break
                except ValueError:
                    print("Error! Please input a number!")
                except:
                    print("Error! Please enter a number between 1-4.")

def binarySearch(user):
    print("\n----------Binary Search by Package Name ----------")
    name = input("Enter package name (press return to return to menu): ")
    if name != "":
        packageSeq = [i.packageName.lower() for i in user]
        theSeq = [i for p in sorted(packageSeq) for i in user if i.packageName.lower() == p]
        current = -1
        l = 0
        r = len(theSeq)
        while (r >= l):
            m = l + ((r - l) // 2)
            if m >= len(theSeq):
                break
            if name.lower() == theSeq[m].packageName.lower():
                current = m
                break
            elif theSeq[m].packageName.lower() > name.lower():
                r = m - 1
            else:
                l = m + 1

        if current == -1:
            print(f"Package {name} not found!")
        else:
            print(f"\nPackage {name} found!")
            print("Customer name: "+str(user[current].customerName)+", Package name: " + str(user[current].packageName) +
                  ", Number of pax: "+str(user[current].numberOfPax) +
                  ", Package cost per pax: $" + str(user[current].packageCost))
            print("Select one to update: ")
            print(f"1. Customer name \n2. Package name \n3. Number of pax \n4. Package cost per pax")
            while True:
                try:
                    selection = input("Enter a number between 1-4 (press return to return to menu): ")
                    if selection == "":
                        break
                    selection = int(selection)
                    if selection < 1 or selection > 4:
                        raise Exception("Error! Please enter a number between 1-4.")

                    if selection == 1:
                        editCustomerName(user, current)
                    elif selection == 2:
                        editPackageName(user, current)
                    elif selection == 3:
                        editNumberOfPax(user, current)
                    elif selection == 4:
                        editPackageCost(user, current)
                    break
                except ValueError:
                    print("Error! Please input a number!")
                except:
                    print("Error! Please enter a number between 1-4.")

if __name__ == "__main__":
    user = recordsData()
    while True:
        try:
            print("----------- Menu ----------- ")
            print("1. Display all records")
            print("2. Sort record by Customer Name using Bubble sort")
            print("3. Sort record by Package Name using Selection sort")
            print("4. Sort record by Package Cost using Insertion sort")
            print("5. Search record by Customer Name using Linear Search and update record")
            print("6. Search record by Package Name using Binary Search and update record")
            print("7. List records range from $X to $Y. e.g $100-200")

            try:
                choice = input("Enter choice (press return to end program): ")
                if choice == "":
                    print("Ending program...")
                    time.sleep(1)
                    print("Bye bye :)")
                    break
                choice = int(choice)
                if choice == 1:
                    displayAll(user)
                elif choice == 2:
                    bubbleSort(user)
                elif choice == 3:
                    selectionSort(user)
                elif choice == 4:
                   insertionSort(user)
                elif choice == 5:
                    linearSearch(user)
                elif choice == 6:
                    binarySearch(user)
                elif choice == 7:
                    listRecords(user)
            except ValueError:
                print("Value error! Please enter a number.")
            except Exception as e:
                print(e)
        finally:
            print("")



