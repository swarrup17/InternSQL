 CREATE TABLE Teams (
    TeamID INT auto_increment PRIMARY KEY,
    TeamName VARCHAR(100) NOT NULL,
    CoachName VARCHAR(100)
);
CREATE TABLE Players (
    PlayerID INT PRIMARY KEY auto_increment,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DOB DATE,
    Role VARCHAR(50),   
    TeamID INT,
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);
CREATE TABLE BowlingStats (
    PlayerID INT,
    MatchID INT,
    Overs FLOAT DEFAULT 0,
    Maidens INT DEFAULT 0,
    RunsConceded INT DEFAULT 0,
    Wickets INT DEFAULT 0,
    EconomyRate FLOAT,
    PRIMARY KEY (PlayerID, MatchID),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
    FOREIGN KEY (MatchID) REFERENCES Matches(MatchID)

);
CREATE TABLE BattingStats (
    PlayerID INT,
    MatchID INT,
    Runs INT DEFAULT 0,
    BallsFaced INT DEFAULT 0,
    Fours INT DEFAULT 0,
    Sixes INT DEFAULT 0,
    StrikeRate FLOAT,
    PRIMARY KEY (PlayerID, MatchIDbattingstatsbattingstats),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
    FOREIGN KEY (MatchID) REFERENCES Matches(MatchID)
);
CREATE TABLE Matches (
    MatchID INTEGER PRIMARY KEY auto_increment,
    MatchDate DATE NOT NULL,
    Venue VARCHAR(100),
    Team1ID INTEGER,
    Team2ID INTEGER,
    Team1Score INTEGER DEFAULT 0,
    Team2Score INTEGER DEFAULT 0,
    WinnerTeamID INTEGER,
    WinBy VARCHAR(50),
    FOREIGN KEY (Team1ID) REFERENCES Teams(TeamID),
    FOREIGN KEY (Team2ID) REFERENCES Teams(TeamID),
    FOREIGN KEY (WinnerTeamID) REFERENCES Teams(TeamID)
);

INSERT INTO Teams (TeamID, TeamName, CoachName) VALUES 
(1, 'Red Tigers', 'John Smith'),
(2, 'Blue Sharks', 'Mary Johnson'),
(3, 'India', 'Rahul Dravid'),
(4, 'Australia', 'Andrew McDonald'),
(5, 'England', 'Brendon McCullum'),
(6, 'New Zealand', 'Gary Stead'),
(7, 'Pakistan', 'Saeed Anwar'),
(8, 'Sri Lanka', 'Chris Silverwood'),
(9, 'West Indies', 'Phil Simmons'),
(10, 'Bangladesh', 'Russell Domingo'),
(11, 'Afghanistan', 'Jonathan Trott'),
(12, 'Ireland', 'Graham Ford'),
(13, 'Zimbabwe', 'Dave Houghton');


