FROM ubuntu:16.04
# Installation:
# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
# Update apt-get sources AND install MongoDB
RUN apt-get update && apt-get install -y mongodb-org
RUN mkdir -p /data/db
RUN apt-get install git -y

RUN git clone https://github.com/HydraData/core.git
RUN mv ./core/* ./

RUN apt-get install python -y
RUN apt-get install python-pip -y
RUN apt-get install python-numpy -y
RUN apt-get install python-scipy -y
RUN pip install scikit-learn

RUN pip install telegram
RUN pip install git+https://github.com/python-telegram-bot/python-telegram-bot.git
RUN pip install pymongo
RUN pip install pandas

#RUN python Profiler.py

EXPOSE 443


