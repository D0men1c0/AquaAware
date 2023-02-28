from datetime import timedelta, date

def date_range_list(start_date, end_date):
    # Return generator for a list datetime.date objects (inclusive) between start_date and end_date (inclusive).
    curr_date = start_date
    while curr_date <= end_date:
        yield curr_date 
        curr_date += timedelta(days=1)

  
def return_list(start_date, end_date):
    sets = date_range_list(start_date, end_date)
    date_list_formattate = []
    for data in sets:
        data_formattata = data.strftime("%d/%m/%y")
        date_list_formattate.append(data_formattata)
        
    return date_list_formattate
