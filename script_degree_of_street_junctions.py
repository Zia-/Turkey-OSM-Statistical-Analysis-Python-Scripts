import csv, psycopg2, operator

connection = psycopg2.connect("host='__host_name__' dbname='__database_name_' user='__database_user_name__' password='__database_password__'")
cursor1 = connection.cursor()

with open('path_to_a_file_where_results_will_get_stored_along_with_the_file_name_in_csv_format', 'wb') as f:
	writer = csv.writer(f, delimiter= ',')
	data = ['seasons_in_number', 'seasons_in_text', 'degree', 'frequency_total']
	writer.writerow(data)

	# Range is from 1 to 88 to cover all the Provinces
	for i in range(1, 88):
		data = [i]
		writer.writerow(data)
		print i
		seasons = ['april_seven','sep_seven','april_eight','sep_eight','april_nine','sep_nine','april_ten','sep_ten','april_eleven','sep_eleven','april_twelve','sep_twelve','april_thirteen','sep_thirteen','april_fourteen','sep_fourteen','april_fifteen','sep_fifteen']	
		valid = ['2004-04-01 00:00:00','2007-04-01 00:00:00','2007-09-01 00:00:00','2008-04-01 00:00:00','2008-09-01 00:00:00','2009-04-01 00:00:00','2009-09-01 00:00:00','2010-04-01 00:00:00','2010-09-01 00:00:00','2011-04-01 00:00:00','2011-09-01 00:00:00','2012-04-01 00:00:00','2012-09-01 00:00:00','2013-04-01 00:00:00','2013-09-01 00:00:00','2014-04-01 00:00:00','2014-09-01 00:00:00','2015-04-01 00:00:00','2015-09-01 00:00:00']
	
		for j in range(0, 18):	
			data = [j+1, seasons[j]]
			writer.writerow(data)
			print i, j
			sql = "SELECT 1 FROM information_schema.tables WHERE table_schema = 's%s' AND table_name = '%s'" % (i, 'turkeylinedates')
			cursor1.execute(sql)
			xxx=0
			for result in cursor1:
				xxx = 1
				if result[0] == 1:
					sql = "with l as (select * from s%s.turkeylinedates where valid_from "\
						"between '2004-04-01 00:00:00' and '%s'), s as (select t.source, t.target, t.geom from "\
						"s%s.turkeylinetopology_ways as t, l where "\
						"st_intersects(l.geom, t.geom)) "\
						"select distinct * from s" % (i, valid[j+1], i)

					cursor1.execute(sql)
					datasource = list()
					datatarget = list()
					for result in cursor1:
						datasource.append(result[0])
						datatarget.append(result[1])
					datamerged = list()
					datamerged = datasource + datatarget
					
					frequencydata = dict()
					for k in range(len(datamerged)):
						key = int(datamerged[k])
						if key in frequencydata:
							frequencydata[key] += 1
						else:
							frequencydata[key] = 1
						
					frequencydata = sorted(frequencydata.items(), key=operator.itemgetter(1), reverse=True)
					finalfreqdata = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
					for l in range(len(frequencydata)):
						key = int(frequencydata[l][1])
						if key in finalfreqdata:
							finalfreqdata[key] += 1
						else:
							print "Found higher degree"

					finalfreqdata = sorted(finalfreqdata.items(), key=operator.itemgetter(0), reverse=False)
					for key1, value1 in finalfreqdata:
						data = ["", "", key1, value1]
						writer.writerow(data)
			if xxx == 0:
				data = [j+1, seasons[j]]
				writer.writerow(data)

print "done!"		





