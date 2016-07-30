from system.core.model import Model
from flask import Flask, flash, session


class QuotesModel(Model):
    def __init__(self):
        super(QuotesModel, self).__init__()

    def addQuote(self, userInfo):
    	errors=[]

        #inital verification before inserting to database
        if len(userInfo['author']) < 3:
            errors.append("Author needs to be at least 3 charcter long")
        elif len(userInfo['message']) < 10:
            errors.append("Quote needs to be at least 10 charcter long")
        if errors:
            return {'status' : False, 'errors' : errors}
        else:
	    	query = "INSERT INTO quotes (author, message, uses_id, created_at, updated_at) VALUES (:author, :message, :id, NOW(), NOW());"
	    	data = { 
	    		'id' : session['id'],
	    		'author': userInfo['author'],
	    		'message': userInfo['message']
	    	}
	        addQuote = self.db.query_db(query, data)
	        return {"status": True}

    def allQuote(self):
    	query = "SELECT  quotes.id as quotesID, quotes.message, users.id as userID, users.first_name FROM quotes JOIN users ON quotes.uses_id = users.id WHERE quotes.id NOT IN (SELECT quote_id from quotes JOIN favorites ON quotes.id = favorites.quote_id where user_id = :id)"
    	data = { 'id': session['id']}
    	allQuote = self.db.query_db(query, data)
    	return (allQuote)

    def userEntries(self, id):
    	query = "SELECT quotes.author, quotes.message, users.id as userID, users.first_name FROM quotes JOIN users ON quotes.uses_id = users.id WHERE uses_id = :id"
    	data = { 'id': id}
    	userEntries = self.db.query_db(query, data)
    	return (userEntries)

    def entryCount(self,id):
    	# how many total entries there are
    	query = "SELECT COUNT(*) AS total FROM quotes WHERE uses_ID = :id"
    	data = { 'id': id}
    	result = self.db.query_db(query, data)
    	entryCount = int(result[0]['total'])
    	return (entryCount)

    def addFav(self, id):
    	query = "INSERT INTO favorites (user_id, quote_id, created_at, updated_at) VALUES (:user_id, :quote_id, NOW(), NOW());"
    	data = { 
    		'user_id' : session['id'],
    		'quote_id': id
    	}
        addFav = self.db.query_db(query, data)
        return {"status": True}

    def allFav(self):
    	query ="SELECT favorites.quote_id as favQID, quotes.author, quotes.message, users.id as userID, users.first_name FROM quotes JOIN users ON quotes.uses_id = users.id JOIN favorites ON quotes.id = favorites.quote_id where user_id = :id"
    	data = {'id': session['id'] }
    	allFav = self.db.query_db(query, data)
    	return (allFav)


    def removeFav(self, id):
    	query = "DELETE FROM favorites WHERE quote_id = :id"
    	data = { 'id': id}
    	removeFav = self.db.query_db(query, data)
        return {"status": True}

