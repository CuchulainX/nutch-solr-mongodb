# BDA Final Project
## DataHarvest: Dockerized Web Crawling, Indexing, and Storage Solution

### Team Members
- Azeem Ahmed
- Shahryar Ahmed

### Project Description
DataHarvest is a cutting-edge web crawling, indexing, and storage solution implemented using Docker. It leverages the power of Docker's containerization to provide seamless deployment, scalability, and portability. With DataHarvest, organizations can efficiently extract and process data from the web, while storing it in a reliable and easily manageable manner. Empowered by Docker, DataHarvest simplifies the setup process, ensures scalability for handling large volumes of data, and offers flexibility across different environments. Experience advanced web crawling and storage with DataHarvest, the Dockerized solution for your data extraction needs.

### Technology Stack
Below mentioned technologies are used in this project:
| Nutch | Solr | MongoDB |
|-------|------|---------|
| <img src=https://svn.apache.org/repos/asf/comdev/project-logos/originals/nutch.svg width="288" height="120" alt="Nutch"/> | <img src=https://svn.apache.org/repos/asf/comdev/project-logos/originals/solr.svg width="288" height="160" alt="Solr"/> | <img src="https://storage-us-gcs.bfldr.com/85s8xk2j3k89b67xr8c7vwmv/v/1069931049/original/MongoDB_ForestGreen.png?Expires=1686073601&KeyName=gcs-bfldr-prod&Signature=Jj6ekJDhgqLy13MhcB_ohikuY78=" width="400" height="101" alt="MongoDB"/> |

Apache Nutch is a highly extensible and scalable web crawler written in Java. It is a part of the Apache Hadoop ecosystem and is used to extract and process data from the web. Apache Solr is an open-source enterprise search platform written in Java. It is used to index and search large volumes of data. MongoDB is a NoSQL database that is used to store data in a document-oriented manner. It is a highly scalable and flexible database that is used to store large volumes of data.

Apache Nutch and Apache Solr operate independently in their respective containers, enabling efficient and scalable web crawling and indexing. The containerized Python environment facilitates seamless data retrieval from the Apache Solr container, while securely storing the results in a cloud-hosted MongoDB database.

### Project Setup
Setup free tier MongoDB Atlas by following the instructions below link:

[MongoDB Atlas Free Tier](https://www.mongodb.com/developer/products/atlas/free-atlas-cluster/)

Before running the project, make sure that you have Docker and Docker Compose installed on your system. If not, follow the instructions below to install them.

Install project specific dependencies using the following command:

```bash
sudo apt-get update && sudo apt-get upgrade -y
```
```bash
sudo apt-get install -y docker.io docker-compose
```
Clone the repository using the following command:
```bash
git clone https://github.com/AzeemQidwai/nutch_solr_mongodb.git
```
Navigate to the project directory using the following command:
```bash
cd nutch_solr_mongodb
```
Setup `auth.json` file in the `root` directory. This file contains the credentials for the MongoDB database. The file should be in the following format:

```json
{
    "username": "username",
    "password": "password"
}
```

Following `Dockerfile` is used to build the `python` image:
```dockerfile
FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py .
COPY ./auth.json .

ENV PYTHONUNBUFFERED=1

CMD [ "python", "-u", "app.py" ]
```

Run the following command to start the project:
```bash
docker-compose up
```
This will create and start the following containers:
- nutch
- solr
- python

To stop the project, run the following command:
```bash
docker-compose down --rmi local
```

### Project Usage
The project can be used to crawl and index data from the web. The data can be retrieved from the MongoDB database using the Python container. The following sections describe the usage of the project in detail.

#### Crawling
To configure the nutch container, simply set the target website in the `seed.txt` file located in the `nutch/urls` directory. Additionally, you can customize the crawling behavior by modifying the `regex-urlfilter.txt` file in the `nutch/conf` directory, allowing you to define specific regex patterns for data extraction.

#### Indexing
To configure the solr container, simply set the target website in the `seed.txt` file located in the `nutch/urls` directory. Additionally, you can customize the indexing behavior by modifying the `schema.xml` file in the `/opt/solr/server/solr/configsets/nutch/conf/` directory, allowing you to define specific fields for data indexing.

#### Data Retrieval
To retrieve data from the `solr` container, python scripts are used. The `python` container is used to run `app.py` which retrieves data from the `solr` container and stores it in the MongoDB database.
