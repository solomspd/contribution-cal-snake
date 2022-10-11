from bisect import bisect_left
import requests
import json
import pygame as pg

import numpy as np


URL = "https://api.github.com/graphql"


def fetch(query):
    token = "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"
    headers = {
        "Content-type": "application/json",
        "Authorization": "token " + token,
    }

    r = requests.post(url=URL, json=query, headers=headers)

    if r.status_code != 200:
        print("Error: " + str(r.status_code))
        return None

    r_dict = json.loads(r.text)

    return mapResponse(r_dict)


def mapResponse(response):
    weeks = (
        response.get("data")
        .get("viewer")
        .get("contributionsCollection")
        .get("contributionCalendar")
        .get("weeks")
    )
    # map objects of weeks to contributionCount
    return list(
        map(
            lambda week: list(
                map(
                    lambda day: day.get("contributionCount"),
                    week.get("contributionDays"),
                )
            ),
            weeks,
        )
    )


def getContributionsCalendar(bins=6):
    query = {
        "query": """
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
  """
    }
    ret = fetch(query)
    mx = max(map(max, ret))
    mn = max(map(min, ret))
    bounds = np.linspace(mn, mx, bins)
    colors = [
        pg.Color(i) for i in ["#2d333b", "#0e4429", "#006d32", "#26a641", "#39d353"]
    ]
    for i in range(len(ret)):
        for j in range(len(ret[i])):
            ret[i][j] = colors[min(bisect_left(bounds, ret[i][j]), len(colors) - 1)]
    return ret
