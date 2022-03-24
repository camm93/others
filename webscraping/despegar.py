"""Dynamic Web Scraping using selenium.
Scraping flights from a flight booking website.
"""
from selenium import webdriver
import pandas as pd

__author__ = "Cristian Murillo"


class Flights:

    def __init__(self, website_url, driver_path_):
        self.website = website_url
        self.driver_path = driver_path_
        self.driver = None

    def connect(self):
        try:
            self.driver = webdriver.Chrome(self.driver_path)
            self.driver.get(self.website)
        except Exception as e:
            print("An error has ocurred {}".format(e))

    def catch_click(self, btn_xpath_):
        """click on the 'ver más ofertas' button"""
        more_btn = self.driver.find_element_by_xpath(btn_xpath_)
        self.driver.execute_script('arguments[0].click()', more_btn)

    def scraper(self, csv_filename_, btn_xpath_):
        self.connect()
        self.catch_click(btn_xpath_)
        flight_descriptions = self.driver.find_elements_by_class_name("offer-card-content")
        flight_prices = self.driver.find_elements_by_class_name("offer-card-pricebox")
        my_flights = []
        for i in range(len(flight_prices)):
            destination = flight_descriptions[i].find_element_by_class_name("offer-card-title").text
            extra = flight_descriptions[i].find_elements_by_class_name("offer-card-description")
            origin, airline = [elem.text for elem in extra]
            price = flight_prices[i].find_element_by_class_name("offer-card-pricebox-price-amount").text
            my_flights.append([destination[9:], origin[16:], airline[4:], price.replace('.', '')])

        df = pd.DataFrame(data=my_flights, columns=["Destination", "Origin", "Company", "Price"])
        print(df)
        df.to_csv(csv_filename_, index=False)

    def close_connection(self):
        self.driver.quit()


if __name__ == "__main__":
    website = "https://www.despegar.com.co/vuelos/pais/colombia"
    driver_path = "D:/Programando/chromedriver"
    csv_filename = "vuelos_despegar.csv"
    btn_xpath = '//em[text()="Ver más ofertas"]'
    flights = Flights(website, driver_path)
    flights.scraper(csv_filename, btn_xpath)
