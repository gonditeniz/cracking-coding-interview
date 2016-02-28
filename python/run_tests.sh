#!/bin/bash

pushd .. > /dev/null
if [ -f $1 ]
then
    nosetests $1 -v -s
else
    nosetests python -v -s
fi
popd > /dev/null
