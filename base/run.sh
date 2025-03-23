#!/bin/bash

# Name of your Python script
PYTHON_SCRIPT="gil.py"

# Number of times to run
NUM_RUNS=100

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: File $PYTHON_SCRIPT not found!"
    exit 1
fi

echo "Running $PYTHON_SCRIPT $NUM_RUNS times..."
echo "----------------------------------------"

# Initialize counter for non-2000000 results
non_expected_count=0

# Run the script NUM_RUNS times
for (( i=1; i<=$NUM_RUNS; i++ ))
do
    # Run the Python script and capture the output
    result=$(python3 "$PYTHON_SCRIPT" | grep -o '[0-9]\+')
    
    # Print the run number and result
    echo "Run $i: Counter = $result"
    
    # Check if the result is not 2000000
    if [ "$result" != "2000000" ]; then
        non_expected_count=$((non_expected_count + 1))
    fi
done

echo "----------------------------------------"
echo "Summary: Ran $PYTHON_SCRIPT $NUM_RUNS times"
echo "Non-2000000 results: $non_expected_count out of $NUM_RUNS ($(echo "scale=2; $non_expected_count*100/$NUM_RUNS" | bc)%)"