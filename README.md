# Automatic Weather Update
Sends an automatic weather update daily
# Below is a step-by-step guide one how to set up the automated email.

## Step 1: Sign up for weatherapi.
The API used is a free weather API called "Weatherapi" (https://www.weatherapi.com/docs/) <br>
Create an account and copy your unique API key


## Step 2: Setting up secret.py
Open secret.py and paste your API key next to the global variable "WEATHER_API_KEY"<br>
Also input your email address beside "EMAIL_ADDRESS" <br>
***creating an app password for Gmail.*** <br>
Due to recent security changes, you will have to generate an app password for your gmail. see: (https://support.google.com/accounts/answer/185833?hl=en)

## Step 3: Setting up weather.py
In weather.py, input your current **city** and **name** into the respective variables

## Step 4: Setting up a cronjob to automate the process
1. Open your terminal
2. input `crontab -e`
3. create a cronjob, see guide on syntax (https://betterprogramming.pub/https-medium-com-ratik96-scheduling-jobs-with-crontab-on-macos-add5a8b26c30) <br>
example for cronjob: `0 8 * * * python3 /Users/josherheng/weather_api_project/email_weather.py` <br>
this code executes at 0800 daily.
4. press `esc` and input `:wq` to save your changes.
5. confirm that you have created a cronfile with `crontab -l`

## crongratulations! you're all set up!
