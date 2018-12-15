'gcloud sql instances describe test'  
gets instance details (connectionName to connect to database)  

./cloud_sql_proxy -instances="vm-testing-219509:europe-west2:table"=tcp:3305 -credential_file="../.gcpkey/key.json" &  
Create connection to database - runs in background  
