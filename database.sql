create databases varelager,
    use varelager;

create table varer ( 
    id int auto_increment primary key,
    varenummer int not null,
    navn varchar(50) not null,
    pris decimal(10, 2) not null,
    antall int not null,
    katogori enum("Elektronikk", "Kontor", "Klaer") not null
);