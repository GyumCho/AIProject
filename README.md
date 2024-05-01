# AIProject
AIProject-CALL grammar correction 

Fine-tuned model files:
- pszemraj/grammar-synthesis-small - https://drive.google.com/drive/folders/1U85SfX2anaKqhgk0LXlyQntxz041klu3?usp=sharing
- prithivida/grammar_error_correcter_v1 - https://drive.google.com/drive/folders/1GX0CTUZ3AvGU7IfmQc4pGiKxGUrf65m9?usp=drive_link

Description of jupyter notebooks:
1. Preprocessing
2. - 2.1 Compute correct sentences
   - 2.2 Comparison analysis between error frequencies of French, Italian and Spanish languages
4. Recreate a dataset with the target frequencies from a larger dataset
5. Train and evaluate the model

Description of content:
1. Inside the main folder, you can check the report which include all contents and process of the project
2. Inside the main folder, you can check the final presentation which include major steps and impact of the project

To run the model:
1. Open up your IDE (I kindly suggest to use Jupyter notebook)
2. Prepare a training csv file with user's language usage
3. Run through 5 ipynb files to check the process of the training and testing.
4. If you want to test with your own language set, make sure to change the name of test file
5. Requirements.txt file is important for environemnt file, make sure the file is in same directory with ipynb files.

The requirements.txt file was generated using an anaconda environment with python v3.10.13.
