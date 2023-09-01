import sqlite3
from textblob import TextBlob

# Establish a connection to SQLite database
conn = sqlite3.connect('C:\\Users\\joysa\\OneDrive\\Living in the US\\Tableau Public\\yelp_dataset\\Yelp_Database.db')
cursor = conn.cursor()

# Fetch tip_text data from the PopularBusiness table
cursor.execute("SELECT tip_text FROM PopularBusiness WHERE tip_text IS NOT NULL;")
tips = cursor.fetchall()

# Perform sentiment analysis
sentiments = []
for tip in tips:
    blob = TextBlob(tip[0])
    sentiments.append((blob.sentiment.polarity, blob.sentiment.subjectivity, tip[0]))

# Add columns for polarity and subjectivity if they don't exist
try:
    cursor.execute("ALTER TABLE PopularBusiness ADD COLUMN polarity REAL;")
    cursor.execute("ALTER TABLE PopularBusiness ADD COLUMN subjectivity REAL;")
except sqlite3.OperationalError:  # columns already exist
    pass

# Update the PopularBusiness table with sentiment scores
cursor.executemany("UPDATE PopularBusiness SET polarity=?, subjectivity=? WHERE tip_text=?;", sentiments)

# Commit changes to the database
conn.commit()

# Close the connection
conn.close()
