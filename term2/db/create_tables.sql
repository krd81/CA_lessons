drop table categories cascade;
drop table items;

create table categories(
    id serial primary key,
    name varchar(100) not null unique,
    description text
);

create table items (
    id serial primary key,
    name varchar(200) not null,
    description text not null,
    category_id integer not null,
    foreign key (category_id) references categories (id)
);

insert into categories (name, description) values
    ('Electronics', 'Gadgets to make your life easier'),
    ('Car Parts', 'Expensive stuff for the box with 4 wheels'),
    ('Sports', 'Get out and play'),
    ('Video Games', 'Stay in and play')
    ;