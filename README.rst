Mac os setup
------------

::

$ docker-machine restart default && eval $(docker-machine env default)
$ docker-machine ip default



Build container
---------------

::

$ docker run -d -p 3306:3306 -e MYSQL_PASS="mypass" clm/mysql_barebone



Run master and slave
--------------------

::

docker run -d -p 3306:3306        \
       -e REPLICATION_PASS="mypass"  \
    -e ON_CREATE_DB="scv"         \
    -e MYSQL_PASS="mypass"        \
    -e STARTUP_SQL="./init.sql"   \
    -e REPLICATION_MASTER="true"    \
    --name mysql   \
    sdia/mysql-barebone


docker run -d -p 3307:3306    \
    -e REPLICATION_SLAVE=true  \
    -e MYSQL_PASS="mypass"    \
    -e ON_CREATE_DB="scv"         \
    -e MYSQL_PASS="mypass"        \
    -e STARTUP_SQL="./init.sql"   \
    --link mysql:mysql   \
    sdia/mysql-barebone



Misc

mysql -u admin -p -h 192.168.99.100

docker rm $(docker ps -a -q) && \
docker rmi $(docker images -q)



docker restart mysql