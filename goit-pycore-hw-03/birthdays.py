from datetime import date, datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = date(today.year, birthday.month, birthday.day)

        if birthday_this_year < today:
            birthday_this_year = date(today.year + 1, birthday.month, birthday.day)

        delta = (birthday_this_year - today).days

        if 0 <= delta <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming