def date_time(time: str) -> str:

    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    time = time.replace(':', '.').replace(' ', '.').split('.')

    day = int(time[0])
    month = months[int(time[1])]
    year = int(time[2])
    hours = int(time[3])
    minutes = int(time[4])

    return '{day} {month} {year} year {hours} {horas} {minutes} {minutos}'.format(day=day, month=month, year=year, hours=hours, minutes=minutes, horas='hour' if hours==1 else 'hours', minutos='minute' if minutes == 1 else 'minutes')


print(date_time('09.05.1945 01:01'))


# if __name__ == '__main__':
#     print("Example:")
#     print(date_time('01.01.2000 00:00'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
#     assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
#     assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
