import pymysql

def CreateTable(tableName):
	#database connection
	connection = pymysql.connect(host="localhost", user="root", passwd="", database="onglocvlog")
	cursor = connection.cursor()
	# Query for creating table
	ArtistTableSql = "CREATE TABLE " +tableName+"""(
	CODE INT(10) PRIMARY KEY AUTO_INCREMENT,
	PRODUCER CHAR(200) NOT NULL,
	CATEGORY CHAR(200) NOT NULL,
	NAME  CHAR(200) NOT NULL,
	ORIGINAL_COST FLOAT(10) NOT NULL,
	SALE_COST FLOAT(10) NOT NULL,
	IMAGE_URL CHAR(200) NOT NULL,
	RATING FLOAT(10)NOT NULL
	)"""

	cursor.execute(ArtistTableSql)
	connection.close()

def DeleteTable(tableName):
	connection = pymysql.connect(host="localhost", user="root", passwd="", database="onglocvlog")
	cursor = connection.cursor()
	dropSql = "DROP TABLE IF EXISTS "+tableName+";"
	cursor.execute(dropSql)
	connection.close()

def InsertItem(tableName, PRODUCER, CATEGORY, NAME, ORIGINAL_COST, SALE_COST, IMAGE_URL, RATING):
	connection = pymysql.connect(host="localhost", user="root", passwd="", database="onglocvlog")
	cursor = connection.cursor()
	# queries for inserting values
	#insert = "INSERT INTO "+tableName+"(PRODUCER, CATEGORY, NAME, ORIGINAL_COST, SALE_COST, IMAGE_URL, RATING) "+"VALUES({},{},{},{},{},{},{});".format(PRODUCER, CATEGORY, NAME, ORIGINAL_COST, SALE_COST, IMAGE_URL, RATING)

	insert = "INSERT INTO "+tableName+"(PRODUCER, CATEGORY, NAME, ORIGINAL_COST, SALE_COST, IMAGE_URL, RATING) "
	insert1 = "VALUES('"+PRODUCER+"','"+CATEGORY+"','"+NAME+"','"+str(ORIGINAL_COST)+"','"+str(SALE_COST)+"','"+IMAGE_URL+"','"+str(RATING)+"');"
	cursor.execute(insert+insert1)

	#commiting the connection then closing it.
	connection.commit()
	connection.close()
	
def SelectAll(tableName):
	connection = pymysql.connect(host="localhost", user="root", passwd="", database="onglocvlog")
	cursor = connection.cursor()
	retrive = "Select * from "+tableName

	#executing the quires
	cursor.execute(retrive)
	rows = cursor.fetchall()
	connection.close()
	return rows

def SelectCodeColumm(tableName):
	connection = pymysql.connect(host="localhost", user="root", passwd="", database="onglocvlog")
	cursor = connection.cursor()
	retrive = "Select CODE from "+tableName

	#executing the quires
	cursor.execute(retrive)
	rows = cursor.fetchall()
	connection.close()
	return rows

def SelectProducerColumm(tableName):
	connection = pymysql.connect(host="localhost", user="root", passwd="", database="onglocvlog")
	cursor = connection.cursor()
	retrive = "Select PRODUCER from "+tableName

	#executing the quires
	cursor.execute(retrive)
	rows = cursor.fetchall()
	connection.close()
	return rows

def SelectCategoryColumm(tableName):
	connection = pymysql.connect(host="localhost", user="root", passwd="", database="onglocvlog")
	cursor = connection.cursor()
	retrive = "Select CATEGORY from "+tableName

	#executing the quires
	cursor.execute(retrive)
	rows = cursor.fetchall()
	connection.close()
	return rows