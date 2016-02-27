#!/bin/bash

pushd .. > /dev/null
nosetests python -v -s
popd > /dev/null
