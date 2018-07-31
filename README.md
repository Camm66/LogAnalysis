
# Log Analysis Project
This project is a report generating tool that queries the database of a mock newspaper site. It operates from the command line to report the following metrics in a plain text format:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## The Data
The queries presented in this module rely on the following data: [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Linux VM Installation
This module operates on a PostgreSQL Database Server provided by a Linux Virtual Machine. Setup can be performed via the steps below.

#### 1. Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system.

#### 2. Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download and install the version for your operating system [here.](https://www.vagrantup.com/downloads.html)

#### 3. Download the VM configuration
Download and unzip the following: [FSND-Virtual-Machine.zip.](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
Inside of this directory is another called vagrant. `cd` into vagrant and enter the command, `vagrant up`, to download and install the Linux operating system.

Once the installation concludes, run `vagrant ssh` to run the the newly installed VM.

## Running the database
Once the VM has been installed, `cd` into the `vagrant` directory and load the data from 'newsdata.sql' with the following command:
* `psql -d news -f newsdata.sql.`

These commands perform the following:
* `psql` — the PostgreSQL command line program
* `-f newsdata.sql` — run the SQL statements in the file _newsdata.sql_
* `-d news` — connect to the database named news which this module operate on.

Explore the data with the following:
* `\dt` — display tables — lists the tables that are available in the database.
* `\d table` — (replace table table name) — shows the database schema for that particular table.

Table names for this database: _articles_, _authors_, _log_

## Create VIEWs

The **get_days_with_most_errors()** module relies on the creation of the following
views in the psql terminal:

```
CREATE VIEW err AS
SELECT DATE(time) AS date, count(status) AS num
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY date;
```

```
CREATE VIEW ok AS
SELECT DATE(time) AS date, count(status) AS num
FROM log
WHERE status = '200 OK'
GROUP BY date;
```


## License
License information is available in the LICENSE.txt file.
# LogAnalysis
