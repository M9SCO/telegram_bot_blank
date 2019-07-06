import logging
import json
#from  bin.database import db_command as db_request
const = json.loads(open("bin/constants").read())


logging.basicConfig(filename='find_ exeption.log',
                    format='--- %(asctime)s ---\n%(filename)s %(levelname)s in line %(lineno)s \n%(message)s',
                    level=logging.ERROR)

print('data opened')