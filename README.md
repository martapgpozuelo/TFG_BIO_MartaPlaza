# Bachelor’s Thesis – Heart Rate Variability (HRV) Analysis

This repository contains the code developed for the Bachelor’s Thesis, focused on the analysis of Heart Rate Variability (HRV) using publicly available physiological databases from PhysioNet.

The analysis is implemented using Jupyter Notebooks and follows a structured workflow, from signal processing to statistical analysis.

## Repository contents

The repository is organized into the following notebooks:

- **NSR-DB.ipynb**  
  This notebook performs an HRV analysis based on the *Normal Sinus Rhythm Database (NSRDB)* available on PhysioNet.  
  The study is carried out using data from the following source:  
  [Normal Sinus Rhythm Database (PhysioNet)](https://www.physionet.org/content/nsrdb/1.0.0/)  

  The notebook includes signal preprocessing, HRV feature extraction, and analysis derived from this database.  
  Due to its moderate size, this notebook can be visualized directly within GitHub.

- **MIT_BIT_Arrythmia_Database.ipynb**  
  This notebook performs the same type of HRV study using the *MIT-BIH Arrhythmia Database*, also available on PhysioNet:  
  [MIT-BIH Arrhythmia Database (PhysioNet)](https://physionet.org/content/mitdb/1.0.0/)  

  Since this database contains a larger number of records and the notebook includes extensive outputs (signal visualizations, intermediate results, and plots), the file size is significantly larger.  
  As a result, **GitHub does not support direct visualization of this notebook in the browser**.  
  However, the file **can be downloaded and executed without any issues** using Jupyter Notebook or Google Colab, where all outputs are displayed correctly.

- **StatisticalAnalysis.ipynb**  
  This notebook contains the statistical analysis of the extracted HRV parameters.

## Execution environment

All notebooks are designed to be executed either locally using Jupyter Notebook or in a cloud-based environment such as **Google Colab**.  
The required libraries and dependencies are specified within the notebooks.
