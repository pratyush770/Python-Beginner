import psycopg2

con = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pratyush")

cur = con.cursor()

#cur.execute("insert into employee (eid, ename , address ) values (%s, %s, %s)", (13412,"Rohan","Hadapsar Pune"))
#cur.execute("insert into employee (eid, ename , address ) values (%s, %s, %s)", (13419,"Aditya","Range hills"))
#cur.execute("delete from employee where eid = 13412")
cur.execute("select eid, ename, address from employee")


rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name {r[1]} address {r[2]}")


con.commit()

cur.close()

con.close()