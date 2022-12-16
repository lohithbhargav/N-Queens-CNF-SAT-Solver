echo "Enter the value of N for nqueens":
read n
python3 nqueens.py $n
minisat input.cnf output
cat output
