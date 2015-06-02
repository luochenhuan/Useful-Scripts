#!/bin/bash
######### MODIFY VARIABLES ###########
dir="a2/" #use relative path, or tar will give warning
excld="" # exclude file or dir, note DON'T ADD / IN THE END
email="zhenhaiyucelia@gmail.com"
######### END       MODIFY ###########
if [ -n "$dir" ]; then
    #echo $(basename $dir)
    if [ -n "$excld" ]; then
        tar -c --exclude="$excld" -f "$(basename $dir).tar" $dir
    else
        tar -cf "$(basename $dir).tar" $dir
    fi
    #email using mutt
    mutt -a "$(basename $dir).tar" -s "new msg" -- $email
else
    echo dir path is empty
fi
