# nupic.hangouts
An example of using NuPIC to detect anomalies in Google Hangouts conversations.

## Usage

1. Install.

    > python setup.py install --user

2. Get your data.

    Visit [Google Takeout](https://www.google.com/settings/takeout), select only the "Hangouts" option, and download.
    Extract the `Hangouts.json` file from the downloaded data.

3. Process your data.

    > python -m nupic_hangouts.scripts.process PATH/TO/Hangouts.json data

4. Run a conversation through a NuPIC model and plot results.

    Pick a conversation in the `data` directory (one of the `.csv` files). The number in the name of the `.csv` file indicates how many total messages are in the conversation.

    >  ./model.py PATH/TO/CONVERSATION.csv output
