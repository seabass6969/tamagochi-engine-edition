def times_cal():
    times = 2120231 
    seconds = (times) % 60
    minutes = (times // 60) % 60
    hours = (times // 60 // 60) % 24
    days = (times // 60 // 60 // 24)
    return "{}d - {}h - {}m - {}s".format(
        days,
        hours,
        minutes,
        seconds,
    )


print(times_cal())
