create table if not exists genre (
	id serial primary key,
	name_genre varchar(100) not null unique
);

create table if not exists artist (
	id serial primary key,
	name_artist varchar(100) not null 
);

create table if not exists artist_genre (
	id serial primary key,
	genre_id integer not null references genre(id),
	artist_id integer not null references artist(id)
);

create table if not exists album (
	id serial primary key,
	name_album varchar(100) not null,
	release_data date not null
);

create table if not exists artist_album (
	id serial primary key,
	artist_id integer not null references artist(id),
	album_id integer not null references album(id)
);

create table if not exists collection (
	id serial primary key,
	name_collectiom varchar(100) not null,
	release_data integer not null
);

create table if not exists track (
	id serial primary key,
	name_track varchar(100) not null,
	song_length numeric(3,2) not null,
	album_id integer references album(id)
);

create table if not exists collection_track_album (
	id serial primary key,
	collection_id integer not null references collection(id),
	track_id integer not null references track(id)
);