PaySense Task
=======================

I have created this task using Django and Django rest framework

Setup project environment
--------------------------
- run $ pyvenv <your-env-name>
- activate environment using $ source <your-env-name>/bin/activate


Install required packages
------------------------
- keeping your environment activated from the root directory of the project run $ pip install -r requirements/base.txt

Set Environment Variables
------------------------
- cd into paysensetask folder and from here run $ export DJANGO_SETTINGS_MODULE='paysensetask.settings.local'

Manually create secrets.json file
---------------------------------


Run the server
---------------
- Now you can run the server from paysensetask folder $ python manage.py runserver


APIs
---------------
- Create a Message 
 - Method : POST 
 - URL: http://127.0.0.1:8000/api/v1/chat-messages/
 - headers: Content-Type: application/json
 - request_body: 
   - {
         "text": "I am Chitrank",
         "source_ip": "192.34.23.43"
     }
 - response_body:
   - {
         
         "meta": {
           "status": 1000,
           "is_error": false,
           "message": ""
         },
         "data": {
           "text": "I am Chitrank",
           "source_ip": "192.34.23.43",
           "created_on": "23 Mar 17 07:24 PM"
         }
     }

- Get List of Messages:
 - Method : GET
 - URL: http://127.0.0.1:8000/api/v1/chat-messages/
 - headers: Content-Type: application/json
 - response_body:
   {
     "meta": {
      "status": 1000,
      "is_error": false,
      "message": ""
     },
     "data": [
      {
        "text": "I am Chitrank",
        "source_ip": "192.34.23.43",
        "created_on": "23 Mar 17 07:24 PM"
      },
      {
        "text": "I am just asking",
        "source_ip": "192.23.54.34",
        "created_on": "23 Mar 17 06:19 PM"
      }
     ]
   }


- Delete a message (only the user with secret token can delete it):
 - Method : DELETE
 - URL: http://127.0.0.1:8000/api/v1/chat-messages/1/
 - headers: Content-Type: application/json
 - request_body:
   {
	"secret_token": "liomessi10"
   }
 - response_body:
   {
     "meta": {
       "status": 1000,
       "is_error": false,
       "message": ""
     },
     "data": {
       "message": "message 'I am just asking' has been deleted"
     }
   }

- Delete all messages
 - Method : DELETE
 - URL: http://127.0.0.1:8000/api/v1/delete-all-messages/
 - headers: Content-Type: application/json
 - request_body:
   {
        "secret_token": "liomessi10",
   }
 - response_body:
   {
     "meta": {
       "message": "",
       "is_error": false,
       "status": 1000
    },
     "data": {
       "message": "All the messages has been deleted"
     }
   }
