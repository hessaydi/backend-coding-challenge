from datetime import date, timedelta
import requests


def langs():
    days = 30
    delta = timedelta(days)
    dat= date.today() - delta

    response = requests.get(f"https://api.github.com/search/repositories?q=created:>{dat}&sort=stars&order=desc")


    langs = {}
    for i in response.json()['items']:
        if i['language'] in langs:
            langs[i['language']]['repos']+=1
            langs[i['language']]['list_of_repos'].append(i['html_url'])
        else:
            details = {
                "repos": 1,
                "list_of_repos":[i['html_url']]
            }
            langs[i['language']] = details
    return langs