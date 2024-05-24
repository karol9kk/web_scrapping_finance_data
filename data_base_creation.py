from data_base_function import*


connection=create_db_connection("localhost","Karol","sqlserwer1","projekt")

config_query= """
CREATE TABLE sentiment_data (
    news_id INT AUTO_INCREMENT PRIMARY KEY,
    news_date VARCHAR(14),
    stock_symbol VARCHAR(10),
    sentiment_score FLOAT
);
"""

delete_querry="""
DELETE FROM news_data;
"""

execute_query(connection,config_query)

connection.commit()

connection.close()