from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import concurrent.futures
from datetime import datetime, timedelta
import os

def generate_dates(start_date_str="2017-04-20", end_date_str="2019-11-11"):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    dates = []
    current = start_date
    while current <= end_date:
        formatted_date = current.strftime("%b%d.%Y").lower()
        dates.append(formatted_date)
        current += timedelta(days=1)
    
    return dates

def scrape_forex_factory(date_str):
    url = f"https://www.forexfactory.com/calendar?day={date_str}"
    print(f"Scraping: {url}")
    
    # Set up headless Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0")
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # Wait for JavaScript to load content
    time.sleep(5)
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    data = []
    current_date = None
    
    rows = soup.select("tr.calendar__row")
    
    for row in rows:
        if "calendar__row--day-breaker" in row.get("class", []):
            date_span = row.select_one("td.calendar__cell span")
            if date_span:
                current_date = date_span.text.strip()
            continue
        
        time_td = row.select_one("td.calendar__time span")
        if not time_td:
            continue
        
        time_val = time_td.text.strip()
        currency = row.select_one("td.calendar__currency span")
        currency = currency.text.strip() if currency else ""
        
        impact_span = row.select_one("td.calendar__impact span[title]")
        impact = impact_span["title"].replace(" Impact Expected", "") if impact_span else ""
        
        event_title = row.select_one("td.calendar__event span.calendar__event-title")
        event_title = event_title.text.strip() if event_title else ""
        
        actual = row.select_one("td.calendar__actual span")
        actual = actual.text.strip() if actual else ""
        
        forecast = row.select_one("td.calendar__forecast span")
        forecast = forecast.text.strip() if forecast else ""
        
        previous = row.select_one("td.calendar__previous span")
        previous = previous.text.strip() if previous else ""
        
        data.append({
            "Date": current_date,
            "Time": time_val,
            "Currency": currency,
            "Impact": impact,
            "Event Title": event_title,
            "Actual": actual,
            "Forecast": forecast,
            "Previous": previous
        })
    
    driver.quit()
    
    return data

def main():
    dates = generate_dates()
    all_data = []
    
    # Define output path
    output_path = "forexfactory_calendar_full.csv"
    temp_output_path = "temp_" + output_path
    
    # Create a counter for completed dates
    completed_dates = 0
    
    # Use ThreadPoolExecutor to run multiple scrapers concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submit scraping tasks
        future_to_date = {executor.submit(scrape_forex_factory, date): date for date in dates}
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(future_to_date):
            date = future_to_date[future]
            try:
                data = future.result()
                if data:
                    all_data.extend(data)
                    completed_dates += 1
                    print(f"Completed scraping for {date}, got {len(data)} entries")
                    
                    # Save data after every completed date
                    temp_df = pd.DataFrame(all_data)
                    temp_df.to_csv(temp_output_path, index=False)
                    print(f"Saved {len(all_data)} entries to temporary file after {completed_dates} dates")
                    
                    # Create more frequent backups - every 5 dates instead of 10
                    if completed_dates % 5 == 0:
                        backup_path = f"backup_{completed_dates}_{output_path}"
                        temp_df.to_csv(backup_path, index=False)
                        print(f"Created backup at {backup_path}")
                    
                    # Also create time-based backups every hour
                    current_hour = datetime.now().strftime("%Y%m%d_%H")
                    hourly_backup_path = f"hourly_backup_{current_hour}_{output_path}"
                    if not os.path.exists(hourly_backup_path):
                        temp_df.to_csv(hourly_backup_path, index=False)
                        print(f"Created hourly backup at {hourly_backup_path}")
                        
            except Exception as exc:
                # Save data even when an exception occurs
                if all_data:
                    error_backup_path = f"error_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{output_path}"
                    pd.DataFrame(all_data).to_csv(error_backup_path, index=False)
                    print(f"Error occurred. Created emergency backup at {error_backup_path}")
                print(f"Error scraping {date}: {exc}")
    
    # Convert results to DataFrame and save final output
    df = pd.DataFrame(all_data)
    df.to_csv(output_path, index=False)
    print(f"Scraping complete. Saved {len(df)} entries to {output_path}")
    
    print(f"Temporary file {temp_output_path} kept as additional backup")

if __name__ == "__main__":
    main()
