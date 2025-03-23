USE bike;

SELECT ROUND(AVG(quantity)) AS 'Stock Average'
FROM stock;

SELECT DISTINCT product_name
FROM product p
JOIN stock s ON p.product_id = s.product_id 
WHERE s.quantity = 0
ORDER BY product_name;

SELECT category_name, SUM(quantity) AS instock
FROM stock s
JOIN product p ON s.product_id = p.product_id
JOIN category c ON p.category_id = c.category_id
JOIN store st ON s.store_id = st.store_id
WHERE st.store_name = 'Baldwin Bikes'
GROUP BY category_name
ORDER BY instock;

USE employees;

SELECT COUNT(emp_no) AS 'Number of Employees'
FROM employees;

SELECT d.dept_name, FORMAT(AVG(salary),2) AS average_salary
FROM employees e
JOIN salaries s ON e.emp_no = s.emp_no
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments d ON de.dept_no = d.dept_no
GROUP BY d.dept_name
HAVING AVG(s.salary) < 60000;

SELECT dept_name, COUNT(e.emp_no) AS 'Number of Females'
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments d ON de.dept_no = d.dept_no
WHERE gender ="F"
GROUP BY dept_name
ORDER BY dept_name;

