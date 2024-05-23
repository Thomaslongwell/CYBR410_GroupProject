docker-compose up

cd ~/CYBR410_GroupProject/opencanary

docker build -t opencanary -f Dockerfile.latest .

bash iptable.sh

echo "We're so up rn"
