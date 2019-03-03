#!/bin/bash

#Script to merge two csv files based on user_id


function sorth() { awk 'NR==1; NR>1{print | "sort"}' "$1"; }
join --header -t, <(sorth file_a.csv) <(sorth file_b.csv) > merged_bash.csv
