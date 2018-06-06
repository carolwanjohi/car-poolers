# Car Poolers
#### An application that allows users to share a ride from one place to another., 01/12/2017


#### By **[Carol Wanjohi](https://github.com/carolwanjohi)**

## Description
[This](https://car-poolers.herokuapp.com/) is an application that allows users to share a ride from one place to another. Users can log into the site, find a driver near them with space in his/her car heading to the same direction as the user and book a space.

## User Stories
As a user I would like to:
* sign up as either a passenger or driver
* view a map of all the pick up points
* set up a profile about me and a general location
* find a list of drivers near me
* view a map of all the pick up points
* review a driver and to be reviewed by a driver
* view the current space left in a driver's car and get to book it

As a driver I would to:
* set up my profile to have details about my car
* set my current location and where I am heading to

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display driver or passenger log in option | N/A | Display links to either the driver or passenger accounts |
| Create a driver account | **Click** driver option <br> First name: John <br> Last name: Doe <br> Phone number: 07******* | Create a driver account and profile for the user and log the user into the site |
| Create a passenger account | **Click** driver option <br> First name: John <br> Last name: Doe <br> Phone number: 07******* | Create a passenger account and profile for the user and log the user into the site |
| Update driver profile | **Click** update profile | Direct the user to a page with a form where the user can update their profile and submit the form |
| Update passenger profile | **Click** update profile | Direct the user to a page with a form where the user can update their profile and submit the form |
| Passenger review a driver | **Click Drivers** in the navbar <br> **Click** on a driver  | Direct user to the selected driver's profile where the user can fill the review form and submit their review |
| Driver review a passenger | **Click Passengers** in the navbar <br> **Click** on a passenger  | Direct user to the selected passenger's profile where the user can fill the review form and submit their review |
| Driver setting current location and destination | **Click** new journey | Direct user to a page with a form where the user can input their current location, destination and submit the form |
| Passenger seeing drivers near them | **Click** explore icon | Direct user to a page with a list of drivers near the current passenger |
| Passenger booking a seat in a car| **Click** driver displayed <br> **Click** book seat | Book seat for passenger |

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet

### Installation Process
```
git clone https://github.com/carolwanjohi/car-poolers.git && cd cd car-poolers
virtualenv virtual or python3.6 -m venv virtual
source virtual/bin/activate
pip3 install -r requirements.txt
```
* Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
USER=<your postgresql username>
PASSWORD=<your postgresql password>
```
* Create Postgres Database
```
psql
CREATE DATABASE pooler;
```
### Running the application
```
./manage.py runserver or python3.6 manage.py runserver
```

### Running the tests
```
./manage.py test or python3.6 manage.py test
```

## Known Bugs

* viewing pick up points feature missing

## Technologies Used
- Python 3.6.2
- Django 1.11.7
- Bootstrap 3
- Postgres Database
- CSS
- HTML
- Heroku

### License

MIT (c) 2017 **[Carol Wanjohi](https://github.com/carolwanjohi)**



