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

"""

<!-- ################################################################################################################# -->

"""

WRITING / BUILDING / RUNNING DOKCER iMAGES:

1. Write Dockerfile:

2. Build Docker Image:
   docker build -t money_api

docker ps # to see running dockers

3. Running our app in docker.
   docker run-p 8000:8000 money_api

<!-- # hit http://0.0.0.0:8000/apidocs/ -->

"""
