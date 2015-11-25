#!/bin/bash
# #Beddne/poprawne: 
# grep ^A errors.m2 > edits.txt | awk '{print $3 echo "    "  $5}' edits.txt


#Procent:
echo "rozwiązanie 1"
A=`grep "^A " errors.m2 | wc -l`
words=$((`grep "^S " errors.m2 | wc -w` - `grep "^S " errors.m2 | wc -l`)) #words - #lines with S
echo `bc <<< "scale=4; $A / $words * 100"`%


echo "rozwiązanie 2"
grep "^A " errors.m2 | wc -l
cp errors.m2 errors
grep ^S errors > temp
sed -i 's/S //g' temp
wc temp -w
