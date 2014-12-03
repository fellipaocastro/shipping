#!/bin/bash
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOGGING_FILENAME="/tmp/shipping_`date +%Y-%m-%d`.log"
echo -e "Shipping calculator\n"
case $1 in
    setup)
        echo -e "Installing dependencies...\n"
        pip install -r $BASE_DIR/requirements/production.txt
        ;;
    run)
        $BASE_DIR/axado.py ${@:2}
        ;;
    log)
        echo -e "Following end of current log file...\n"
        tail -F $LOGGING_FILENAME
        ;;
    test)
        echo "Running the test suit..."
        nosetests tests
        ;;
    check)
        echo -e "Running source code checker...\n"
        flake8 $BASE_DIR
        ;;
    *)
        echo "Usage:"
        echo -e "  axado/manage.sh <command>\n"
        echo "Available commands:"
        echo "  setup\
                                                Install dependencies"
        echo "  run <origin> <destination> <receipt> <weight>\
        Start shipping calculator"
        echo "  log\
                                                  Follow end of current log \
file"
        echo "  test\
                                                 Run the test suit"
        echo "  check\
                                                Run source code checker"
        ;;
esac
