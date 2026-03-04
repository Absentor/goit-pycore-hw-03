from datetime import date, datetime

def get_days_from_today(date_string):
    try:      
        option_date = datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return None
    
    delta = date.today() - option_date.date()
    return (delta.days)
    