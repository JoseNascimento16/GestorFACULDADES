<h1 align="center">Sistema Gestor de Faculdades</h1>

## About ![pin-img](https://user-images.githubusercontent.com/110631271/215866770-755c96a6-17fa-4a7c-9c05-23693843f01c.png)

The Sistema Gestor de Faculdades was developed in 4 days as an exercise. Its a mannagement system that can manage Courses, subjects, professors, students and their grades.

## Used technologies ![pin-img](https://user-images.githubusercontent.com/110631271/215866770-755c96a6-17fa-4a7c-9c05-23693843f01c.png)
<li>Python 3.9</li>
<li>Django 4.1</li>
<li>Javacript</li>
<li>HTML and CSS</li>
<li>Bootstrap</li>
<li>PostgreSQL</li>

## Functionalities ![pin-img](https://user-images.githubusercontent.com/110631271/215866770-755c96a6-17fa-4a7c-9c05-23693843f01c.png)

- Basic CRUD (Create, read, update, delete) of all entities: Courses, subjects, professors, students, grades using Bootstrap MODALS.
- A table for each entity and their attributes
- A table containing all the courses showing the number of professors, students and their mean grade for each course.
- A table listing the professor, students and grades of a subject.

## Business rules ![pin-img](https://user-images.githubusercontent.com/110631271/215866770-755c96a6-17fa-4a7c-9c05-23693843f01c.png)

- Each course can have many subjects.
- Each subject can have only 1 professor and as many students as needed.
- A student can be registered in any subject of his course.
- On a course removal, its subjects and students grades are removed as well.
- On a subject removal, the students grades related to it are removed too.
