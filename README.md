# Product Price Comparison Script

This Python script allows users to compare product prices across different e-commerce websites (currently supporting Amazon, Snapdeal, and Flipkart). It scrapes product information from the provided URLs and displays the results in a formatted table.

## Features

- Supports multiple e-commerce websites (Amazon, Snapdeal, Flipkart)
- Handles CAPTCHA challenges by displaying the image and allowing user input
- Presents results in a neat, tabular format using PrettyTable
- Extracts product names and prices from web pages

## Requirements

To run this script, you need Python 3.x and the following libraries:

- requests
- tldextract
- beautifulsoup4
- opencv-python
- numpy
- prettytable

You can install these dependencies using pip:

```
pip install requests tldextract beautifulsoup4 opencv-python numpy prettytable
```

## Usage

`git clone https://github.com/Rudhra0811/PriceComparision.git`
<br/>
`cd PriceComparision`

1. Run the script:
   ```
   python product_price_comparison.py
   ```

2. When prompted, enter two URLs for the same product from different supported e-commerce websites.

3. The script will attempt to scrape the product information. If a CAPTCHA is encountered, it will display the CAPTCHA image and prompt you to enter the CAPTCHA text.

4. After processing both URLs, the script will display a table with the following information for each product:
   - Domain (website name)
   - Product Name
   - Price

## Limitations

- The script currently supports only Amazon, Snapdeal, and Flipkart.
- It may break if the websites change their HTML structure.
- CAPTCHA handling is basic and may not work for all types of CAPTCHAs.

## Future Improvements

- Add support for more e-commerce websites
- Implement more robust CAPTCHA handling
- Add error handling and retry mechanisms for failed requests
- Implement logging for better debugging
- Add option to export results to CSV or other formats

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.
