# xlab-test
Тестовое задание для Xlab

## Установка 


Требования к системным пакетам:

 - Python 3.11
 - Poetry
 - PostgreSQL
 - Redis
 
 
 Создание базы данных PostgreSQL:
 
    ~ $ psql postgres
    psql (14.6 (Homebrew))

    postgres=# create database xlab_test;
 
 
 Все переменные окружения прописаны в `dev.env`
 
 Необходимо скопировать его в `.env` и подставить нужные значения
 
    cp dev.env .env
    vim .env


 Установка зависимостей и активация env:
  
    cd ~/path/to/project/
    poetry install
    poetry shell

Запуск проекта:
    
    ./dev.sh

