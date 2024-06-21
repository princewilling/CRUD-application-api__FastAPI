[![Build and Deploy Code](https://github.com/princewilling/CRUD_application_api__FastAPI/actions/workflows/build-deploy.yml/badge.svg)](https://github.com/princewilling/CRUD_application_api__FastAPI/actions/workflows/build-deploy.yml)

# CRUD API with FastAPI

## Core functionality

- User Auth
- Create Post
- Read Post
- Update Post
- Delete Post
- UpVote and DownVote Post
- Comment on Post

## How To Run

Requires; Docker and Docker Compose

It would be benificial if you're conversant with using docker and docker compose.

- Install Docker: <https://docs.docker.com/engine/install/>
- Install Docker Compose: <https://docs.docker.com/compose/install/>

To make the api easy to run and accessible, docker and docker-compose is used. Docker allows to build, test, and deploy applications quickly. Compose is a tool for defining and running multi-container Docker applications(the api app and postgres db in this case). Check the `Dockerfile` and `docker-compose-*.yml` to gain more insight.

EXECUTE `$ docker compose --file docker-compose-*.yml build` to build the docker image for the api

EXECUTE `$ docker compose --file docker-compose-*.yml up` to spin-up the api containter and postgres container

EXECUTE `$ docker compose --file docker-compose-*.yml down` to stop and romove running containers

To run without docker;

Create and Activate a virtual env on your machine

EXECUTE: `pip install -r requirements.txt` to install dependencies

EXECUTE: `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload` to start api application

## API Endpoints

### User Sign UP

    curl --request POST \
    --url http://localhost:8000/users \
    --header 'Content-Type: application/json' \
    --data '{
        "email": "eternal@gmail.com",
        "password":1234
    }'

    output:
        {"id": 1,
        "email": "eternal@gmail.com",
        "created_at": "2023-03-17T09:34:33.277682+00:00"
        }

### User Log IN

    curl --request POST \
    --url http://localhost:8000/login \
    --header 'Content-Type: multipart/form-data' \
    --form username=eternal@gmail.com \
    --form password=1234

    output:
    
        {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNDY4NzF9.aPwEc2HQCWNlVsPiOFWYFn0-gr9V6ojAoVjs3DVX6ew",
        "token_type": "bearer"
        }

### Get User

:unlock:    *! does not require authentication*

    curl --request GET \
    --url http://127.0.0.1:8000/users/1

    output:
    
        {"id": 1,
        "email": "eternal@gmail.com",
        "created_at": "2023-03-16T21:10:02.120403+00:00"
        }

### Create Post

:closed_lock_with_key:      *! does require authentication*

    curl --request POST \
    --url http://127.0.0.1:8000/posts/ \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNTE2ODB9.dwP_Aw7eVaNP1fnAi4ZvYul8owO4YnUmXdAEAx98eNw' \
    --header 'Content-Type: application/json' \
    --data '{
        "title": "Better Days",
        "content": "We never count the hours untill they are running ou"
        }'

    output:
    
        {"title": "Better Days",
        "content": "We never count the hours untill they are running ou",
        "published": true,
        "id": 1,
        "created_at": "2023-03-17T10:45:23.036179+00:00",
        "owner_id": 1,
        "owner": {
            "id": 1,
            "email": "eternal@gmail.com",
            "created_at": "2023-03-16T21:10:02.120403+00:00"
            }
        }

### Get Posts

:closed_lock_with_key:      *! does require authentication*

    curl --request GET \
    --url http://127.0.0.1:8000/posts/ \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNTE2ODB9.dwP_Aw7eVaNP1fnAi4ZvYul8owO4YnUmXdAEAx98eNw'

    output:
        [
            {
            "Post": {
            "title": "Better Days",
            "content": "We never count the hours untill they are running out",
            "published": true,
            "id": 2,
            "created_at": "2023-03-17T10:54:32.874489+00:00",
            "owner_id": 1,
            "owner": {
                "id": 1,
                "email": "eternal@gmail.com",
                "created_at": "2023-03-16T21:10:02.120403+00:00"
                }
            },
            "votes": 0
            },
            {
            "Post": {
            "title": "Dreamer",
            "content": "I might show up a little late",
            "published": true,
            "id": 3,
            "created_at": "2023-03-17T10:55:28.023388+00:00",
            "owner_id": 1,
            "owner": {
                "id": 1,
                "email": "eternal@gmail.com",
                "created_at": "2023-03-16T21:10:02.120403+00:00"
                }
            },
            "votes": 0
            },
            {
            "Post": {
            "title": "Better Days",
            "content": "We never count the hours untill they are running ou",
            "published": true,
            "id": 1,
            "created_at": "2023-03-17T10:45:23.036179+00:00",
            "owner_id": 1,
            "owner": {
                "id": 1,
                "email": "eternal@gmail.com",
                "created_at": "2023-03-16T21:10:02.120403+00:00"
                }
            },
            "votes": 0
            }
        ]

