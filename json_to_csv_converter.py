import json
import pandas as pd

# List of JSON file paths and their corresponding desired output CSV names
files = {
    'C:\\Users\\joysa\\OneDrive\\Living in the US\\Tableau Public\\yelp_dataset\\yelp_academic_dataset_business.json': 'yelp_academic_dataset_business.csv',
    'C:\\Users\\joysa\\OneDrive\\Living in the US\\Tableau Public\\yelp_dataset\\yelp_academic_dataset_checkin.json': 'yelp_academic_dataset_checkin.csv',
    'C:\\Users\\joysa\\OneDrive\\Living in the US\\Tableau Public\\yelp_dataset\\yelp_academic_dataset_review.json': 'yelp_academic_dataset_review.csv',
    'C:\\Users\\joysa\\OneDrive\\Living in the US\\Tableau Public\\yelp_dataset\\yelp_academic_dataset_tip.json': 'yelp_academic_dataset_tip.csv',
    'C:\\Users\\joysa\\OneDrive\\Living in the US\\Tableau Public\\yelp_dataset\\yelp_academic_dataset_user.json': 'yelp_academic_dataset_user.csv'
}

for input_path, output_name in files.items():
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))

    df = pd.DataFrame(data)
    output_path = input_path.rsplit('\\', 1)[0] + '\\' + output_name  # Saving the CSV in the same directory as the JSON files
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
