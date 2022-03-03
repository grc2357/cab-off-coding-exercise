# API Documentation

The API has the following endpoints.

1. /hello_world/

    The hello_world endpoint receives a GET request and returns the JSON data {"greeting": "Hello World"}.

2. /add_numbers/

    This endpoint receives a POST request with the JSON data {"numbers": [num1, num2]} and returns
    the JSON data {"result": num1+num2}.
    This endpoint accepts any values that can be converted to a float with Python's float() function.
    In the event that incorrect data is received, a 400 Bad Request status code is returned with the JSON data.
    
    {"detail": ["The input must be an array of two numbers!"]}

3. /link_strings/

    This endpoint receives a POST request with the JSON data {"strings": ["str1", "str2"]} and returns
    the JSON data {"string": "str1-str2"}.
    In the event that incorrect data is received, a 400 Bad Request status code is return with the JSON data.

    {"detail": ["The input must be an array of two strings!"]}

## Instructions for use

As it's in the desirable skills, I have assumed that the machine on which the API is to be evaluated has docker installed 
and therefore I have included the following files.

* Dockerfile
* docker-compose.yml
* requirements.txt

Once this repository has been cloned, navigate to the location of the docker-compose.yml file and enter the command

* docker-compose build

to create the docker image and then enter the command

* docker-compose up

to start the container.

The active container will be listening on port 8000, so opening a browser at http://127.0.0.1:8000(endpoint), 
where (endpoint) is one of the endpoints listed above, should give access to the Django REST framework interface.
Alternatively, the API has also been tested with Postman with the same urls.

## Tests

In Docker Desktop, select the container running this code and then click CLI.
The CLI should open in the directory containing manage.py, if not navigate there and enter the command

* python manage.py test

to run the nine automated tests.