FROM debian:jessie

MAINTAINER Lukas Nemec

RUN apt-get update
RUN apt-get install build-essential python3 python3-pip --yes

RUN mkdir -p /www/flask_workshop
# Kvuli setup.py (nacitame z readme description).
COPY README.md /www/flask_workshop
COPY db.sqlite /www/flask_workshop/
COPY *.py /www/flask_workshop/
COPY user /www/flask_workshop/user

RUN cd /www/flask_workshop; pip3 install .

# Nastavime aktualni pracovni adresar uvnitr projektu.
WORKDIR /www/flask_workshop/
# To je kuli sqlite DB, ktera ma relativni cestu a je uvnitr projektu.
CMD ["python3", "workshop.py"]
EXPOSE 5000