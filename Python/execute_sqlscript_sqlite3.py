import sqlite3
import os
import sys

# python-dotenv to load up all the entries in this file as environment variables so they are accessible with os.environ.get.
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# find root directory path
project_root_path = os.path.dirname(find_dotenv())

# creating a path for DATA and SCRIPTS directory
data_dir = os.path.join(project_root_path, 'DATA')
scripts_dir = os.path.join(project_root_path, 'SCRIPTS')

def execute_sqlite_command(dbpath, scriptpath):
    '''
    Purpose: Runs SQL scripts against the sqlite database but reads no values back. 
             You can use it for create, insert, update and delete statements
    
    Arguments: 
    1) dbpath - the path should include path location including filename
    2) scriptpath - the path should include path location including filename
    
    To do:  Exceptions handling. The current exception handling does nothing
            except tell you “something” went wrong.
    '''
    try:
        # sql connection
        cnx = sqlite3.connect(dbpath)
        cur = cnx.cursor()
       
        # open and close scriptfile after the script has been read
        scriptFile = open(scriptpath, 'r')
        script = scriptFile.read()
        scriptFile.close()
    
        # executescript method executes every line of the SQL script separated by ';'
        # as well as hits commit after everything is done.
        cur.executescript(script)
        #cur.executescript('drop table if exists paper_authors;')   
        
        # hit commit if everything has gone to satisfaction
        cnx.commit()

    except Exception:
        print ("Something went wrong:%s",Exception)


    finally:    
        cnx.close()

# RELEASE THE KRAKEN!

execute_sqlite_command(dbpath = os.path.join(data_dir, 'database.sqlite'),
                       scriptpath = os.path.join(scripts_dir,'import.sql'))