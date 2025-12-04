import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

# -----------------------------
# Database Connection
# -----------------------------
def get_connection():
    return sqlite3.connect('Cricket.db')

# -----------------------------
# Initialize Database
# -----------------------------
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Teams table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Teams (
        TeamID INTEGER PRIMARY KEY,
        TeamName VARCHAR(100) NOT NULL,
        CoachName VARCHAR(100)
    )
    ''')
    
    # Players table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Players (
        PlayerID INTEGER PRIMARY KEY,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        DOB DATE,
        Role VARCHAR(50),
        TeamID INTEGER,
        FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
    )
    ''')
    
    # Matches table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Matches (
        MatchID INTEGER PRIMARY KEY,
        MatchDate DATE NOT NULL,
        Venue VARCHAR(100),
        Team1ID INTEGER,
        Team2ID INTEGER,
        FOREIGN KEY (Team1ID) REFERENCES Teams(TeamID),
        FOREIGN KEY (Team2ID) REFERENCES Teams(TeamID)
    )
    ''')
    
    # BattingStats table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BattingStats (
        PlayerID INTEGER,
        MatchID INTEGER,
        Runs INTEGER DEFAULT 0,
        BallsFaced INTEGER DEFAULT 0,
        Fours INTEGER DEFAULT 0,
        Sixes INTEGER DEFAULT 0,
        StrikeRate FLOAT,
        PRIMARY KEY (PlayerID, MatchID),
        FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
        FOREIGN KEY (MatchID) REFERENCES Matches(MatchID)
    )
    ''')
    
    # BowlingStats table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BowlingStats (
        PlayerID INTEGER,
        MatchID INTEGER,
        Overs FLOAT DEFAULT 0,
        Maidens INTEGER DEFAULT 0,
        RunsConceded INTEGER DEFAULT 0,
        Wickets INTEGER DEFAULT 0,
        EconomyRate FLOAT,
        PRIMARY KEY (PlayerID, MatchID),
        FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
        FOREIGN KEY (MatchID) REFERENCES Matches(MatchID)
    )
    ''')
    
    conn.commit()
    conn.close()

# -----------------------------
# CRUD Operations - Teams
# -----------------------------
def create_team(team_id, team_name, coach_name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Teams VALUES (?, ?, ?)", (team_id, team_name, coach_name))
        conn.commit()
        return True, "Team added successfully!"
    except sqlite3.IntegrityError:
        return False, "Team ID already exists!"
    finally:
        conn.close()

def read_teams():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM Teams", conn)
    conn.close()
    return df

def update_team(team_id, team_name, coach_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Teams SET TeamName=?, CoachName=? WHERE TeamID=?", 
                   (team_name, coach_name, team_id))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0

def delete_team(team_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Teams WHERE TeamID=?", (team_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0

# -----------------------------
# CRUD Operations - Players
# -----------------------------
def create_player(player_id, first_name, last_name, dob, role, team_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?)", 
                       (player_id, first_name, last_name, dob, role, team_id))
        conn.commit()
        return True, "Player added successfully!"
    except sqlite3.IntegrityError:
        return False, "Player ID already exists!"
    finally:
        conn.close()

def read_players():
    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT p.*, t.TeamName 
        FROM Players p 
        LEFT JOIN Teams t ON p.TeamID = t.TeamID
    """, conn)
    conn.close()
    return df

def update_player(player_id, first_name, last_name, dob, role, team_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE Players 
                      SET FirstName=?, LastName=?, DOB=?, Role=?, TeamID=? 
                      WHERE PlayerID=?""", 
                   (first_name, last_name, dob, role, team_id, player_id))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0

def delete_player(player_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Players WHERE PlayerID=?", (player_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0

# -----------------------------
# CRUD Operations - Matches
# -----------------------------
def create_match(match_id, match_date, venue, team1_id, team2_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Matches VALUES (?, ?, ?, ?, ?)", 
                       (match_id, match_date, venue, team1_id, team2_id))
        conn.commit()
        return True, "Match added successfully!"
    except sqlite3.IntegrityError:
        return False, "Match ID already exists!"
    finally:
        conn.close()

def read_matches():
    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT m.MatchID, m.MatchDate, m.Venue, 
               t1.TeamName as Team1, t2.TeamName as Team2
        FROM Matches m
        LEFT JOIN Teams t1 ON m.Team1ID = t1.TeamID
        LEFT JOIN Teams t2 ON m.Team2ID = t2.TeamID
    """, conn)
    conn.close()
    return df

def update_match(match_id, match_date, venue, team1_id, team2_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE Matches 
                      SET MatchDate=?, Venue=?, Team1ID=?, Team2ID=? 
                      WHERE MatchID=?""", 
                   (match_date, venue, team1_id, team2_id, match_id))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0

def delete_match(match_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Matches WHERE MatchID=?", (match_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0

# -----------------------------
# CRUD Operations - Batting Stats
# -----------------------------
def create_batting_stat(player_id, match_id, runs, balls_faced, fours, sixes):
    conn = get_connection()
    cursor = conn.cursor()
    strike_rate = (runs / balls_faced * 100) if balls_faced > 0 else 0
    try:
        cursor.execute("""INSERT INTO BattingStats 
                          VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                       (player_id, match_id, runs, balls_faced, fours, sixes, strike_rate))
        conn.commit()
        return True, "Batting stats added successfully!"
    except sqlite3.IntegrityError:
        return False, "Batting stats already exist for this player and match!"
    finally:
        conn.close()

def read_batting_stats():
    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT b.*, p.FirstName || ' ' || p.LastName as PlayerName
        FROM BattingStats b
        LEFT JOIN Players p ON b.PlayerID = p.PlayerID
    """, conn)
    conn.close()
    return df

# -----------------------------
# CRUD Operations - Bowling Stats
# -----------------------------
def create_bowling_stat(player_id, match_id, overs, maidens, runs_conceded, wickets):
    conn = get_connection()
    cursor = conn.cursor()
    economy_rate = (runs_conceded / overs) if overs > 0 else 0
    try:
        cursor.execute("""INSERT INTO BowlingStats 
                          VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                       (player_id, match_id, overs, maidens, runs_conceded, wickets, economy_rate))
        conn.commit()
        return True, "Bowling stats added successfully!"
    except sqlite3.IntegrityError:
        return False, "Bowling stats already exist for this player and match!"
    finally:
        conn.close()

def read_bowling_stats():
    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT b.*, p.FirstName || ' ' || p.LastName as PlayerName
        FROM BowlingStats b
        LEFT JOIN Players p ON b.PlayerID = p.PlayerID
    """, conn)
    conn.close()
    return df

# -----------------------------
# Streamlit App
# -----------------------------
def main():
    st.set_page_config(page_title="Cricket Database CRUD", layout="wide")
    st.title("🏏 Cricket Database Management System")
    
    # Initialize DB
    init_db()
    
    # Sidebar menu
    menu = st.sidebar.selectbox("Select Table", 
                                ["Dashboard", "Teams", "Players", "Matches", "Batting Stats", "Bowling Stats"])
    
    if menu == "Dashboard":
        st.header("📊 Database Dashboard")
        
        # Teams
        st.subheader("👥 Teams")
        teams_df = read_teams()
        st.dataframe(teams_df, use_container_width=True)
        st.metric("Total Teams", len(teams_df))
        st.divider()
        
        # Players
        st.subheader("🏃 Players")
        players_df = read_players()
        st.dataframe(players_df, use_container_width=True)
        st.metric("Total Players", len(players_df))
        if not players_df.empty:
            st.bar_chart(players_df['Role'].value_counts())
        st.divider()
        
        # Matches
        st.subheader("🏟️ Matches")
        matches_df = read_matches()
        st.dataframe(matches_df, use_container_width=True)
        st.metric("Total Matches", len(matches_df))
        st.divider()
        
        # Batting Stats
        st.subheader("🏏 Batting Statistics")
        batting_df = read_batting_stats()
        st.dataframe(batting_df, use_container_width=True)
        if not batting_df.empty:
            top_scorers = batting_df.nlargest(5, 'Runs')[['PlayerName', 'Runs', 'StrikeRate']]
            col1, col2 = st.columns(2)
            with col1:
                st.write("Top 5 Run Scorers")
                st.dataframe(top_scorers, hide_index=True)
            with col2:
                st.bar_chart(top_scorers.set_index('PlayerName')['Runs'])
        st.divider()
        
        # Bowling Stats
        st.subheader("🎯 Bowling Statistics")
        bowling_df = read_bowling_stats()
        st.dataframe(bowling_df, use_container_width=True)
        if not bowling_df.empty:
            top_bowlers = bowling_df.nlargest(5, 'Wickets')[['PlayerName', 'Wickets', 'EconomyRate']]
            col1, col2 = st.columns(2)
            with col1:
                st.write("Top 5 Wicket Takers")
                st.dataframe(top_bowlers, hide_index=True)
            with col2:
                st.bar_chart(top_bowlers.set_index('PlayerName')['Wickets'])
    else:
        # CRUD Operations
        operation = st.sidebar.radio("Operation", ["Create", "Read", "Update", "Delete"])
        
        # Teams
        if menu == "Teams":
            st.header("Teams Management")
            if operation == "Create":
                with st.form("create_team"):
                    team_id = st.number_input("Team ID", min_value=1, step=1)
                    team_name = st.text_input("Team Name")
                    coach_name = st.text_input("Coach Name")
                    submitted = st.form_submit_button("Add Team")
                    if submitted:
                        success, msg = create_team(team_id, team_name, coach_name)
                        st.success(msg) if success else st.error(msg)
            elif operation == "Read":
                st.dataframe(read_teams(), use_container_width=True)
            elif operation == "Update":
                with st.form("update_team"):
                    team_id = st.number_input("Team ID", min_value=1, step=1)
                    team_name = st.text_input("New Team Name")
                    coach_name = st.text_input("New Coach Name")
                    submitted = st.form_submit_button("Update Team")
                    if submitted:
                        st.success("Team updated!") if update_team(team_id, team_name, coach_name) else st.error("Team not found!")
            elif operation == "Delete":
                team_id = st.number_input("Team ID to Delete", min_value=1, step=1)
                if st.button("Delete Team"):
                    st.success("Team deleted!") if delete_team(team_id) else st.error("Team not found!")
        
        # Players
        elif menu == "Players":
            st.header("Players Management")
            if operation == "Create":
                with st.form("create_player"):
                    player_id = st.number_input("Player ID", min_value=1, step=1)
                    first_name = st.text_input("First Name")
                    last_name = st.text_input("Last Name")
                    dob = st.date_input("Date of Birth", value=date(2000,1,1))
                    role = st.selectbox("Role", ["Batsman","Bowler","All-Rounder","Wicket-Keeper"])
                    team_id = st.number_input("Team ID", min_value=1, step=1)
                    submitted = st.form_submit_button("Add Player")
                    if submitted:
                        success, msg = create_player(player_id, first_name, last_name, str(dob), role, team_id)
                        st.success(msg) if success else st.error(msg)
            elif operation == "Read":
                st.dataframe(read_players(), use_container_width=True)
            elif operation == "Update":
                with st.form("update_player"):
                    player_id = st.number_input("Player ID", min_value=1, step=1)
                    first_name = st.text_input("New First Name")
                    last_name = st.text_input("New Last Name")
                    dob = st.date_input("New Date of Birth", value=date(2000,1,1))
                    role = st.selectbox("New Role", ["Batsman","Bowler","All-Rounder","Wicket-Keeper"])
                    team_id = st.number_input("New Team ID", min_value=1, step=1)
                    submitted = st.form_submit_button("Update Player")
                    if submitted:
                        st.success("Player updated!") if update_player(player_id, first_name, last_name, str(dob), role, team_id) else st.error("Player not found!")
            elif operation == "Delete":
                player_id = st.number_input("Player ID to Delete", min_value=1, step=1)
                if st.button("Delete Player"):
                    st.success("Player deleted!") if delete_player(player_id) else st.error("Player not found!")
        
        # Matches
        elif menu == "Matches":
            st.header("Matches Management")
            if operation == "Create":
                with st.form("create_match"):
                    match_id = st.number_input("Match ID", min_value=1, step=1)
                    match_date = st.date_input("Match Date", value=date.today())
                    venue = st.text_input("Venue")
                    team1_id = st.number_input("Team 1 ID", min_value=1, step=1)
                    team2_id = st.number_input("Team 2 ID", min_value=1, step=1)
                    submitted = st.form_submit_button("Add Match")
                    if submitted:
                        success, msg = create_match(match_id, str(match_date), venue, team1_id, team2_id)
                        st.success(msg) if success else st.error(msg)
            elif operation == "Read":
                st.dataframe(read_matches(), use_container_width=True)
            elif operation == "Update":
                with st.form("update_match"):
                    match_id = st.number_input("Match ID", min_value=1, step=1)
                    match_date = st.date_input("New Match Date", value=date.today())
                    venue = st.text_input("New Venue")
                    team1_id = st.number_input("New Team 1 ID", min_value=1, step=1)
                    team2_id = st.number_input("New Team 2 ID", min_value=1, step=1)
                    submitted = st.form_submit_button("Update Match")
                    if submitted:
                        st.success("Match updated!") if update_match(match_id, str(match_date), venue, team1_id, team2_id) else st.error("Match not found!")
            elif operation == "Delete":
                match_id = st.number_input("Match ID to Delete", min_value=1, step=1)
                if st.button("Delete Match"):
                    st.success("Match deleted!") if delete_match(match_id) else st.error("Match not found!")
        
        # Batting Stats
        elif menu == "Batting Stats":
            st.header("Batting Statistics Management")
            if operation == "Create":
                with st.form("create_batting"):
                    player_id = st.number_input("Player ID", min_value=1, step=1)
                    match_id = st.number_input("Match ID", min_value=1, step=1)
                    runs = st.number_input("Runs", min_value=0, step=1)
                    balls_faced = st.number_input("Balls Faced", min_value=0, step=1)
                    fours = st.number_input("Fours", min_value=0, step=1)
                    sixes = st.number_input("Sixes", min_value=0, step=1)
                    submitted = st.form_submit_button("Add Batting Stats")
                    if submitted:
                        success, msg = create_batting_stat(player_id, match_id, runs, balls_faced, fours, sixes)
                        st.success(msg) if success else st.error(msg)
            elif operation == "Read":
                st.dataframe(read_batting_stats(), use_container_width=True)
        
        # Bowling Stats
        elif menu == "Bowling Stats":
            st.header("Bowling Statistics Management")
            if operation == "Create":
                with st.form("create_bowling"):
                    player_id = st.number_input("Player ID", min_value=1, step=1)
                    match_id = st.number_input("Match ID", min_value=1, step=1)
                    overs = st.number_input("Overs", min_value=0.0, step=0.1)
                    maidens = st.number_input("Maidens", min_value=0, step=1)
                    runs_conceded = st.number_input("Runs Conceded", min_value=0, step=1)
                    wickets = st.number_input("Wickets", min_value=0, step=1)
                    submitted = st.form_submit_button("Add Bowling Stats")
                    if submitted:
                        success, msg = create_bowling_stat(player_id, match_id, overs, maidens, runs_conceded, wickets)
                        st.success(msg) if success else st.error(msg)
            elif operation == "Read":
                st.dataframe(read_bowling_stats(), use_container_width=True)


if __name__ == "__main__":
    main()
