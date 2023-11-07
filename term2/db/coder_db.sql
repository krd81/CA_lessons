drop table STUDENTS;
drop table TEACHERS;
drop table SUBJECTS;
drop table ENROLLMENTS;

create table STUDENTS(
    student_id serial primary key,
    f_name text not null,
    l_name text not null,
    dob date
);

create table TEACHERS(
    teacher_id serial primary key,
    teacher_name text not null
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