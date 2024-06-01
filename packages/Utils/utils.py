from datetime import datetime
import pytz

def convert_date(date):
    # Define UTC timezone
    utc_timezone = pytz.utc
    # Define IST timezone
    ist_timezone = pytz.timezone('Asia/Kolkata')
    # Convert UTC time to IST
    ist_time = date.replace(tzinfo=utc_timezone).astimezone(ist_timezone)
    return ist_time