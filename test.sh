#!/bin/sh

# Author : Zara Ali
# Copyright (c) Tutorialspoint.com
# Script follows he

git add .
read MESSAGE
git commit -m "$MESSAGE"
git push origin master
