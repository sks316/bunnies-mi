# bunnies-mi

[![love-badge][]][love] [![mipy-badge][]][mipy]

[![follow-badge][]][follow]

A bunnyposting bot for Misskey! Posts bunnies to the Fediverse every hour.

## Running the bot

First, clone the bot. Then, install dependencies:

```
pip install -r requirements.txt
```

Now make a new file named `config.py` in the bot's directory. Paste the following:

```
homeserver = "YOUR-HOMESERVER-HERE"
token = "YOUR-TOKEN-HERE"
```

Replace `YOUR-HOMESERVER-HERE` with the URL for your Misskey server. Now go to the API section of your account settings and generate a new access key, and replace `YOUR-TOKEN-HERE` with it. Run the bot and you'll be posting cute buns every hour!


[love]: https://lillie2523.carrd.co
[love-badge]: https://custom-icon-badges.herokuapp.com/badge/-Made%20with%20love...-555555?style=for-the-badge&logo=heart

[mipy]: https://github.com/yupix/Mi.py
[mipy-badge]: https://custom-icon-badges.herokuapp.com/badge/-...and%20mi.py-555555?style=for-the-badge&logo=misskey

[follow]: https://stop.voring.me/@bunnies
[follow-badge]: https://custom-icon-badges.herokuapp.com/badge/-follow%20%40bunnies%40stop.voring.me-555555?style=for-the-badge&logo=misskey