#!/anaconda3/bin/python3

with open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_tickets_withyen.tsv', 'r') as infile, \
     open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_tickets_withcomma.tsv', 'w') as outfile:
    data = infile.read()
    data = data.replace("円", "")
    outfile.write(data)

with open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_products_withyen.tsv', 'r') as infile, \
     open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_products_withcomma.tsv', 'w') as outfile:
    data = infile.read()
    data = data.replace("円", "")
    outfile.write(data)

with open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_services_withyen.tsv', 'r') as infile, \
     open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_services_withcomma.tsv', 'w') as outfile:
    data = infile.read()
    data = data.replace("円", "")
    outfile.write(data)


