import requests
from uagents import Agent, Context, Bureau, Model
from uagents.setup import fund_agent_if_low
from plyer import notification
from twilio.rest import Client
import tkinter as tk

# Create an agent for Alice
alice = Agent(name="alice", endpoint="http://localhost:8000")
alice_wallet = alice.wallet

# Create an agent for Bob
bob = Agent(name="bob", endpoint="http://localhost:8001")

# Create a login agent to collect user input
login_agent = Agent(name="login", endpoint="http://localhost:8002")

# Configure the Twilio client
account_sid = "ACc9c3dda4014509874d198b814ede3192"
auth_token = "728c906d44efa18bdb7b116b26451178"
client = Client(account_sid, auth_token)


# Define a message model
class Message(Model):
    text: str


# Define a Login model
class Login(Model):
    base: str
    foreign: str  # Modified to accept a comma-separated list
    thresholds: str  # Modified to accept a comma-separated list of thresholds


# Create a dictionary to store login information
login_info = {}


# Function to handle user login and store input
@login_agent.on_message(model=Login)
async def user_login(ctx: Context, sender: str, login_info_msg: Login):
    login_info[sender] = login_info_msg


# Function to check the exchange rate
def check_exchange_rate(base, foreign, threshold_list):
    amount = 100
    messages = []
    thresholds = [
        float(threshold) for threshold in threshold_list.split(",")
    ]  # Split and convert thresholds to float

    for foreign_currency, threshold in zip(foreign.split(","), thresholds):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={foreign_currency}&from={base}&amount={amount}"
        headers = {"apikey": "h0tmZtMCP1Q7iavlGQpEu4viqvEbxdcj"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            rate = data["info"]["rate"]
            if rate > threshold:
                message = f"Exchange rate ({base} to {foreign_currency}) is higher than the threshold by: {rate - threshold}"
            else:
                message = f"Exchange rate ({base} to {foreign_currency}) is lower than the threshold by: {threshold - rate}"
            messages.append(message)
        else:
            messages.append("Error getting exchange rate data")

    return messages


def display_all_currencies():
    all_currencies = "\n".join(currency_symbols)

    # Create a new window to display the currencies
    currencies_window = tk.Toplevel()
    currencies_window.title("All Currencies")
    currencies_window.geometry("400x400")

    # Create a Text widget for displaying currencies
    text_widget = tk.Text(currencies_window, wrap="word", height=20, width=40)
    text_widget.pack(expand=True, fill="both")

    # Add the currency list to the Text widget
    text_widget.insert("1.0", all_currencies)

    # Create a scrollbar and associate it with the Text widget
    scrollbar = tk.Scrollbar(currencies_window, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)


def fetch_currencies():
    url = "https://api.apilayer.com/exchangerates_data/symbols"
    headers = {"apikey": "h0tmZtMCP1Q7iavlGQpEu4viqvEbxdcj"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        currencies = response.json()
        # return both key and value
        return [f"{key} - {value}" for key, value in currencies["symbols"].items()]

    else:
        return []


currency_symbols = fetch_currencies()


# Function to ask for login information from the user using a GUI
def currCheck():
    login_window = tk.Tk()
    login_window.title("HAP Currency Service")

    show_currencies_button = tk.Button(
        login_window, text="Show All Currencies", command=display_all_currencies
    )
    show_currencies_button.pack()

    base_label = tk.Label(login_window, text="Enter the base currency:")
    base_label.pack()
    base_entry = tk.Entry(login_window)
    base_entry.pack()

    foreign_label = tk.Label(
        login_window, text="Enter the foreign currencies (comma-separated):"
    )
    foreign_label.pack()
    foreign_entry = tk.Entry(login_window)
    foreign_entry.pack()

    thresholds_label = tk.Label(
        login_window, text="Enter the thresholds (comma-separated):"
    )
    thresholds_label.pack()
    thresholds_entry = tk.Entry(login_window)
    thresholds_entry.pack()

    def submit_login_info():
        base = base_entry.get()
        foreign = foreign_entry.get()
        thresholds = thresholds_entry.get()
        login_info[login_agent.address] = Login(
            base=base, foreign=foreign, thresholds=thresholds
        )
        login_window.destroy()

    # show_currencies_button = tk.Button(login_window, text="Show All Currencies", command=display_all_currencies)
    # show_currencies_button.pack()

    submit_button = tk.Button(login_window, text="Submit", command=submit_login_info)
    submit_button.pack()

    login_window.mainloop()


# Function to continuously check thresholds and send notifications
@bob.on_interval(period=10.0)
async def threshold_checker(ctx: Context):
    for sender, login_data in login_info.items():
        base = login_data.base
        foreign = login_data.foreign
        threshold_list = login_data.thresholds

        # Check the exchange rates
        messages = check_exchange_rate(base, foreign, threshold_list)

        # Send the messages to Alice
        for message in messages:
            await ctx.send(alice.address, Message(text=message))

            # Send a notification
            notification.notify(
                title="Exchange Rate Alert",
                message=message,
                app_icon=None,
                timeout=10,
            )


# Create a bureau and add agents
bureau = Bureau()
bureau.add(alice)
bureau.add(bob)
bureau.add(login_agent)

# Create a GUI for user login
currCheck()

# Run the bureau
bureau.run()
