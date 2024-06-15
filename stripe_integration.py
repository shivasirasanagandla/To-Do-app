# stripe_integration.py
import stripe
from flask import Flask, jsonify, request
from app import app

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Pro License',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8050/success',
        cancel_url='http://localhost:8050/cancel',
    )
    return jsonify(id=session.id)
