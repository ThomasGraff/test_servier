# test_servier

## Python :

Pour lancer : python \_\_main\_\_.py

Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses 
volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?

- Changer le format d'input afin d'avoir un format lisible plus rapidement, et pouvant être compressé.
- Ne pas utiliser de produit cartésien car ce dernier peut prendre du temps et surtout beaucoup de mémoire. Il faut l'appliquer sur des dataframes de taille raisonnable ou bien ne plus l'utiliser.
- Utiliser un système distribué afin de répartir les taches sur différentes machines. Cela permet d'accélérer le traitement sûr de nombreuses données.

Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de 
telles volumétries 

- En première étape on pourrait changer le format des inputs de CSV à Parquet. Le format CSV n'est pas conseillé pour les échanges de données. Les données ne sont pas compressées, le schéma n'est pas "enforced", et la lecture d'un CSV implique de lire toutes les colonnes de toutes les lignes, contrairement à Parquet, ce qui accélère le traitement.
- Deuxièmement, on peut remplacer Pandas par Spark, Dask ou une autre solution afin de distribuer notre traitement sur plusieurs noeuds. Koalas serait la solution la moins impactant dans le code de ce projet et ne nécessiterait que de changer de suffixe toutes les fonctions Pandas.


## SQL :

Fait sur MS SQL

1 - 
```sql
SELECT date, SUM(prod_price*prod_qty) AS ventes FROM transactions WHERE date BETWEEN '2019-01-01' AND '2019-12-31' 
GROUP BY date ORDER BY date
```
2- 

```sql
SELECT * FROM
(
  SELECT client_id, prod_qty*prod_price AS ventes, product_type FROM transactions JOIN product_nomenclature 
  ON transactions.prop_id=product_nomenclature.product_id WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
)t
PIVOT(
    SUM(ventes)
    FOR product_type IN (
        [MEUBLE], 
        [DECO])
) AS ventes_type;
```
