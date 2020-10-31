import psycopg2
import pandas as pd
import sys

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        # print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    # print("Connection successful")
    return conn


def postgresql_to_dataframe(conn, select_query):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    column_names = [ x.name for x in cursor.description]
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples,columns=column_names)
    return df

import allure
def step_query_db(param_dic, select_query):
    conn = connect(param_dic)
    # column_names = ["user_id", "email", "fullname"]
    # Execute the "SELECT *" query
    df = postgresql_to_dataframe(conn, f"select * from users")
    allure.attach(df.head().to_html(),select_query,allure.attachment_type.HTML)
