# stockmangement
rm -rf wine_products/migrations/
rm -rf wine_reports/migrations/

python manage.py makemigrations wine_products
python manage.py makemigrations wine_reports
python manage.py migrate

python manage.py insert_category
python manage.py insert_quantity_using_csv


ALTER SEQUENCE wine_products_categorie_id_seq RESTART WITH 1;

