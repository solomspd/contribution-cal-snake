
import requests
import json

URL = "https://api.github.com/graphql"

def fetch(query):
    token = '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'
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'token ' + token,
    }

    r = requests.post(url = URL, json = query, headers= headers)
    
    if r.status_code != 200:
        print('Error: ' + str(r.status_code))
        return None

    r_dict = json.loads(r.text)

    return mapResponse(r_dict)

def mapResponse(response):
    weeks = response.get('data').get('viewer').get('contributionsCollection').get('contributionCalendar').get('weeks')
    #map objects of weeks to contributionCount
    return list(map(lambda week: list(map(lambda day: day.get('contributionCount'), week.get('contributionDays'))), weeks))

    

def getContributionsCalendar():
    query ={'query':'''
    {
        viewer { 
            contributionsCollection {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            contributionCount
                        }
                    }
                }
            }
        }
    }
  '''}
    return fetch(query)