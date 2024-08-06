use django_learning;

create table personnes(
    id int not null auto_increment primary key,
    nom varchar(200),
    prenom varchar(200),
    date_naissance date
);
create table dog(
    id int not null auto_increment primary key,
    nom varchar(50),
    date_naissance date
);

insert into personnes values(
    default, 'Rakoto', 'Jean', '2003-05-28'
); 
insert into dog values(
    default, 'Miles', '2020-09-30'
);