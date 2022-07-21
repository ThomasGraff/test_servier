# test_servier

## Python :

Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses 
volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?

- Changer le format d'input
- Ne pas utiliser de produit cartésien
- Utiliser un système distribué

Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de 
telles volumétries 

- En première étape on pourrait changer le format des input de csv à parquet par exemple, pour rendre plus efficient le traitement.
- Deuxiemement, on peut remplacer Pandas par Spark ou Dask afin d'avoir un système distribué.


## SQL :

1 - SELECT date, prod_price*prod_qty AS ventes FROM transaction ORDER BY date

2- 

SELECT * FROM
(
  SELECT client_id, prod_qty*prod_price as ventes, product_type FROM transaction JOIN product_nomenclature 
  ON transactions.prop_id=product_nomenclature.product_id WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
)t
PIVOT(
    SUM(ventes)
    FOR product_type IN (
        [MEUBLE], 
        [DECO])
) AS ventes_type;
