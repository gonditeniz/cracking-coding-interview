#!/bin/bash

for suite in $(ls *.h)
do
    cxxtestgen --error-printer -o Runner.cpp $suite
    g++ Runner.cpp -o runner -I/usr/include/cxxtest/
    ./runner
done
