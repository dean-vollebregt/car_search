#!/bin/bash
set -euxo pipefail

function build_car_search() {
    cd lambda/car_search
    python3.8 -m venv v-env && source v-env/bin/activate
    pip3.8 install -r requirements.txt -t ./
    zip -r carSearch.zip * -x "v-env*" -x "*.dist-info*"
    aws s3 sync . s3://car-search-demo --acl private --exclude "*" --include "carSearch.zip"
    rm -rf carSearch.zip
    deactivate
}

build_car_search