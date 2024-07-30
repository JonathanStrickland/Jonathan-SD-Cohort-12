# Description: QAP 4 for One Stop Insurance Company
# Name: Jonathan Strickland
# Date: July 23rd 2024

# Libraries

import datetime
import time
import sys
from formatvalue import to_upper_title, to_upper_case, format_dollar


# Constants

CONST_DAT = "const.dat"
MAX_CLAIM_AMOUNT = 50000.00
CURRENT_DATE = datetime.datetime.now()

# Functions

# Calculates Premiums

def calc_premium(numcars, liability, glass, loaner, basicprem, discount, extraliability, glasscover, loanercost, hstrate):
    totalbasicprem = basicprem + (numcars - 1) * basicprem * discount
    extracost = 0
    if liability == "Yes":
        extracost += numcars * extraliability
    if glass == "Yes":
        extracost += numcars * glasscover
    if loaner == "Yes":
        
        extracost += numcars * loanercost
    totalprem = totalbasicprem + extracost
    hst = totalprem * hstrate
    totalcost = totalprem + hst
    return totalprem, hst, totalcost


def process_payment(totalcost, paymethod, processfee, downpay=0): # downpay=0 defaults the down payment to 0
    if paymethod == "Full":
        return totalcost
    else:
        remaincost = totalcost - downpay if paymethod == "Down Pay" else totalcost
        monthpay = (remaincost + processfee) / 8
        return monthpay

# Identifies valid provinces

def valid_prov(province):
    validprov = ['ON', 'QC', 'NS', 'NB', 'MB', 'BC', 'PEI', 'SK', 'AB', 'NL', 'YT', 'NT', 'NU']
    return province in validprov

