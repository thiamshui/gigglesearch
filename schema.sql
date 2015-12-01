drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  query text not null,
  rating1 integer not null,
  rating2 integer not null,
  rating3 integer not null,
  rating4 integer not null,
  rating5 integer not null,
  avgrating integer not null
);
