# voucher-project

## Features

* User Authentication (Login/Register)
* Product Purchase Flow
* Razorpay Integration (Test Mode)
* Fake Payment System (for demo reliability)

## Tech Stack

* Django
* Python
* SQLite
* Razorpay API

## Setup Instructions

1. Clone the repo
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run server:
   python manage.py runserver

## Environment Variables

Create a `.env` file and add:
RAZORPAY_KEY=your_key
RAZORPAY_SECRET=your_secret

## Demo

* Login, select product, and test payment

## Note

Fake payment system is added to ensure smooth demo without real transactions.

