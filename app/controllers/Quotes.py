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
        return self.load_view('dashboard.html')

    def addQuote(self):
        #add new quote
        return redirect('/dashboard')

    def addFavorite(self, id):
        #make a quote a favorite
        return redirect('/dashboard')

    def removeFavorite(self,id):
        #remove a quote from favorite list
        return redirect('/dashboard')

    def userEntrie(self):
        #show all of the qoutes the user created
        #show the count of the number of quotes
        return self.load_view('userDetails.html')


