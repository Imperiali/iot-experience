import pandas as pd

dataset_1_1_data = pd.read_csv("../../Data/Raw/01_Steps.csv")
dataset_1_2_data = pd.read_csv("../../Data/Raw/02_Sleep.csv")

dataset_1_data_certo = pd.merge(dataset_1_1_data, dataset_1_2_data, on='date', how='outer')

dataset_1_data_certo.to_csv(r"../../Data/Processed/datasetConcatAT.csv", index=False)