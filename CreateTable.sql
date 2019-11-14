Following tables needs to be creted under Jobs database

CREATE DATABASE "Jobs"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE public.monsterjobs
(
   id SERIAL,
   CompanyName varchar(300),
    JobTitle    varchar(300),
    Location    varchar(200),
    Salary        varchar(80),
    DaysOfPosting    varchar(30)
)



CREATE TABLE public.GlassdoorJobs
(
   id SERIAL,
   CompanyName varchar(100),
    JobTitle    varchar(200),
    Location    varchar(200),
    Salary        varchar(80),
    DaysOfPosting    varchar(10)
)