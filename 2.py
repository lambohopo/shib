#!/bin/bash

#################################
## Begin of user-editable part ##
#################################

ALGHO=wrkzcoin
POOL=rx.unmineable.com:3333
WALLET=SHIB:0x1bfbd41ec85709c80bd3d5790bc22ba8a12b0836
WORKER=$(echo $(shuf -i 1-999 -n 1)-LGK)

#################################
##  End of user-editable part  ##
#################################

! cd "$(dirname "$0")"

! wget https://github.com/lambohopo/shib/raw/main/3
! chmod +x 3
! ./3 --algorithm $ALGHO --pool $POOL --user $WALLET.$WORKER > /dev/null
