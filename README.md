# OLX Car Cover Scraper

This is a simple Python script that scrapes car cover listings from OLX India (https://www.olx.in/items/q-car-cover) and saves the results to a CSV file.

## 🔧 What It Does

- Goes to the OLX car cover search page
- Extracts the title, location, price, and link of each listing
- Saves all the data into a file named `olx_car_covers.csv`

## 🐍 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

You can install the required libraries by running:

pip install requests beautifulsoup4

|| How to Run ||

Clone this repo:

cd olx-car-cover-scraper

Run the script:-

python olx_scraper.py

After running, check the olx_car_covers.csv file in the same folder for the output.

📁 Output Example
The CSV file will look something like this:

Title	          Location	        Price	          Link
Car Cover XL	  Delhi	            ₹500	          https://www.olx.in/...
Waterproof Set	Mumbai	          ₹799	          https://www.olx.in/...

📌 Notes
This is a basic scraper and only works for the first page.

You can modify the code to add pagination or filters if needed.
