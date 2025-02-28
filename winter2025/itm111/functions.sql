USE magazine;

SELECT magazineName, ROUND(magazinePrice*.97,2) AS '3% off' FROM magazine;

SELECT subscriberKey, ROUND(DATEDIFF('2020-12-20', subscriptionStartDate)/365) AS 'Years since subscription' FROM subscription;

SELECT subscriptionStartDate, subscriptionLength, DATE_FORMAT(DATE_ADD(subscriptionStartDate, interval subscriptionLength month), '%M %d, %Y') AS 'Subscription end' from subscription;

USE bike;

SELECT SUBSTRING(product_name, 1, LOCATE(' - ', product_name)) AS 'Product Name without Year' FROM product ORDER BY product_id LIMIT 14;

SELECT * FROM product;

SELECT product_name, CONCAT('$',FORMAT(list_price/3,2, 'C')) AS 'One of 3 payments' FROM product WHERE model_year = 2019;