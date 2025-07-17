#!/bin/bash
git add .
read -p "Enter commit message: " commitMsg
git commit -m "$commitMsg"
git push
