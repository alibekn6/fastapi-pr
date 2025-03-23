#!/bin/bash

urlencode() {
    python3 -c "import urllib.parse; print(urllib.parse.quote('$1'))"
}


generate_random_string() {
    LC_ALL=C tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 12
}

max=100

start_time=$(date +%s)

for i in $(seq 1 $max); do
    name=$(generate_random_string)
    description=$(generate_random_string)


    curl -X POST "http://127.0.0.1:8000/tasks?name=$name&description=$description" \
        -H "Content-Type: application/json" -w "Request $i: %{time_total}s\n"
done

end_time=$(date +%s)

elapsed_time=$((end_time - start_time))

echo "Total time spent on $max post requests is : $elapsed_time seconds"
