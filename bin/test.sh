#!/bin/bash
set -euxo pipefail

# Run tests
cd lambda/car_search
python3.8 -m pytest -v -s ./test
