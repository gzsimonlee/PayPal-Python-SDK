# This class was generated on Mon, 29 Jan 2018 15:08:25 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# payment_create_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class PaymentCreateRequest:
    """
    Creates a sale, an authorized payment to be captured later, or an order. To create a sale, authorization, or order, include the payment details in the JSON request body. Set the `intent` to `sale`, `authorize`, or `order`. Include payer, transaction details, and, for PayPal payments only, redirect URLs. The combination of the `payment_method` and `funding_instrument` determines the type of payment that is created. For more information, see [Payments REST API](/docs/integration/direct/payments/).<blockquote><strong>Note:</strong> Authorizations are guaranteed for up to three days, though you can attempt to capture an authorization for up to 29 days. After the three-day honor period authorization expires, you can [reauthorize](#authorization_reauthorize) the payment.</blockquote>
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/payments/payment?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, payment):
        self.body = payment
        return self
