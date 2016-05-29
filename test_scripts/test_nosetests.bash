#!/bin/bash

set -u
set -i

for f in env env3; do
	for e in "" PROD DEV; do
		CMD="./${f}/bin/nosetests --cover-tests -v --process-timeout=1 tests api frontend"
		
		if [ -z "$e" ]; then
			echo -e "\n\n*** RUNNING: $CMD ***"
			$CMD
			errcode=$?
		else
			echo -e "\n\n*** RUNNING: ENV=${e} $CMD ***"
			ENV=${e} $CMD
			errcode=$?
		fi 
		
		if [ $errcode -ne 0 ]; then
			if [ -z "$e" ]; then
				echo "FAILED with CMD: $CMD" 
			else
				echo "FAILED with CMD: ENV=${e} $CMD" 
			fi
			exit 1
		fi 
		
		if [ -z "$e" ]; then
			echo "*** END: $CMD ***"
		else
			echo "*** END: ENV=${e} $CMD ***"
		fi
		
	done
done 
