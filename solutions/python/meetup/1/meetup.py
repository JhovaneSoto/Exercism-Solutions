from datetime import date,timedelta
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self,message):
        self.message=message
        
weekday_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}
days_th=["first", "second", "third", "fourth", "fifth",
            "sixth", "seventh", "eighth", "ninth", "tenth"]

teenth=[13,14,15,16,17,18,19]
def meetup(year, month, week, day_of_week):
    temp_date = date(year,month,1)
    lista = []
    num_day = weekday_map[day_of_week]
    while temp_date.month == month:
        if temp_date.weekday() == num_day:
            lista.append(temp_date.day)
        temp_date += timedelta(days=1)
        
    day_result = 1
    if week in days_th:
        idx=days_th.index(week)
        if idx>=len(lista):
            raise MeetupDayException("That day does not exist.")
        day_result=lista[idx]
    if week=="last":
        day_result=lista[-1]
    if week=="teenth":
        for candidate in lista:
            if candidate in teenth:
                day_result=candidate
                break
    out_date=date(year,month,day_result)
    return out_date
