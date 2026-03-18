from datetime import datetime, timedelta

def calculate_expiry(days):
    return datetime.now() + timedelta(days=days)
