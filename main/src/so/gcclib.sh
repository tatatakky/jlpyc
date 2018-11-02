#!/bin/sh
command="gcc -shared -fPIC -o libcube.so cube.c"
eval $command
