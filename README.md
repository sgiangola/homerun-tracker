# homerun-tracker
a web app to track a homerun pool using Flask and React

for full context, the homerun pool process is to have each entry pick from ranked tiers of sluggers and the person who has the highest aggregate at the end of the season wins. Player choices are not unique and each entry has access to every player on the pre-selected list.

this app uses a Flask backend to serve pages as well as for API calls for a local postgresql install. DDL setup scripts have not been included but update_db.py contains the ETL logic to update the database with data from https://www.mysportsfeeds.com/. 

this app also uses React for frontend UI. Calls to the flask API are made thru JSX via Axios. My first official foray into React so pay no mind to whatever may seem cobbled together =)

again note that db setup is not included:

run flask app

`python app.py`

run webpack to observe jsx for changes

`webpack --watch`

special thanks to the boilerplate repo found here: https://github.com/bonniee/react-flask
