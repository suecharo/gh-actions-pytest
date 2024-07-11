function main() {
    echo "In run.sh"

    echo "=== env ========"

    env

    echo "=== pip list ========"

    python3 -m pip list

    echo "=== which ========"

    which python3

    echo "=== echo PYTHONPATH ========"

    echo $PYTHONPATH

    echo "=== exec module ========"

    python3 -c "from test_pkg.mod import echo_foo; echo_foo()"
}

main
