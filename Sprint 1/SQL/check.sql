select count(*) FROM player;
select count(*) FROM game;
select count(*) FROM instructor;
select count(*) FROM demandPattern;
select count(*) FROM instructs;
select count(*) FROM created;
select count(*) FROM plays_in;
select count(*) FROM pattern;
select count(*) FROM pattern_player;
select count(*) FROM pattern_instructor;

-- Some use useful queries for later

SELECT G.name, I.name FROM player P, instructor I, game G, instructs Ins 
                    WHERE Ins.playerID = P.playerID AND Ins.instructorID = I.instructorID