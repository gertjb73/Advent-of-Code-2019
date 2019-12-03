# 1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0
# 1 0 0 3 1 1 2 3 1 3 4 3 1 5 0 3 2 6 1 19 1 19 5 23 2 10 23 27 2 27 13 31 1 10 31 35 1 35 9 39 2 39 13 43 1 43 5 47 1 47 6 51 2 6 51 55 1 5 55 59 2 9 59 63 2 6 63 67 1 13 67 71 1 9 71 75 2 13 75 79 1 79 10 83 2 83 9 87 1 5 87 91 2 91 6 95 2 13 95 99 1 99 5 103 1 103 2 107 1 107 10 0 99 2 0 14 0

array_name_initial=(1 0 0 3 1 1 2 3 1 3 4 3 1 5 0 3 2 6 1 19 1 19 5 23 2 10 23 27 2 27 13 31 1 10 31 35 1 35 9 39 2 39 13 43 1 43 5 47 1 47 6 51 2 6 51 55 1 5 55 59 2 9 59 63 2 6 63 67 1 13 67 71 1 9 71 75 2 13 75 79 1 79 10 83 2 83 9 87 1 5 87 91 2 91 6 95 2 13 95 99 1 99 5 103 1 103 2 107 1 107 10 0 99 2 0 14 0)
array_name=("${array_name_initial[@]}") 

needed_result=19690720
noun=0
verb=0
max_value_noun=10
max_value_verb=10
found=false

printf "\nInitial program:\n"
printf "${array_name[*]}\n"

array_name[1]=$noun
array_name[2]=$verb

while [ $noun -le $max_value_noun -a $found = false ] ; do
	verb=0
	printf "$noun:\n"

	while [ $verb -le $max_value_verb -a $found = false ] ; do
		array_name=("${array_name_initial[@]}") 
		array_name[1]=$noun
		array_name[2]=$verb
		# printf "${array_name[*]}\n"
		index0=0
		while [ ${array_name[index0]} != 99 ] ; do
		    index1=`expr $index0 + 1`
		    index2=`expr $index0 + 2`
		    index3=`expr $index0 + 3`
			key_index0=${array_name[index0]}
			key_index1=${array_name[index1]}
			key_index2=${array_name[index2]}
			key_index3=${array_name[index3]}
			value_index0=${array_name[key_index0]}
			value_index1=${array_name[key_index1]}
			value_index2=${array_name[key_index2]}
			value_index3=${array_name[key_index3]}
		
			if [ $key_index0 -eq 1 ]
			then
				result=`expr $value_index1 + $value_index2`
				# printf "PLUS\t"
				# printf "($index0: $key_index0: $value_index0) - ($index1 : $key_index1: $value_index1) - ($index2 : $key_index2: $value_index2) - ($index3 : $key_index3: $value_index3)\tResult: $result\n"
				# printf "$value_index1 + $value_index2 = $result\t"
				# printf "so array possition $key_index3 (now $value_index3) will become $result\t\t\t"
				array_name[key_index3]=$result
				# printf "${array_name[key_index3]}\n"
			fi
			if [ $key_index0 -eq 2 ]
			then
				result=$(($value_index1*$value_index2))
				# printf "MULT\t"
				# printf "($index0: $key_index0: $value_index0) - ($index1 : $key_index1: $value_index1) - ($index2 : $key_index2: $value_index2) - ($index3 : $key_index3: $value_index3)\tResult: $result\n"
				# printf "$value_index1 x $value_index2 = $result\t"
				# printf "so array possition $key_index3 (now $value_index3) will become $result\t\t\t"
				array_name[key_index3]=$result
				# printf "${array_name[key_index3]}\n"
			fi
		
		    index0=`expr $index0 + 4`
		    
		done
		if [ $needed_result -eq ${array_name[0]} ]
		then
			printf "Noun:\t$noun\tVerb:\t$verb\tResult:\t${array_name[0]} - $needed_result: Needed result ***** FOUND IT *****\n"
			printf "${array_name[*]}\n"
			atc_temp_result=$((100*$noun))
			atc_result=`expr $atc_temp_result + $verb`
			printf "Result for Advent to Code (100 * Noun + Verb): $atc_result"
			found=true
		else
			if [ $needed_result -gt ${array_name[0]} ]
			then
				printf "< "
			fi
			if [ $needed_result -lt ${array_name[0]} ]
			then
				printf "> "
			fi
		#	 printf "Noun:\t$noun\tVerb:\t$verb\tResult:\t${array_name[0]} - $needed_result: Needed result\n"
		fi
		verb=`expr $verb + 1`
	done
	if [ $needed_result -eq ${array_name[0]} ]
	then
		printf "\nNoun:\t$noun\tVerb:\t$verb\tResult:\t${array_name[0]} - $needed_result: Needed result ***** FOUND IT *****\n"
		printf "${array_name[*]}\n"
	else
		printf "\nNoun:\t$noun\tVerb:\t$verb\tResult:\t${array_name[0]} - $needed_result: Needed result\n"
	fi
	noun=`expr $noun + 1`
done

printf "\nFinal program:\t\t"
printf "${array_name[*]}\n"
printf "\nResult:\t${array_name[0]}\n\n"
