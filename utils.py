from db_setup import Session
from models import TomatoObj
from helper import dateBreaker, dateToId

def getTomato(date):
    s = Session()
    tomato = s.query(TomatoObj).filter_by(date=date).first()
    s.close()
    return tomato

def incTomato(date):
    s = Session()
    tom = getTomato(date)
    currCount = tom.count + 1
    s.query(TomatoObj).filter_by(date=date).update(dict(
        count = currCount
    ))
    retCount = currCount
    s.commit()
    s.close()
    return retCount

def checkDate(date):
    dateCheck = getTomato(date)
    return dateCheck is None

def initDate(date):
    s = Session()
    dateArr = dateBreaker(date)
    tomO = TomatoObj(id=dateToId(dateArr), date=date, count=0)
    s.add(tomO)
    s.commit()
    s.close()

def main():
    date = "06/14/2021"
    checkDate(date)
    initDate(date)

if __name__ == "__main__":
    main()