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
pip install requirements.txt
```

Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:
```sh
pip install -r requirements.txt

python app/unemployment.py

#To avoid inputting the API key every single time:

ALPHAVANTAGE_API_KEY="abc123" python app/unemployment.py

```

