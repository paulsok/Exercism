def tally(rows):
    abbr = ('Team', 'MP', 'W', 'D', 'L', 'P')
    tmpl = '{:30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}'
    results = {}
    table = []

    for row in rows:
        team_1, team_2, team_1_score = row.split(';')

        if team_1_score == 'win':
            team_2_score = 'loss'
        elif team_1_score == 'draw':
            team_2_score = 'draw'
        else:
            team_2_score = 'win'

        results.setdefault(team_1, []).append(team_1_score)
        results.setdefault(team_2, []).append(team_2_score)

    for team in results:
        wins = results[team].count('win')
        losses = results[team].count('loss')
        draws = results[team].count('draw')
        points = wins * 3 + draws
        table.append([team, len(results[team]), wins, draws, losses, points])

    table_str = [[str(i) for i in j] for j in table]
    table_sort = sorted(sorted(table_str), key=lambda x: x[5], reverse=True)
    tournament = [tmpl.format(*i) for i in table_sort]
    tournament.insert(0, tmpl.format(*abbr))

    return tournament
