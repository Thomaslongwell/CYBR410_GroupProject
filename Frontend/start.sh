docker-compose up

cd $PWD/opencanary

docker build -t opencanary -f Dockerfile.latest .

docker run --rm --detach -p 8444:443 -p 8881:8080 -p 33061:3306 -p 2201:22 -p 63791:6379 -p 3391:3389 -p 50601:5060 -p 1162:161 -p 1124:123 -p 1070:69 -p 8002:8001 -p 2301:23 -p 14331:1433 -p 5901:5000 -v "${PWD}/data/.opencanary.conf":"/root/.opencanary.conf" --name opencanary opencanary

bash iptable.sh

echo "We're so up rn"
