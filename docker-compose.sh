#!/bin/bash
current=$(pwd)


read -p "Do you want to compose up(Y/n)?" CONT

if [[ "$CONT" = "Y" ]] || [[ "$CONT" = "y" ]] || [[ "$CONT" = "" ]]; then
    echo -ne 'Starting docker compose'
    sleep 1
    echo -ne "."
    echo -ne "."
    echo -ne "."
    sleep 1


    # main website
    docker-compose -f docker-compose-bolcom.yaml build
    docker-compose -f docker-compose-bolcom.yaml up -d

else
    echo -ne '\e[33mRemoving all containers/images/volumes\e[0m'
    sleep 1
    echo -ne "."
    echo -ne "."
    echo -ne "."
    sleep 1

    # stop all containers
    docker stop $(docker ps -aq)
    # remove all containers
    docker rm $(docker ps -aq)
    # remove all images
    docker rmi $(docker images -q)
    # remove all volumes
    docker volume prune -f
fi



echo -e '\e[32mDone\e[0m'
sleep 5