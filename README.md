# first-inclassapp-october-2023
23Oct2023 First App Development (Unemployment Report) 

## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

Install packages:
```sh
pip install -r requirements.txt
```

## Email Setup
Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

# or

If you get errors, try Mailgun:
    Instructions and corresponding email sending code to a new "Mailgun" section in the email sending notebook:
    https://colab.research.google.com/drive/1fiTIru-RmPV2s0nsy5SHh3Nn3ffOZioS?usp=sharing

## Follow Setup
Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...
ALPHAVANTAGE_API_KEY="_________"

SENDGRID_API_KEY="_________"
SENDER_ADDRESS="example.gmail.com"

# SENDGRID_API_KEY = getpass("Please input your Sendgrid API Key: ")
# SENDER_ADDRESS = getpass("Please input your Sender Email Address: ")


# OR

## MAIL GUN SET UP:
# example ".env file" contents:
MAILGUN_API_KEY="______________"
MAILGUN_SENDER_ADDRESS="example@school.edu"
MAILGUN_DOMAIN="______________.mailgun.org"

```


## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:
```sh
pip install -r requirements.txt

# python app/unemployment.py
python -m app.unemployment

#To avoid inputting the API key every single time:

ALPHAVANTAGE_API_KEY="abc123" python app/unemployment.py
```


Send an email:
```sh
python app/email.service.py
```




## Testing

Run rests:
```sh
pytest
```