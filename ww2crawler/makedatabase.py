from .database import DataBase
from .analyse_text import analyse_post
from .iterpostsincache import readposts

def insert_in_database(path, database):
    db = DataBase(database)
    for p in readposts(path):
        db.insert_post(
            **analyse_post(p)
            )
    db.flush() # make sure last is inserted
        
