FROM debian:stretch

LABEL maintainer="step21 <step21@devtal.de>"
ENV LANG C.UTF-8

RUN mkdir /web;mkdir /web/poeticrelief
WORKDIR /web/poeticrelief

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y python3.5 apache2 libapache2-mod-wsgi-py3 python3-pip python3-setuptools python3-wheel sqlite3 curl && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./ /web/poeticrelief

RUN pip3 install -r /web/poeticrelief/requirements-py3.txt

# Apache conf
RUN a2enmod wsgi rewrite

COPY poeticrelief-wsgi.conf /etc/apache2/sites-available/

RUN a2ensite poeticrelief-wsgi

RUN curl --output /web/poeticrelief/poerelief/teidb_dev.sqlite https://chaostal.de/~step21/teidb_dev.sqlite

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND", "-e", "info"]
