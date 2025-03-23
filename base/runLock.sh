#!/bin/bash

PYTHON_SCRIPT="prod.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: File $PYTHON_SCRIPT not found!"
    echo "Please create this file with your threaded counter code."
    exit 1
fi

RUNS=1000

echo "Starting benchmark with $RUNS runs of $PYTHON_SCRIPT..."
echo "===================================="

total_start=$(date +%s.%N)

for (( i=1; i<=$RUNS; i++ ))
do
    echo "0" > counter.txt
    
    python3 "$PYTHON_SCRIPT" > /dev/null 2>&1
    
    if (( i % 100 == 0 )); then
        echo "Completed $i runs..."
    fi
done

total_end=$(date +%s.%N)

total_time=$(echo "$total_end - $total_start" | bc)

avg_time=$(echo "scale=6; $total_time / $RUNS" | bc)

echo "===================================="
echo "Benchmark Results:"
echo "Total runs: $RUNS"
echo "Total time: $total_time seconds"
echo "Average time per run: $avg_time seconds"
echo "Runs per second: $(echo "scale=2; $RUNS / $total_time" | bc)"