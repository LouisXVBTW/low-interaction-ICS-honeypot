# Stage 1

This wille be for general notes are i recode this for when im taking screenshots and writing it up

#### What is stage 1?

Stage 1 is creating the main file structure, designing the basic protocols and loading all of them from the protocols folder. This will have to include unit testing somehow.

 - [x] ==Basic file structure==
 - [x] ==Design basic protocol==
 - [x] ==Generate multiple protocols==
 - [x] ==Make everything run in parrallel==
 - [x] ==Unit tests==

 so um apparently unit testing sockets is no fun :)


 ### Testing

| Testing | Problems |
| :-: | :-:| 
|Test sample_protocol| &check; |
|Test reply from sample_protocol| &check;|
|Make and test all protocols | &check;|

# Stage 2

### What is stage 2?

Stage 2 is creating and designing the database, create testing, inplement into code. unless i can think of something else instead. 

- [x] ==create/design database==
- [x] ==Add logging to the protocols==
- [x] ==create testing==


connect honeypot protocols to DB

**==Whats does my db need to collect?==**
- amount of connections from ip
- we need a general front page data one with all ip counts, which service got the most attention, geo location, shodan scan, pewpewmap?

| Testing | Problems |
| :-: | :-:| 
|test db|&check;|
|input data to db|&check;|
|fetch data from db |&check;| 

NEED TO DOCUMENT THE UPDATING THE DATABASE EVERY MINUTE PART


# Stage 3

Used fastapi and css and jinja2 html templates and chart.js to make a simple front end dashboard. Need to show the data collection from the database and show how everything was made ;) 
show the use of APIs toget the geo data stuff, but that should all be for stage 2 i think, or maybe i can move it and keep it in stage3. IDK for sure yet, ill do alot of writing tmrw cause ive almost done this anyways.  