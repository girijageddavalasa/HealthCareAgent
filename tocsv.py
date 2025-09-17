import pandas as pd
from sqlalchemy import create_engine

# Update this with your Postgres credentials and database
DATABASE_URI = 'postgresql://postgres:postgrespassword@localhost:5432/apple_health'

def import_csv_to_postgres(csv_file_path):
    # Create database engine
    engine = create_engine(DATABASE_URI)

    # Load CSV into DataFrame
    df = pd.read_csv(csv_file_path)

    # Rename columns to match table schema
    df.rename(columns={
        'creationDate': 'creation_date',
        'startDate': 'start_date',
        'endDate': 'end_date'
    }, inplace=True)

    # Convert 'value' column to numeric, invalid values become NaN
    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    # Drop rows where 'value' is NaN to avoid insert errors
    df = df.dropna(subset=['value'])

    # Ensure 'unit' column is string type
    df['unit'] = df['unit'].astype(str)

    # Insert DataFrame into Postgres (append to existing table)
    df.to_sql('health_measurements', engine, if_exists='append', index=False)

    print("CSV data imported successfully!")

if __name__ == '__main__':
    csv_path = r'C:\Users\dharm\OneDrive\Desktop\GIRIJADL\Interv\final14\AppleWatch.csv'
    import_csv_to_postgres(csv_path)
