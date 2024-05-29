# README
---
This living document serves as a tool to help with redeployment. Eventually, this document should become the README for this distribution as it will cover all the dependencies and how-to's in order to begin this deployment from scratch.

## Dependencies

This project has a number of key dependencies that are needed in
order to ensure it runs smoothly.

- Docker: Please follow the instructions located [here](https://docs.docker.com/engine/install/ubuntu/)
- Docker Compose: `sudo apt install docker-compose`
- Git: `sudo apt install git`
- Sysdig: `sudo apt install sysdig`
- Tshark: `sudo apt install tshark`

## Cloning the Git Repo

```bash
git clone https://github.com/Thomaslongwell/CYBR410_GroupProject.git
```

## Running the Front End

### Build Docker Containers

*Flask*
- Change directory `cd Frontend/Flask`
- Build Flask container `docker build -t flasky .`
- Change directory back to front end `cd ..`
*nginx*
- change directory `cd nginx`
- Build nginx container `docker build -t fnginx .`
- Change directory `cd ..`

### Build Open Canary Container and Run Services

Within the `Frontend` directory

```bash
./start.sh
```

Alternatively

```Bash
bash start.sh
```

## Running Logging
- In the project's root directory, edit `scap_logging.sh` to reflect a safe location for logs to be saved.
- Run 
```Bash
./scap_logging.sh
```

- Alternatively 
```Bash
bash scap_logging.sh
```

## Running SQL Server

- Change directory `cd sqlServer`
- Run `docker compose up .`