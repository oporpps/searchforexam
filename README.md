# SEARCHFOREXAM
Setup for ubuntu server, You can create server on windows with docker compose
## Ubuntu Setup
```shell
apt update -y && apt upgrade -y && apt install git
```
```shell
git clone https://github.com/oporpps/searchforexam
```
```shell
cd searchforexam
```
```shell
chmod +x docker.sh && chmod +x deploy.sh
```
```shell
./docker.sh
```
```shell
./deploy.sh
```