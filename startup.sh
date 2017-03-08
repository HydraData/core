#!/bin/sh
nohup sh -c mongod &
nohup sh -c python Profiler.py&