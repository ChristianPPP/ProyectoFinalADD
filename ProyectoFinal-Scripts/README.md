Archivo FB_CouchDB.ipynb:
Contiene el script que nos permite realizar Facebook scraping para almacenar la información extraída en la base de datos CouchDB. Para ello se establece conexión con CouchDB, 
luego se utiliza el scraper de Facebook mediante la librería para definir los campos que se buscan extraer, asignarlos a un documento, convertirlos a un dataset y insertarlo
a CouchDB.

Archivo Query_SQLSERVER.ipynb:
Contiene el script que nos permite generar una tabla en una base determinda de SQL server, para posteriormente insertar datos en la misma. Para ello primero se realizará la
conexión a la base de datos de SQL server, luego ejecutaremos el query para generar la tabla con sus respectivos campos, una vez generada la tabla se ejecutará un query para
insertar la información almacenada en el archivo ".csv".

Archivo WEB_MongoDBAtlas.py:
Contiene el script que nos permite realizar web scraping para obtener datos de una tabla desde una página web para ser almacenada en la base de datos de MongoDB Atlas. Para
ello se establece la conexión con MongoDB Atlas, posteiormente se especifica la página desde la cual se realizará la extracción de los datos, siendo necesario especificar:
la url, número de páginas si se requiere, los tipos de etiquetas como lo son "tr" y "td", con ello generamos un documento con los campos que se requieran y se utiliza la 
variable que almacena la información del html para guardarla en el documento, finalemnte el documento se inserta en la base de datos especificada de MongoDB Atlas.
