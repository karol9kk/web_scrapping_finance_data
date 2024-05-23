from data_base_function import*


connection=create_db_connection("localhost","Karol","sqlserwer1","projekt")

config_query= """
CREATE TABLE news_data (
    news_id INT AUTO_INCREMENT PRIMARY KEY,
    news_date DATE,
    company_name VARCHAR(255),
    sentiment_score FLOAT
);
"""

delete_querry="""
DELETE FROM news_data;
"""

execute_query(connection,delete_querry)

connection.commit()

connection.close()