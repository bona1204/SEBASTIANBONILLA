SELECT
    cliente_id,
    STRFTIME('%Y-%m', fecha) AS anio_mes,
    SUM(cantidad * precio) AS ingreso_total
FROM
    ventas
GROUP BY
    cliente_id,
    anio_mes
ORDER BY
    cliente_id,
    anio_mes;