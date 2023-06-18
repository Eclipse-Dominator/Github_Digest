from datetime import datetime, timedelta
import pytz
import sys
from os import environ

utc = pytz.utc

try:
    localtz = pytz.timezone(environ["TIMEZONE"])
except pytz.UnknownTimeZoneError:
    print("Unknown timezone specified, using UTC instead.", file=sys.stderr)
    localtz = pytz.utc

get_now = lambda :datetime.now(utc)

def convertToDateTime(x: str) -> datetime:
    """
    convertToDateTime converts a string that is in UTC time to a datetime object.
    This function is used to convert the string returned by the GitHub GraphQL API to a datetime object.

    args:
        x: str - the string to be converted

    returns:
        datetime - the converted datetime object
    """
    dt = datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ")
    return dt.replace(tzinfo=utc)

def format_local(dt: datetime) -> str:
    """
    format_local formats a datetime object to a string in the local timezone.

    args:
        dt: datetime - the datetime object to be formatted
    """
    return dt.astimezone(localtz).strftime("%Y-%m-%d %H:%M:%S")

def format_to_utc(dt: datetime) -> str:
    """
    format_to_utc formats a datetime object to a string in the UTC timezone.

    args:
        dt: datetime - the datetime object to be formatted

    returns:
        str - the formatted string
    """
    return dt.astimezone(utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def get_n_day_prior(n: int) -> datetime:
    """
    get_n_day_prior returns the datetime object n days prior to the current time in UTC time.

    args:
        n: int - the number of days prior

    returns:
        datetime - the datetime object n days prior to the current time in UTC time
    """
    return datetime.now(utc) - timedelta(days=n)

