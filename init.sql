DROP TABLE IF EXISTS events;
CREATE TABLE events (
       ts timestamp default current_timestamp,
       event text
);
