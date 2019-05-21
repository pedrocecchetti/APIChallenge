# APIChallenge

This is an API created for the coding Challenge of Bemobi.

The API works as a URLshortener. 
You Send the URL that you want short and the API will return the new URL and some other info. 

## Installing
First you need to have python3 and pip installed in your machine.

Then go to your projects folder and clone this repository
```git clone https://github.com/pedrocecchetti/APIChallenge.git```

`cd APIChallenge`

You should set up an Virtualenv for the application, and as soon as you have the venv active just run:

```pip install -r requirements.txt```

You must setup your DB for the Database engine you're using, this project was build on POSTGRESQL.

Before running `db_setup.py` change the **create_engine** function argument with the DB you're working with, username and password, address and port.

You should follow this template:
```DBENGINE://USER:PASSWORD@ADDRESS:PORT/DB_NAME```

In my Project this was how it was set up:
```postgres://postgres:postgres@localhost:5432/shortenerapi```

After finishing the DB Setup and edited db_setup.py just run it:
```python db_setup.py```

Then you just have to run the app with:

```python app.py```


## Using the API
The API has 2 functionalities:

1. URLs and compute the time it took to do it
2. Retrieve the original URL that was shortened and redirect the user to it.

###1. To short the URL you must:
- Send a POST request to `localhost:8000/create` with parameters:
    - url(obligatory)
    - CUSTOM_ALIAS (Optional)

#### Example
To create a shortURL for the google website with alias=*gugel* you must send the request in the following format:
    ```POST localhost:8000/create?url=http://google.com&CUSTOM_ALIAS=gugel```

The response will be a JSON with the following format:

```  
    {  
        "alias": "gugel",  
        "id": 5,  
        "original_url": "http://google.com",  
        "shortened_url": "/u/gugel",  
        "time_taken": "775.21ms"  
    }  
```

###2. To Retrieve a shortened URL:

- You must send a GET request to `localhost:8000/u/<alias>`

#### Example
To retrieve the google shortened URL we created you just have to send a GET as the following:
    
    ```GET localhost:8000/u/gugel```

- You'll be redirected to the original URL