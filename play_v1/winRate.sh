#!/bin/bash

win_num=0
draw_num=0
lose_num=0
for((i=1;i<=10;i++))
do
    result=`python play_as_black.py | grep wins`
    if [ -z "$result" ]
    then
        let "draw_num += 1"
        continue
    fi
    white_result=`echo "$result" | grep white`
    if [ -z "$white_result" ]
    then
        let "lose_num += 1"
        continue
    fi
    let "win_num += 1"
done

echo "The white win rate is $win_num / 10,"
echo "The white lose rate is $lose_num / 10,"
echo "The white draw rate is $draw_num / 10."

exit 0
