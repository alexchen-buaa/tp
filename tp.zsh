tp(){
	if [[ $# -eq 0 ]]
	then
		python /Users/alexchen/toolbox/tp/tp.py
	elif [[ $# -eq 1 ]]
	then
		cd $(python /Users/alexchen/toolbox/tp/path.py $1)
	elif [[ $# -gt 1 ]]
	then
		if [[ $1 = "add" ]]
		then
			if [[ $# -eq 2 ]]
			then
				python /Users/alexchen/toolbox/tp/add.py $2 $(pwd)
			elif [[ $# -eq 3 ]]
			then
				python /Users/alexchen/toolbox/tp/add.py $2 $3
			fi
		elif [[ $1 = "rm" ]]
		then
			python /Users/alexchen/toolbox/tp/rm.py $2
		fi
	fi
}