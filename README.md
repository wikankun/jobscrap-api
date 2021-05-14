# Jobscrap API

Jobstreet Scrapping Application API

## How to run locally

- Provides `.env` file with your environment variables
- Run `virtualenv env`
- Run `. env/bin/activate`
- Run `pip install requirements.txt`
- Run `uvicorn app.app:app --reload`


## Deployed to Heroku

### Site URL

https://jobstreetscrap-api.herokuapp.com/

### Endpoints

- `GET` /jobs?apiKey=`your apikey`
- `GET` /jobs/:id?apiKey=`your apikey`

public `apikey` = 1234567asdfgh
