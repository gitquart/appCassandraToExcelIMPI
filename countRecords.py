import database as db


query='select id from thesis.impi_docs_master where year=2020'
db.getLargeQuery(query)



