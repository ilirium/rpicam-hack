#!/usr/bin/env bash

# Stage: Strict mode options
# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
# More details about "E" and "x":
# https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -eu -o pipefail

export SERVER_IP_ADDRESS="raspberrypi.local"

# Step: Results
rsync -arz -v --info=progress2 --partial --rsh=ssh \
  "ilirium@${SERVER_IP_ADDRESS}:/home/ilirium/Projects/rpicam-hack/experiments/series001/out" \
  "/Users/ilirium/Library/CloudStorage/OneDrive-Personal/software-engineering/code-2025/rpicam-hack/experiments/series001"
