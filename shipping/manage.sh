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
        $ROOT_PATH/shipping/axado.py
        ;;
    test)
        echo "Running the test suit..."
        nosetests --with-yanc --with-spec --spec-color shipping.tests
        ;;
    check)
        echo "Running flake8 source code checker..."
        echo ""
        flake8 $ROOT_PATH --verbose
        ;;
    *)
        echo "Usage:"
        echo "  ./manage.sh <command>"
        echo ""
        echo "Available commands:"
        echo "  setup         Install dependencies"
        echo "  run           Start shipping calculator"
        echo "  test          Run the test suit"
        echo "  check         Run flake8 source code checker"
        ;;
 esac