def main():

    
    while True:
        
        # Loads the programs constants from const.dat

        with open(CONST_DAT, "r") as file:
            filecontent = file.read()

        filelist = filecontent.split(", ")
        policynum = int(filelist[0])
        basicprem = float(filelist[1])
        discount = float(filelist[2])
        extraliability = float(filelist[3])
        glasscover = float(filelist[4])
        loanercost = float(filelist[5])
        hstrate = float(filelist[6])
        processfee = float(filelist[7])
        
        claims = []

        firstname = to_upper_title(input("Enter customer's first name: "))
        lastname = to_upper_title(input("Enter customer's last name: "))
        address = to_upper_title(input("Enter customer's address: "))
        city = to_upper_title(input("Enter customer's city: "))
        province = to_upper_case(input("Enter customer's province: "))

        while not valid_prov(province):
            print("Invalid province. Please enter a valid province.")
            province = to_upper_case(input("Enter customer's province: "))

        postalcode = to_upper_case(input("Enter customer's postal code: "))
        phonum = input("Enter the customers phone number (10 Digits): ")
        
        while not (phonum.isdigit() and len(phonum) == 10):
                phonum = input("Invalid phone number. Enter a valid 10-digit phone number: ")

        numcars = int(input("Enter the number of cars being insured: "))
        liability = to_upper_case(input("Do you want extra liability coverage? (Y/N): "))
        if liability == "Y":
            liability = "Yes"
        else:
            liability = "No"
        glass = to_upper_case(input("Do you want glass coverage? (Y/N): "))
        if glass == "Y":
            glass= "Yes"
        else:
            glass= "No"
        loaner = to_upper_case(input("Do you want loaner car coverage? (Y/N): "))
        if loaner == "Y":
            loaner= "Yes"
        else:
            loaner= "No"
        paymethod = to_upper_title(input("Enter payment method. (Full/Monthly/Down Pay): "))

        downpay = 0
        if paymethod == "Down Pay":
            downpay = float(input("Enter the down payment amount: "))

        claims = []
        
        while True:
            claimnum = input("Enter claim number (or 'done' to finish): ")
            if claimnum.upper() == "DONE":
                break
            claimdate = input("Enter the claim date: (YYYY-MM-DD): ")
            claimamount = float(input("Enter claim amount: "))
            while claimamount > MAX_CLAIM_AMOUNT:
                    claimamount = float(input(f"Invalid amount. Enter a claim amount <= ${MAX_CLAIM_AMOUNT:.2f}: "))

            claims.append((claimnum, claimdate, claimamount)) # Adds a claim to the list

        totalprem, hst, totalcost = calc_premium(numcars, liability, glass, loaner, basicprem, discount, extraliability, glasscover, loanercost, hstrate)
        monthpay = process_payment(totalcost, paymethod, processfee, downpay=0)

        # Makes the date the 1st of the following month for the users first payment
        
        firstpayment = datetime.date.today()
        if firstpayment.month == 12:
            firstpaydate = firstpayment.replace(year=firstpayment.year + 1, month=1, day=1)
        else:
            firstpaydate = firstpayment.replace(month=firstpayment.month + 1, day=1)

        # Saves policy data to customer.dat

        f = open("customer.dat", "a")

        f.write(f"Policy Number: {policynum}, ")
        f.write(f"First Name: {firstname}, ")
        f.write(f"Last Name: {lastname}, ")
        f.write(f"Address: {address}, ")
        f.write(f"City: {city}, ")
        f.write(f"Province: {province}, ")
        f.write(f"Postalcode: {postalcode}, ")
        f.write(f"Phone Number: {phonum}, ")
        f.write(f"Number of Cars: {numcars}, ")
        f.write(f"Extra Liability: {liability}, ")
        f.write(f"Glass Coverage: {glass}, ")
        f.write(f"Loaner Coverage: {loaner}, ")
        f.write(f"Payment Method: {paymethod}, ")
        f.write(f"Date: {CURRENT_DATE.strftime("%d-%b-%y")}, ")
        f.write(f"Total Cost: {totalcost}")
        f.write(f"\n")

        f.close()


        def loading_bar(load):
            for l in range(load):
                time.sleep(0.1) # Creates delay on the loading bar
                sys.stdout.write(f"\rLoading: [{"#" * (l + 1)}{"." * (load - l - 1)}] {int((l + 1) / load * 100)}%") # Makes the progress bar look like its downloading
                sys.stdout.flush() # Makes the loading bar update in real time
            print()

        print()
        loading_bar(30)

        print(f"Data Saved!")
        print()
        print()

        print(f"     One Stop Insurance Company")
        print(f"-------------------------------------")
        print(f"")
        print(f"Policy Number:   {policynum:<11}")
        print(f"Name:            {firstname} {lastname:<27}")
        print(f"Address:         {address:<11}")
        print(f"City:            {city:<11}")
        print(f"Province:        {province:<11}")
        print(f"Postal code:     {postalcode:<11}")
        print(f"Date:            {CURRENT_DATE.strftime("%d-%b-%y"):<14}")
        
        areacode = phonum[:3]
        first3 = phonum[3:6]
        last4 = phonum[6:]
        
        print(f"Phone Number:    ({areacode:<3}) {first3:<3}-{last4:<4}")
        print(f"\n-------------------------------------")
        print(f"")
        print(f"Number of Cars:        {numcars:>14}")
        print(f"Extra Liability:       {liability:>14}")
        print(f"Glass Coverage:        {glass:>14}")
        print(f"Loaner Car:            {loaner:>14}")
        print(f"Payment Method:        {paymethod:>14}")
        
        if paymethod == 'Down Pay':
            print(f"Down Payment:          {format_dollar(downpay):>14}")

        print(f"Total Premium:         {format_dollar(totalprem):>14}")
        print(f"HST:                   {format_dollar(hst):>14}")
        print(f"Total Cost:            {format_dollar(totalcost):>14}")
        
        if paymethod != 'Full':
            print(f"Processing Fee:        {format_dollar(processfee):>14}")
            print(f"Monthly Payment:       {format_dollar(monthpay):>14}")
            print(f"First Payment Date:    {firstpaydate.strftime("%d-%b-%y"):>14}")

        print(f"")
        

        print("\nPrevious Claims:")
        print()
        print("  Claim #    Claim Date     Amount")
        print("------------------------------------")
       
        for claim in claims:
            print(f"  {claim[0]:<10} {claim[1]:<12} {format_dollar(claim[2]):<11}")

        
        newpolicynum = policynum + 1

        # Saves the new policy number to const.dat

        with open(CONST_DAT, "w") as file:

            filelist = [newpolicynum, basicprem, discount, extraliability, glasscover, loanercost, hstrate, processfee]
            for item in filelist[:-1]:
                file.write(f"{item}, ")
            file.write(f"{filelist[-1]}")

        print("\nPolicy data has been saved. Next policy number: ", newpolicynum)

        more_customers = input("\nDo you want to enter another customer (Y/N)? ").upper()
        if more_customers != 'Y':
            break

        
if __name__ == "__main__":
    main()