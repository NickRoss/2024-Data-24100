# This is the 2024 Class, not the current course.
# Software Engineering for Data Science

Instructor: Nick Ross 

Office Hours: My current office hours will be from 9-10AM on Wed and Fri. However, I'm generally around and strongly recommend emailing me to schedule rather than just show up.

Office Location: Ryerson 257H

How to contact: My contact information is on canvas.

<details style="padding: 10px; background-color: var(--color-canvas-subtle); border-radius: 5px;">
<summary>💡 <strong>Updates for next year</strong></summary>
This box contains a list of changes that should be done for next year<br>

1. For the group names make sure that people are not putting "GROUP" and instead just putting the numbers there.
2. Have everyone put their data in a location on the host set by ENV rather than zips inside the repo
3. Everyone uses a DSI Clinic Repo with branch protections and not an admin.
4. When using flask -- just always start with `python app.py` rather than `flask run`
5. use `uv` inside the container
6. use pyenv and python 3.15 or something new which requires the env
7. Fix Part 3 to only load ~5 of the years. It is too many for some machines.
8. Move pdb to autodocs lectures. It is short.
9.  Add information about log rotation to logs
10. Add "F" to pyproject.toml
11. Update late policy on assignments if more than 5 hours => 50% off.
12. Options to add: Merging data
13. Options to add: github actions with testing & coding standards
14. TDD
15. For testing more about coverage, provide some examples and different types. End of lecture 16.
16. Final Exam was WAY too easy and short.
17. Quizzes need to be more consistent on difficulty level. 2-3 easy questions and one hard question requiring writing python code.
18. Add the ability to reset accounts via makefile in the assignment (part 5? part 6?)
```bash
db_truncate: build
	docker run $(COMMON_DOCKER_FLAGS) $(IMAGE_NAME) \
	sqlite3 $(DB_PATH) "DELETE FROM accounts; DELETE FROM stocks_owned;"
```
19.  Maybe lean into pyproject.toml, its way more modern. Use it for testing and requirements.
20.  Rewrite rubrics to help graders. Be more specific on a number of ongoing issues (branch protection violations, separation of concerns, unused code, inconsistent abstractions, etc.)
21. Learning objectives need to be expanded for each week, especially toward the end. Focus on hard skills. Per conversation with other faculty increase pre-req questions.
</details>

## Course Description

This course is designed to equip students with the practical skills and theoretical knowledge necessary to excel at the intersection of data science and software engineering. Through a hands-on approach, students will delve into the core tools and concepts that form the backbone of this interdisciplinary field, including data modeling, building data pipelines and software development best-practices. Emphasis will be placed on real-world applications, enabling students to work on projects that simulate professional scenarios and challenges. This course is ideal for those looking to deepen their understanding of how data-focused technologies are developed and deployed.

## Prerequisites

This course assumes that you are familiar with the basic concepts of Python programming as you would find in the core data science courses. 

If you are unsure or are looking for a refresher on what is expected, please take a look at this [prerequisite doc](./docs/prequisites.md).

## Course Overview

This course is designed to expose data science students to deeper computing concepts that are likely need throughout their careers. We will do this in a project-based method where students will work in small groups using common data science tools to build an entire pipeline from raw data to putting the data into a relational database to serving that data through an API.

As a by product of this effort, after taking this course students should have experience managing their own computing environment and be able to build software with an understanding of best practices. 

## Course Assessment

The final grade of this course will be determined by five components:

| Component | Percent of Grade | 
| --- | --- | 
| Professionalism (Ind.) | 5\% | 
| Project (Group) | 30\% | 
| Quizzes (Ind.) | 30\% | 
| Final Project Deliverable (Group) | 15\% | 
| Final Exam (Ind.) | 20\% | 

### Professionalism (Ind.)

In this class professionalism means:

- Showing up on time
- Showing up prepared
- Contributing to class
- Being responsible to your group when doing group work
- Communicating respectfully and appropriately to your peers, TAs and faculty

Students who show up on time and pay attention in class have a tendency to do extremely well in this class. The opposite if also true; students who fail to make an effort, fail to contribute in class and fail to pay attention have a tendency to do poorly in this class. 

This grade is assigned individually.

### Project (Group)

Over the course of the quarter you and your group will be working on a large software engineering project. This project will have multiple deliverables during the quarter that you will need to complete as we build up to our final API and backend.

This grade is assigned as a group. You can find the project regrade policy [here](./assignments/regrade_policy.md). Please read before asking for a regrade.


### Quizzes (Ind.)

