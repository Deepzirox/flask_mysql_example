import pymysql

db = pymysql.connect("localhost", "deep", "deepzirox", "example")

cursor = db.cursor()

query = """
CREATE TABLE Players(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256)
);
"""

query2 = """
INSERT INTO Players(name) VALUES("ANdres");
"""

getRows = """
SELECT * FROM Players;
"""

cursor.execute(getRows)

rows = cursor.fetchall()

ndict = {}

for r in rows:
	ndict.update({r[0] : r[1]})

print(ndict)



#db.commit()
db.close()