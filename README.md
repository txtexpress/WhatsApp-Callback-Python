# WhatsApp Callback Python
Server Callback para responder mensajes de WhatsApp

- Requerimeintos:
Falcon
WSGI HTTP SERVER (cherry, uWSGI, Guinicorn, etc...)

- Start:

gunicorn -b 0.0.0.0 pythonCallbackSrv:api --reload

