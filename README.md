## Git clone the application

```

    git clone https://github.com/dendy1922/testing_task.git
    
```
## Create a virtual environment inside the application 

```

    pip install virtualenv
    
    virtualenv -p python3 venv  

    source venv/bin/activate
    

```

## Docker commands for server

```

    // moving to server directory
    cd flaskapp

    // List all running container
    docker ps

    // list all containers
    docker ps -a


    // list all docker images
    docker images

    // build a docker image
    docker build -t flaskapp:latest . 

    // run a docker container in daemon mode with ports exposed
    docker run -it -d -p 5000:5000 flaskapp

    // for stopping docker container
    docker stop <id>


```
## Install Python modules for testing 
```

   cd ..
   cd tests
   pip3 install -r requirements.txt 
    
```
## Testing  

```    

    //use pytest command for testing 
    pytest -v -s 

```
