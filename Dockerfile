FROM debian:stretch

LABEL maintainer="step21 <step21@devtal.de>"
ENV LANG C.UTF-8

ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid 
ENV APACHE_LOCK_DIR /var/lock/apache2 
ENV APACHE_LOG_DIR /var/log/apache2

RUN mkdir /web
WORKDIR /web

RUN apt-get update && apt-get install -y --no-install-recommends python3.5 apache2 libapache2-mod-wsgi-py3 python3-pip python3-setuptools python3-wheel

COPY ./ /web
RUN ls /web
RUN cd /web

RUN pip3 install -r /web/requirements-py3.txt

# Apache conf
RUN a2enmod wsgi rewrite

COPY poeticrelief-wsgi.conf /etc/apache2/sites-enabled/

EXPOSE 80

#ENTRYPOINT [ "python3" ]

#CMD [ "run.py" ]   	

CMD ["apache2", "-D", "FOREGROUND", "-e", "info"]