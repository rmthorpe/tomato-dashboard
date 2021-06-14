import datetime

def dateBreaker(date):
    dateArr = []
    i = 0
    dateLen = len(date)
    num = ""
    while dateLen > i:
        if date[i] != "/":
            num += date[i]
        else:
            dateArr.append(int(num))
            num = ""
        i += 1
    dateArr.append(int(num))   
    return dateArr

def dateToId(dateArr):
    year = (dateArr[2] - 2020) * 10000
    month = dateArr[0] * 100
    day = dateArr[1]
    return year + month + day

def getDateStr():
    today = datetime.datetime.now()
    day = today.day
    month = today.month
    year = today.year
    dateStr = str(month) + "/" + str(day) + "/" + str(year)
    return dateStr

def main():
    a = dateBreaker("6/14/2021")
    print(a)

if __name__ == "__main__":
    main()