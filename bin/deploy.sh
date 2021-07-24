#!/bin/bash
set -euxo pipefail

function deploy_car_search() {
    aws lambda update-function-code --function-name carSearch --s3-bucket car-search-demo --s3-key carSearch.zip
}

function update_cloudformation_stack() {
    cd cloudformation
    aws s3 sync . s3://car-search-demo --exclude "*" --include "car_search.yml"
    aws cloudformation update-stack --stack-name carSearch \
    --template-url 'https://car-search-demo.s3-ap-southeast-2.amazonaws.com/car_search.yml' --capabilities CAPABILITY_NAMED_IAM
    cd ..
}

function sync_public_assets() {
    cd ./public
    aws s3 sync . s3://car-search-demo
}

function main(){
  deploy_car_search
  update_cloudformation_stack
  sync_public_assets
}

main