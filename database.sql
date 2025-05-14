create databases varelager,
    use varelager;

create table person ( 
    id int auto_increment primary key,
    for_navn varchar(50) not null,
    etter_navn varchar(50) not null,
    aar timestamp not null default current_timestamp,|
    antall int not null

 
);