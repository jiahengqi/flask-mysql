FROM python:2.7.12

RUN echo "\
deb http://mirrors.163.com/debian/ jessie main non-free contrib \n\
deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib \n\
deb http://mirrors.163.com/debian/ jessie-backports main non-free contrib \n\
deb-src http://mirrors.163.com/debian/ jessie main non-free contrib \n\
deb-src http://mirrors.163.com/debian/ jessie-updates main non-free contrib \n\
deb-src http://mirrors.163.com/debian/ jessie-backports main non-free contrib \n\
deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib \n\
deb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib \n\
" > /etc/apt/sources.list


RUN apt-get update
RUN echo "mysql-server mysql-server/root_password password 123" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password 123" | debconf-set-selections
RUN apt-get install -y mysql-server
RUN apt-get install -y mysql-client 

RUN pip install --upgrade pip
RUN pip install Flask==1.0.2 \
    SQLAlchemy==1.2.9 \
    mysql-connector-python

WORKDIR /APP

ADD . /APP
RUN service mysql start && \
mysql -uroot -p123 -e \
"create database test;\
use test;\
create table if not exists t1 (user_name char(16),pwd char(16));\
insert into t1 value ('aaa','aa0'),('aab','aa1'),('aac','aa2'),('aad','aa3');" 
CMD /usr/bin/mysqld_safe & python app.py 


