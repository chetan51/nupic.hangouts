# nupic.hangouts
An example of using NuPIC to detect anomalies in Google Hangouts conversations.

## Usage

1. Get your data.

    Visit [Google Takeout](https://www.google.com/settings/takeout), select only the "Hangouts" option, and download.
    Extract the `Hangouts.json` file from the downloaded data.

2. Process your data.

   Run `process.py PATH/TO/Hangouts.json PATH/TO/OUTPUT_DIRECTORY`.
