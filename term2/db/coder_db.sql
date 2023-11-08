drop table STUDENTS;
drop table TEACHERS;
drop table SUBJECTS;
drop table ENROLLMENTS;

create table STUDENTS(
    student_id serial primary key,
    f_name text not null,
    l_name text not null,
    email text not null,
    dob date
);

create table TEACHERS(
    teacher_id serial primary key,
    f_name text not null,
    l_name text not null
);

create table SUBJECTS(
    subject_id serial primary key,
    subject_name text not null,
    
    teacher_id integer not null,
    foreign key (teacher_id) references TEACHERS (teacher_id) on delete set null
);

create table ENROLLMENTS(
    enrollment_id serial primary key,
    
    student_id integer not null,
    foreign key (student_id) references STUDENTS (student_id) on delete cascade,

    subject_id integer not null,
    foreign key (subject_id) references SUBJECTS (subject_id) on delete cascade,

    enrollment_date date default 'today'
);

insert into students (f_name, l_name, email, dob) values 
    ('Victoria', 'Linley', 'victoria.linley@gmail.com', '07/02/1991'),
    ('Mary', 'Spencer', 'm.spencer@gmail.com', '08/24/1994'),
    ('Fiona', 'Taylor', 'f.taylor@gmail.com', '03/18/1990'),
    ('Mark', 'Jones', 'm-jones@gmail.com', '09/10/1993'),
    ('Harry', 'Bennett', 'harry.bennett@gmail.com', '05/25/1992')
    ;

insert into teachers (f_name, l_name) values
    ('Daniel', 'Simpson'),
    ('Gareth', 'Carter'),
    ('Pauline', 'Singer'),
    ('Rachel', 'Thompson')
    ;

insert into subjects (subject_name, teacher_id) values
    ('Web Programming', 1),
    ('Software Development', 2),
    ('Mathematics', 3),
    ('Information Technology', 4),
    ('Computer Science', 3)
    ;

insert into enrollments (student_id, subject_id) values
    (1, 2),
    (2, 2),
    (3, 1),
    (4, 3),
    (5, 4),
    (6, 1),
    (6, 2),
    (7, 4),
    (8, 5),
    (9, 3)
    ;