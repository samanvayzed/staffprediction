#!/bin/bash

PRED_HOME=/Users/samanvay/zed/sales_pred

/usr/bin/sed 's/,//g' ${PRED_HOME}/mysql_data/note_tickets.tsv > ${PRED_HOME}/mysql_data/note_tickets1.tsv 
/usr/bin/sed 's/,//g' ${PRED_HOME}/mysql_data/note_products.tsv > ${PRED_HOME}/mysql_data/note_products1.tsv
/usr/bin/sed 's/,//g' ${PRED_HOME}/mysql_data/note_services.tsv > ${PRED_HOME}/mysql_data/note_services1.tsv

/usr/bin/sed 's/円//g' ${PRED_HOME}/mysql_data/note_tickets1.tsv > ${PRED_HOME}/mysql_data/note_tickets.tsv
/usr/bin/sed 's/円//g' ${PRED_HOME}/mysql_data/note_products1.tsv > ${PRED_HOME}/mysql_data/note_products.tsv
/usr/bin/sed 's/円//g' ${PRED_HOME}/mysql_data/note_services1.tsv > ${PRED_HOME}/mysql_data/note_services.tsv


/usr/bin/sed 's/¥//g' ${PRED_HOME}/mysql_data/note_tickets.tsv > ${PRED_HOME}/mysql_data/note_tickets1.tsv  
/usr/bin/sed 's/¥//g' ${PRED_HOME}/mysql_data/note_products.tsv > ${PRED_HOME}/mysql_data/note_products1.tsv
/usr/bin/sed 's/¥//g' ${PRED_HOME}/mysql_data/note_services.tsv > ${PRED_HOME}/mysql_data/note_services1.tsv
