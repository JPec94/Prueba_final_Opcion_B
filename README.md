# Prueba Final Opción B

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