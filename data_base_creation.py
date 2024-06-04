from data_base_function import*


connection=create_db_connection("localhost","Karol","sqlserwer1","projekt")

config_querry= """
CREATE TABLE sentiment_data (
    news_id INT AUTO_INCREMENT PRIMARY KEY,
    news_date VARCHAR(30),
    stock_symbol VARCHAR(40),
    sentiment_score FLOAT
);
"""

delete_querry="""
DROP TABLE sentiment_data;
"""

execute_query(connection,config_querry)

connection.commit()

connection.close()