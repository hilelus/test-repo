import cx_Oracle

if __name__ == '__main__':
	
		connection = cx_Oracle.connect('scott/tiger@oca11')
		
		cursor = connection.cursor()
		cursor.execute('select * from user_tables')
		
		print connection.version, ' ' ,connection.version.split('.')
		
		idx = 1
		for row in cursor.fetchall():
			#print 'row = ',row['table_name']
			print '\n\nRow #',str(idx)
			print '\n'
			for col in row:
				print col,
			#print row
			#pass
			idx += 1
		
		cursor.close()
		connection.close()