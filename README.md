# API Test
This is a test API. 
The goal of the test is to check specific architecture design.
The functions of this API are focused around NLP:
* Main content extraction
* Part of speech (POS)
* Name entity recognition (NER)
 
## Summary

For future reference I will here the entire process I did to get a fully functioning API.
### Files

#### grab_text_ana_analyze.py
This is the **hearth** of the API, here we have the NLP engine, that for each received URL can extract the main content or analyze POS and NER.

#### main.py
This is the API itself, built using `fastapi`, which facilitate the documentation of the API.

#### requirements.txt
All the necessary packages. There is an issue with the `spacy` english model. 
which needs to be updated with the full URL of the model. Otherwise, we get an error while trying to download the model in the server.

#### Procfile
Calling `gunicorn` which create a server with 4 workers.


### Process
1. This whole project is uploaded to [GitHub](https://github.com/dorlavie/testApi)
2. The GitHub repo is synchronized with [HEROKU app](https://dashboard.heroku.com/apps/dor-la-vie-testapi)
3. HEROKU initiate a sever with all the requirements (according to `requirements.txt`). Which make an [operational API already](https://dor-la-vie-testapi.herokuapp.com/docs)
4. To gain user management and monetisation functionality, we connect the HEROKU app to [rapidAPI](https://rapidapi.com/dorlavie/api/test1972)