Each Thursday (starting week \#2) there will be a short quiz (15-30 minutes) given at the start of the course. These quizzes are _cumulative_ over the course of the quarter. Note that the lowest quiz grade will be dropped at the end.

More information on the quizzes is provided in the [course material](#course-material) section below.

This grade is assigned individually. You can find the quiz regrade policy [here](./assignments/regrade_policy.md). Please read before asking for a regrade.


### Final Project Deliverable (Group)

At the end of the quarter your final group's final github repo will undergo a significant assessment to make sure that it meets the criteria established during the course. 

This grade is assigned as a group.

### Final Exam (Ind.)

There will be a final exam given according to the exam calendar. This will be cumulative from the material in the quarter and will be similar in style and difficulty to the quizzes. Per the [final exam calendar](https://registrar.uchicago.edu/calendars/final-exams/), it looks like it is scheduled for Thursday December 12th from 10:00-12:00. Please make sure that you verify this for yourself.

This grade is assigned individually. There is more information about the final [here](./lesson_plan/finals_week.md).

## Course Material

Lectures will be traditional chalk-talks and computer-aided demonstrations. While there aren't slides, my lecture notes will be provided in this repository for reference.

These notes represent the content of the course and what is expected to be covered on the quiz, I strongly recommend students attend the lecture for the full experience. 

During lecture we will be doing some hands-on activities and verifications that, while described in the notes, are better experienced in-person rather than live. 

### Quiz Material

After each lecture (roughly) the lecture notes will be provided. Appended to the end of the lecture notes will be a set of quiz objectives that describe the material that can appear on the quiz. 

These quiz objectives _do not_ cover the entire material from the lecture but are the only material that will be asked for on the quiz.

That being said, it is important to internalize these concepts because, while the list of learning objectives at the end describe the basic building blocks of what is asked, they may be asked in conjunction to generate a quiz question. 

For example: Consider two quiz objectives objectives of `use wildcards to match files which follow a pattern` and another  `move files within a file system`. It is perfectly reasonable to ask a question on the quiz such as `move all .txt files from the /data subdirectory to the /text_data subdirectory` which would require using both. 

## Course Outline

In this course we will cover the following topics which will enable us to build a full data pipeline, diagnose issues and serve data via an API. Each topic will last approximately a week.

Course Notes can be found linked inside each lesson plan.

| Topic | Topics | Assignments | Notes \& Plan | 
| --- | --- | --- | --- | 
| 1: Introduction | <ul><li>The Terminal</li><li>File Management</li><li>Environments</li></ul> | <ul><li>[Preliminaries](./assignments/prelims.md)</li><li>[Prereqs](./docs/prequisites.md)</li></ul> | <ul><li>[Lesson Plan](./lesson_plan/week_1.md)</li></ul>
| 2: Docker, Make and git | <ul><li>Docker</li><li>Make</li><li>git</li><li>Environments</li></ul> | <ul><li>[Quiz #1A](./quiz/quiz1A.pdf)</li><li>[Quiz #1B](./quiz/quiz1B.pdf)</li><li>[Quiz #1 AK](./quiz/quiz1AK.md)</li></ul> | <ul><li>[Lesson Plan](./lesson_plan/week_2.md)</li></ul> |
| 3: Flask | <ul><li>REST</li><li>Flask</li><li>Requests</li></ul> | <ul><li>[Project Part I Due](./project_assignments/part_1.md)</li><li>[Project Part I Rubric](./project_assignments/part_1_rubric.md)</li><li>[Quiz #2A](./quiz/quiz2A.pdf)</li><li>[Quiz #2 AK](./quiz/quiz2AK.md)</li></ul>  | <ul><li>[Lesson Plan](./lesson_plan/week_3.md)</li></ul>
| 4: Flask & Code Quality | <ul><li>Additional Requests</li><li>Organizing code</li><li>Separation of Concerns</li><li>DRY</li><li>Separation of Concerns</li></ul> |  <ul><li>[Project Part II Due](./project_assignments/part_2.md)</li><li>[Project Part II Rubric](./project_assignments/part_2_rubric.md)</li><li>[Quiz #3A](./quiz/quiz3A.pdf)</li><li>[Quiz #3A AK](./quiz/quiz3AK.md)</li></ul> | <ul><li>[Lesson Plan](./lesson_plan/week_4.md)</li></ul> |
| 5: Code quality control and organization | <ul><li>Abstraction</li><li>Linting</li></ul> | <ul><li>[Project Part III Due](./project_assignments/part_3.md)</li><li>[Project Part III Rubric](./project_assignments/part_3_rubric.md)</li><li>[Quiz #4](./quiz/quiz4A.pdf)</li><li>[Quiz #4 AK](./quiz/quiz4AK.md)</li></ul> | <ul><li>[Lesson Plan](./lesson_plan/week_5.md)</li></ul> | 
| 6: Data Pipeline | <ul><li>SQLite</li><li>CRUD</li></ul> |  <ul><li>[Project Part IV Due](./project_assignments/part_4.md)</li><li>[Project Part IV Rubric](./project_assignments/part_4_rubric.md)</li><li>[Quiz #5](./quiz/quiz5A.pdf)</li><li>[Quiz #5 AK](./quiz/quiz5AK.md)</li></ul> | <ul><li>[Lesson Plan](./lesson_plan/week_6.md)</li></ul> |
| 7: Data Pipeline \#2 | <ul><li>More CRUD</li><li>Testing</li></ul> | <ul><li>[Project Part V Due](./project_assignments/part_5.md)</li><li>[Project Part V Rubric](./project_assignments/part_5_rubric.md)</li></ul> |  <ul><li>[Lesson Plan](./lesson_plan/week_7.md)</li></ul> | 
| 8: Adding Features | <ul><li>Logging in Python</li><li>Autodocs with mkdocs</li></ul> | <ul><li>[Project Part VI Due](./project_assignments/part_6.md)</li><li>[Project Part VI Rubric](./project_assignments/part_6_rubric.md)</li><li>[Quiz #6](./quiz/quiz6A.pdf)</li><li>[Quiz #6 AK](./quiz/quiz6AK.md)</li></ul> | <ul><li>[Lesson Plan](./lesson_plan/week_8.md)</li></ul> |
| 9: Testing and Merging | <ul><li>pdb</li><li>PyTest</li></ul> | <ul><li>[Project Part VII Due](./project_assignments/part_7.md)</li><li>[Project Part VII Rubric](./project_assignments/part_7_rubric.md)</li><ul> | <ul><li>[Lesson Plan](./lesson_plan/week_9.md)</li></ul> | 
| 10: Finals Week | |<ul><li>[Project Part VIII Due](./project_assignments/part_8.md)</li><li>[Project Part VIII Rubric](./project_assignments/part_8_rubric.md)</li><li>[Exam](./quiz/FinalExam.pdf)</li><li>[Exam AK](./quiz/FinalExamAK.md)</li><ul>  | <ul><li>[Finals Info](./lesson_plan/finals_week.md)</li></ul> | 

## Canvas

All grade (and due date) information will be posted on Canvas. If you do not have access to Canvas please send me an email as soon as possible. 

## Odds and Ends

- **Cheating is not tolerated. At all.** Unless an assignment is clearly designated as group work, I expect it to be done alone. The University's code of academic integrity can be found online, and I expect it to be followed. Disciplinary action will be taken against any student found violating this code. This includes:
  - **Plagiarism** — intentionally or unintentionally representing the words or ideas of another person as your own; failure to properly cite references; manufacturing references.
  - Working with another person when independent work is required.
  - Submission of the same paper in more than one course without the specific permission of each instructor.
  - Submitting a paper written by another person or obtained from the internet.
  - The penalties for violation of the policy may include a failing grade on the assignment, a failing grade in the course, and/or a referral to the Academic Integrity Committee.

- **Attendance is expected.** All exams are in-person and use pencil and paper.

- The quickest way to reach me is via email.

- **Class participation is expected.**  I expect class to include discussions.

- **Accommodations:** If you require any accommodations for this course, as soon as possible please provide the instructor with a copy of your Accommodation Determination Letter (provided to you by the Student Disability Services office) so that you may discuss with them how your accommodations may be implemented in this course. The University of Chicago is committed to ensuring the full participation of all students in its programs. If you have a documented disability (or think you may have a disability) and, as a result, need a reasonable accommodation to participate in class, complete course requirements, or benefit from the University's programs or services, you are encouraged to contact Student Disability Services as soon as possible. To receive reasonable accommodation, you must be appropriately registered with Student Disability Services. Please contact the office at (773) 702-6000, TTY (773) 795-1186, disabilities@uchicago.edu, or visit the website at [disabilities.uchicago.edu](https://disabilities.uchicago.edu). Student Disability Services is located at 5501 S. Ellis Avenue.

- As an instructor, one of my responsibilities is to help create a safe learning environment on our campus. I also have a mandatory reporting responsibility related to my role as a faculty member. I am required to share information regarding sexual misconduct or information about a crime that may have occurred with the University.

- The University of Chicago is a community of scholars dedicated to research, academic excellence, and the pursuit and cultivation of learning. Members of the University community cannot thrive unless each is accepted as an autonomous individual and is treated without regard to characteristics irrelevant to participation in the life of the University. Our university is committed to fostering a safe, productive learning environment. Title IX and our school policy prohibits discrimination on the basis of sex. Sexual misconduct — including harassment, domestic and dating violence, sexual assault, and stalking — is also prohibited at our university.

- Our university encourages anyone experiencing sexual misconduct to talk to someone about what happened, so they can get the support they need and our university can respond appropriately. If you wish to speak confidentially about an incident of sexual misconduct, want more information about filing a report, or have questions about school policies and procedures, please contact Bridget Collier (Associate Provost for Equal Opportunity Programs and Title IX Coordinator for the University) at [bcollier@uchicago.edu](mailto:bcollier@uchicago.edu) or (773) 834-6367.

- Our university is legally obligated to investigate reports of sexual misconduct, and therefore it cannot guarantee the confidentiality of a report, but it will consider a request for confidentiality and respect it to the extent possible. As instructors, we are also required by our school to report incidents of sexual misconduct and thus cannot guarantee confidentiality. We must provide our Title IX coordinator with relevant details such as the names of those involved in the incident.
