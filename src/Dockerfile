FROM python:3.8-alpine

ARG USER=challenge1
ENV HOME /home/$USER

# install sudo as root
RUN apk add --update sudo

# add new user
RUN adduser -D $USER \
        && echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER \
        && chmod 0440 /etc/sudoers.d/$USER

USER $USER
WORKDIR $HOME

COPY requirements.txt requirements.txt
COPY app.py app.py

RUN pip install -r requirements.txt

CMD ["python","app.py"]
