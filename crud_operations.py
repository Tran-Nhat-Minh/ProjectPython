import pandas as pd

def create_record(df, record):
    df = df.append(record, ignore_index=True)
    return df

def read_record(df, index):
    if index < len(df):
        return df.iloc[index]
    else:
        print("Record not found.")
        return None

def update_record(df, index, updated_record):
    if index < len(df):
        df.iloc[index] = updated_record
    else:
        print("Record not found.")
    return df

def delete_record(df, index):
    if index < len(df):
        df.drop(index, inplace=True)
    else:
        print("Record not found.")
    return df