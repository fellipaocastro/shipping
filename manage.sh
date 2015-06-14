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

        $BASE_DIR/main.py ${@:2}

        ;;

    log)

        echo -e "Following end of current log file...\n"

        tail -F $LOGGING_FILENAME

        ;;

    test)

        echo "Running the test suit..."

        nosetests test

        ;;

    check)

        echo -e "Running source code checker...\n"

        flake8 $BASE_DIR

        ;;

    shell)

        ipython

        ;;

    *)

        echo "Usage:"

        echo -e "  ./manage.sh <command>\n"

        echo "Available commands:"

        echo "  setup\
                                                Install dependencies"

        echo "  run <origin> <destination> <receipt> <weight>\
        Start shipping calculator"

        echo "  test\
                                                 Run the test suit"

        echo "  log\
                                                  Follow end of current log \
file"

        echo "  check\
                                                Run source code checker"

        echo "  shell\
                                                Open an enhanced Interactive Python"

        ;;

esac
