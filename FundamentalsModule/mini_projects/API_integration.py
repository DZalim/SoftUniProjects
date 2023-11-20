import requests


def team_statistics():

    url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

    querystring = {"league": "39", "season": "2020", "team": "33"}

    headers = {
        "X-RapidAPI-Key": "0f16fb60d8msh01b51a076d4e221p14b12bjsn396540799724",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        date = response.json()

        print(date)

    except requests.exceptions.RequestException as e:
        print("Error", e)


current_team_statistics = team_statistics()
print(current_team_statistics)
