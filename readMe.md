# E-commerce Product Data Harvester

The E-commerce Product Data Harvester is a Python script designed to automate the extraction of product information from popular e-commerce websites such as Amazon and eBay. This tool enables users to specify a product of interest and the number of items they wish to retrieve from each site. The script navigates to the respective websites, performs a search, and extracts the names and prices of the top products matching the search criteria. The retrieved data is then saved to a CSV file for further analysis or reference.

## Key Features

- **Automated Data Retrieval:** Retrieve product information from Amazon and eBay without manual intervention.
- **Customizable Search Parameters:** Specify the product name and the number of items to search for.
- **Web Scraping with Selenium:** Utilize Selenium WebDriver for web scraping capabilities.
- **CSV Output:** Save the extracted data to a CSV file for easy manipulation and analysis.
- **User-Friendly Interface:** Interact with the script via a simple dialogue box for inputting search parameters.
- **Error Handling:** Robust error handling and timeout management ensure smooth performance.

## Usage

1. **Install Dependencies:**
   - Ensure you have Python 3.x installed on your system.
   - Install the required Python packages using `pip install -r requirements.txt`.

2. **Launch the Script:**
   - Run the `product_data_harvester.py` script using Python.
   - Alternatively, execute the `main.py` file for a graphical user interface.

3. **Input Search Parameters:**
   - When prompted, enter the product name and the desired number of items to search for.

4. **Data Retrieval:**
   - The script will automatically navigate to Amazon and eBay, retrieve the specified product information, and save it to a CSV file.

5. **CSV Output:**
   - Once the process is complete, a dialogue box will prompt you indicating that the CSV file has been generated.

## Dependencies

- Python 3.x
- Selenium WebDriver
- Tkinter (for GUI)
- CSV module

## Notes

- Make sure to have the necessary WebDriver (e.g., ChromeDriver) installed and configured.
- Ensure an active internet connection for accessing the e-commerce websites.
- Adjust the timeout settings in the script (`fetch_top_products` function) if needed.

## Author
- Neil Duraiswami

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
