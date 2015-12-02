drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  query text not null,
  result1 text not null,
  result2 text not null,
  result3 text not null,
  result4 text not null,
  result5 text not null,
  rating1 integer not null,
  rating2 integer not null,
  rating3 integer not null,
  rating4 integer not null,
  rating5 integer not null
);
