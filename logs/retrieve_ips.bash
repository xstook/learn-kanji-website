#!/usr/bin/env bash

log_file="log.txt"

if [[ $# == 1 ]]; then
	log_file="$1"
fi


sed -nr "s/^([0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3})(.*)/\1/p" "$log_file" | sort -u



