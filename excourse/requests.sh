#!/bin/bash

urlencode() {
    python3 -c "import urllib.parse; print(urllib.parse.quote('$1'))"
}


generate_random_string() {
    LC_ALL=C tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 12
}

max=1000
for i in $(seq 1 $max); do
    name=$(generate_random_string)
    description=$(generate_random_string)

    encoded_name=$(urlencode "$name")
    encoded_description=$(urlencode "$description")

    curl -X POST "http://127.0.0.1:8000/tasks?name=$encoded_name&description=$encoded_description" \
        -H "Content-Type: application/json"
done
