# Load Database pacakge

import sqlite3

conn = sqlite3.connect('C:/Users/dj/OneDrive/Desktop/NLP Project/App/database.db')
c = conn.cursor()

# Fxn
def create_page_visited_table():
    c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')

def add_page_visited_details(pagename, timeOfvisit):
    c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?, ?)', (pagename, timeOfvisit))
    conn.commit()

def view_all_page_visited_details():
    c.execute('SELECT * FROM pageTrackTable')
    data = c.fetchall()
    return data

# Fxn To Track Input & Prediction
def create_emotionclf_table():
    c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT, prediction TEXT, probability NUMBER, timeOfvisit TIMESTAMP)')

def add_prediction_details(rawtext, prediction, probability, timeOfvisit):
    c.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit) VALUES (?, ?, ?, ?)', (rawtext, prediction, probability, timeOfvisit))
    conn.commit()

def view_all_prediction_details():
    c.execute('SELECT * FROM emotionclfTable')
    data = c.fetchall()
    return data

# app.py

import streamlit as st
from datetime import datetime
from track_utils import create_page_visited_table, add_page_visited_details, view_all_page_visited_details, create_emotionclf_table, add_prediction_details, view_all_prediction_details

# Rest of the code

def main():
    # Create a database connection
    conn = sqlite3.connect('C:/Users/dj/OneDrive/Desktop/NLP Project/App/database.db')

    # Create the necessary tables
    create_page_visited_table()
    create_emotionclf_table()

    # Rest of the code

if __name__ == '__main__':
    main()
