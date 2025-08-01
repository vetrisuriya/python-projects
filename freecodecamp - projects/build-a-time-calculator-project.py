def add_time(start_time, duration, start_day=None):

    time_part, period = start_time.split()
    start_hour_str, start_minute_str = time_part.split(':')

    start_hour = int(start_hour_str)
    start_minute = int(start_minute_str)

    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    duration_hour_str, duration_minute_str = duration.split(':')
    duration_hour = int(duration_hour_str)
    duration_minute = int(duration_minute_str)

    total_start_minutes = start_hour * 60 + start_minute
    total_duration_minutes = duration_hour * 60 + duration_minute

    new_total_minutes = total_start_minutes + total_duration_minutes

    new_hour_24 = (new_total_minutes // 60) % 24
    new_minute = new_total_minutes % 60

    days_passed = new_total_minutes // (24 * 60)

    if new_hour_24 >= 12:
        new_period = "PM"
        if new_hour_24 > 12:
            new_hour_12 = new_hour_24 - 12
        else:
            new_hour_12 = 12
    else:
        new_period = "AM"
        if new_hour_24 == 0:
            new_hour_12 = 12
        else:
            new_hour_12 = new_hour_24

    new_minute_formatted = str(new_minute).zfill(2)

    new_time_str = f"{new_hour_12}:{new_minute_formatted} {new_period}"

    if start_day:
        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        
        start_day_lower = start_day.lower()
        
        try:
            start_day_index = days_of_week.index(start_day_lower)
        except ValueError:
            return "Error: Invalid start day provided."

        new_day_index = (start_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index].capitalize()
        new_time_str += f", {new_day}"

    if days_passed == 1:
        new_time_str += " (next day)"
    elif days_passed > 1:
        new_time_str += f" ({days_passed} days later)"

    return new_time_str
