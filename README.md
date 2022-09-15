# Giuseppes Pizzeria

Guiseppes is a family run pizzeria and this webiste has been designed to provide a booking and contact service

## Description

This website has been designed to allow the user/customer create, update or delete a booking without having to call the resurant
to create a booking. It also allows the user to view an online menu so they can have an informed decision on weather they would book the resurant or not. The contact section allows the user to contact the resturant with any complaints or questions about the establishment/menu.


### Dependencies

All the dependencies can be found in the "requirements.txt" file.


### Installing

* The project can be downloaded from https://github.com/AlrxDaley/Giuseppes-Pizzeria-Milestone
* To get the prioject working you will need to install the requirments.txt file, use the command below to install it
```
    - pip install -r requirements.txt
```

### Executing program

* To execute the program open the terminal
* type "python3 manage.py runserver"
* click enter and a IP links should apear in the terminal
* command click the link and it will take you to the page

## User Stories

* See/Download the menu
    - i have implemented half of this user story by having the menu displayed on the front page of the web page

* See available time
    - i havent been able to apply this user story due to complications with the CRUD functionalties that have taken longer 
    then expected to solve this is the same with #5,7,8,9 user stories

* Create a booking
    - i have implemented this with the Curd functionlity along with the #1 and #2 user stories aswell


## Testing

I have tested the website in multiple ways, such as using auto testing functions supplied by django aswell 
as letting people use the website to find bugs.

You can find the testing function in the ``` test.py ``` file.

## Bugs

    #1 When trying to update the user booking but you dont want to change the time or date of the original booking it throws up
    an error talking about a formatting issue.
        - i plan to fix this error by finding a way to keep the datefield formatted in the correct way. i will also check if the input is empty
        and if it is the date that was previously in the field will be reinstreted into the field.
    
    #2 The second error is very much similar to the 

## Future developments

## Wire Frames
<img src="https://res.cloudinary.com/dkpchnxiu/image/upload/v1663268686/GiuseppesImages/booking%20page.png">
<img src="https://res.cloudinary.com/dkpchnxiu/image/upload/v1663268686/GiuseppesImages/booking%20form.png">
<img src="https://res.cloudinary.com/dkpchnxiu/image/upload/v1663268685/GiuseppesImages/contact%20form.png">
<img src="https://res.cloudinary.com/dkpchnxiu/image/upload/v1663268685/GiuseppesImages/main%20page.png">
## Authors

Contributors names and contact info

Alex Daley 

Alexander_daley@icloud.com


## Acknowledgments

I would like to give acknowlagements to the multiple stack overlfow sources and the django documentation i have used/looked into
to help fix bugs add functionality.
- https://stackoverflow.com
- https://docs.djangoproject.com/en/4.1/


