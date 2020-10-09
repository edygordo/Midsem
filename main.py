def billingaddress():
    f = open("Customers Address", "r")
    lineList = f.readlines()
    f.close()
    print("Delivering to Address:- " + lineList[len(lineList) - 1])


def deliverycharges(x):
    if x == 1:
        print("Generating Bill for Gaming System")
        print("NVIDIA SLI 4GB:- 100")
        print("Kingston DDR4 8GB:- 100")
        print("Seagate 1TB:- 100")
        print("Liquid Nitrogen Cooling:- 100")
        print("Total:- 400")

    elif x == 2:
        print("Generating Bill for Normal Work Bench")
        print("Intel HD 6000:- 100")
        print("Kingston DDR4 4GB:- 100")
        print("Seagate 512GB:- 100")
        print("Twin Fan CPU Cooler:- 100")
        print("Total:- 400")

    elif x == 3:
        print("Generating Bill for Scientific System")
        print("NVIDIA SLI 16GB:- 100")
        print("Kingston DDR4 16GB:- 100")
        print("Seagate 2TB:- 100")
        print("Liquid Nitrogen Cooling:- 100")
        print("Total:- 400")

    billingaddress()


def storeaddress(x):
    f = open("Customers Address", "a")
    address = input("Please enter your billing Address:- ")
    f.write(address+"\n")
    f.close()
    deliverycharges(x)


def confirmorder(x):
    if x == 1:
        print("Order confirmed for Gaming System")
        f = open("Gaming System", "r")
        while True:
            line = f.readline()
            if not line:
                break
            else:
                for letters in line:
                    if letters == "-":
                        print("Ordering is Required for " + line)
                        break

        print("Order Confirmed")
        f.close()
        storeaddress(x)

    elif x == 2:
        print("Order confirmed for Normal Workbench")
        f = open("Normal Workbench", "r")
        while True:
            line = f.readline()
            if not line:
                break
            else:
                for letters in line:
                    if letters == "-":
                        print("Ordering is Required for " + line)
                        break

        print("Order Confirmed")
        f.close()
        storeaddress(x)

    elif x == 3:
        print("Order confirmed for Scientific Computing System")
        f = open("Scientific Computing", "r")
        while True:
            line = f.readline()
            if not line:
                break
            else:
                for letters in line:
                    if letters == "-":
                        print("Ordering is Required for "+line)
                        break

        print("Order Confirmed")
        f.close()
        storeaddress(x)


def clarification(x):
    if x == 1:
        print("Detail Explanation of Quotation of Gaming System")
        print("NVIDIA Graphic Processor is required for extra GPU power to run high graphic demanding games")
        print("Minimum 8GB of RAM is required so that games do not crash")
        print("Games are very space demanding so 1TB of space is required atleast")
        print("To Avoid CPU throttling heat dissipation is important issue hence liquid nitrogen cooling system is "
              "required")
        confirmation = input(print("Do you want to confirm this order?(y/n)"))
        if confirmation == "y":
            confirmorder(x)
        else:
            print("Order Cancelled")

    elif x == 2:
        print("Detail Explanation of Quotation of Normal Workbench")
        print("On board graphic card is sufficient for normal day work")
        print("Minimum 4GB of RAM is sufficient for most apps")
        print("Normal apps and photos and videos wont require much space")
        print("CPU fan cooler would be enough to dissipate heat")
        confirmation = input(print("Do you want to confirm this order?(y/n)"))
        if confirmation == "y":
            confirmorder(x)
        else:
            print("Order Cancelled")

    elif x == 3:
        print("Detail Explanation of Quotation of Scientific Computing System")
        print("For parallel processing in ML/AI work GPUs are necessary so high end graphic card is required")
        print("Minimum 8GB of RAM is required for simulation of models")
        print("A huge amount of data sets needs to be stored so minimum of 2TB space is required")
        print("Running Simulation is very CPU/GPU intensive work so to avoid throttling Liquid Nitrogen cooling "
              "System required")
        confirmation = input(print("Do you want to confirm this order?(y/n)"))
        if confirmation == "y":
            confirmorder(x)
        else:
            print("Order Cancelled")


def quotation(x):
    if x == 1:
        print("Quotation for Gaming System is:- ")
        print("Graphics Card:- 4GB NVIDIA SLI")
        print("RAM:- 8GB DDR4 Kingston")
        print("Memory:- 1TB SSD Seagate")
        print("Thermal Cooling System:- Liquid Nitrogen Cooling System")
        choice = input(print("Do You Want to see Clarification of Quotation? (y/n)"))
        if choice == "y":
            clarification(x)
        else:
            confirmorder(x)

    elif x == 2:
        print("Quotation for Normal Workbench is:- ")
        print("Graphics Card:- Intel HD 6000 On Board Graphic Card")
        print("RAM:- 4GB DDR4 Kingston")
        print("Memory:- 512GB SSD Seagate")
        print("Thermal Cooling System:- Twin Fan CPU Cooler")
        choice = input(print("Do You Want to see Clarification of Quotation? (y/n)"))
        if choice == "y":
            clarification(x)
        else:
            confirmorder(x)

    elif x == 3:
        print("Quotation for Scientific Computing System is:- ")
        print("Graphics Card:- 16GB NVIDIA SLI")
        print("RAM:- 16GB DDR4 Kingston")
        print("Memory:- 2TB SSD Seagate")
        print("Thermal Cooling System:- Liquid Nitrogen Cooling System")
        choice = input(print("Do You Want to see Clarification of Quotation? (y/n)"))
        if choice == "y":
            clarification(x)
        else:
            confirmorder(x)


def sysrequest(x):
    if x == 1:
        print("Gaming System Requested")
        quotation(x)
    elif x == 2:
        print("Normal WorkBench Requested")
        quotation(x)
    elif x == 3:
        print("Scientific Computing System Requested")
        quotation(x)


print("Welcome to System Supplier Toolbox")
valid = True
while valid:
    x = int(input("Enter type of system you want:- (1) for Gaming, (2) for Normal Workbench, (3) for scientific "
                  "Computing"))
    if x != 1 and x != 2 and x != 3:
        print("Invalid Choice Please Select Again: ")
    else:
        sysrequest(x)
        valid = False
