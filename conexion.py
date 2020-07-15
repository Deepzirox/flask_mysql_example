import pymysql

def startDataBase():
	db = pymysql.connect("localhost", "deep", "deepzirox", "example")
	cursor = db.cursor()
	return (db, cursor)

def insertUser(n, dc):
	query2 = f"""
	INSERT INTO Players(name) VALUES('{n}');
	"""
	dc[1].execute(query2)
	dc[0].commit()
	dc[0].close()

def getUsers(dc):
	getRows = """
	SELECT * FROM Players;
	"""

	dc[1].execute(getRows)

	rows = dc[1].fetchall()
	dc[0].close()
	return rows

def parseRows(tupUsers):
	ndict = {}
	for i in tupUsers:
		ndict.update({i[0] : i[1]})

	return ndict

