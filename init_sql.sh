#!/bin/bash

/usr/bin/mysqld_safe &
sleep 5
mysql -uroot -p123 -e \
"create database test;\
use test;\
create table if not exists t2 (idx char(16),val char(16));\
insert into t2 value ('aaa','aa0'),('aab','aa1'),('aac','aa2'),('aad','aa3');"
jobs
tail -f /etc/hosts