###########
# BUILDER #
###########

# pull official base image
FROM python:3.8-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install source packages dependencies
RUN apk add --update \
  build-base \
  cairo \
  cairo-dev \
  cargo \
  freetype-dev \
  gcc \
  gdk-pixbuf-dev \
  gettext \
  jpeg-dev \
  lcms2-dev \
  libffi-dev \
  musl-dev \
  openjpeg-dev \
  openssl-dev \
  pango-dev \
  poppler-utils \
  postgresql-client \
  postgresql-dev \
  py-cffi \
  python3-dev \
  rust \
  tcl-dev \
  tiff-dev \
  tk-dev \
  zlib-dev

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.8-alpine

# create directory for the app user
ENV APP_HOME=/home/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# create the app user
RUN addgroup -S app && adduser -S app -G app

# install dependencies
RUN apk update && apk add libpq libjpeg
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*
RUN rm -rf /wheels

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
# ENTRYPOINT ["/home/app/entrypoint.sh"]
