## Pre-requisites:
- Docker

## How to run this project
1.) Build the container

```
docker build . -t pssh-error-reproduction
```

2.) Run the container

```
docker run -p 8000:8000 pssh-error-reproduction
```