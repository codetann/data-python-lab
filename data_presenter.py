from util import cupcake_store

# Process Data
csv_file = open('Cupcakeinvoices.csv')

for line in csv_file:
    line = line.rstrip('/n').split(',')
    
    # - creates invoice and add the totals to the day total and flavor total
    cupcake_store.create_invoice(line)

# Present Data
cupcake_store.bar_graph()

# Close File
csv_file.close()





