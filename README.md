# AntiqueAtlas
## Accessing
### Install and Create a Virtual Environment
Step 1: Create a virtual environment.

Unix/Linux/macOS users run the following command 
```
python3 -m venv env
```
Windows users run the following command
```
py -m venv env
```
Step 2: Activate the virtual environment and verify it

Unix/Linux/macOS users run the following command 
```
source env/bin/activate
```
Windows users run the following command
```
.\env\Scripts\activate
```
If you have trouble in creating or activating the virtual environment refer to [this article](https://www.geeksforgeeks.org/python-virtual-environment/).

### Clone a GitHub Repository  

Copy the URL of the GitHub repository if you want to clone it. Run the git clone command in the terminal or git bash to clone the repository.
```
Syntax: git clone "URL of GitHub repository"
```
```
git clone https://github.com/Nandana-Neo/AntiqueAtlas.git

```
Navigate to project1 folder that has manage.py folder
### Deploy Django Project from GitHub

After the repository is cloned successfully change the directory to the recent clone repository in which the Django project is kept.
```
cd project1
```
Install the requirements (if any). Most of the projects have requirements.txt file which specifies the requirements of that project, so let’s install the requirements of it from the file.
```
pip install -r requirements.txt
```
```
Note: If the project don’t have the requirement.txt file you have to install requirements Individually which are required for the project. e.g., Django,python etc.
```

Run the Django server by running the below command.
```
python3 manage.py runserver
```


Go to the web browser and enter http://127.0.0.1:8000 to verify whether the application is running fine or not.

## Introduction
This website was created using HTML, CSS and Javascript for Frontend; Django for Backend; PostgreSQL for the database.<br>
This website consists of both fully functional frontend & backend. <br>
The contributors to this project are 
- NAILA FATHIMA
- NANDANA ANAND
- PRARTHANA PHUKAN
- VAISHNAVI RAJESH PAI

## Home page


https://github.com/Nandana-Neo/AntiqueAtlas/assets/129848120/ac35cb19-fd86-4ef8-857e-2875e4beaa48


- The home page of the website consists of an interesting collage, an image slider and an interactive navigation bar which connects across all the webpages.
- Required transitions have been incorporated to make provide an interesting user experience.

## Search page
![search1](https://github.com/Nandana-Neo/AntiqueAtlas/assets/129848120/f1ad1a88-4490-4721-8c6a-88c548b7ba56)
- Upon clicking the search button in the navigation bar, you reach the search page of the website.
- The search page has option to search for monuments according to their name/country/state/year/construction materials/architecture style.
  ![sea](https://github.com/Nandana-Neo/AntiqueAtlas/assets/129848120/80987ee4-c686-4aa3-aced-d0dcc6dfefd7)

- Depending on the search parameters provided by the user, a table with the fitting monument appears on the screen.
  ![search2](https://github.com/Nandana-Neo/AntiqueAtlas/assets/129848120/9dc1e804-306c-482c-9e9e-ed8de368fb40)

- The user can hover over and select the monument of his/her choice.
  ![search3](https://github.com/Nandana-Neo/AntiqueAtlas/assets/129848120/ddf29429-ecf8-405a-afea-f7542620fc8b)

  
- They will be then directed to the correspondiing monument page.

## Monument page


https://github.com/Nandana-Neo/AntiqueAtlas/assets/129848120/4cae835b-ef74-44ff-999d-18acdb8b6200


- They user will be welcomed by a dazzling image of the monument.
- They can scroll down to learn more information about the monument such as its location, year of construction, architecture style and materials used for its construction.
- They can also have an overview about the monument and read its interesting facts.
- Upon further scrolling, the users can either click and view the street view or the google map link of the monument.
- Required transitions have been incorporated to make provide an interesting user experience.

## Contact Us
![Contactpg](https://github.com/Nandana-Neo/AntiqueAtlas/assets/129848120/1c28b993-e386-46df-bd31-edc005b57595)

- If the user wants to add more to the catalogue/monuments that havent been documented yet, then he/she could do so by leaving a message for the admin.
- The name, mailid and the message sent by the user will be stored in the database for the admin to access it.
## Admin
- The admin page is for the admin user which as of now is using the user admin page of django which has to be improved.
  
## About Us
- A simple web-page has been included to provide users with the information about the contributors to this project.

## Scope of improvement
- The existing dataabse could be extended to thousands of monuments from around the world.
- we could have a login page, where the users could login to their respective accounts and bookmark the monuments that they have visited/want to visit.
- We could add nearby tourist attractions for each monument.

## Setup
Follow the instructions provide in below to setup all the required installations to run this fully functional website
https://www.geeksforgeeks.org/clone-and-run-a-django-project-from-github/
  
