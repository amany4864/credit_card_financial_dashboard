import pandas as pd
import os
import logging
import time
from sqlalchemy import create_engine
from dotenv import load_dotenv

#Setup Logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

#Load Environment
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

#Create Engine
try:
    engine = create_engine(
        f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    )
    logging.info("Successfully connected to MySQL database.")
except Exception as e:
    logging.error(f"Failed to connect to MySQL: {e}")
    raise

#Ingestion Function
def ingest_db(df, table_name, engine):
    try:
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        logging.info(f"Appended {len(df)} rows into `{table_name}`.")
        return True 
    except Exception as e:
        logging.error(f"Failed to ingest `{table_name}`: {e}")
        return False 

#Loader 
def load_raw_data_continuously(check_interval_seconds=900):
    
    processed_files = set() 
    
    while True: 
        try:
            logging.info("Checking for new files...")
            data_path = 'data'
            
            # Get the list of current CSV files in the directory
            current_files = {file for file in os.listdir(data_path) if file.endswith('.csv')}
            
            # Determine which files are new
            new_files = current_files - processed_files #Set difference to find new files
            
            if not new_files:
                logging.info("No new files found. Waiting for next check.")
            else:
                for file in new_files: 
                    try:
                        file_path = os.path.join(data_path, file)
                        df = pd.read_csv(file_path)

                        #Match table name based on filename
                        if "customer" in file.lower():
                            table_name = "customer"
                        elif "transaction" in file.lower():
                            table_name = "transaction"
                        else:
                            table_name = file.replace('.csv', '')

                        logging.info(f"New file found: {file} → will append to `{table_name}` table")
                        
                        success = ingest_db(df, table_name, engine)
                        if success:
                            processed_files.add(file) #Add to our 'memory' set
                            
                    except Exception as e:
                        logging.error(f"Error processing file `{file}`: {e}")

            #Wait before checking again
            time.sleep(check_interval_seconds)
            
        except Exception as e:
            logging.critical(f"A critical error occurred in the main loop: {e}")
            time.sleep(60) 


if __name__ == '__main__':

    load_raw_data_continuously(check_interval_seconds=5400)
    

