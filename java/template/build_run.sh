#!/bin/bash

for suite in $(ls *Test.java)
do
    echo "Running test $suite"
    javac -cp .:/usr/share/java/junit4.jar $suite
    filename="${suite%.*}"
    java -cp .:/usr/share/java/junit4.jar org.junit.runner.JUnitCore $filename
done
