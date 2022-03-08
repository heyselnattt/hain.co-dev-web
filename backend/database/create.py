import psycopg2

from data_models import Admin
from database.security import create_salt, encrypt_password
from database_operation import DatabaseOperator

pg_heroku = DatabaseOperator()
cursor = pg_heroku.get_cursor()


def add_admin_to_database(admin: Admin) -> Admin:
    salt = create_salt()
    encrypted_password = encrypt_password(admin.admin_password, salt)
    try:
        sql = """INSERT INTO hainco_admin(
                    admin_full_name, 
                    admin_username, 
                    admin_position, 
                    admin_is_active,
                    admin_password_salt,
                    admin_password_hash
                    ) VALUES(%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (admin.admin_full_name,
                             admin.admin_username,
                             admin.admin_position,
                             admin.admin_is_active,
                             salt,
                             encrypted_password))
        pg_heroku.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        return admin
