import sys
import os
import sqlite3
import gzip

def main():
	output_dir = os.path.dirname(__file__) + '/output'
	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)
	con = sqlite3.connect(sys.argv[1])
	cur = con.cursor()
	for row in cur.execute("select Z_PK, ZDATA from ZICNOTEDATA where ZDATA is not null"):
		data = gzip.decompress(row[1])
		string = data.decode('utf-8', errors='ignore')
		# Cut off header
		string = string[12:]
		# Find where content ends
		offset = 0
		for ch in string:
			if ch.isprintable() or ch.isspace() or ch == '￼':
				offset += 1
			else:
				break
		string = string[0:offset]
		first_line = string.partition('\n')[0]
		filename = "{} - {}".format(row[0], first_line[:20])
		with open(os.path.join(output_dir, filename), 'w') as file:
			file.write(string)
		print(filename)

if __name__ == '__main__':
	main()
