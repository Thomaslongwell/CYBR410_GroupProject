docker-compose up

cd $PWD/opencanary

docker build -t opencanary -f Dockerfile.latest .

bash iptable.sh

echo "We're so up rn"
