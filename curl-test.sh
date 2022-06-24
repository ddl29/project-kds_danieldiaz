#! /bin/bash

NAME=$(echo $RANDOM | md5sum | head -c 6)

echo "TESTING POST"
curl --request POST http://localhost:5000/api/timeline_post -d 'name='$NAME'&email='$NAME'@net.com&content=Testing '$NAME''
echo "TESTING GET"
curl --request GET http://localhost:5000/api/timeline_post
echo "TESTING DELETE"
curl --request DELETE http://localhost:5000/api/timeline_post -d 'name='$NAME''
