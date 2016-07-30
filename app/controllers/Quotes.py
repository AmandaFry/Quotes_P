from system.core.controller import *
from flask import Flask, flash, session, request, redirect

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        self.load_model('QuotesModel')

    def dashboard(self):
        # need this if people just type in the dashbaord you need to be pass login to get here.
        try:
            session['id']
        except:
            return redirect ('/')
        allQuote = self.models['QuotesModel'].allQuote()
        allFav = self.models['QuotesModel'].allFav()
        print allFav
        return self.load_view('dashboard.html', allQuote=allQuote, allFav=allFav)

    def addQuote(self):
        #add new quote
        userInfo = {
            'author':request.form['author'],
            'message':request.form['message']
        }
        addnew = self.models['QuotesModel'].addQuote(userInfo)
        if addnew['status']  == False:
            #return to logon page and show errors
            for message in addnew['errors']:
                flash(message)
            return redirect('/dashboard')
        else:
            return redirect('/dashboard')

    def addFav(self, id):
        #make a quote a favorite
        addFav = self.models['QuotesModel'].addFav(id)
        return redirect('/dashboard')

    def removeFav(self,id):
        #remove a quote from favorite list
        removeFav = self.models['QuotesModel'].removeFav(id)
        return redirect('/dashboard')

    def userEntries(self, id):
        #show all of the qoutes the user created
        entries = self.models['QuotesModel'].userEntries(id)
        #show the count of the number of quotes
        entryCount = self.models['QuotesModel'].entryCount(id)
        return self.load_view('userDetail.html', entries=entries, entryCount=entryCount)


