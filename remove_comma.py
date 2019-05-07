#!/anaconda3/bin/python3


with open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_tickets_withcomma.tsv', 'r') as infile, \
     open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_tickets.tsv', 'w') as outfile:
    data = infile.read()
    data = data.replace("円", "")
    #data = data.replace(",", "")

    outfile.write(data)

with open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_products_withcomma.tsv', 'r') as infile, \
     open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_products.tsv', 'w') as outfile:
    data = infile.read()
    data = data.replace("円", "")
    #data = data.replace(",", "")
    outfile.write(data)

with open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_services_withcomma.tsv', 'r') as infile, \
     open(r'/Users/samanvay/zed/sales_pred/mysql_data/note_services.tsv', 'w') as outfile:
    data = infile.read()
    data = data.replace("円", "")
    #data = data.replace(",", "")	
    outfile.write(data)

