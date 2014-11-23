#!/bin/bash

ROOT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

echo "Shipping calculator"
echo ""

case $1 in
    setup)
        echo "Installing dependencies..."
        echo ""
        pip install -r $ROOT_PATH/requirements/local.txt
        ;;
    run)
        $ROOT_PATH/shipping/axado.py $2 $3 $4 $5
        ;;
    test)
        echo "Running the test suit..."
        nosetests shipping.tests
        ;;
    check)
        echo "Running source code checker..."
        echo ""
        flake8 $ROOT_PATH --verbose
        ;;
    *)
        echo "Usage:"
        echo "  ./manage.sh <command>"
        echo ""
        echo "Available commands:"
        echo "  setup\
                                                 Install dependencies"
        echo "  run <origin> <destination> <receipt> <weight>\
         Start shipping calculator"
        echo "  test\
                                                  Run the test suit"
        echo "  check\
                                                 Run source code checker"
        ;;
 esac
