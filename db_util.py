import psycopg2

## TODO: change DB paramters
db_host = `aws rds describe-db-instances |\
     jq -r '.DBInstances[]|select(.DBInstanceIdentifier=="postgresforlambdatest").Endpoint|.Address'`
db_port = 5432
db_name = "dbname"
db_user = "username"
db_pass = "password"
db_table = "tablename"


def make_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print "I am unable to connect to the database"
    return conn


def save_data(conn, query):
    cursor = conn.cursor()
    cur.execute(query)
    conn.commit()

    return 
