#!/bin/bash
mysql -u arjun -h dbURL --password=dbpassword --local_infile=1 << EOF
LOAD DATA local INFILE 'md.csv' INTO TABLE md FIELDS TERMINATED BY ',' ENCLOSED BY '\"' lines terminated by '\n' Ignore 1 lines;
commit;
EOF