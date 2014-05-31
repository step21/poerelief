drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  loc text not null,
  text text not null,
  ddate date not null,
  inscr text not null,
  name text not null,
  comment text not null,
-- more fields as appropriate / also make separate field with locsa
);