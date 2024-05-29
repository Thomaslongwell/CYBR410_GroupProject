for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

# Add Docker's official GPG key:
apt-get update
apt-get install ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update

apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

apt install docker-compose

apt install sysdig

apt install tshark

docker compose up

cd $PWD/opencanary

docker build -t opencanary -f Dockerfile.latest .

docker run --rm --detach -p 8444:443 -p 8881:8080 -p 33061:3306 -p 2201:22 -p 63791:6379 -p 3391:3389 -p 50601:5060 -p 1162:161 -p 1124:123 -p 1070:69 -p 8002:8001 -p 2301:23 -p 14331:1433 -p 5901:5000 -v "${PWD}/data/.opencanary.conf":"/root/.opencanary.conf" --name opencanary opencanary

cd ..

bash ip_blocking.sh

echo "We're so up rn"
