# CurrencyConv by Amay Doshi, Hemant Purswami and Priyanshi Furiya
HackAI_230429


Currency Exchange Monitor & Alert Agent
Overview
This Currency Exchange Monitor & Alert Agent is a Python application that allows users to monitor exchange rates between a base currency and one or more foreign currencies. Users can set thresholds for alerts, and when the exchange rate crosses these thresholds, they receive notifications. The application uses the uAgent library for agent-based communication and integrates with a currency exchange API for real-time exchange rate data.

Features
•	User Input: Users can input their base currency, one or more foreign currencies (comma-separated), and threshold values (comma-separated) using a graphical user interface (GUI).
•	Real-Time Exchange Rates: The application connects to a currency exchange API to fetch real-time exchange rate data.
•	Threshold Alerts: Users can set thresholds for exchange rate alerts. When the exchange rate crosses these thresholds, the application sends notifications to the user.
•	Agent-Based Communication: The application uses the uAgent library to create agents that communicate with each other. The agents include Alice (the user), Bob (the monitor), and a login agent for collecting user input.
•	Notifications: Notifications are sent to the user using the Twilio API and the Plyer library for desktop notifications.
•	Currency Information: Users can view a list of all available currencies.
•	Modular Structure: The code is organized into functions and classes for better readability and maintainability.

Prerequisites
Before running the application, you need to set up the following:
•	Install the required Python libraries: requests, uagents, plyer, twilio, and tkinter.
•	Obtain an API key for the currency exchange API and set it in the myheader dictionary.

Usage
1.	Run the application by executing the Python script.
2.	The GUI will prompt you to enter your base currency, foreign currencies, and threshold values.
3.	Click the "Show All Currencies" button to view a list of all available currencies.
4.	Click the "Submit" button to save your login information.
5.	The application will continuously monitor exchange rates and send notifications when thresholds are crossed.

Code Organization
•	main.py: The main script that sets up agents, handles user input, and runs the agent-based communication.
•	uagents: A package containing the uAgent library and its dependencies.
•	plyer: Configuration for desktop notifications.
•	tkinter: GUI elements for user input.

Acknowledgments
•	This application is powered by the uAgent library.
•	Exchange rate data is retrieved from the currency exchange API.
•	Notifications are sent using the Plyer library.

Thank you for using the Currency Exchange Monitor & Alert Agent! We hope it helps you stay informed about exchange rate fluctuations.

To generate an API key for the ExchangeRates API provided by apilayer (https://apilayer.com/marketplace/exchangerates_data-api), you can follow these steps:
1.	Visit the apilayer Marketplace: Open your web browser and navigate to the apilayer Marketplace.
2.	Sign Up or Log In: If you don't already have an apilayer account, you will need to sign up for one. If you have an account, log in using your credentials.
3.	Select ExchangeRates API: In the marketplace, find the ExchangeRates API or use the search bar to locate it. Click on the API to view its details.
4.	Pricing and Plans: Review the pricing and plans for the ExchangeRates API. Choose a plan that suits your requirements and budget.
5.	Create an API Key: After subscribing to a plan, you will be able to create an API key. This key is what you will use to authenticate your requests to the ExchangeRates API.
6.	Access and Manage Your API Key: Once your API key is generated, you will typically be shown the key on the screen or sent it via email. Make sure to copy and securely store your API key. You won't be able to access it again from the apilayer website for security reasons.
7.	Start Using the API: You can now start using your API key to make requests to the ExchangeRates API. Include your API key in the headers or query parameters of your HTTP requests, depending on the API's authentication requirements.

To generate an API key and use Twilio for sending SMS messages or making phone calls, you need to follow these steps:
Sign Up for a Twilio Account: If you don't already have a Twilio account, you'll need to sign up for one. Go to the Twilio website (https://www.twilio.com/) and create an account. You may need to provide some personal and payment information.
Log In to your Twilio Dashboard: After creating an account, log in to your Twilio dashboard.

Get Your Account SID and Auth Token: Once logged in, you'll see your Account SID and Auth Token on the dashboard. These are your primary credentials for accessing Twilio's services. Keep them secure and do not share them publicly.

Generate an API Key: To generate an API key, follow these steps:
a. In your Twilio dashboard, navigate to "API Keys" under the "Settings" section.
b. Click the "Create API Key" button.
c. Provide a friendly name for your API key (for your reference) and select the appropriate permissions. You can create an API key with "Full Access" or specify more limited permissions depending on your use case.
d. Click the "Create API Key" button.
e. Once created, you'll be shown your API Key and Secret. Make sure to save these credentials in a secure location, as you won't be able to access the secret again.
Using Twilio in Your Application: With your API key and secret in hand, you can start using Twilio in your application.

You may use the .pyw file to run the application continuously. If any error occurs, you may use the .py file.
