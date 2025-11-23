from mysql.connector import pooling

class DB:
  _pool = pooling.MySQLConnectionPool(
    pool_size=5,
    host = "localhost",
    user = "root",
    password = "",
    database = "db"
  )

  @staticmethod
  def get_conn():
    return DB._pool.get_connection()