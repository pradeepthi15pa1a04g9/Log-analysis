## Log-analysis Project

### Overview

In this project I was tasked to create a reporting tool which can print reports based on real world web-application data, with fields representing informaton that a webserver would record, such as status codes and URL paths. This reporting tool is use Python program using  'psycopg2' module to connect the database.
  * The **authors** table includes information about the authors of articles.
  * The **articles** table includes the articles themselves.
  * The **log** table includes one entry for each time a user has accessed the site.
  
#### The project drives following conclusions:
   * Most popular three articles of all time.
   * Most popular article authors of all time.
   * Days on which more than 1% of requests lead to error.
   
#### PreRequisites:
  * Python
  * Vagrant
  * Virual box

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading 


#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
 ```
    $ vagrant up
  ```
  2. Then Log into this using command:
   
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.
  
#### Setting up the database:
 Load the data in local database using the command:
   
  ```
    psql -d news -f newsdata.sql
  ```
    
#### Running the Program:
1. Within the VM, navigate to 'cd  /vagrant'
2. Run 'psql'
3. Connect to the database '\c  news'
4. Enter the views listed above
5. Exit 'psql'
