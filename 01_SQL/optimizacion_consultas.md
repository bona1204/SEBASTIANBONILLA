## Estrategias de Optimización de Consultas

### Índices (Indexes)
Un índice es una estructura de datos que mejora la velocidad de recuperación de datos en una tabla. Funciona como el índice de un libro, permitiendo que la base de datos encuentre una fila específica sin tener que leer la tabla completa. Es ideal para columnas usadas frecuentemente en cláusulas `WHERE` y `JOIN`.

### Particiones (Partitions)
La partición divide una tabla grande en piezas más pequeñas y manejables. Para una tabla de ventas, particionar por fecha (ej. una partición por mes) es muy efectivo. Cuando una consulta filtra por un rango de fechas, la base de datos solo escanea las particiones relevantes, reduciendo drásticamente el volumen de datos a procesar.

### Clustering
El clustering ordena y almacena físicamente las filas de la tabla en el disco según una clave específica, como `cliente_id`. Esto significa que todos los registros de un mismo cliente se guardan juntos. Para consultas que agrupan o filtran por esa clave, el rendimiento mejora significativamente al minimizar las operaciones de lectura del disco.