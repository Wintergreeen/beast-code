/*
* Kyle Hart
* 2 Sept 2017
*
* Project: beastcode
* File: create_tables.sql
* Description: Creates database schema and tables for the beastcode project
*/

CREATE DATABASE IF NOT EXISTS league;
USE league;

DROP TABLE IF EXISTS raw_schedule;
CREATE TABLE raw_schedule(
    team_id int,
    team_name varchar(50),
    game_date date,
    opp_id int,
    opp_name varchar(50),
    team_score int,
    opp_score int,
    location varchar(20)
);

DROP TABLE IF EXISTS raw_offence;
CREATE TABLE raw_offence(
    team_id int,
    team_name varchar(50),
    game_date date,
    uniform_num int,
    lname varchar(25),
    fname varchar(25),
    rush_att int,
    rush_gain int,
    rush_loss int,
    rush_net int,
    rush_td int,
    pass_att int,
    pass_cmp int,
    pass_intc int,
    pass_yards int,
    pass_td int,
    pass_conv int,
    ttl_plays int,
    ttl_yards int,
    rec_cmp int,
    rec_yards int,
    rec_td int,
    intc_cmp int,
    intc_yards int,
    intc_td int,
    fumb_cmp int,
    fumb_yards int,
    fumb_td int,
    punt_cmp int,
    punt_yards int,
    punt_ret_cmp int,
    punt_ret_yards int,
    punt_ret_td int,
    ko_ret_cmp int,
    ko_ret_yards int,
    ko_ret_td int,
    ttl_td int,


)

)
DROP TABLE IF EXISTS team;
CREATE TABLE team(

)
