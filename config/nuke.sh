#!/bin/bash

echo Dropping the Database
psql -c "DROP DATABASE pdnj;"

echo Creating the Database
psql -c "CREATE DATABASE pdnj WITH OWNER $USER;"

echo Giving Permissions
psql -c "GRANT ALL PRIVILEGES ON DATABASE pdnj TO cagywpagoe;"
