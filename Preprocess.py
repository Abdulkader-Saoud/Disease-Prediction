import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('datasetV1.csv')

diseases = data['Disease']

data = data.drop('Disease', axis=1)

one_hot_encoded_data = pd.get_dummies(data, prefix='', prefix_sep='')

merged_data = one_hot_encoded_data.groupby(axis=1, level=0).max()

processed_data = pd.concat([diseases, merged_data], axis=1)

disease_label_encoder = LabelEncoder()
processed_data['Disease'] = disease_label_encoder.fit_transform(processed_data['Disease'])

encoded_diseases_df = pd.DataFrame({'Encoded_Disease': processed_data['Disease'], 'Disease': diseases})
encoded_diseases_df = encoded_diseases_df.drop_duplicates()

# processed_data.to_csv('processed_data.csv', index=False)

# encoded_diseases_df.to_csv('encoded_diseases.csv', index=False)