# nupic.hangouts
An example of using NuPIC to detect anomalies in Google Hangouts conversations.

## Usage

1. Install dependencies.

    Follow installation instructions for [Unicorn](https://github.com/numenta/numenta-apps/tree/master/unicorn).
    
    Install [matplotlib](http://matplotlib.org/).

2. Install nupic.hangouts.

    > python setup.py install --user

3. Get your data.

    Visit [Google Takeout](https://www.google.com/settings/takeout), select only the "Hangouts" option, and download.
    Extract the `Hangouts.json` file from the downloaded data.

4. Process your data.

    > python -m nupic_hangouts.scripts.process PATH/TO/Hangouts.json data

5. Run a conversation through a NuPIC model and plot results.

    Pick a conversation in the `data` directory (one of the `.csv` files). The number in the name of the `.csv` file indicates how many total messages are in the conversation.

    >  ./model.py PATH/TO/CONVERSATION.csv output

## Example output

![Example Output](https://raw.githubusercontent.com/chetan51/nupic.hangouts/master/images/example.png)
_The red triangles are points of high anomaly._
