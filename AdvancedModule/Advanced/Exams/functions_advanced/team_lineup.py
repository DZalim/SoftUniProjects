def team_lineup(*args):
    country_dict = {}

    for player, country in args:
        if country not in country_dict.keys():
            country_dict[country] = []
        country_dict[country].append(player)

    sorted_dict = sorted(country_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''

    for country, players in sorted_dict:
        result += f'{country}:\n'
        for player in players:
            result += f'  -{player}\n'

    return result.strip()


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