INSERT INTO Players (PlayerID, FirstName, LastName, DOB, Role, TeamID) VALUES
(1, 'Swarup', 'Dahal', '2000-05-15', 'Batsman', 1),
(2, 'Rohit', 'Shrestha', '1999-03-22', 'Bowler', 1),
(3, 'Anita', 'Koirala', '2001-08-10', 'All-Rounder', 2),
(4, 'Virat', 'Kohli', '1988-11-05', 'Batsman', 3),
(5, 'Rohit', 'Sharma', '1987-04-30', 'Batsman', 3),
(6, 'Jasprit', 'Bumrah', '1993-12-06', 'Bowler', 3),
(7, 'David', 'Warner', '1986-10-27', 'Batsman', 4),
(8, 'Pat', 'Cummins', '1993-05-08', 'Bowler', 4),
(9, 'Joe', 'Root', '1990-12-30', 'Batsman', 5),
(10, 'Jofra', 'Archer', '1995-04-01', 'Bowler', 5),
(11, 'Kane', 'Williamson', '1990-08-08', 'Batsman', 6),
(12, 'Trent', 'Boult', '1989-07-22', 'Bowler', 6),
(13, 'Babar', 'Azam', '1994-10-15', 'Batsman', 7),
(14, 'Shaheen', 'Afridi', '2000-04-06', 'Bowler', 7),
(15, 'Dimuth', 'Karunaratne', '1988-08-21', 'Batsman', 8),
(16, 'Wanindu', 'Hasaranga', '1997-07-29', 'All-Rounder', 8),
(17, 'Kemar', 'Roach', '1988-07-30', 'Bowler', 9),
(18, 'Shai', 'Hope', '1993-07-27', 'Batsman', 9),
(19, 'Shakib', 'Al Hasan', '1987-03-24', 'All-Rounder', 10),
(20, 'Mushfiqur', 'Rahim', '1987-09-09', 'Wicket-Keeper', 10),
(21, 'Rashid', 'Khan', '1998-09-20', 'Bowler', 11),
(22, 'Mohammad', 'Nabi', '1985-09-19', 'All-Rounder', 11),
(23, 'Paul', 'Stirling', '1990-09-03', 'Batsman', 12),
(24, 'Kevin', 'O''Brien', '1984-03-04', 'Batsman', 12),
(25, 'Sean', 'Williams', '1986-09-26', 'All-Rounder', 13),
(26, 'Craig', 'Ervine', '1985-02-23', 'Batsman', 13),
(27, 'Mohammad', 'Shan', '1995-05-10', 'Batsman', 11),
(28, 'Andy', 'Balbirnie', '1991-10-16', 'Batsman', 12),
(29, 'Regis', 'Chakabva', '1987-09-20', 'Wicket-Keeper', 13),
(30, 'Mujeeb', 'Ur Rahman', '2001-03-28', 'Bowler', 11),
(31, 'Fawad', 'Ahmad', '1992-03-17', 'Bowler', 11),
(32, 'George', 'Dockrell', '1992-07-16', 'Bowler', 12),
(33, 'Tim', 'Chand', '1988-11-01', 'Batsman', 13),
(34, 'Hashmat', 'ullah', '1994-03-10', 'Batsman', 11),
(35, 'Curtis', 'Campher', '1999-10-31', 'All-Rounder', 12),
(36, 'Brendan', 'Taylor', '1986-02-06', 'Batsman', 13),
(37, 'Nawroz', 'Mardan', '2000-01-12', 'All-Rounder', 11),
(38, 'Stuart', 'Patterson', '1991-06-20', 'Bowler', 12),
(39, 'Brian', 'Chari', '1992-05-15', 'All-Rounder', 13),
(40, 'Sharafuddin', 'Ashraf', '1995-08-30', 'Batsman', 11);


INSERT INTO Matches (MatchID, MatchDate, Venue, Team1ID, Team2ID, Team1Score, Team2Score, WinnerTeamID, WinBy) VALUES
(1, '2025-12-05', 'Stadium A', 1, 2, 250, 245, 1, '5 runs'),
(2, '2025-12-10', 'Stadium B', 1, 2, 260, 265, 2, '5 runs'),
(3, '2025-01-15', 'Melbourne Cricket Ground', 3, 4, 280, 270, 3, '10 runs'),
(4, '2025-02-10', 'Lord''s Cricket Ground', 5, 6, 300, 295, 5, '5 runs'),
(5, '2025-03-15', 'Gaddafi Stadium', 7, 8, 250, 245, 7, '5 runs'),
(6, '2025-04-10', 'Kensington Oval', 9, 10, 280, 300, 10, '20 runs'),
(7, '2025-05-05', 'R. Premadasa Stadium', 8, 7, 260, 261, 7, '1 wicket'),
(8, '2025-06-20', 'Sher-e-Bangla Stadium', 10, 9, 275, 270, 10, '5 runs'),
(9, '2025-07-05', 'Kabul International Cricket Stadium', 11, 12, 305, 289, 11, '16 runs'),
(10, '2025-07-10', 'The Village', 12, 13, 220, 218, 12, '2 runs'),
(11, '2025-07-15', 'Harare Sports Club', 13, 11, 240, 250, 11, '10 runs'),
(12, '2025-08-01', 'Kabul International Cricket Stadium', 11, 13, 300, 298, 11, '2 runs'),
(13, '2025-08-05', 'The Village', 12, 11, 270, 275, 11, '5 runs'),
(14, '2025-08-10', 'Harare Sports Club', 13, 12, 265, 260, 13, '5 runs');


