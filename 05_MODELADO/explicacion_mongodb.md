## Modelado en MongoDB: Embedding vs. Referencing

Para modelar un pedido con múltiples ítems, se utilizó la técnica de **embedding (incrustación)**.

La razón principal es que los ítems de un pedido tienen una relación de **contención** con el pedido; no existen de forma independiente. Incrustar los ítems como un array dentro del documento del pedido ofrece dos ventajas clave:

1.  **Rendimiento de Lectura:** Toda la información de un pedido se puede obtener con una única consulta a la base de datos, evitando la necesidad de "joins" (operaciones `$lookup`), lo que resulta en una latencia mucho menor.

2.  **Atomicidad:** Las operaciones de creación o actualización de un pedido y todos sus ítems se pueden realizar en una sola transacción atómica a nivel de documento, lo que garantiza la consistencia de los datos.  