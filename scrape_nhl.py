import pandas as pd
import requests
from datetime import datetime, timedelta

def scrape_schedule_one_week(start_date):

    url = f"https://api-web.nhle.com/v1/schedule/{start_date}"
    return

def scrape_full_schedule(start_date='2023-10-07', end_date='2024-04-18'):

    full_schedule = pd.DataFrame()

    scrape_day = start_date

    while scrape_day <= end_date:

        print(scrape_day)

        week_scrape = scrape_full_schedule(scrape_day)

        full_schedule = full_schedule._append(week_scrape)

        # Don't like this because it has to look through the full_schedule.date n times. Should be able to look at the most recent date added. Peek?
        last_day_scraped = max(full_schedule.date)

        # Convert last_day_scraped to datetime object, add a day, then convert result back into string with strftime
        scrape_day = datetime.strftime(
            (
                datetime.strptime(last_day_scraped, "%Y-%m-%d").date()
                + timedelta(days=1)
            ),
            "%Y-%m-%d",
        )
        # interested to see what other types there are
        return full_schedule[full_schedule.type == 'R']

    return




