### Get Post(s) (With Query Param)

:closed_lock_with_key:      *! does require authentication*

    curl --request GET \
    --url 'http://127.0.0.1:8000/posts/?limit=1&search=Days' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNTE2ODB9.dwP_Aw7eVaNP1fnAi4ZvYul8owO4YnUmXdAEAx98eNw'

    output:

        [
            {
            "Post": {
            "title": "Better Days",
            "content": "We never count the hours untill they are running ou",
            "published": true,
            "id": 1,
            "created_at": "2023-03-17T10:45:23.036179+00:00",
            "owner_id": 1,
            "owner": {
                "id": 1,
                "email": "eternal@gmail.com",
                "created_at": "2023-03-16T21:10:02.120403+00:00"
                }
            },
            "votes": 0
            }
        ]

### Get Single Post

:closed_lock_with_key:      *! does require authentication*

    curl --request GET \
    --url http://127.0.0.1:8000/posts/3 \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNTE2ODB9.dwP_Aw7eVaNP1fnAi4ZvYul8owO4YnUmXdAEAx98eNw'

    output:

        {
            "Post": {
            "title": "Dreamer",
            "content": "I might show up a little late",
            "published": true,
            "id": 3,
            "created_at": "2023-03-17T10:55:28.023388+00:00",
            "owner_id": 1,
            "owner": {
            "id": 1,
            "email": "eternal@gmail.com",
            "created_at": "2023-03-16T21:10:02.120403+00:00"
            }
            },
        "votes": 0
        }

### Update Post

:closed_lock_with_key:      *! does require authentication*

    curl --request PUT \
    --url http://127.0.0.1:8000/posts/1 \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNTM5NjJ9.A4pPQltzAFZFxkHi_8COeId3Jxm9Yrot6Tm47bv1sVU' \
    --header 'Content-Type: application/json' \
    --data '{
        "title": "Mad Love The Prequel",
        "content": "Greet everydody for here"
        }'

    output:
        {
            "title": "Mad Love The Prequel",
            "content": "Greet everydody for here",
            "published": true,
            "id": 1,
            "created_at": "2023-03-17T10:45:23.036179+00:00",
            "owner_id": 1,
            "owner": {
            "id": 1,
            "email": "eternal@gmail.com",
            "created_at": "2023-03-16T21:10:02.120403+00:00"
            }
        }

### Delete Post

:closed_lock_with_key:      *! does require authentication*

    curl --request DELETE \
    --url http://127.0.0.1:8000/posts/4 \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNTM5NjJ9.A4pPQltzAFZFxkHi_8COeId3Jxm9Yrot6Tm47bv1sVU'

    output:
        status code: 204

### Up Vote a Post

:closed_lock_with_key:      *! does require authentication*

    curl --request POST \
    --url http://127.0.0.1:8000/vote \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNTM5NjJ9.A4pPQltzAFZFxkHi_8COeId3Jxm9Yrot6Tm47bv1sVU' \
    --header 'Content-Type: application/json' \
    --data '{
        "post_id": 1,
        "dir": 1
    }'

    output:
        {
            "message": "successfully added vote"
        }

### Remove Up Vote on Post

:closed_lock_with_key:      *! does require authentication*

    curl --request POST \
    --url http://127.0.0.1:8000/vote \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NzkwNTM5NjJ9.A4pPQltzAFZFxkHi_8COeId3Jxm9Yrot6Tm47bv1sVU' \
    --header 'Content-Type: application/json' \
    --data '{
        "post_id": 1,
        "dir": 0
    }'

    output:
        {
            "message": "successfully deleted vote"
        }
