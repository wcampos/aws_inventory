import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

conn = mysql.connector.connect(
    host=config['DB_CONFIG']['db_host'],
    port=3306,
    user=config['DB_CONFIG']['db_user'],
    password=config['DB_CONFIG']['db_password'],
    database=config['DB_CONFIG']['db_name']
)


def add_profile(in_name, in_access, in_secret):
    sql_statement = ("INSERT INTO profiles "
                     "(name, access_key, secret_key) "
                     "VALUES (%(name)s, %(access_key)s, %(secret_key)s)")

    data_profile = {
        'name': in_name,
        'access_key': in_access,
        'secret_key': in_secret,
    }

    try:
        cursor = conn.cursor()
        cursor.execute(sql_statement, data_profile)
        conn.commit()
        return_msg = "The profile " + in_name + " was added to the DB!"
    except mysql.connector.Error as err:
        return_msg = "Something went wrong! Refer to: {}".format(err)

    conn.close()
    print(return_msg)


def get_profiles():
    sql_statement = "select name from inventory.profiles"

    try:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        results = [''.join(q) for q in cursor.fetchall()]
    except mysql.connector.Error as err:
        results = "Something went wrong! Refer to: {}".format(err)
    conn.close()
    return results


def get_profile_params(in_name):
    sql_statement = "select name, access_key, secret_key from inventory.profiles where name = '" + in_name + "'"

    try:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        results = [q for q in cursor.fetchall()]
    except mysql.connector.Error as err:
        results = "Something went wrong! Refer to: {}".format(err)
    conn.close()
    print(results)


def profile_exists(in_name):
    profiles = get_profiles()
    if profiles.count(in_name) > 0:
        return_msg = "A profile with name: " + in_name + " already exists!"
    else:
        return_msg = "No profile found with this name!"
    print(return_msg)

# Test
# print(get_profiles())
# add_profile("vse-test1", "65d6a5da5d65a", "dahdhakdkasdas4d4sd4sd")
# profile_exists("vse-test2")
