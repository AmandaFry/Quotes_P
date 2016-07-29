from system.core.model import Model
from flask import Flask, flash, session
from datetime import datetime
import re

NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')
THREEPLUS = re.compile(r'^[A-Za-z\d]{3,}$')
TENPLUS = re.compile(r'^[A-Za-z\d]{10,}$')

class QuotesModel(Model):
    def __init__(self):
        super(QuotesModel, self).__init__()

    def addQuote(self, userInfo):
    	query = "INSERT INTO quotes (author, message, uses_id, created_at, updated_at) VALUES (:author, :message, :id, NOW(), NOW());"
    	data = { 
    		'id' : session['id'],
    		'author': userInfo['author'],
    		'message': userInfo['message']
    	}
        addQuote = self.db.query_db(query, data)
        return {"status": True}
 
