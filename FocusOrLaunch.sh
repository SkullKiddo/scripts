#!/bin/bash



if [ "$1" == "Firefox" ]; then
    window=$(wmctrl -l | grep "Mozilla Firefox")
    if [ -z "$window" ]; then
        firefox&
    else
        wmctrl -a "Mozilla Firefox"
    fi
fi

if [ "$1" == "VScode" ]; then
    window=$(wmctrl -l | grep "\- Visual Studio Code")
    if [ -z "$window" ]; then
        code&
    else
        wmctrl -a "- Visual Studio Code"
    fi
fi

if [ "$1" == "Terminal" ]; then
    window=$(wmctrl -l | grep "Terminal -\|bsc19596@login1") #que contenga "Terminal -" o "bsc19596@login1"
    if [ -z "$window" ]; then
        terminator&
    else
        wmctrl -a "Terminal - "
    fi
fi
