# install postgres timescaledb extension

## apt installation UBUNTU

https://docs.timescale.com/timescaledb/latest/how-to-guides/install-timescaledb/self-hosted/ubuntu/installation-apt-ubuntu/#installation-apt-ubuntu

sudo apt install timescaledb-2-postgresql-12 # postgresql-12 or postgresql-13 (version)

HINT: Please preload the timescaledb library via shared_preload_libraries.
This can be done by editing the config file at: /etc/postgresql/12/main/postgresql.conf
and adding 'timescaledb' to the list in the shared_preload_libraries config. # Modify postgresql.conf:
shared_preload_libraries = 'timescaledb'

## Post installation setup

https://docs.timescale.com/timescaledb/latest/how-to-guides/install-timescaledb/post-install-setup/

psql -U postgres -h localhost
\c database
CREATE EXTENSION IF NOT EXISTS timescaledb;

## Add Hypertable (special index for timeseries to an existing table)

https://docs.timescale.com/timescaledb/latest/getting-started/create-hypertable/

SELECT create_hypertable('site_yahoos','pub_date', migrate_data=>'true');
SELECT create_hypertable('tweets','tweet_dt');

## APPLICATION INSTALLATION

# CALL SAMPLE

http://localhost:8101/tweets?symbol=AAPL&from_dt=2021-10-4 12:11:30

# API application

python3 app.py

## dependency

None
