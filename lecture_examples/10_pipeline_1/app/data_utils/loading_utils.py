import csv
import os
import sqlite3

import pandas as pd

DB_PATH = os.environ["DB_PATH"]
DATA_DIR = os.environ["DATA_DIR"]


def load_data_pandas():
    """Previous code
    loads to a DF
    """
    file_path = "/app/src/data/all_seasons.csv"
    df = pd.read_csv(file_path)
    df = df.loc[
        df.season == "2022-23",
        [
            "player_name",
            "college",
            "team_abbreviation",
        ],
    ]

    # load_data_sql()
    return df


def load_data():
    """
    Loading data with SQL
    """
    conn = create_db_connection()

    query = """select player_name,
            college,
            team_abbreviation
        from player_stats
    where season = '2022-23';"""

    df = pd.DataFrame(execute_query_return_list_of_dicts_lm(conn, query))

    return df


def create_db_connection(db_path=None):
    """Sqlite specific connection function
    takes in the db_path
    """
    if not db_path:
        db_path = DB_PATH

    if not os.path.exists(db_path):
        raise FileExistsError(f"Database does not exist at: {db_path}")

    conn = sqlite3.connect(db_path)
    return conn


def execute_query_return_list_of_dicts_lm(conn, sql_query):
    """
    Low memory version of loading command command
    """

    cursor = conn.cursor()
    cursor.execute(sql_query)
    description_info = cursor.description

    headers = [x[0] for x in description_info]
    return_dict_list = []

    while True:
        single_result = cursor.fetchone()

        if not single_result:
            break

        single_result_dict = dict(zip(headers, single_result))
        return_dict_list.append(single_result_dict)

    return return_dict_list


def load_csv_to_db(conn, csv_path, table_name):
    """Load a CSV file into an existing SQLite table.

    Args:
        csv_path: Path to the CSV file
        conn: SQLite connection
        table_name: Name of the existing table
    """

    with open(csv_path) as f:
        reader = csv.reader(f)
        headers = next(reader)[1:]  # Get column names
        headers = ["id"] + headers

        # Prepare INSERT statement
        placeholders = ",".join("?" for _ in headers)
        insert_sql = (
            f"INSERT INTO {table_name} ({','.join(headers)})"
            f" VALUES ({placeholders})"
        )
        # Insert all rows
        cur = conn.cursor()
        # import pdb; pdb.set_trace()
        cur.executemany(insert_sql, reader)
        conn.commit()
    print(f"Loaded {cur.rowcount} rows to {table_name} successfully")
    return True


def execute_sql_command(conn, sql_query):
    cur = conn.cursor()
    cur.execute(sql_query)
    conn.commit()
    return None


def create_player_stats_table(conn):
    """Create an table for basketball player statistics."""
    create_table_ball = """
    CREATE TABLE player_stats (
        id INTEGER PRIMARY KEY,
        player_name TEXT NOT NULL,
        team_abbreviation TEXT,
        age REAL,
        player_height REAL,
        player_weight REAL,
        college TEXT,
        country TEXT,
        draft_year INTEGER,
        draft_round INTEGER,
        draft_number INTEGER,
        gp INTEGER,            -- games played
        pts REAL,              -- points
        reb REAL,              -- rebounds
        ast REAL,              -- assists
        net_rating REAL,
        oreb_pct REAL,         -- offensive rebound percentage
        dreb_pct REAL,         -- defensive rebound percentage
        usg_pct REAL,          -- usage percentage
        ts_pct REAL,           -- true shooting percentage
        ast_pct REAL,          -- assist percentage
        season TEXT            -- storing as TEXT since it's in YYYY-YY format
    )
    """

    execute_sql_command(conn, create_table_ball)


def create_empty_sqlite_db(db_path=None):
    """Creates an empty SQLite database at the specified path.
    Errors out if a database already exists at that path.

    Parameters:
        path (str): The file path where the SQLite database will be created.

    """
    if not db_path:
        db_path = DB_PATH
    # Check if the file already exists
    if os.path.exists(db_path):
        raise FileExistsError(f"Database already exists at {db_path}")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Connect to the database (this will create it if it doesn't exist)
    conn = sqlite3.connect(db_path)

    # Close the connection immediately to keep it as an empty database
    conn.close()

    print(f"Database created at {db_path}")
    return True


def rm_db(db_path=None):
    """Delete the Database file
    not recoverable, be careful
    """
    if not db_path:
        db_path = DB_PATH

    if os.path.exists(db_path):
        os.remove(db_path)

    print(f"Database at {db_path} removed")

    return None


def create_and_load_basketball_data(csv_path, table_name):
    conn = create_db_connection()
    create_player_stats_table(conn)
    load_csv_to_db(conn, csv_path, table_name)


def add_player(player_info):
    conn = create_db_connection()
    query = """
    INSERT INTO player_stats
    (player_name, team_abbreviation, college, season)
    VALUES
    (?, ?, ?, '2022-23')
    """

    params = (
        player_info["player_name"],
        player_info["team"],
        player_info.get("college"),
        # '2022-23' is hardcoded in the query
    )

    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()


def delete_player(player_name):
    conn = create_db_connection()
    query = """
    DELETE FROM player_stats
    WHERE player_name = ?
    AND season = '2022-23'
    """

    params = (player_name,)

    cursor = conn.cursor()
    cursor.execute(query, params)

    if cursor.rowcount == 0:
        raise ValueError(f"No player found with name: {player_name}")

    conn.commit()
