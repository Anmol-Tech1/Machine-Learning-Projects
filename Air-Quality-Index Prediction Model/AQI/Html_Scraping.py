import os
import time
import requests
import sys

# function to retrieve html page for data collection


def retrieve_html():
    for year in range(2013, 2019):
        for month in range(1, 13):
            if(month < 10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(
                    month, year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(
                    month, year)

            # retrieve html from url
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')

            # Check for Dir if not available make the DIR
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))

            # open the Dir
            with open("Data/Html_Data/{}/{}.html".format(year, month), "wb") as output:
                output.write(text_utf)

        sys.stdout.flush()


# main program
if __name__ == '__main__':
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()

    print("Time Taken {}".format(stop_time-start_time))
