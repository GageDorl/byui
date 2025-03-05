USE v_art;

SELECT artfile
FROM artwork
WHERE period = 'Impressionism';

SELECT artfile
FROM artwork aw
INNER JOIN artwork_keyword ak ON aw.artwork_id = ak.artwork_id
INNER JOIN keyword k ON ak.keyword_id = k.keyword_id
WHERE keyword = 'flowers';

SELECT fname, lname, title
FROM artist 
LEFT JOIN artwork 
ON artist.artist_id=artwork.artist_id;

USE magazine;

SELECT magazineName, subscriberLastName, subscriberFirstName
FROM magazine m
INNER JOIN subscription st ON m.magazineKey = st.magazineKey
INNER JOIN subscriber s ON st.subscriberKey = s.subscriberKey
ORDER BY magazineName;

SELECT magazineName
FROM magazine m
INNER JOIN subscription st ON m.magazineKey = st.magazineKey
INNER JOIN subscriber s ON st.subscriberKey = s.subscriberKey
WHERE subscriberFirstName = 'Samantha' AND subscriberLastName = 'Sanders'
ORDER BY magazineName;

USE employees;

SELECT first_name, last_name
FROM employees e
INNER JOIN dept_emp de ON e.emp_no = de.emp_no 
INNER JOIN departments d ON d.dept_no = de.dept_no
WHERE dept_name = 'Customer Service'
ORDER BY last_name
LIMIT 5;

SELECT first_name, last_name, dept_name, salary, s.from_date
FROM employees e
INNER JOIN salaries s ON e.emp_no = s.emp_no
INNER JOIN dept_emp de ON e.emp_no = de.emp_no 
INNER JOIN departments d ON d.dept_no = de.dept_no
WHERE first_name = 'Berni' AND last_name = 'Genin'
ORDER BY from_date desc
LIMIT 1;