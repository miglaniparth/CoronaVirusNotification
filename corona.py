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
    url = ("https://corona.lmao.ninja/v2/countries/India?yesterday&strict&query")
    while True:
        response = requests.get(url)
        var = response.json()
        print(var)
        mystr=f'''
Total Cases = {var['cases']}
Active Cases = {var['active']}
Total Deaths = {var['deaths']}
Source : NovelCOVID API'''
        notify(mystr)
        time.sleep(60*60)
