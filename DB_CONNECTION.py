import pyodbc

class DB:
    def __init__(self):
        print("Connecting to the database...")
        self.conn = pyodbc.connect(
            "DRIVER={SQL Server};" \
            "SERVER=ABDELRAHMANMANS;" \
            "DATABASE=universty 4;" \
            "Trusted_Connection=yes;TrustServerCertificate=yes"
        )
        self.cur = self.conn.cursor()
        print("Connection successful.")

    def run(self, q, p=None):
        print(f"Running query: {q}")
        self.cur.execute(q, p or [])
        self.conn.commit()
        print("Query executed.")

    def all(self, q, p=None):
        print(f"Fetching all results for query: {q}")
        self.cur.execute(q, p or [])
        result = self.cur.fetchall()
        print(f"Fetched {len(result)} row(s).")
        return result

    def one(self, q, p=None):
        print(f"Fetching one row for query: {q}")
        self.cur.execute(q, p or [])
        result = self.cur.fetchone()
        if result:
            print("One row fetched.")
        else:
            print("No results found.")
        return result

    def close(self):
        self.cur.close()
        self.conn.close()
        print("Connection closed.")
DB = DB()