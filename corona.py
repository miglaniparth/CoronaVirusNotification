from plyer import notification
import requests
import time


def notify(mystr):
    notification.notify(
        title='  COVID-19 Update for INDIA',
        message=mystr,
        app_icon='C:\\Users\\parth\\Downloads\\corona-virus-568595.ico',
        timeout=10)


if __name__ == '__main__':
    url = ("https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search?search=india")
    while True:
        response = requests.get(url)
        var = response.json()
        d1=var['data']
        l1=d1['rows']
        d2=l1[0]
        mystr=f'''
Total Cases = {d2['total_cases']}
Active Cases = {d2['active_cases']}
Total Deaths = {d2['total_deaths']}
Source : API from postman.com'''
        notify(mystr)
        time.sleep(60*60)