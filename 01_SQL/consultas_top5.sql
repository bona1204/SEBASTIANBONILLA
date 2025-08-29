SELECT
    producto_id,
    SUM(cantidad) AS total_vendido
FROM
    ventas
GROUP BY
    producto_id
ORDER BY
    total_vendido DESC
LIMIT 5;    