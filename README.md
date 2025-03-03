# django_botiga
DOCUMENTACIO

- CATALOG:
    - Model del product amb 10 items inicials: ![alt text](img/image.png)

- CRUD:
    - GET: ![alt text](img/image-1.png)
    - POST: ![alt text](img/image-2.png)
    - PUT: ![alt text](img/image-3.png)
    - DELETE: ![alt text](img/image-4.png) ![alt text](img/image-5.png)


- PAYMENT

    - MODEL: ![alt text](img/image-6.png)

    - La verificació de les dades de pagament es fa amb el metode verifcar_tarjeta a payment/views.py. Verifica que el num de la tarjeta sigui de 16 dígits, qul el cvc sigui de 3, i que la tarjeta no estigui caducada.
    ![alt text](img/image-9.png)
    ![alt text](img/image-10.png)
    ![alt text](img/image-11.png)

    - Verificació User: 
        - Només es pot afegir un payment a un usuari existent a la bbdd. ![alt text](img/image-8.png)
        
        - Si no és existent: ![alt text](img/image-7.png)

    - Enllaç amb order:
        - Si l'estat de pagament és completat, l'estat de l'order enllaçada al pagament per l'id canvia a completat també.
            - L'ordre 2 està en pendent: ![alt text](img/image-12.png)

            - Si el pagament que estigui assossiat a l'ordre 2 es completa, l'esta s'actualitza: 
            https://drive.google.com/file/d/1vo0SGzvhn1ePPSvnRp_C_42fBV45EA3Z/view?usp=sharing
