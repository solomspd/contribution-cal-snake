import requests
import json
from dotenv import load_dotenv
import os
import logging
import io

load_dotenv()  # take environment variables from .env.

URL = "https://api.github.com/graphql"


def fetch(query):
    token = os.environ.get("ACCESS_TOKEN")
    headers = {
        "Content-type": "application/json",
        "Authorization": "token " + token,
    }

    r = requests.post(url=URL, json=query, headers=headers)

    if r.status_code != 200:
        print("Error: ", r.status_code)
        logging.error("Error: " + str(r.status_code))
        return None

    r_dict = json.loads(r.text)
    pic = io.BytesIO(
        requests.get(
            f"https://github.com/{r_dict['data']['viewer']['login']}.png"
        ).content
    )
    return map_response(r_dict), pic


def map_response(response):
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


def get_data():
    query = {
        "query": """
    {
        viewer { 
            login,
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
    logging.debug(ret)
    return ret
