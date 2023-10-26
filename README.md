# bckPower

![League of legend Logo](https://oyster.ignimgs.com/mediawiki/apis.ign.com/league-of-legends/8/86/League_of_legends_logo_transparent.png?width=640)

| Release Date(s) | Framework | Github | Official Links | Demo |
| :-----------------: | :-----------:| -----:| -----------------:| -------:|
| October 23, 2023   | Django, Python, PostgreSQL | [bckPower](https://github.com/yonathanavila/bckPower) | [API](https://google.com) | [YouTube](http://youtube.com) |

|    Name      | Base Path | Route | Search Param | Example |
| :----------: | :--------:| :----:| :-----------:| :-----: |
| Tournament rankings | /api/v1/rankings/ | tournament_rankings/{tournament_id}/ | stage _string_ | http://127.0.0.1:8000/api/v1/ranking/tournament_rankings/108998961191900167?stage=Groups |
| Global rankings | /api/v1/rankings/ | global_rankings/ | number_of_teams _number_ | http://127.0.0.1:8000/api/v1/ranking/global_rankings?number_of_teams=20 |
| Team rankings | /api/v1/rankings/ | team_rankings/ | team_ids _array_ | http://127.0.0.1:8000/api/v1/ranking/team_rankings?team_ids=[98767991853197861,98767991926151025,98767991853197861] |
## Inspiration

League of legend is my favorite game, and data analysis is one of my favorites topics in computing science

## What it does

Return the champions by ranking 

## How we built it

The projects is build it with Django REST Framework and PostgreSQL DB.

## Challenges we ran into

- Complexion of the data struct
- Analysis and model the DB
-Upload the information inside the DB

## Accomplishments that we're proud of

- Return to my favorite framework Django 
- Build in my favorite game

## What we learned

- Complexion of query data
- Technical thinking to take decisions

## What's next for Power Ranking API

- Maintenance the information at the time
- Better documentation and building process
- Add IA to add graphs about stats (Lineal regressions, etc)