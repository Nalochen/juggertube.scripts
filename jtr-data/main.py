import requests

from TournamentDetailsParser import parser as tournament_parser
from TournamentOverviewParser import parser as overview_parser

tournament_url = 'https://turniere.jugger.org/'
previous_suffix = 'index.event.php#previous'
tournament_suffix = 'tournament.php?id='


def main():
    response = requests.get(tournament_url + previous_suffix)

    juggertube_html = response.text

    overview_parser.feed(juggertube_html)

    tournament_response = requests.get(tournament_url + tournament_suffix +
                                       overview_parser.tournament_array[0].tournament_id)
    tournament_html = tournament_response.text
    tournament_parser.feed(tournament_html)

    start, end = tournament_parser.get_temp_dates()

    tournaments = []

    for tournament in overview_parser.tournament_array:
        response = requests.get(tournament_url + tournament_suffix + tournament.tournament_id)
        tournament_html = response.text

        tournament_parser.feed(tournament_html)

        start, end = tournament_parser.get_temp_dates()

        tournament.start_date = start
        tournament.end_date = end

        tournaments.append(tournament)

    outfile = open('tournaments.json', 'w', encoding="utf-8")
    for tournament in overview_parser.tournament_array:
        line = ('{"id": "' + tournament.tournament_id + '", "name": "' + tournament.name + '", "start_date": "' +
                tournament.start_date + '", "end_date": "' + tournament.end_date + '", "city": "' +
                tournament.city + '", "country": "' + tournament.country + '"},\n')
        outfile.write(line)


if __name__ == '__main__':
    main()
