import requests
import openai
from flask import Flask
import csv

API_KEY = open('API_KEY.txt', 'r').read()
API_KEY = API_KEY.strip()
openai.api_key = API_KEY

data = []
with open('trivia.txt', 'r') as file:
    for line in file:
        data.append(line)

prompt = data[16]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
    ]
)

x = response['choices'][0]["message"]["content"]
y = response['choices'][0]["message"]["role"]

print(prompt)
print(x)

default = "Answer to be provided by chatgpt"

# define the column names
columns = ['Prompt', 'Answer']
prompt = prompt.strip('"')
prompt = prompt.strip(',')
data = [[prompt, x]]

"""
# open the CSV file for writing
with open('output.csv', mode='a', newline='') as file:
    # create a CSV writer object
    writer = csv.writer(file)

    # write the data to the file
    for row in data:
        writer.writerow(row)
"""