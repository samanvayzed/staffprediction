#!/bin/bash

PRED_HOME=/Users/samanvay/zed/sales_pred
MYSQL_PATH=/usr/local/mysql/bin/mysql

rm ${PRED_HOME}/mysql_data/*

${MYSQL_PATH} jtsboard_jts -uroot -p < ${PRED_HOME}/mysql_scripts/note_tickets.sql > ${PRED_HOME}/mysql_data/note_tickets.tsv

${MYSQL_PATH} jtsboard_jts -uroot -p < ${PRED_HOME}/mysql_scripts/note_products.sql > ${PRED_HOME}/mysql_data/note_products.tsv


${MYSQL_PATH} jtsboard_jts -uroot -p < ${PRED_HOME}/mysql_scripts/note_services.sql > ${PRED_HOME}/mysql_data/note_services.tsv

echo "reached here"
/usr/bin/sed 's/,//g' ${PRED_HOME}/mysql_data/note_tickets.tsv > ${PRED_HOME}/mysql_data/note_tickets1.tsv
/usr/bin/sed 's/,//g' ${PRED_HOME}/mysql_data/note_products.tsv > ${PRED_HOME}/mysql_data/note_products1.tsv
/usr/bin/sed 's/,//g' ${PRED_HOME}/mysql_data/note_services.tsv > ${PRED_HOME}/mysql_data/note_services1.tsv

/usr/bin/sed 's/円//g' ${PRED_HOME}/mysql_data/note_tickets1.tsv > ${PRED_HOME}/mysql_data/note_tickets.tsv
/usr/bin/sed 's/円//g' ${PRED_HOME}/mysql_data/note_products1.tsv > ${PRED_HOME}/mysql_data/note_products.tsv
/usr/bin/sed 's/円//g' ${PRED_HOME}/mysql_data/note_services1.tsv > ${PRED_HOME}/mysql_data/note_services.tsv


/usr/bin/sed 's/¥//g' ${PRED_HOME}/mysql_data/note_tickets.tsv > ${PRED_HOME}/mysql_data/note_tickets1.tsv
/usr/bin/sed 's/¥//g' ${PRED_HOME}/mysql_data/note_products.tsv > ${PRED_HOME}/mysql_data/note_products1.tsv
/usr/bin/sed 's/¥//g' ${PRED_HOME}/mysql_data/note_services.tsv > ${PRED_HOME}/mysql_data/note_services1.tsv

cat ${PRED_HOME}/mysql_data/note_tickets1.tsv | tr "\\t" "," > ${PRED_HOME}/mysql_data/note_tickets.csv
cat ${PRED_HOME}/mysql_data/note_products1.tsv | tr "\\t" "," > ${PRED_HOME}/mysql_data/note_products.csv
cat ${PRED_HOME}/mysql_data/note_services1.tsv | tr "\\t" "," > ${PRED_HOME}/mysql_data/note_services.csv

rm ${PRED_HOME}/mysql_data/*.tsv
