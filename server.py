from waitress import serve
from picappAPI.wsgi import application  # Remplacez 'nom_du_projet' par le nom de votre projet Django

serve(application, host='0.0.0.0', port=8000, url_scheme='https')
