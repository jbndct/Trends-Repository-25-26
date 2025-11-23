from core.db import DB
from models.model import Wrestler

class WrestlerRepository:
  def create(self, wrestler: Wrestler):
    conn = DB.get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO wrestlers (name, age) VALUES (%s, %s)",
                  (wrestler.name, wrestler.age)
    )
    conn.commit()
    conn.close()

  def get_all(self):
    conn = DB.get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM wrestlers")
    rows = cursor.fetchall()
    conn.close()
    return [Wrestler(**r) for r in rows]