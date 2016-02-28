#!/bin/bash

CHAPTER=""
NUM_EXERCISES=""

function usage
{
    echo "This script initalizes a chapter directory"
    echo -e "Usage: $0 [options]"
    echo -e "\t -c Chapter number. Mandatory"
    echo -e "\t -e Number of exercises in chapter. Mandatory"
}

while getopts "c:e:h" opt; do
  case $opt in
    c)
      CHAPTER=$OPTARG
      ;;
    e)
      NUM_EXERCISES=$OPTARG
      ;;
    h)
      usage
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

if [[ -n "$CHAPTER" ]] && [[ -n "$NUM_EXERCISES" ]]
then
    cp -r template chapter$CHAPTER
    cd chapter$CHAPTER
    for i in `seq 1 $NUM_EXERCISES`
    do
      base_filename="Exercise$i"
      base_classname="Exercise$i"
      cp Template.cpp $base_filename.cpp
      cp TemplateSuite.h $base_filename"Suite.h"
      sed -i s/Template/$base_filename/g $base_filename"Suite.h"
    done
    rm -f Template*
    rm -f runner
    cd - > /dev/null
else
    echo -e "Mandatory options not specified\n"
    usage
fi
