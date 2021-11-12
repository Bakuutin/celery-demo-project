FROM python:3.9
RUN groupadd -g "${USER_GID:-1000}" dockeruser && useradd -r -u "${USER_GID:-1000}" -g dockeruser -s /bin/sh -d /srv dockeruser
WORKDIR /srv
RUN pip install -U pip pipenv

COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock
RUN pipenv install --deploy --system --ignore-pipfile

USER dockeruser
EXPOSE 8000
