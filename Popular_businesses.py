import sqlite3

conn = sqlite3.connect('C:\\Users\\joysa\\OneDrive\\Living in the US\\Tableau Public\\yelp_dataset\\Yelp_Database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE PopularBusiness AS
SELECT
    pb.business_id,
    pb.name,
    pb.city,
    pb.state,
    pb.categories,
    pb.avg_rating,
    pb.total_reviews,
    r.user_id,
    u.name AS user_name,
    u.yelping_since,
    r.stars AS review_stars,
    r.date AS review_date,
    t.text AS tip_text,
    t.date AS tip_date
FROM (    
    SELECT
        business_id,
        name,
        city,
        state,
        categories,
        AVG(stars) AS avg_rating,
        SUM(review_count) AS total_reviews
    FROM business
    GROUP BY business_id, name, city, state, categories
    HAVING avg_rating > 4.5 AND total_reviews > 100
    LIMIT 50) pb
JOIN review r ON pb.business_id = r.business_id
JOIN user u ON r.user_id = u.user_id
LEFT JOIN tip t ON pb.business_id = t.business_id AND r.user_id = t.user_id;
""")

# Commit the transaction
conn.commit()

# Close the connection
conn.close()



