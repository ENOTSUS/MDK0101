create table if not exists Orders(
	id integer primary key autoincrement,
	datetime varchar(256) not null,
	menu_positionID integer not null,
	userID integer no null,
	foreign key (menu_positionID) references Menu(id),
	foreign key (userID) references User(id)
);

create table if not exists Cuisine(
	id integer primary key autoincrement,
	name varchar(256) not null
);

create table if not exists Dish(
	id integer primary key autoincrement,
	name varchar(256) not null,
	cooking_time integer not null,
	cuisineID integer not null,
	foreign key (cuisineID) references Cuisine(id)
);

create table if not exists Menu(
	id integer primary key autoincrement,
	price integer not null,
	dishID integer not null,
	foreign key (dishId) references Dish(id)
);

create table if not exists User(
	id integer primary key autoincrement,
    name varchar(256) not null,
    password varchar(256) not null,
    post varchar(256) not null default "User"
);
