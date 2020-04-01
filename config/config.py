with open("./config/databaseconfig", "r") as file:
    for line in file:
        globals()[line.split("=")[0].strip()] = line.split("=")[1].strip()

clientid = '66089243330-0v89mjjn6bvlfhqhjskqlio6gq14vcqe.apps.googleusercontent.com'
clientsecret = 'a1P2nBT4vxEkPud3ZlgPWtK8'

SECRET_KEY = '8=5&jz29rqci3$n-+9#i=s32e&ls%47m!0rmkju!4j=_18yftb',

HEROKU_NAME = 'd85nbjor0qa3nf'
HEROKU_USER = 'zbswqwdpozylvm'
HEROKU_PASSWORD = '5cab2ee3e064a7aa73ff202a98d588c65093e3023d04f908ea27d0b775b5dfb4'
HEROKU_HOST = 'ec2-54-152-175-141.compute-1.amazonaws.com'
HEROKU_PORT = '5432'
TRAVIS_USER = 'postgres'
TRAVIS_NAME = 'pdnj'
