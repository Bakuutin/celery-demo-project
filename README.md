# Demo celery project

## Usage

```bash
get_random_string() {
    tr -dc A-Za-z0-9 < /dev/urandom | head -c 32
}

# create required variables
cat << EOF > .env
USER_GID=1000
SECRET_KEY=$(get_random_string)
POSTGRES_PASSWORD=$(get_random_string)
RABBITMQ_DEFAULT_PASS=$(get_random_string)
EOF

docker-compose up -d postgres
docker-compose run --rm app ./manage.py migrate
docker-compose up -d
```

Open [http://localhost:8000/reports]

## Optional: install packages locally

```bash
pipenv --python 3.9
pipenv install
set -o allexport; source .env; set +o allexport  # load .env content to current terminal
./manage.py check
```
