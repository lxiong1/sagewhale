from flask_restx import Namespace, Resource, fields

api = Namespace(
    "subscriber_info",
    description="Subscriber information related operations",
)

demographics_model = api.model(
    "Demographics",
    {
        "id": fields.String(
            required=True,
            description="UUID identifying demographics of subscriber",
        ),
        "gender": fields.String(required=False),
        "age": fields.Integer(required=False),
        "race": fields.String(required=False),
        "marital_status": fields.String(
            required=False, description="Person's relationship with a significant other"
        ),
        "education": fields.String(
            required=False, description="Degree of achieved education"
        ),
        "household_income": fields.String(
            required=False, description="Range of household income"
        ),
    },
)

email_product_model = api.model(
    "EmailProduct",
    {
        "product_type": fields.String(
            required=True, description="Type of product email advertised to subscriber"
        ),
        "total_send_rate": fields.Integer(
            required=True, description="Send rate of emails sent to subscriber"
        ),
        "total_open_rate": fields.Integer(
            required=True, description="Open rate of emails sent to subscriber"
        ),
    },
)

email_performance_model = api.model(
    "EmailPeformance",
    {
        "id": fields.String(
            required=True,
            description="UUID identifying email performance of subscriber",
        ),
        "products": fields.List(
            fields.Nested(email_product_model),
            required=False,
            description="Product type that was emailed to subscriber",
        ),
        "subscriber_id": fields.Integer(required=True, description="Id of subscriber"),
    },
)

subscriber_model = api.model(
    "Subscriber",
    {
        "id": fields.String(required=True, description="UUID identifying subscriber"),
        "first_name": fields.String(
            required=False,
            description="First name of subscriber",
        ),
        "last_name": fields.String(
            required=False,
            description="Last name of subscriber",
        ),
        "full_name": fields.String(
            required=False,
            description="Full name of subscriber",
        ),
    },
)

subscriber_info_model = api.model(
    "SubscriberInfo",
    {
        "subscriber": fields.Nested(
            subscriber_model, required=True, description="Subscriber personal data"
        ),
        "demographics": fields.Nested(
            demographics_model,
            required=True,
            description="Statistical characteristics of subscriber",
        ),
        "email_performance": fields.Nested(
            email_performance_model,
            required=True,
            description="Performance of emails sent to subscriber",
        ),
    },
)


@api.route("/<string:id>")
class SubscriberInfo(Resource):
    def get(self, id):
        """Get subscriber information by id"""
        return {}

    @api.expect([subscriber_info_model], validate=True)
    @api.marshal_list_with([subscriber_info_model], code=201)
    def post(self):
        """Store JSON or CSV file with content containing subscriber information"""
        return [], 201
