#!/usr/bin/env bash

# Stage: Strict mode options
# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
# More details about "E" and "x":
# https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -eu -o pipefail

DISPLAY=:0 python3 -m experiments.series001.ex001_first_try
