-- All entities created here
CREATE TABLE player ( 
    playerID INTEGER NOT NULL UNIQUE,
    playerName CHAR(50) NOT NULL,
    playerEmail CHAR(50) NOT NULL,
    playerPass VARCHAR(60) NOT NULL,
    inventory INTEGER NOT NULL,
    backorder INTEGER NOT NULL,
    downstream_playerID INTEGER,
    upstream_playerID INTEGER,
    PRIMARY KEY (playerID)
);

CREATE TABLE game ( 
    sessionID INTEGER NOT NULL UNIQUE,
    distributor_present BOOLEAN,
    wholesaler_present BOOLEAN,
    active BOOLEAN,
    info_sharing BOOLEAN,
    info_delay INTEGER,
    rounds_completed INTEGER,
    starting_inventory INTEGER NOT NULL,
    weeks_played INTEGER,
    sessionLength INTEGER NOT NULL,
    holding_cost DOUBLE,
    backlog_cost DOUBLE,
    PRIMARY KEY (sessionID)
);

CREATE TABLE instructor (
    instructorID INTEGER NOT NULL UNIQUE,
    instructorName CHAR(50) NOT NULL,
    instructorEmail CHAR(50) NOT NULL,
    instructorPass VARCHAR(60) NOT NULL,
    default_gameID INTEGER NOT NULL,
    plots VARCHAR(60),
    PRIMARY KEY (instructorID)
);

CREATE TABLE demandPattern (
    demandID INTEGER NOT NULL UNIQUE,
    weeks INTEGER NOT NULL,
    demandName CHAR(50) NOT NULL,
    demands INTEGER(9) NOT NULL,
    owned_by VARCHAR(60) NOT NULL,
    PRIMARY KEY (demandID)
);

CREATE TABLE demand (
    demandID INTEGER NOT NULL UNIQUE,
    weeks INTEGER NOT NULL,
    demands INTEGER(9) NOT NULL,
    PRIMARY KEY (demandID)
);

-- Tables for relationships

CREATE TABLE instructs (
    instructorID INTEGER,
    playerID INTEGER,
    FOREIGN KEY (instructorID) REFERENCES instructor (instructorID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (playerID) REFERENCES player (playerID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (instructorID,playerID)
);

CREATE TABLE created (
    instructorID INTEGER,
    sessionID INTEGER,
    FOREIGN KEY (instructorID) REFERENCES instructor (instructorID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sessionID) REFERENCES game (sessionID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (instructorID,sessionID)
);

CREATE TABLE plays_in (
    sessionID INTEGER,
    playerID INTEGER,
    FOREIGN KEY (sessionID) REFERENCES game (sessionID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (playerID) REFERENCES player (playerID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (sessionID,playerID)
);

CREATE TABLE pattern (
    sessionID INTEGER,
    demandID INTEGER,
    FOREIGN KEY (sessionID) REFERENCES game (sessionID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (demandID) REFERENCES demandPattern (demandID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (sessionID,demandID)
);

CREATE TABLE pattern_player (
    playerID INTEGER,
    demandID INTEGER,
    FOREIGN KEY (playerID) REFERENCES player (playerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (demandID) REFERENCES demandPattern (demandID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (playerID,demandID)
);

CREATE TABLE pattern_instructor (
    instructorID INTEGER,
    FOREIGN KEY (instructorID) REFERENCES instructor (instructorID) ON DELETE CASCADE ON UPDATE CASCADE,
    demandID INTEGER,
    FOREIGN KEY (demandID) REFERENCES demandPattern (demandID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (instructorID,demandID)
);

CREATE TABLE demands_Plot (
    demandID INTEGER,
    FOREIGN KEY (demandID) REFERENCES demand (demandID) ON DELETE CASCADE ON UPDATE CASCADE,
    demandID INTEGER,
    FOREIGN KEY (demandID) REFERENCES demandPattern (demandID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (instructorID,demandID)
);