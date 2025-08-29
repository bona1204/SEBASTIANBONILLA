## Explicación del Error

El error en el código original `df.groupby("cliente_id")["cantidad"].sum` se debe a que **`.sum`** es un **método** en pandas, no un atributo.

La corrección es invocar el método con `sum()`.

