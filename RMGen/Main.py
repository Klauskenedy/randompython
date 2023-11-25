import random

def cpr_gen():
    #Generates date-values for first 6 slots
    day = random.randint(1, 31)
    if day < 10:
        day = str(0) + str(day)
    month = random.randint(1, 12)
    if month < 10:
        month = str(0) + str(month)
    year = random.randint(1, 99)
    if year < 10:
        year = str(0) + str(year)
        
    #Generates values for the 4 last slots
    iid = random.randint(1, 9999)
    if iid < 10:
        iid = str(0) + str(0) + str(0) + str(iid)
    elif iid < 100:
        iid = str(0) + str(0) + str(iid)
    elif iid < 1000:
        iid = str(0) + str(iid)

    #Formatting the values, into an usable cpr and returns it
    cpr = str(day) + str(month) + str(year) + "-" + str(iid)
    print(cpr)
    return cpr

cpr_gen()