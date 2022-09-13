def func1(hours, minutes, fwd, back):
    if minutes + fwd >= 60:
        return "{}:00".format(hours + 1)
    else:
        ostatok = 60 - (minutes + fwd)
    if minutes - back < 0:
        return "{}:00".format(hours)
    else:
        ostatok2 = minutes - back
    if ostatok < ostatok2:
        return "{}:{:02d}".format(hours, 60-ostatok)
    else:
        return "{}:{:02d}".format(hours, ostatok2)


watch_time = input("Enter current time: ")
inp_fwd_bck = input("Enter backward and forward ")
hours, minutes = [int(i) for i in watch_time.split(":")]
back, fwd = [int(i) for i in inp_fwd_bck.split()]
print(func1(hours, minutes, fwd, back))
