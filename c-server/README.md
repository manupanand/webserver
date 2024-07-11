# Using libmicrohttpd

```
sudo apt-get install libmicrohttpd-dev -y

```
# RHEL 
```sudo dnf install epel-release -y 
sudo dnf install libmicrohttpd libmicrohttpd-devel -y
```
# Run 
```
gcc -o server server.c -lmicrohttpd
./server

```