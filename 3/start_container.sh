#!/bin/bash

docker build --tag bio_test . && docker run --rm -it -p 8080:8080 -v .:/host  bio_test "$@"