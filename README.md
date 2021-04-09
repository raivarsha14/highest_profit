# highest_profit challenge by SADA U

Thanks to SADA U for providing the opportunity to participate in the challenge.

This repo is about solving the highest profit challenge. The challange asked to read a CSV file as RAW from GitHub repo and then answer the 3 questions asked based on the data.

The challenge is completed using Python. I decided to use Pandas library as the data is relatively small.
To filter out non-numeric profit values, I first converted the profit column to numeric type forcing the non-numeric values to be replaced by NaN (null) and then dropping the rows where profit column contains NaN values.

To run the script, you can run the 'run.sh' script by executing the following command on the terminal after changing to the folder where you have cloned this repo:
`sh run.sh`

That will produce answers to all 3 questions asked in the challenge.

The highest_profit.py file has the python code used to solve the problem. Why the certain code is being used, has been explained in the file using in-line comments.