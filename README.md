<h1>Django Bidding Web App</h1>
Welcome to our Django-based web application for auctioning products, where simplicity meets functionality. This platform is designed to facilitate an efficient and engaging bidding process for a variety of items.

<h2>Features</h2>
***Open Listings***: Any registered user can list products for auction.
***Active Bidding***: Interested buyers can place bids on any listed item.
***Timed Auctions***: Sellers have the option to set a timer, after which the highest bidder is automatically selected.
***Seller's Choice***: Sellers may also manually select a winner at their discretion.
***User Dashboards***: Separate dashboards for sellers and buyers to manage activities.
***AI Price Prediction***: Utilizes AI to predict car prices, aiding sellers in setting starting bids.
***Admin Panel***: Robust admin panel for managing listings, users, and site settings.
***Image Storage***: Capability to store and display images for each item.
***Automatic Unavailability***: Items are set to 'unavailable' after the auction end date/time passes.
Getting Started
To get started with this project, follow the instructions below:

<h3>Set up a virtual environment:</h3>
```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

<h3>Install the required dependencies:</h3>
```
pip install -r requirements.txt
```
<h3>Train the AI Model:</h3>

Navigate to the ./utils/CarPrice directory and Ensure that this model is trained before you start the server as it is essential for the AI price prediction feature.

<h3>Run the Development Server:</h3>

After training the model, start the Django development server:

```
python manage.py runserver
```
<h2>Usage</h2>

<h3>Once the server is up and running:</h3>

Visit the homepage and sign up for an account.
Navigate to the seller dashboard to list an item for auction.
Use the buyer dashboard to view active listings and place bids.
Admins can log into the admin panel to oversee the auction process and manage listings.
Final Notes
This application is built with the goal of providing a seamless auction platform that is both user-friendly and feature-rich. We hope it serves your bidding needs effectively!

Happy Bidding!
