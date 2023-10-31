# Backend Power Ranking API (bckPower) 

![League of legend Logo](https://oyster.ignimgs.com/mediawiki/apis.ign.com/league-of-legends/8/86/League_of_legends_logo_transparent.png?width=640)

| Release Date(s) | Framework | Github | Official Links | Demo |
| :-----------------: | :-----------:| -----:| -----------------:| -------:|
| October 23, 2023   | Django, Python, PostgreSQL | [bckPower](https://github.com/yonathanavila/bckPower) | [API](http://3.17.97.72:3301/api/v1/) | [YouTube](http://youtube.com) |

|    **API**      | Base Path | Route | Search Param | Example |
| :----------: | :--------:| :----:| :-----------:| :-----: |
| Tournament rankings | /api/v1/rankings/ | tournament_rankings/{tournament_id}/ | stage _string_ | [example 1](http://3.17.97.72:3301/api/v1/ranking/tournament_rankings/108998961191900167?stage=Groups) |
| Global rankings | /api/v1/rankings/ | global_rankings | number_of_teams _number_ | [example 2](http://3.17.97.72:3301/api/v1/ranking/global_rankings?number_of_teams=20) |
| Team rankings | /api/v1/rankings/ | team_rankings | team_ids _array_ | [example 3](http://3.17.97.72:3301/api/v1/ranking/team_rankings?team_ids=[98767991853197861,98767991926151025,98767991853197861]) |


|**AWS**|**Service name**|**Description**|**Endpoint**|
|:-----:|:--------------:|:-------------:|:----------:|
||Lightsail|The Backend Power Lol (bckPower) is deployed to in AWS Lightsail Bitnami Django Service|[URL](http://3.17.97.72)||
||Lightsail PostgreSQL|The PostgresSQL database is deployed in AWS Lightsail database management|ls-fcc8a31413cdfcad6aecb291ce3443af29d3deaa.cktpqzyjhu2w.us-east-2.rds.amazonaws.com|
## Inspiration

League of Legends is my favorite game, and data analysis is one of my favorite topics in computing science,  deploy in AWS for the first time was an amazing experience, choosing what service the correct was a hard task but It was done

## What it does

Return the champions by ranking 

## How we built it

The project is built with Django REST Framework and PostgreSQL DB.

## Challenges we ran into

- Complexion of the data struct
- Analysis and model of the DB
- Upload the information inside the DB

## Accomplishments that we're proud of

- Return to my favorite framework Django 
- Build in my favorite game

## What we learned

- Complexion of data querying
- Technical thinking to make decisions in what service are the correct to deploy

## What's next for Power Ranking API

- Maintenance of the information at the time
- IA integration for make graphs about stats (Lineal regressions, etc)
