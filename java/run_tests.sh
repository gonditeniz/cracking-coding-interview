#!/bin/bash

function run_chapter
{
    cd $1
    ./build_run.sh
    cd - > /dev/null
}

if [ -d "$1" ]
then
    echo "Running test in $1"
    run_chapter $1
else
    echo "Running all tests"
    for chapter_folder in $(find . -maxdepth 1 -name "chapter*")
    do
        echo "Running test in $chapter_folder"
        run_chapter $chapter_folder
    done
fi
