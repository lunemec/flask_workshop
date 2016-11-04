FROM debian:jessie

MAINTAINER Lukas Nemec

RUN apt-get update
# Pro UWSGI BACHA! na uwsgi-plugin-python3!
RUN apt-get install build-essential python3 python3-pip nginx uwsgi uwsgi-plugin-python3 --yes

RUN mkdir -p /www/flask_workshop
# Kvuli setup.py (nacitame z readme description).
COPY README.md /www/flask_workshop
COPY db.sqlite /www/flask_workshop/
COPY *.py /www/flask_workshop/
COPY user /www/flask_workshop/user

RUN cd /www/flask_workshop; pip3 install .

# Smazat default nginx configy.
RUN rm /etc/nginx/sites-enabled/default
# Nakopirovat NginX config.
COPY nginx.conf /etc/nginx/sites-enabled/nginx.conf

# Nakopirovat spousteci skript.
COPY run.sh /www/flask_workshop/

# Nastavime aktualni pracovni adresar uvnitr projektu.
# To je kuli sqlite DB, ktera ma relativni cestu a je uvnitr projektu.
WORKDIR /www/flask_workshop/
CMD ["bash", "run.sh"]
EXPOSE 80