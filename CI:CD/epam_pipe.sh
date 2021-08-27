#!/bin/bash
#
# Performs simple CI:CD Pipeline


set -eu

REPO="${1:-$'https://github.com/Kolyavolkov/epam'}" # Copy URL to your repo
PIPE="${2:-$'EPAM'}" # Directory name where you want to keep cloned repo
APP_FILE="${3:-$'app.py'}" # File to be lintered
BUILD_DIR="${4:-$'my_flask_app'}" # Dir with docker file
SECRET="${5:-$'/Users/volkov/Documents/Gitrepo/Docker/my_flask_app/.env'}" # Path to .env file
TAG="$(git tag)"

####
# Finds file you want to check and executes pylint
####

function linter() {
  find . -name "$APP_FILE" | xargs pylint --exit-zero
}


####
# Builds image and pushes it to docker hub repo
####

function build_image() {
  cd "$(find . -type d -name $BUILD_DIR)"
  docker build -t kolyavolkov/my_flask_app:latest -t kolyavolkov/my_flask_app:$TAG .
}

function push_image() {
  docker push kolyavolkov/my_flask_app:latest
  docker push kolyavolkov/my_flask_app:$TAG
}

function dock_comp() {
  docker-compose --env-file "$SECRET" up -d
}

####
# Checks if remote repo is available locally, if not creates dir named $PIPE 
# at current working dir and clones repo there.
# When repo is available localy runs pylint and docker build if version differs
####

function pull_repo() {
  echo -e "Pulling from remote repository \xe2\x9c\x85"
  
  if [[ ! -d "./$PIPE" ]]; then
      git clone $REPO
  fi

  git -C ./$PIPE pull > /dev/null
  touch .lastcommit
  PIPE_LAST_COMMIT=$(cat .lastcommit)
  PIPE_REAL_COMMIT=$(git -C ./$PIPE rev-parse --short HEAD 2> /dev/null || echo 0)

  if [[ "$PIPE_LAST_COMMIT" != "$PIPE_REAL_COMMIT" ]]; then
    echo $PIPE_REAL_COMMIT > .lastcommit
    linter
    build_image
    push_image
    dock_comp
    echo -e "Done \xe2\x9c\x85"
  else
    echo -e "No changes at remote repo \xe2\x9d\x8e"
  fi
}

pull_repo

