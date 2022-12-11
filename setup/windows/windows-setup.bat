::    ██╗    ██╗██╗   ██╗ █████╗ ██╗     
::    ██║    ██║██║   ██║██╔══██╗██║     
::    ██║ █╗ ██║██║   ██║███████║██║     (code by WUAL)
::    ██║███╗██║██║   ██║██╔══██║██║     
::    ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
::    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝  

echo off

:: Pip Installs

python conf-script.py

:: MySQL Conf

set/p user= Write your MySQL user:
set/p password= Write your MySQL password:
set database = "mlp"

mysql -h localhost -u %user% -p %password% -e 'CREATE DATABASE %mlp%'
mysql -h localhost -u %user% -p %password% -e 'SHOW TABLES FROM mlp'
mysql -h localhost -u %user% -p %password% -e 'CREATE TABLE vault (site VARCHAR(255), usser VARCHAR(255), password VARCHAR(255))'

set msql_example1= "site_example"
set msql_example2= "user_example"
set msql_example3= "password_example"

mysql -h localhost -u %user% -p %password% -e 'INSERT INTO clientes (site, usser, password) VALUES (%msql_example1%, %msql_example2%, %msql_example3%)'

exit
