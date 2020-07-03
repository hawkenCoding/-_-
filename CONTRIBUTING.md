# Contribution guidelines

These guidelines are inspired by the contribution guidelines in our other project, [hawkencoding.github.io](https://github.com/hawkenCoding/hawkenCoding.github.io/blob/master/README.md).

## Basics

- Never commit directly to the `master` branch. This is because the `master` branch is set up to automatically deploy to the Heroku app. Every time you push a commit to `master`, Heroku will begin the build process using the new code. If your code causes something bad to happen, that change will immediately be reflected in the live copy of the bot. Instead, use a topic branch and pull requests.

- Follow good Python coding practices and style. For example, use variables names like `descriptive_name`, not `confusingAndLongName`. 

- Use a lot of descriptive comments in your code. It is better to over-comment than under-comment. Remember that this project is designed to be educational, and what's obvious to you may not be obvious for everyone.

- Have fun and don't be afraid to try out something new!

## Getting started

Follow these steps to start working on the bot.

1. On your system's command line environment, navigate to the folder where you keep other programming projects. 

2. Type `git clone https://github.com/hawkenCoding/-_-` (or copy/paste it) and press .

3. Make a virtual environment. Virtual environments are a way to isolate this project's dependencies from those of other projects. If you don't know how to do this, Google it.

4. Run `pip install -r requirements.txt` to actually install the requirements for this project.

If you want to add something new to the bot, follow the instructions under the Add a new feature section. If you want to run the bot yourself, see the Testing section to learn how.

## Adding a new feature

For easy organization, this bot is split into different cogs. You can think of each cog as a separate functionality of the bot.

1. Create a new branch in the git repository using `git checkout -b [name]`, where `[name]` is the name of your new feature.

1. In the project directory, run `python -m discord newcog [name]` to create a new cog.

1. Add the newly created cog to the new branch using `git add cogs/[name].py`.

1. Find and open the new file that was created under the `/cogs/` directory.

1. To add a new command, create a new method inside the class that was generated. Right on top of the `def` statement, add `@commands.command` to let the API know that this is a new command. The first parameter should be `self` (as always), and the second parameter should be `ctx`, the object that your command will use to interact with Discord. 

1. Commit your changes using `git commit -m "added new feature [name]"`. If you make further edits, `git add` and `git commit` again.

1. Test that your code is working! This is an important step. Follow the instructions under the Testing section.

1. Push your code up to the GitHub using `git push origin [name]`. To see your uploaded code, go to the GitHub repository and change the branch from `master` to `[name]`.

1. Open a pull request on GitHub to get your feature added to the actual bot on the Hawken Coding Club Discord server.

For more details on how to implement your feature, see the discord.py documentation.

## Testing

It is important that the bot is tested before it is deployed. Because a Discord bot is designed to work directly with Discord, you need to set up a Discord environment to test your own copy of the bot.

1. Follow the instructions in "Getting started" to get a copy of the repository locally. Run `pip show python_dotenv` to double-check that you have the `python_dotenv` package installed.

1. Set up a Discord server to run your bot on. You can either use an existing server where you have the "Manage Server" permission, or set up a personal server just for testing your bot.

1. Go to the Discord developer portal website. Create a new app. You can name it `-_-` or whatever you want.

1. In the portal, create a bot for your new app. Copy the secret token on the bot page. Do not share this secret key with anyone else.

1. Go to the OAuth2 page. Create a URL for inviting your bot by checking the bot checkbox, then the relevant permissions. If you don't know what permissions to set, just check Administrator (but be careful, since that will allow the bot to do anything a human admin can do).

1. Paste the URL into your browser. Follow the prompts, making sure to select the server you configured earlier. The bot has now been invited to that server but has not yet joined.

1. Go back to your project directory. Create a new file named `.env`. Type `DISCORD_TOKEN=`, then paste in the bot token you copied earlier. On the next line, type `COMMAND_PREFIX=`, then any command prefix you want. 

1. Run the `bot.py` file using `python bot.py` or a configuration in your IDE, if you have one. 

Congratulations! You should now be able to interact with your bot on the configured server. If you're a Hawken Coding Club member and you're having trouble, ask for help on the Hawken Coding Club Discord. 

If your code utilizes a lot of business logic, you can write unit tests using a library like `pytest`. 