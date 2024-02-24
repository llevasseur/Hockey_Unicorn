# Main Functions
scrape_full_schedule - not referenced

parameters: start_date in yyyy-mm-dd format, end_date

sets full_schedule to pandas.DataFrame()

iterate through each data from start_date to end_date

use _append on full_schedule and set full_schedule to it. Append week_scrape which is scrape_schedule_one_week


scrape_one_week - referenced in scrape_full_schedule

parameters: start_date in yyyy-mm-dd format
Get url using start_date

Using requests, the python library, get the data from the url and set timeout to 500ms












