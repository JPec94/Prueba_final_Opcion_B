# <p align="center">Prueba Final Opción B
## Parte 1
1. <p align="justify">Conseguir extraer datos de una fuente online, en mi caso la voy a obtener de la página que presento en el siguiente enlace.
* [PATIODEMOTOS.COM](https://www.patiodemotos.com/ecuador/top/nuevas)

2. <p align="justify">Lo siguiente es inspeccionar cada uno de los elementos, la idea es encontrar la clase que contiene las caracteristicas que exciben cada una de las motocicletas en el sitio web.

[![img.png](https://i.postimg.cc/s2fhKvqh/img.png)](https://postimg.cc/hXwvtPSD)

3. <p align="justify">Luego se procede a definir el navegador, url del sitio web y la clase principal en python para extraer la lista de elementos.
```javascript
driver = webdriver.Edge()
driver.get("https://www.patiodemotos.com/ecuador/anunciante/yamaha-ecuador")
moto_list = driver.find_elements(By.CLASS_NAME, "even")
```
4. <p align="justify"> Se continúa con la búsqueda y extracción de información, donde se hace un ciclo for para obtener información de cada una de las clases.
```javascript
for f in moto_list.
  moto = f.find_element(By.CLASS_NAME, "views-field-title").text
  price_m = f.find_element(By.CLASS_NAME, "views-field-field-precio").text
  city_m = f.find_element(By.CLASS_NAME, "views-field-field-ciudad").text
  owner_m = f.find_element(By.CLASS_NAME, "views-field-body").text
  telf_m = f.find_element(By.CLASS_NAME, "views-field-field-tel").text
```
5. <p align="justify">Del mismo modo se procede a imprimir las variables definidas para cada una de las caracteristicas de la lista, dando como resultado:

[![img1.png](https://i.postimg.cc/RZ9qbM47/img1.png)](https://postimg.cc/RNsMWx3h)

## Parte 2

1. <p align="justify">Para almacenar esta información de forma estructurada se utilizó la base de datos en la nube MongosDB, donde se configuró el cluster para su guardar está información como se realizó en la clase.
```javascript
    def __init__(self):
        user = os.getenv("MONGODB_USER")
        password = os.getenv("MONGODB_PASS")
        uri = f"mongodb+srv://{user}:{password}@datapruebafinal.cbsjndj.mongodb.net/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
```
2. <p align="justify">Del mismo modo se debe configurar el usuario y contraseña por motivos de seguridad, esto permite habilitar la conexión con el servidor de mongos para el almacenamiento de la información dando como resultado:

[![img2.png](https://i.postimg.cc/pLbPLxTm/img2.png)](https://postimg.cc/MvDC9C1w)

3. <p align="justify">Para evidenciar el análisis de los datos obtenidos se realizá un diagrama de pastel para evaluar cual de las motocicletas es la más cara, obteniendo así que la Yahama YZF 690.

[![img3.png](https://i.postimg.cc/gkYBmTyv/img3.png)](https://postimg.cc/LhbVVvbX)

## Parte 3
1. <p align="justify">Para el servicio web se uso Python + Flask, donde se accedio a la base de datos MongoDB para  imprimir todos los datos almacenados, estos se pudieron apreciar en el navegador EDGE.
[![img4.png](https://i.postimg.cc/NFYyWTHx/img4.png)](https://postimg.cc/k61XS2wV)

2. <p align="justify">Para empezar tenemos que agregar la libreria Flask, posterior a esto creamos un nuevo archivo de python para vincular y extraer la información de la base de datos de MongoDB.
```javascript
    self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client['datapruebafinal']
        self.collection = self.db['moto_list']
```
3. <p align="justify">Del mismo modo creamos un archivo .html para mostrar cada uno de los datos de MongoDB en una aplicación web Flask, está plantilla se la personalizó con cada una de las variables que se extrajo al momento de crear las listas.

```javascript
    <h1>Listado de Motos</h1>
    <table>
        <thead>
            <tr>
                <th>Tipo</th>
                <th>Costo</th>
                <th>Ubicación</th>
                <th>Persona</th>
                <th>Teléfono</th>
            </tr>
        </thead>
        <tbody>
            {% for moto in moto_data %}
                <tr>
                    <td>{{ moto.type }}</td>
                    <td>{{ moto.cost }}</td>
                    <td>{{ moto.location }}</td>
                    <td>{{ moto.person }}</td>
                    <td>{{ moto.phone }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
```
## CONCLUSIONES

* <p align="justify">

