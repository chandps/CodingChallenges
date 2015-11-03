def convertTo24(s): #Sample: '07:05:45PM'
    time, day = list(map(int, s[:8].split(':'))), s[-2:]
    hour = time[0]
    if(day=="PM"):
        if hour != 12:
            hour = hour + 12
    if(day=="AM"):
        if hour == 12:
            hour = 0
    return '%02d:%02d:%02d' % (hour,time[1],time[2])

x = input()
print(convertTo24(x))