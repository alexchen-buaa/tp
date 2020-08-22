tp(){
	if [[ $# -eq 0 ]]
	then
		python ${TP_INSTALL}/tp.py
	elif [[ $# -eq 1 ]]
	then
		cd $(python ${TP_INSTALL}/path.py $1)
	elif [[ $# -gt 1 ]]
	then
		if [[ $1 = "add" ]]
		then
			if [[ $# -eq 2 ]]
			then
				python ${TP_INSTALL}/add.py $2 $(pwd)
			elif [[ $# -eq 3 ]]
			then
				python ${TP_INSTALL}/add.py $2 $3
			fi
		elif [[ $1 = "rm" ]]
		then
			python ${TP_INSTALL}/rm.py $2
		fi
	fi
}
