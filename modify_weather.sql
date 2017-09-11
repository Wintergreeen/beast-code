DROP TABLE IF EXISTS weather;
CREATE TABLE weather(
    gdate date not null,
    station_id VARCHAR(20) NOT NULL,
    prcp VARCHAR (8),
    snow VARCHAR (8),
    CONSTRAINT pk_weather PRIMARY KEY(gdate, station_id)
);

CREATE INDEX idx_gdate ON weather (gdate);

INSERT INTO weather (gdate, station_id, prcp, snow)
     SELECT DISTINCT
		STR_TO_DATE(SUBSTR(raw_weather.date from 1 for 10), '%Y-%m-%d'),
		raw_weather.station,
		raw_weather.PRCP,
		raw_weather.SNOW
	FROM raw_weather
	JOIN team ON 1=1
        AND raw_weather.station = team.station_id
	JOIN game ON 1=1
        AND team.team_id =  game.team_1_id
	WHERE 1=1
		AND STR_TO_DATE(SUBSTR(raw_weather.date from 1 for 10), '%Y-%m-%d') = game.game_date;
