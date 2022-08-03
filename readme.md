
### Debemos de isntalar estos archivos
pip install selenium
pip install webdriver-manager
pip install schedule
pip install pytelegrambotapi --upgrade
pip install beautifulsoup4
pip install python-telegram-bot-calendar
### Si queremos agreggar una nueva loteria

- PRIEMRO TENGO QUE AGREGAR UN ARCHIVO VARIABLES_ENTORNO y agregar alli sus variables a usar

os.environ["TOKEN_NOTIFICACIONES"]  =   ''      # Token de Telegram
os.environ["TOKEN_PREMIAR"]         =   ""      # Token de Telegram
os.environ["TOKEN_BOT_PADRE"]       =   ""      # Token de Telegram
os.environ["API_MONGO_DB"]          =   ""      # Api de la base de datos
os.environ["INTENTOS"]              =   '100'   # Cuantos intentos se buscara
os.environ["TIEMPO_A_ESPERAR"]      =   '5'     # Tiempo que se va adetener el time
os.environ["TIEMPO_A_BUSCAR"]       =   '5'     # Que cada tiempo va a buscar los numeros

print("INICIARON BIEN LAS VARIABLES")


- Primero agregamos sus datos a la carpeta de Datos_Loterias con el formnato establecido
- Luego agregamos las varibales de los diferentes nombres
- Y por ultimo creamos una instancia de ella