# stockmangement
rm -rf products/migrations/
rm -rf reports/migrations/

python manage.py makemigrations products
python manage.py makemigrations reports
python manage.py migrate

python manage.py insert_category
python manage.py insert_quantity_using_csv
python manage.py insert_products

ALTER SEQUENCE products_categorie_id_seq RESTART WITH 1;




#save stock recived date internally
