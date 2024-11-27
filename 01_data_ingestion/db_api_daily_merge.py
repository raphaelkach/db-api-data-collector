import os
import pandas as pd
import logging

logging.basicConfig(filename='empty_files.log', level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def combine_csv_by_date(folder_path, output_folder):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The directory {folder_path} does not exist.")
    
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    date_files = {}

    for file in files:
        parts = file.split('_')
        date = parts[0]
        hour = parts[1][:2]
        if date not in date_files:
            date_files[date] = {}
        date_files[date][hour] = file

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for date, hour_files in date_files.items():
        valid_dfs = []
        
        all_hours = set(f"{i:02d}" for i in range(24))
        missing_hours = all_hours - set(hour_files.keys())
        
        if missing_hours:
            missing_hours_str = ", ".join(sorted(missing_hours))
            logging.warning(f"Missing hours for date {date}: {missing_hours_str}")

        for hour, file in hour_files.items():
            df = pd.read_csv(os.path.join(folder_path, file))
            if df.empty:
                logging.warning(f"The file {file} is empty and will be skipped.")
            else:
                valid_dfs.append(df)
        
        if valid_dfs:
            combined_df = pd.concat(valid_dfs, ignore_index=True)
            combined_df.to_csv(os.path.join(output_folder, f'{date}.csv'), index=False)
            
combine_csv_by_date('././01_data/01_raw/API', '././01_data/02_intermediate')