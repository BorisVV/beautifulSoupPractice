

from bs4 import BeautifulSoup
import requests





'First scraping'
# 'http://www.startribune.com/weather/'

def write_report(report): # This writes the data to a text file
    f = open('weatherReport.txt', 'wb')
    f.write(bytes(report, encoding="ascii"))
    f.close


def get_url(url): # This gets the url and set ups the soup.
    url = requests.get(url)
    soup = BeautifulSoup(url.content, 'html.parser')
    return soup


urlSoupNY = get_url('http://www.nytimes.com/weather')
def get_newYork(urlSoupNY): # This the second options for now.
    container = urlSoupNY.findAll('div', {'class': 'wCurrent'})
    conditions = container[0].text.strip()
    return conditions


urlSoupMN = get_url('http://www.startribune.com/weather/')
def get_weateter(urlSoupMN): # This is for the weather to be pulled.
    container = urlSoupMN.find('div', {'class': 'current-condition-mod'})
    conditions = container.span.text.strip()
    return conditions


def main(): # This is to get the data.
    print('''
    Enter a number for a city.
    1. Minneapolis, MN
    2. New York, NY
    ''')
    # This gets the information for each city.
    enterCity = input('Please select one of the from the list:\n')
    while True:
        if enterCity == '1':
            print('This are the conditions for your city today \n' + get_weateter(urlSoupMN))
            write_report(get_weateter(urlSoupMN))
            break
        if enterCity == '2':
            print('This are the conditions for your city today \n' + get_newYork(urlSoupNY))
            #TODO write to file failing
            # write_report(get_newYork(urlSoupNY))
            break
        else:
            print('City not in the list')
            continue

if __name__ == '__main__':
    main()
