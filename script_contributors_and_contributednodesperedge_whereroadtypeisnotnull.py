import csv, psycopg2, operator

connection = psycopg2.connect("host='localhost' dbname='zia_turkey_edge' user='postgres' password='zia123'")
cursor1 = connection.cursor()
    
with open('/home/administrator/zia/NewTurkeySlices/Edge/count_contributors_and_contributingnodesperedge_wherehighwayisnotnull.csv', 'wb') as f:    
    writer = csv.writer(f, delimiter = ',')
    data = ['seasons_in_number', 'seasons_in_text', 'contributor_user_id', 'counts_nodesconstitutingedge_bythatuser_extraadded']
    writer.writerow(data)

    # Range is from 1 to 88 to cover all the Provinces
    for i in range(1, 88):
        data = [i]
        writer.writerow(data)
        print i
        seasons = ['april_seven','sep_seven','april_eight','sep_eight','april_nine','sep_nine','april_ten','sep_ten','april_eleven','sep_eleven','april_twelve','sep_twelve','april_thirteen','sep_thirteen','april_fourteen','sep_fourteen','april_fifteen','sep_fifteen']
        valid = ['2004-04-01 00:00:00','2007-04-01 00:00:00','2007-09-01 00:00:00','2008-04-01 00:00:00','2008-09-01 00:00:00','2009-04-01 00:00:00','2009-09-01 00:00:00','2010-04-01 00:00:00','2010-09-01 00:00:00','2011-04-01 00:00:00','2011-09-01 00:00:00','2012-04-01 00:00:00','2012-09-01 00:00:00','2013-04-01 00:00:00','2013-09-01 00:00:00','2014-04-01 00:00:00','2014-09-01 00:00:00','2015-04-01 00:00:00','2015-09-01 00:00:00']
        sumall = 0

        for j in range(0, 18):
            sql = "SELECT 1 FROM information_schema.tables WHERE  table_schema = 's%s' AND table_name = '%s'" % (i, seasons[j])
            cursor1.execute(sql)
            xxx = 0
            for result in cursor1:
                xxx = 1
                if result[0] == 1:
                    sql = "select user_id, st_dumppoints(geom) as dump1 from s%s.%s where road_type is not null" % (i, seasons[j])
                    cursor1.execute(sql)
                    user_count = dict()
                    for result in cursor1:
                        key = int(result[0])
                        if key in user_count:
                            user_count[key] += 1
                        else:
                            user_count[key] = 1
		    # The following new sorted user_count is tuple now, not the dictionary
		    user_count = sorted(user_count.items(), key=operator.itemgetter(1), reverse=True)
		    print user_count
                    data = [j+1, seasons[j]]
                    writer.writerow(data)
		    for key1, value1 in user_count:
                        data = ["", "", key1, value1]
                        writer.writerow(data)
            if xxx == 0:
                data = [j+1, seasons[j]]
                writer.writerow(data)
print "done!"





                    




                
