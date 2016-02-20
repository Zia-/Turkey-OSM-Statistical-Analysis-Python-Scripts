import csv
import psycopg2

connection = psycopg2.connect("host='localhost' dbname='zia_turkey_edge' user='postgres' password='zia123'")
cursor1 = connection.cursor()
    
with open('/home/administrator/zia/NewTurkeySlices/Edge/count_nodesconstitutinghighways_wherehighwayisnotnull.csv', 'wb') as f:    
    writer = csv.writer(f, delimiter = ',')
    data = ['seasons_in_number', 'seasons_in_text', 'count_nodesconstitutinghighways_wherehighwayisnotnull_extraadded', 'count_nodesconstitutinghighways_wherehighwayisnotnull_addedaccumulated']
    writer.writerow(data)
    for i in range(1, 88):
        data = [i]
        writer.writerow(data)
        print i
        seasons = ['april_seven','sep_seven','april_eight','sep_eight','april_nine','sep_nine','april_ten','sep_ten','april_eleven','sep_eleven','april_twelve','sep_twelve','april_thirteen','sep_thirteen','april_fourteen','sep_fourteen','april_fifteen','sep_fifteen']
        sumall = 0
        
        #calculate area in km2
        sql = "select st_area(geom)*10000 from turkey_districts900913 where gid = %s" % (i)
        cursor1.execute(sql)
        for area in cursor1:
            area = area[0]
        
        for j in range(0,18):
            sql = "SELECT 1 FROM information_schema.tables WHERE  table_schema = 's%s' AND table_name = '%s'" % (i, seasons[j])
            cursor1.execute(sql)
            xxx = 0
            for result in cursor1:
                xxx = 1
                if result[0] == 1:
                    sql = "with dumppoints as (select st_dumppoints(geom) from s%s.%s where road_type is not null) select count(*) from dumppoints" % (i, seasons[j])
                    cursor1.execute(sql)
                    for result in cursor1:
                        result = (result[0]/area)
                        sumall = sumall + result
                        data = [j+1, seasons[j], result, sumall]
                        writer.writerow(data)
                        print j+1, seasons[j], result, sumall
            if xxx == 0:
                data = [j+1, seasons[j], 0, sumall]
                writer.writerow(data)
                print j+1, seasons[j], 0, sumall

print "done!!"

        
        








