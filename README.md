# docker Commands

"""
A Docker image is a file used to execute code in a Docker container. Docker images act as a set of instructions to build a Docker container, like a template. Docker images also act as the starting point when using Docker. An image is comparable to a snapshot in virtual machine (VM) environments.Docker is used to create, run and deploy applications in containers. A Docker image contains application code, libraries, tools, dependencies and other files needed to make an application run. When a user runs an image, it can become one or many instances of a container.

Docker images have multiple layers, each one originates from the previous layer but is different from it. The layers speed up Docker builds while increasing reusability and decreasing disk use. Image layers are also read-only files. Once a container is created, a writable layer is added on top of the unchangeable images, allowing a user to make changes.

Docker images are also immutable. While they can't be changed, they can be duplicated, shared or deleted.

In virtual machines, if a resource is aloote dto vm1, it can nt be used by any other virtual machines even if its idle.

consider how your env you have set on developer side , but QA side doesnt have same setting

docker conatainer solves these problem. a docker has

- process ID
- network trace/config
- root dir # i.e. different folder structure inside this docker to mantain isolation

so it brings Enviroment standardization, Isolation, portablity and " Build once and deploy everywhere"

In conda env, we cerate a new env (for `requirments.txt`)

so afeter creating env, we create this env as a docker image/container

WSGI(web server gateway interface): a web server would be communication with our flask app using wsgi

Whenever you are going to work with docker, you need to start with `base image`. This `base image` will be downloaded from `dockerhub`. In `docker hub`, there are several base images. A base image in Docker serves as the foundation upon which you build your own custom container images. It's a pre-existing image containing various components like an operating system, programming languages, tools, or other software, depending on its purpose. Here's a breakdown of the key points:

What it does:

Provides a starting point for your image, eliminating the need to build everything from scratch.
Saves time and effort by including common components you might otherwise need to install manually.
Offers various options to fit your specific needs:
Official Docker images: A curated set of high-quality images hosted on Docker Hub, covering common operating systems, languages, and tools.
Community-created images: A vast library of images contributed by individuals and organizations on Docker Hub.
Custom base images: You can also create your own base image tailored to your specific requirements.
Key terms:

- Parent image: Sometimes used interchangeably with "base image," especially when referring to the image specified in the FROM instruction of a Dockerfile.
- Scratch image: Docker's minimal image offering a blank slate for starting from absolute scratch, suitable for advanced users with full control over their image content.

Suppose your base image is `ubuntu`. Now on top of that `base image`, we can start adding different components i.e. anaconda python env. Now on top of that anaconda python env, we can install packages like `flask`. Encapsulating it all toegther results in a `docker image`. Now we can dockerize this image and take it to anyother similar base image env and install it over there. Now we still need to understand following commands to interact

These commands will be used in DockerFile:

- FROM: to create `base image`we need this statement i.e.

- COPY: sampleFlaskApp created on host machine, I have some folder structure for that. Each and every docker has its own user root folder for iisolation purposes. So I need to copy from host system to user root folder present in user root system.

- EXPOSE: Each docker image has a network interface.. so we can use this command for exposing some port, so we can access this whole application by using this port

- WORKDIR: In docker we should know from where this aparticular application is located should run i.e. my code is in this directory

- RUN: to install packages. It will install anaconda env and all packages like flask
  RUN pip install -r requirement.txt

- CMD: to run executable file i.e. app.py.. it will run those file
  CMD python app.py

- ENTRYPOINT: defines main executable

- ENV sets env variables

"""

<!-- ################################################################################################################# -->

"""

WRITING / BUILDING / RUNNING DOKCER iMAGES:

1. Write Dockerfile:

2. Build Docker Image:
   docker build -t money_api

   build command create docker image using Dockerfile(contains instructions to build image) and context(locatin of files to be included in the build)

   In context, only keep files that arre necessary for the build.

docker ps # to see running dockers

3. Running our app in docker.
   docker run-p 8000:8000 money_api

<!-- # hit http://0.0.0.0:8000/apidocs/ -->

"""

"""
docker ps: shows all running containers
docker images: shows all docker images; Docker images act as read-only templates used to create containers.
docker search: search for images in docker repository

python: latest # here latest is tag

# PULLING AN IMAGE:

docker pull

# Running container

docker run -it python # if you haven't pull, it will be automatically pulled.
docker stop <id>

# Basic Docker CLI Commands:

    docker run: Use this command to create and start a new container based on an image. You can specify options such as port mapping, volume mounting, and environment variables.

    docker ps: This command lists the running containers on your system, providing information about their status, names, and IDs.

    docker images: Use this command to view a list of available Docker images on your system. These images serve as the blueprints for creating containers.

    docker build: This command is used for building a Docker image from a Dockerfile, which is a script that specifies how to create the image.

    docker pull: Use this command to download Docker images from a container registry, such as Docker Hub.

    docker stop and docker start: These commands allow you to stop and start containers, respectively.

    docker rm: This command removes one or more containers. Be cautious with this command, as it permanently deletes containers.

    docker rmi: Use this command to remove one or more images. Make sure you don't need the image anymore before deleting it.

# Advanced Docker CLI Usage:

    docker exec: You can execute commands inside a running container using this command. It's useful for troubleshooting or interacting with a container's shell.

    docker logs: This command provides access to the logs generated by a running container, which is helpful for debugging and monitoring.

    docker-compose: Docker Compose is a tool that allows you to define and manage multi-container applications in a single file. You can use the docker-compose command to start, stop, and manage these multi-container setups.

    docker network: Docker allows you to create custom networks to connect containers. This command helps you manage network configurations for your containers.

"""

