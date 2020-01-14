# Desafio Celero Back-end

### Project

This was made using Django and Django REST Framework

### Setup

Install the depencies

Using Pipenv
```sh
$ pipenv shell
$ pipenv install
```

Using pip
```sh
$ pip install -r requirements.txt
```

Migrate the databse

```sh
$ cd celero
celero$ ./manage.py makemigrations
celero$ ./manage.py migrate
```


To populate the database execute
```sh
celero$ ./setup
```

or passing the number os rows to read(runs quickly)
```sh
celero$ ./setup nrows
```

To start the server
```sh
celero$ ./manage.py runsever
```

To run the tests
```sh
celero$ ./manage.py test
```

### API endpoints:

#### Sport
    GET:    /sports/ -> list all sports.
    GET:    /sports/[id]/ -> info of one sport.
    POST:   /sports/ -> create new sport.
    PATCH:  /sports/[id]/ -> modify sport.
    PUT:    /sports/[id]/ -> modify sport(require all fields).
    DELETE: /sports/[id]/ -> remove sport.

##### Examples:

**GET: /sports/**

```json
[
    {
        "name":"Sport Name",
        "id": 1
    },
    {
        "name":"Sport Name 2",
        "id": 2
    }
]
```

**POST: /sports/**

```json
{
    "name":"Sport Name",
}
```


**GET: /sports/1/**
```json
{
	"name":"Sport Name",
    "id": 1
}
```

#### Event

    GET:    /events/ -> list all events.
    GET:    /events/[id]/ -> info of one event.
    POST:   /events/ -> create new event.
    PATCH:  /events/[id]/ -> modify event.
    PUT:    /events/[id]/ -> modify event(require all fields).
    DELETE: /events/[id]/ -> remove event. 

##### Examples:

**GET: /events/**

```json
[
    {
        "name":"Event Name",
        "sport": 1,
        "id": 1
    },
    {
        "name":"Event Name 2",
        "sport": 2,
        "id": 2
    }
]
```

**POST: /events/**

```json
{
    "name":"Event Name",
    "sport": 1
}
```

**GET: /events/1/**

```json
{
	"name":"Event Name",
    "sport": 1,
    "id": 1
}
```

#### Olympic

    GET:    /olympics/ -> list all olympics.
    GET:    /olympics/[id]/ -> info of one olympic.
    POST:   /olympics/ -> create new olympic.
    PATCH:  /olympics/[id]/ -> modify olympic.
    PUT:    /olympics/[id]/ -> modify olympic(require all fields).
    DELETE: /olympics/[id]/ -> remove olympic.


##### Examples:

**GET: /olympics/**

```json
[
    {
        "year": 2020,
        "city": "City Name",
        "season": "Summer",
        "id": 1
    },
    {
        "year": 2020,
        "city": "City Name 2",
        "season": "Winter",
        "id": 2
    }
]
```

**POST: /olympics/**

```json
{
    "year":2020,
    "city": "City Name",
    "season": "Winter"
}
```

**GET: /olympics/1/**

```json
{
    "year": 2020,
    "city": "City Name",
    "season": "Summer",
    "id": 1
}
```

#### Team

    GET:    /teams/ -> list all teams.
    GET:    /teams/[id]/ -> info of one team.
    POST:   /teams/ -> create new team.
    PATCH:  /teams/[id]/ -> modify team.
    PUT:    /teams/[id]/ -> modify team(require all fields).
    DELETE: /teams/[id]/ -> remove team. 

##### Examples:

**GET: /teams/**

```json
[
    {
        "noc": "ABC",
        "name": "Name",
        "notes": null,
        "id": 1
    },
    {
        "noc": "DEF",
        "name": "Name 2",
        "notes": "note",
        "id": 1
    }
]
```

**POST: /teams/**

```json
{
    "noc": "ABC",
    "name": "Name",
}
```

**GET: /teams/1/**

```json
{
    "noc": "ABC",
    "name": "Name 1",
    "notes": "note",
    "id": 1
}
```

#### Athlete

    GET:    /athletes/ -> list all athletes.
    GET:    /athletes/[id]/ -> info of one athlete.
    POST:   /athletes/ -> create new athlete.
    PATCH:  /athletes/[id]/ -> modify athlete.
    PUT:    /athletes/[id]/ -> modify athlete(require all fields).
    DELETE: /athletes/[id]/ -> remove athlete. 

##### Examples:

**GET: /athletes/**

```json
[
    {
        "name": "Name",
        "sex": "Female",
        "team": 2,
        "id": 1
    },
    {
        "name": "Name 2",
        "sex": "Male",
        "team": 1,
        "id": 2
    }
]
```

**POST: /athletes/**

```json
{
    "name": "Name",
    "sex": "Male",
    "team": 1
}
```

**GET: /athletes/1/**

```json
{
    "noc": "ABC",
    "name": "Name 1",
    "notes": "note",
    "id": 1
}
```

#### OlympicEvent

    GET:    /olympicEvents/ -> list all olympicEvents.
    GET:    /olympicEvents/[id]/ -> info of one olympicEvent.
    POST:   /olympicEvents/ -> create new olympicEvent.
    PATCH:  /olympicEvents/[id]/ -> modify olympicEvent.
    PUT:    /olympicEvents/[id]/ -> modify olympicEvent(require all fields).
    DELETE: /olympicEvents/[id]/ -> remove olympicEvent. 

##### Examples:

**GET: /olympicEvents/**
```json
[
    {
        "medal": null,
        "event": 1,
        "olympic": 1,
        "athlete": 1,
        "age": 30,
        "height": 180,
        "weight": 70,
        "id": 1
    },
    {
        "medal": "Gold",
        "event": 2,
        "olympic": 2,
        "athlete": 2,
        "age": 27,
        "height": 180,
        "weight": 70,
        "id": 2
    }
]
```

**POST: /olympicEvents/**

```json
{
    "medal": "Silver",
    "event": 1,
    "olympic": 1,
    "athlete": 1,
    "age": 30,
    "height": 180,
    "weight": 70,
}
```

**GET: /olympicEvents/1/**

```json
{
    "medal": "Silver",
    "event": 1,
    "olympic": 1,
    "athlete": 1,
    "age": 30,
    "height": 180,
    "weight": 70,
    "id": 1
}
```

## Models

### Sport

| Field | Type    |
|-------|---------|
|   id  | Integer |
| name  | String  |


### Events

| Field     | Type        |
|-----------|-------------|
|   id(PK)  | Integer     |
| name      | String      | 
| sport     | Foreign Key |


### Olympic

| Field     | Type    |
|-----------|---------|
|   id(PK)  | Integer |
| year*     | Inter   |
| season**  | String  |
| city      | String  |

**\*Year has a min value of 1896 and max value of 32767**
**\*\*Season can only have one of these values: Summer or Winter**

### Team

| Field     | Type    |
|-----------|---------|
|   id(PK)  | Integer |
|   noc*    | String  |
| name      | String  |
| notes     | String  |

**\*NOC is fixed at three characters**


### Athlete

| Field     | Type         |
|-----------|--------------|
| id(PK)    | Integer      |
| team      | Foreign Key  |
| name      | String       |
| sex*      | String       |

**\*Sex can only have one of these values: Male or Female**
### OlympicEvent
| Field   | Type             |
|---------|------------------|
|   id    | Integer          |
| medal*  | String           |
| event   | Foreign Key      |
| olympic | Foreign Key      |
| athlete | Foreign Key      |
| age     | Positive Integer |
| height  | Positive Integer |
| weight  | Positive Integer |

**\*Medal can have one of these values: Gold, Silver or Bronze**

## Missing part
-   Deploy to a server

## Future Changes
-   Improve Test
-   Improve script to populate the database(takes long time to run)
-   User authentication and restricted access to modify and create
