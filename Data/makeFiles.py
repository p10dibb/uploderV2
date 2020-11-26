import os;


path=os.getcwd()



runnerFile=open("runCopies.sql","w")

runnerFile.write('SET CLIENT_ENCODING TO \'utf8\';\n')
runnerFile.write('CREATE TABLE Business( business_id CHAR(22) NOT NULL, name VARCHAR(300),address VARCHAR(300),city VARCHAR(50),state CHAR(2),zipcode VARCHAR(30),latitude double precision,longitude double precision,stars double precision,numTips INTEGER,is_open INTEGER,numCheckins INTEGER,PRIMARY KEY (business_id));\n')
runnerFile.write('COPY business FROM \''+path+'/Data/business.csv\' DELIMITER \',\' CSV HEADER;\n')
runnerFile.write('CREATE TABLE Users (average_stars FLOAT,cool   INTEGER,fans INTEGER,funny INTEGER,usefull INTEGER,name VARCHAR(50),tipcount INTEGER,user_id VARCHAR(22) PRIMARY KEY NOT NULL,yelping_since VARCHAR(30),total_likes  INTEGER);\n')

for i in range(0,5):
    runnerFile.write(' COPY users FROM \''+path+'/Data/users'+str(i)+'.csv\' DELIMITER \',\' CSV HEADER;\n')
runnerFile.write('CREATE TABLE Friends(user_id VARCHAR(22) NOT NULL,friend_id VARCHAR(22) NOT NULL,PRIMARY KEY(user_id,friend_id),FOREIGN KEY(user_id) REFERENCES Users(user_id),FOREIGN KEY(friend_id) REFERENCES Users(user_id));\n')
for i in range(0,20):
    runnerFile.write('COPY friends FROM \''+path+'/Data/friends'+str(i)+'.csv\' DELIMITER \',\' CSV HEADER;\n')

runnerFile.write('CREATE TABLE Tip(tip_text VARCHAR,likes INTEGER,user_id VARCHAR NOT NULL,business_id VARCHAR NOT NULL,day Integer NOT NULL,month Integer NOT NULL,year Integer NOT NULL,hour Integer NOT NULL,minute Integer NOT NULL,second INteger NOT NULL,PRIMARY KEY(business_id,user_id,year,month,day,hour,minute,second),FOREIGN KEY(business_id) REFERENCES Business(business_id),FOREIGN KEY(user_id) REFERENCES Users(user_id));\n')
for i in range(0,4):
    runnerFile.write('COPY tip FROM \''+path+'/Data/tips'+str(i)+'.csv\' DELIMITER \'<\' CSV HEADER;\n')

runnerFile.write('CREATE TABLE Review(Review_ID VARCHAR(30) PRIMARY KEY NOT NULL,User_ID VARCHAR(30),Business_ID VARCHAR(30),Stars FLOAT,Useful INTEGER,Funny INTEGER,Cool Integer,Text VARCHAR(1000000),Day Integer NOT NULL,Month Integer NOT NULL,Year Integer NOT NULL,Hour Integer NOT NULL,Minute Integer NOT NULL,Second INteger NOT NULL,FOREIGN KEY (User_ID) References Users(user_id),FOREIGN KEY (Business_ID) References Business(business_id));\n')
for i in range(0,161):
    runnerFile.write('COPY review FROM \''+path+'/Data/review'+str(i)+'.csv\' DELIMITER \'<\' CSV HEADER;\n')

runnerFile.write('CREATE TABLE  Attributes(business_id CHAR(22) NOT NULL,attribute_key VARCHAR(50) NOT NULL,attribute VARCHAR(300),FOREIGN KEY (business_id) REFERENCES Business(business_id),PRIMARY KEY (business_id,attribute_key));\n')
runnerFile.write('COPY attributes FROM \''+path+'/Data/attributes.csv\' DELIMITER \',\' CSV HEADER;\n')

runnerFile.write('CREATE TABLE Categories(business_id char(22) NOT NULL,category VARCHAR(50) NOT NULL,FOREIGN KEY (business_id) REFERENCES Business(business_id),PRIMARY KEY (business_id,category));\n')
runnerFile.write('COPY categories FROM \''+path+'/Data/categories.csv\' DELIMITER \',\' CSV HEADER;\n')

runnerFile.write('CREATE TABLE Hours(business_id CHAR(22) NOT NULL, day VARCHAR(10) NOT NULL, open_time VARCHAR(5),close_time VARCHAR(5),FOREIGN KEY (business_id) REFERENCES Business(business_id), PRIMARY KEY (business_id,day));\n')
runnerFile.write('COPY hours FROM \''+path+'/Data/hours.csv\' DELIMITER \',\' CSV HEADER;\n')

runnerFile.write('  CREATE TABLE Checkin(business_id VARCHAR(22) NOT NULL,year  INTEGER NOT NULL,month INTEGER NOT NULL,day INTEGER NOT NULL, hour INTEGER NOT NULL, minute INTEGER NOT NULL,second INTEGER NOT NULL,PRIMARY KEY (business_id,year,month,day,hour,minute,second),FOREIGN KEY (business_id) REFERENCES Business(business_id));\n')
for i in range(0,200):
    runnerFile.write('COPY checkin FROM \''+path+'/Data/checkin'+str(i)+'.csv\' DELIMITER \',\' CSV HEADER;\n')
