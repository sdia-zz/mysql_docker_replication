Mac os setup
------------

.. code::

  $ docker-machine restart default && eval $(docker-machine env default)
  $ docker-machine ip default



Build container
---------------

.. code::

  $ docker run -d -p 3306:3306 -e MYSQL_PASS="mypass" clm/mysql_barebone



Run master and slave
--------------------

Master ...


.. code::

  docker run -d -p 3306:3306        \
    -e REPLICATION_PASS="mypass"    \
    -e ON_CREATE_DB="scv"           \
    -e MYSQL_PASS="mypass"          \
    -e STARTUP_SQL="./init.sql"     \
    -e REPLICATION_MASTER="true"    \
    --name mysql                    \
    sdia/mysql-barebone


Slave ...


.. code::
  docker run -d -p 3307:3306      \
    -e REPLICATION_SLAVE=true     \
    -e MYSQL_PASS="mypass"        \
    -e ON_CREATE_DB="scv"         \
    -e MYSQL_PASS="mypass"        \
    -e STARTUP_SQL="./init.sql"   \
    --link mysql:mysql            \
    sdia/mysql-barebone



Misc
----

.. code::

  mysql -u admin -p -h 192.168.99.100


.. code::
  docker rm $(docker ps -a -q) && \
  docker rmi $(docker images -q)


.. code::
  docker restart mysql