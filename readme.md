
### Debemos de isntalar estos archivos
pip install selenium
pip install webdriver-manager
pip install schedule
pip install pytelegrambotapi --upgrade
pip install python-telegram-bot-calendar
pip install psutil
pip install Flask
pip install pyngrok
pip install waitress
### Si queremos agreggar una nueva loteria

- PRIEMRO TENGO QUE AGREGAR UN ARCHIVO VARIABLES_ENTORNO y agregar alli sus variables a usar

os.environ["TOKEN_NOTIFICACIONES"]  =   ''      # Token de Telegram
os.environ["TOKEN_PREMIAR"]         =   ""      # Token de Telegram
os.environ["TOKEN_BOT_PADRE"]       =   ""      # Token de Telegram
os.environ["API_MONGO_DB"]          =   ""      # Api de la base de datos
os.environ["INTENTOS"]              =   '100'   # Cuantos intentos se buscara
os.environ["TIEMPO_A_ESPERAR"]      =   '5'     # Tiempo que se va adetener el time
os.environ["TIEMPO_A_BUSCAR"]       =   '5'     # Que cada tiempo va a buscar los numeros
os.environ['NGROK_TOKEN']           =   ''      # TOKEN DE NGROK PARA EL BOT DE TELEGRAM
os.environ['MI_CHAT_ID']            =   ''      # ESTO ES SOLO PARA ENVIAR UNA NOTIIFCACION AL ABRIR EL BOPT


- Primero agregamos sus datos a la carpeta de Datos_Loterias con el formnato establecido
- Luego agregamos las varibales de los diferentes nombres
- Y por ultimo creamos una instancia de ella


### Para bsucar un super pales
- Primero creamos la variables del objecto en el archivo de Variables
- primero vamos a la funcion saber_super_pale, aqui lo agregamos las variables
- Luego vamos a el archivo de Objectos_para_automaticos y agregamos la variables
- Por ultimo vamos a el archivo de automatico para que se busque solo