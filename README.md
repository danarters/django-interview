## Task 
* Add functionality to the homepage to display a different message when the user has been to the page before as opposed to a first time visitor. In addition, add functionality to display the number of times a user has visited the page. Describe the limitations of your approach, and scenarios where an incorrect message could be displayed 

## Setup
* Clone the repo 
* Install the requirements (just django here)
* Modify any necessary code without using any outside modules to complete the task. The homepage code is located in ./interview/tracking/views.py

## Boilerplate
* Out of the box django project with a single app
* The added app (tracking) has been added to the INSTALLED_APPS 
* A url with no extension (http://127.0.0.1:8000/) is routed to tracking.views.home by including the tracking urls in the project's urlpatterns 
* The template rendered by the base url (http://127.0.0.1:8000/) is ./interview/templates/index.html, and is currently using django template syntax