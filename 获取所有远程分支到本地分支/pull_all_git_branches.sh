#!/bin/bash
# 获取所有远程分支到本地分支

for branch in `git branch -a | grep remotes | grep -v HEAD | grep -v master`; do
    git branch --track ${branch##*/} $branch
done
