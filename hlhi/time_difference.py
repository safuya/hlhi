from datetime import datetime, timedelta


def run(bought: datetime, sold: datetime) -> timedelta:
    return sold - bought
