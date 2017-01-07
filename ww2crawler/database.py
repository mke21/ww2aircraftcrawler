#!/usr/bin/env python3
import sqlite3 as lite
from os.path import exists

class DataBase(object):
    """
    Object to connect to a database,
    When not exists, it will create the file and structure
    """
    def __init__(self, path):
        """
        path = path to location where file should be
        """
        created = exists(path)
        # create connection
        self.con = lite.connect(path)
        
        if not created:
            self.create_structure()
            self.id = 0
        else:
            cur = self.con.cursor()
            cur.execute("SELECT MAX(id) from Posts")
            self.id = cur.fetchone()[0]
        if not self.id: self.id = 0    

        self.postbuffer = []
        self.acbuffer = []

    def __insert(self, sql, values):
        with self.con:
            try:
                cur = self.con.cursor()
                cur.executemany(sql, values)
            except lite.Error:
                if self.con:
                    self.con.rollback()
                raise
            
    def create_structure(self):
        with self.con:
            cur = self.con.cursor()
            # posts table
            cur.execute(
                """
                CREATE TABLE Posts(
                    id INTEGER PRIMARY KEY,
                    month INTEGER,
                    year INTEGER,
                    author TEXT,
                    postno INTEGER
                )"""
                )
            cur.execute(
                """
                CREATE TABLE Aircraft(
                    post INTEGER,
                    name TEXT,
                    FOREIGN KEY(post) REFERENCES Posts(rowid)
                    )
                """
                )

    def flush(self):
        if self.postbuffer:
            self.__insert(
                "INSERT INTO Posts VALUES(?,?,?,?,?)",
                self.postbuffer
                )
            self.__insert(
                "INSERT INTO Aircraft VALUES(?,?)",
                self.acbuffer
                )
            self.postbuffer = []
            self.acbuffer = []
            
    def insert_post(self, month, year, author, postno, aircraft):
        """
        aircraft = list of aircraft names
        returns 0 if not inserted
        returns id of post if inserted
        """
        if not aircraft:
            # ignore the ones without aircraft names
            return
        else:
            self.id += 1
            self.postbuffer.append(
                (self.id, int(month), int(year), author, int(postno))
                )
            self.acbuffer += [ (self.id, a) for a in aircraft ]
            if len(self.postbuffer) >= 50000:
                self.flush()

