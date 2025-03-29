USE university_data;

SELECT first_name, last_name, DATE_FORMAT(birthdate, '%M %d, %Y') as 'Sept Birthdays'
FROM students WHERE birthdate REGEXP '-09-';

SELECT last_name, first_name,
 floor(DATEDIFF(NOW(), birthdate)/365.25) AS Years,
 floor(DATEDIFF(now(), birthdate)%365.25) AS Days,
 CONCAT(floor(DATEDIFF(NOW(), birthdate)/365.25),' - Yrs, ', floor(DATEDIFF(now(), birthdate)%365.25), ' - Days') AS 'Years and Days'
 FROM students
 ORDER BY birthdate;
 
SELECT first_name, last_name
FROM students st
JOIN enrollments e ON st.students_id = e.students_id
JOIN sections s ON e.section_id = s.section_id
JOIN faculty f ON s.faculty_id = f.faculty_id
WHERE f.faculty_id = 4
ORDER BY last_name;

SELECT faculty_fname, faculty_lname
FROM faculty f
JOIN sections s ON f.faculty_id = s.faculty_id
JOIN enrollments e ON s.section_id = e.section_id
JOIN students st ON e.students_id = st.students_id
JOIN terms t ON s.term_id = t.term_id
WHERE st.students_id = 7 and t.term_year = 2018 and t.term_season = 'Winter'
ORDER BY faculty_lname;

SELECT first_name, last_name
FROM students st
JOIN enrollments e ON st.students_id = e.students_id
JOIN sections s ON e.section_id = s.section_id
JOIN courses c ON s.course_id = c.course_id
JOIN terms t ON s.term_id = t.term_id
WHERE course_title = 'Econometrics' and t.term_year = 2019 and t.term_season = 'Fall'
ORDER BY last_name;

SELECT d.departments_code, courses_num, course_title
FROM courses c
JOIN departments d ON c.department_id = d.department_id
JOIN sections s ON c.course_id = s.course_id
JOIN enrollments e ON s.section_id = e.section_id
JOIN students st ON e.students_id = st.students_id
JOIN terms t ON s.term_id = t.term_id
WHERE st.students_id = 7 and term_season = 'Winter'
ORDER BY course_title;

SELECT term_season as term, term_year as year, COUNT(students_id) as Enrollment
FROM enrollments e
JOIN sections s ON e.section_id = s.section_id
JOIN terms t ON s.term_id = t.term_id
WHERE term_season = 'Fall' and term_year = 2019
GROUP BY term and year;

SELECT college as Colleges, COUNT(course_title) as 'Number of Courses'
FROM colleges c
JOIN departments d ON c.colleges_id = d.colleges_id
JOIN courses cr ON d.department_id = cr.department_id
GROUP BY college
ORDER BY college;

SELECT faculty_fname, faculty_lname, SUM(section_capacity) as TeachingCapacity
FROM faculty f
JOIN sections s ON f.faculty_id = s.faculty_id
JOIN terms t ON s.term_id = t.term_id
WHERE term_season = 'Winter' and term_year = 2018
GROUP BY faculty_fname, faculty_lname
ORDER BY TeachingCapacity;

SELECT last_name, first_name, sum(credits) as Credits
FROM students st
JOIN enrollments e ON st.students_id = e.students_id
JOIN sections s ON e.section_id = s.section_id
JOIN courses c ON s.course_id = c.course_id
JOIN terms t ON s.term_id = t.term_id
WHERE term_year = 2019 and term_season = 'Fall'
GROUP BY last_name, first_name
HAVING SUM(credits) >3
ORDER BY Credits DESC;