USE v_art;

INSERT INTO artist (fname, lname, dob, dod, country, local) VALUES ('Johannes', 'Vermeer', 1632, 1674, 'Netherlands', 'n');

SELECT * FROM artist ORDER BY lname;

UPDATE artist SET dod =  1675 WHERE artist_id = 9;

DELETE FROM artist WHERE artist_id = 9;

USE bike;

SELECT first_name, last_name, phone FROM customer WHERE city = 'Houston';

SELECT product_name, list_price, list_price-500 "Discount Price" FROM product WHERE list_price >=5000 ORDER BY list_price DESC;

SELECT first_name, last_name, email FROM staff WHERE NOT(store_id=1);

SELECT product_name, model_year, list_price FROM product WHERE product_name REGEXP 'spider';

SELECT product_name, list_price FROM product WHERE list_price >= 500 AND list_price <= 550 ORDER BY list_price;

SELECT first_name, last_name, phone, street, city, state, zip_code FROM customer WHERE (phone is NOT NULL AND city REGEXP 'ach|och') OR last_name = 'William' LIMIT 5;