import pandas as pd
import numpy as np

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

def clean_data(df):
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Fill missing values or handle incorrect formats
    df.fillna(method='ffill', inplace=True)
    
    # Example: Correcting data types
    df['CreditScore'] = df['CreditScore'].astype(int)
    
    return df

def standardize_data(df):
    # Example: Standardizing column names
    df.columns = [col.lower() for col in df.columns]
    
    # Example: Normalizing numerical data
    df['creditscore'] = (df['creditscore'] - df['creditscore'].mean()) / df['creditscore'].std()
    
    return df