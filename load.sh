#!/bin/bash
mysql -u arjun -h dburl --password=dbpassword --local_infile=1  << EOF
LOAD DATA local INFILE 'weather.csv' INTO TABLE weather FIELDS TERMINATED BY ',' ENCLOSED BY '\"' lines terminated by '\n' Ignore 1 lines;
commit;
EOF