INSERT INTO BattingStats (PlayerID, MatchID, Runs, BallsFaced, Fours, Sixes, StrikeRate) VALUES
(1, 1, 50, 40, 6, 2, 125.0),
(3, 1, 35, 30, 4, 1, 116.7),
(4, 3, 85, 72, 10, 1, 118.0),
(7, 3, 60, 45, 7, 3, 133.3),
(9, 4, 110, 95, 12, 2, 115.7),
(11, 4, 92, 88, 8, 1, 104.5),
(13, 5, 78, 65, 8, 1, 120.0),
(15, 5, 45, 38, 4, 1, 118.4),
(18, 6, 90, 72, 10, 2, 125.0),
(19, 6, 56, 50, 5, 1, 112.0),
(16, 7, 65, 52, 6, 1, 125.0),
(14, 7, 22, 18, 2, 0, 122.2),
(20, 8, 71, 60, 7, 1, 118.3),
(17, 8, 48, 40, 4, 0, 120.0),
(21, 9, 55, 38, 6, 1, 144.7),
(22, 9, 32, 28, 4, 0, 114.3),
(23, 9, 70, 60, 8, 2, 116.7),
(24, 10, 48, 40, 5, 0, 120.0),
(25, 10, 35, 30, 4, 1, 116.7),
(26, 10, 62, 50, 7, 1, 124.0),
(27, 11, 41, 32, 4, 0, 128.1),
(28, 11, 55, 45, 6, 1, 122.2),
(29, 11, 30, 28, 3, 0, 107.1),
(30, 12, 65, 50, 7, 2, 130.0),
(31, 12, 27, 25, 3, 0, 108.0),
(32, 12, 40, 38, 4, 0, 105.3),
(33, 13, 52, 42, 5, 1, 123.8),
(34, 13, 48, 40, 5, 1, 120.0),
(35, 13, 33, 28, 3, 0, 117.9),
(36, 14, 60, 50, 6, 1, 120.0),
(37, 14, 39, 32, 4, 0, 121.9),
(38, 14, 45, 40, 4, 1, 112.5),
(39, 14, 50, 45, 5, 1, 111.1),
(40, 14, 55, 48, 6, 2, 114.6);


INSERT INTO BowlingStats (PlayerID, MatchID, Overs, Maidens, RunsConceded, Wickets, EconomyRate) VALUES
(2, 1, 10, 1, 45, 3, 4.5),
(3, 1, 4, 0, 28, 1, 7.0),
(6, 3, 10, 2, 48, 2, 4.8),
(8, 3, 10, 1, 52, 3, 5.2),
(10, 4, 9, 0, 58, 2, 6.4),
(12, 4, 10, 1, 45, 4, 4.5),
(14, 5, 10, 1, 50, 3, 5.0),
(16, 5, 8, 0, 42, 2, 5.25),
(17, 6, 10, 1, 55, 4, 5.5),
(19, 6, 9, 0, 48, 2, 5.33),
(16, 7, 10, 0, 60, 3, 6.0),
(14, 7, 9, 0, 45, 2, 5.0),
(20, 8, 10, 1, 50, 3, 5.0),
(17, 8, 8, 0, 40, 2, 5.0),
(21, 9, 10, 1, 50, 3, 5.0),
(30, 9, 8, 0, 42, 2, 5.25),
(31, 9, 9, 0, 48, 2, 5.33),
(22, 10, 10, 2, 45, 3, 4.5),
(32, 10, 8, 0, 40, 1, 5.0),
(38, 10, 9, 0, 46, 2, 5.11),
(37, 11, 10, 1, 50, 3, 5.0),
(39, 11, 8, 0, 42, 2, 5.25),
(40, 12, 9, 0, 48, 2, 5.33),
(34, 12, 10, 1, 50, 3, 5.0),
(27, 13, 8, 0, 45, 1, 5.62),
(35, 13, 9, 1, 48, 2, 5.33),
(36, 14, 10, 2, 52, 4, 5.2),
(31, 14, 8, 0, 40, 2, 5.0),
(22, 14, 9, 1, 47, 3, 5.22);


