# Documentación del Proyecto

## 1. Cómo está organizado este proyecto
Organicé el proyecto en carpetas numeradas para que todo encajara con cada parte de la prueba. Para mantener las cosas ordenadas y no tener archivos repetidos por todos lados, creé una carpeta central llamada `data` donde guardé los `ventas.csv` y `compras.json` originales.

## 2. Cómo ejecutar todo

### Lo que necesitas
* **Python** (con la versión 3.8 o una más nueva estarás bien).
* **Docker Desktop** (para la parte extra).
*  **librerías de Python**, que puedes instalar con este comando en tu terminal:
    `pip install pandas duckdb`

### Ejecutando cada parte
* **01\_SQL:** Entra a esta carpeta y ejecuta `python run_queries.py`. El script se encargará de correr las consultas SQL y crear los archivos con los resultados automáticamente.
* **02\_PYTHON:** Ve a esta carpeta y ejecuta los dos scripts: `python analizar_compras.py` y luego `python corregir_ventas.py`.
* **03\_PIPELINE:** Entra aquí y ejecuta `python pipeline.py`. Esto creará el archivo `ventas_procesadas.csv`.
* **04\_AWS\_SIMULADO:** Esta parte es un poco más larga. Primero, ejecuta `python aws_simulation.py`. Luego, mientras sigue corriendo, copia el archivo `ventas.csv` a la carpeta `input`. Verás cómo el script mueve la carpeta a procesed y crea un archivo en output. Para detenerlo, solo presiona `Ctrl + C`.
* **07\_DOCKER (Bonus):** Desde la carpeta principal del proyecto (la raíz), ejecuta `docker build -t belcorp-pipeline -f 07_DOCKER/Dockerfile .` para construir la imagen, y luego `docker run belcorp-pipeline` para correrla.

## 3. Algunas decisiones clave que tomé
* **Hacer la parte de SQL más realista:** En lugar de solo escribir las consultas SQL, creé un pequeño script de Python que las ejecuta de verdad sobre el archivo CSV. Sentí que se parecía más a lo que haría un ingeniero de datos en la vida real.
* **Mantener los datos ordenados:** Decidí desde el principio crear una carpeta `data` central. Simplemente se sintió más limpio que tener copias del mismo CSV esparcidas por todos lados.
* **Asegurarme de que los scripts simplemente funcionen:** Usé una herramienta estándar de Python (`pathlib`) para manejar las rutas de los archivos. Lo bueno de esto es que los scripts deberían funcionar sin problemas, sin importar en qué computadora se ejecuten.
* **Construir una imagen de Docker inteligente:** Para la parte de Docker, me aseguré de que el `Dockerfile` estuviera configurado para construirse correctamente desde la carpeta principal. Esto le permite tomar el script de la carpeta `07_DOCKER` y los datos de la carpeta `data` sin ningún problema.