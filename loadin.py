import mysql.connector
import boto
import timeit
from subprocess import call



access=''
secret=''
entered =""
s3conn = boto.connect_s3(aws_access_key_id=access,aws_secret_access_key=secret)

conn = mysql.connector.connect(user='', password='',
                               host='',
                               database='')

cur = conn.cursor()
def loadfroms3():
    bucket_cont=s3conn.get_bucket('aj-bucket1')
    for key in bucket_cont:
        if key.name == entered:
            tempkey=key
    start_time = timeit.default_timer()
    tempkey.get_contents_to_filename('weather.csv')
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    print 'time taken to load file into s3  =  '+str(total_time)


def createquery():
    query = "CREATE TABLE `weather` (`Country or Territory` text,`Station Name` text, `WMO Station Number` int(11) DEFAULT NULL,  `Unit` text,  `Jan` double DEFAULT NULL,  `Feb` double DEFAULT NULL,  `Mar` double DEFAULT NULL,  `Apr` double DEFAULT NULL,  `May` double DEFAULT NULL,  `Jun` double DEFAULT NULL,  `Jul` double DEFAULT NULL,  `Aug` double DEFAULT NULL,  `Sep` double DEFAULT NULL,  `Oct` double DEFAULT NULL,  `Nov` double DEFAULT NULL,  `Dec` double DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    start_time = timeit.default_timer()
    cur.execute(query)
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    print 'time taken to create table  =  '+str(total_time)

def loaddataintotable():
    start_time = timeit.default_timer()
    call('sh load.sh', shell=True)
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    print 'time taken to load file into table  =  ' + str(total_time)

def find_max():
    start_time = timeit.default_timer()
    query ="select  max(mar) as max_mar,max(jun)as max_jun,min(mar) as min_mar,min(jun)as min_jun from weather"
    cur.execute(query)
    rows=cur.fetchall()
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    print 'time taken to find max  =  ' + str(total_time)


def user_val():
    max = raw_input("Enter max value \n")
    start_time = timeit.default_timer()
    #query ="select count(mar),count(jun) from weather where mar<=%s and jun<=%s",(max,max)
    #print query
    count=0
    cur.execute("select count(mar),count(jun) from weather where mar<=%s and jun<=%s",(max,max))
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    rows = cur.fetchall()
    for r in rows:
        print r[0]
    print 'time taken to find max  =  ' + str(total_time)

def sum():
    max = raw_input("Enter max value \n")
    start_time = timeit.default_timer()
    #query ="select count(mar),count(jun) from weather where mar<=%s and jun<=%s",(max,max)
    #print query
    count=0
    cur.execute("update  weather set jan=(mar+jun) where  mar<=%s and jun<=%s",(max,max))
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    print 'time taken to find max  =  ' + str(total_time)




choice=raw_input("Enter your choice \n1.load csv from s3 \n2.Creaete Table\n3.findmax \n4.user max valu\n5 Eight")
if int(choice) == 1:
    #no_memcache()
    loadfroms3()
elif int(choice) == 2:
    loaddataintotable()

elif int(choice) == 3:
    find_max()

elif int(choice) == 4:
    user_val()

elif int(choice) == 5:
    sum()
else:
    print "Enter correct choice"
cur.close()
conn.close()


