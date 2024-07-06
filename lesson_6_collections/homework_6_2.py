def format_time(seconds: int) -> str:
    if 8640000 > seconds >= 0:
        result = ""
        days = seconds // 86400
        remaining_seconds = seconds % 86400
        hours = remaining_seconds // 3600
        hours_str = str(hours).zfill(2)

        remaining_seconds %= 3600
        minutes = remaining_seconds // 60
        minutes_str = str(minutes).zfill(2)

        seconds = remaining_seconds % 60
        seconds_str = str(seconds).zfill(2)

        result += format_days(days) + ", " + hours_str + ":" + minutes_str + ":" + seconds_str
        return result
    else:
        return "Забагато або замало секунд."


def format_days(days: int) -> str:
    day_forms = {
        0: "днів",
        1: "день",
        2: "дні",
    }
    result = str(days) + " "
    last_digit = days % 10
    if last_digit == 1 and days != 11:
        result += day_forms.get(1)
    elif (days % 10 in (2, 3, 4)) and days not in (11, 12, 13, 14):
        result += day_forms.get(2)
    # elif days == 11 or days == 12 or days == 13 or days == 14:
    #     result += day_forms.get(0)
    # elif last_digit == 2 or last_digit == 3 or last_digit == 4:
    #     result += day_forms.get(2)
    else:
        result += day_forms.get(0)
    return result


'''    if days % 10 == 1 and days != 11:
        result += day_forms.get(1)
    elif (days % 10 in (2, 3, 4)) and days not in (11, 12, 13, 14):
        result += day_forms.get(2)'''


def get_input() -> int:
    return int(input("Введіть кількість секунд від 0 до 8640000\n"))


# inputted_seconds = get_input()
# formatted_time = format_time(inputted_seconds)

print(format_time(3715200))

# testing
assert format_time(224930) == '2 дні, 14:28:50', f"{format_time(224930)}"
assert format_time(466289) == '5 днів, 09:31:29', f"{format_time(466289)}"
assert format_time(950400) == '11 днів, 00:00:00'
assert format_time(1209600) == '14 днів, 00:00:00'
assert format_time(1900800) == '22 дні, 00:00:00'
assert format_time(8639999) == '99 днів, 23:59:59'
assert format_time(22493) == '0 днів, 06:14:53'
assert format_time(7948799) == '91 день, 23:59:59'
