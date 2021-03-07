INSERT INTO player VALUES (1, 'Hamlet', 'hamlet@bingmail.com','hamlet1210',10,5,2,NULL);
INSERT INTO player VALUES (2, 'Horatio', 'horatio@dbmail.com','horatio2522',5,0,3,1);
INSERT INTO player VALUES (3, 'Rob', 'rob@mmail.com','stel@1214',3,1,4,2);
INSERT INTO player VALUES (4, 'Jamie', 'jamiebond@bingmail.com','jbond007',5,0,NULL,3);

INSERT INTO game VALUES(1, TRUE, TRUE, TRUE, TRUE, 7,0,12,0,10,5.50,7.50);
INSERT INTO game VALUES(2, TRUE, TRUE, TRUE, TRUE, 5,0,10,0,12,4.50,10.50);

INSERT INTO instructor VALUES(1,"Pete","pete@dbmail.com","pete@1480",1,NULL);

INSERT INTO demandPattern VALUES (1,1,"week 1",45,"player");

INSERT INTO instructs VALUES (1,1);
INSERT INTO instructs VALUES (1,2);
INSERT INTO instructs VALUES (1,3);
INSERT INTO instructs VALUES (1,4);

INSERT INTO created VALUES (1,1);
INSERT INTO created VALUES (1,2);

INSERT INTO plays_in VALUES (1,1);
INSERT INTO plays_in VALUES (1,2);
INSERT INTO plays_in VALUES (2,3);
INSERT INTO plays_in VALUES (2,4);

INSERT INTO pattern VALUES (1,1);
INSERT INTO pattern VALUES (2,1);

INSERT INTO pattern_player VALUES (1,1);
INSERT INTO pattern_player VALUES (3,1);

INSERT INTO pattern_instructor VALUES (1,1);
INSERT INTO pattern_instructor VALUES (1,1);