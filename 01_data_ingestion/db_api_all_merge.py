import os
import pandas as pd

def combine_all_csv_files(input_folder, output_file):
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"The directory {input_folder} does not exist.")
    
    files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    if not files:
        print("No CSV files found in the directory.")
        return
    
    dfs = []
    for file in files:
        file_path = os.path.join(input_folder, file)
        df = pd.read_csv(file_path)
        dfs.append(df)
    
    combined_df = pd.concat(dfs, ignore_index=True)
    
    combined_df.to_csv(output_file, index=False)
    print(f"All CSV files in '{input_folder}' have been combined into '{output_file}'.")
    
input_folder = '././01_data/02_intermediate'
output_file = '././01_data/03_processed/combined.csv'

combine_all_csv_files(input_folder, output_file)