"""

# Docker volumes

to create create data thet presists, we need to create and attatch a volume to our container.

docker volume ls
docker volume create <name>
docker run -v <name>:/my-mounted-vol -it bash

- `-v y-vol:/my-mounted-vol:` This flag defines a volume mount:
  ** -v: Specifies that we're mounting a volume.
  ** y-vol: This is the name of the volume on the host system (your machine).
  \*\* /my-mounted-vol: This is the directory inside the container where the volume will be mounted.
  So if you run your container again

  docker run -v y-vol:/my-mounted-vol -it bash
  \*\*\* echo "Hello Vol!">my-mounted-vol/hello.txt
  now stop container and run that command again and you would be able to accesss that volume

"""

"""

# RUNNING A DATABASE IN CONTAINER

docker run -e POSTGRES_PASSWORD=psswrd -e POSTGRES_USER=admin -p 5432:5432 -v postgres-vol:/var/lib/postgressql/data -d postgres

\*\* -e POSTGRES_PASSWORD=psswrd -e POSTGRES_USER=admin: These set environment variables inside the container
\*\*-p 5432:5432: This maps the container's port 5432 (which is the default Postgres port) to the same port on your host machine. This allows you to connect to the database from outside the container.
**-v postgres-vol:/var/lib/postgressql/data: This mounts a volume from your host machine (named postgres-vol) to the directory inside the container where PostgreSQL stores its data (/var/lib/postgressql/data). This makes the data persistent, meaning it will be preserved even if you stop and restart the container.
** -d:
In the Docker command docker run -d bash, the -d flag stands for detached mode. When you run a container in detached mode, it runs in the background without attaching a pseudo-tty (terminal) to it. This means you won't have direct interactive access to the container's shell. This runs the container in the background, meaning it won't attach a terminal to it.
\*\* postgres: This specifies the image to use for the container. In this case, it's the official postgres image from Docker Hub.

To connect to this container we are going to use exec command because its inndeteached mode terminal is not available.

     docker exec -it d7d4ab450c5e bash

docker exec -it d7d4ab450c5e bash allows you to attach a terminal to a running Docker container in detached mode. Here's a breakdown of what it does:

Components:

docker exec: This command is used to execute a process inside a running container.
-it: These flags specify:
-i: Enables interactive mode, attaching a pseudo-tty (terminal) to the container.
-t: Allocates a pseudo-tty, which is necessary for attaching a terminal.
d7d4ab450c5e: This is the container ID of the container you want to attach to. You can find container IDs using docker ps.
bash: This specifies the command to run inside the container. In this case, it's the bash shell, providing a command-line interface.

# you can use .dockerignore file

# docker build creates images... images run in container using docker run

"""

# DOCKER COMPOSE

Docker Compose is a powerful tool that simplifies the management of multi-container applications in Docker. It allows you to define and run complex, interconnected services with just a single configuration file. If you're new to Docker Compose, here's how it can help you streamline your containerized applications:

1. Compose Files:

   Docker Compose relies on a configuration file called a "docker-compose.yml." This file is where you define your application's services, networks, volumes, and their configurations. It's essentially a blueprint for your multi-container setup.

2. Service Definitions:

   In the docker-compose.yml file, you specify the services you want to run as containers. Each service can represent a different component of your application, like a web server, a database, or an API. You define the container image, environment variables, ports, and other settings for each service.

3. Networking and Volumes:

   Docker Compose simplifies network and storage management. You can define custom networks to connect your services and create volumes for persistent data storage, ensuring data can be shared and accessed between containers seamlessly.

4. Dependency Management:

   Docker Compose allows you to declare dependencies between services. For instance, you can specify that your web server should start only after the database service is up and running. This ensures that your multi-container application starts in the correct order.

5. Launching the Application:

   To start your multi-container application, navigate to the directory containing your docker-compose.yml file and run the docker-compose up command. Docker Compose will build and start the containers as per your specifications.

6. Scaling and Management:

   Docker Compose enables you to scale services up or down by specifying the number of desired containers for a service. It simplifies management, making it easy to stop, start, or remove your application containers.

7. Environment Configuration:

   Docker Compose supports environment-specific configuration using .env files. You can store environment-specific variables in these files and reference them in your docker-compose.yml.

Docker Compose is particularly beneficial for data engineers and developers working with complex, multi-component applications. It simplifies the development, testing, and deployment of these applications by ensuring that all services work together seamlessly, regardless of the environment.

Docker compose define orchestrations/service in YAML file.
There are multiple possible sections in the compose file.

- The main one being one for services. Each service represents one or more instance of a running container.
- there can be a section to define network communication between the services or between the services and outside.
- It can also define persistent volume storage and
- configuration that can be shared by other elemennts in the compose file.

"""

"""

# Airflow

- is a workflow managment platforn
- manages data engineering pipelines
- these workflows are defined as acyclic graphs
- Takes and dependencies are defined in python