-- select all data from table every table
select  * from teams;
select * from players;
select * from matches;
select * from bowlingstats;
select * from battingstats;

-- display the name and run of player with highest run 
select p.PlayerID,p.FirstName,P.LastName, bt.Runs
from players p join battingstats bt on p.PlayerID=bt.PlayerID order by bt.Runs DESC limit 1 ;

-- display the name and total wicket of player with highest wicket
select p.PlayerID,p.FirstName,P.LastName, bw.Wickets
from players p join bowlingstats bw on p.PlayerID=bw.PlayerID order by bw.Wickets DESC limit 1 ;

-- display the match result for matchID 4 with the player scoring highest run
-- and highest wicket taker
select m.MatchID,m.WinnerTeamID,m.WinBy,t.TeamID,t.TeamName,
p.PlayerID, p.FirstName,P.LastName, bt.runs as highestrun, bw.wickets as highestwicket from matches m left join 
players p ON p.TeamID=m.WinnerTeamID left join battingstats bt on bt.PlayerID=p.PlayerID and bt.MatchID=m.MatchID
left join bowlingstats bw on bw.PlayerID=p.PlayerID and bw.MatchID=m.MatchID  left join Teams t on t.TeamID=m.WinnerTeamID where m.matchID=4;

-- display player name with the maximum number of sixes
select p.PlayerID, concat(p.FirstName,'  ',p.LastName) as FullName, 
bt.Sixes from players p join battingstats bt on bt.PlayerID=p.PlayerID 
order by  bt.Sixes DESC limit 1; 

-- display the numbers of boundaries hit by every batsman i.e. fours and sixes
select concat(p.FirstName,' ',p.LastName) as name, sum(b.Sixes+b.Fours) as Boundaries
 from players p join battingstats as b on b.PlayerID=p.PlayerID group by name order by Boundaries desc;
 
--  add a performance category based on runs:
-- 0-20?:poor,20-40: average,50-100:good,100+: excellent
select b.PlayerID,concat(p.FirstName,' ',p.LastName) as full_name,b.Runs,b.StrikeRate,
CASE
  WHEN b.Runs<20 then 'poor'
  when	b.Runs>=20 and b.Runs<40 then 'average'
  when b.Runs>=40 and b.Runs<100 then 'good'
  when b.Runs>=100 then 'excellent'
  else null
end as performance_category
from players p join battingstats b on b.PlayerID=p.PlayerID order by b.Runs desc ;

 -- add bowling category based on wickets
 -- 0:poor, 1-2:decent 3-4 good 5+: excellent
select b.PlayerID,concat(p.FirstName,' ',p.LastName) as full_name, b.Wickets,b.EconomyRate,
case 
   when b.Wickets=0 then 'poor'
   when b.Wickets=1 or b.Wickets=2 then 'decent'
   when b.Wickets=3 or b.Wickets=4 then 'good'
   when b.Wickets>=5 then 'excellent'
   else null
end as bowling_performance
from players p join bowlingstats b on b.PlayerID=p.PlayerID order by b.Wickets desc;

-- show the oldest player
select PlayerID,concat(FirstName,' ',LastName)as fullname,DOB from players where DOB= (
select min(DOB) from players);

--  show all rounders (runs>30 and wickets>1 )
select p.PlayerID,concat(p.FirstName,' ',p.LastName)as full_name,
p.Role,bt.Runs,bw.Wickets from players p join battingstats bt
on bt.PlayerID=p.PlayerID 
join bowlingstats bw on bw.PlayerID=p.PlayerID
where p.Role='All-rounder' and bt.Runs>30 and bw.Wickets>1

--   


 
