.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students
         where color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students
         where color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students 
         group by smallest having count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color 
     from students as first, students as second
        where first.pet = second.pet and first.song = second.song and first.time < second.time 
;

CREATE TABLE sevens AS
  SELECT seven from students, numbers 
       where students.number = 7 and students.time = numbers.time and numbers."7" = "True";  
           


CREATE TABLE average_prices AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE lowest_prices AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE shopping_list AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

