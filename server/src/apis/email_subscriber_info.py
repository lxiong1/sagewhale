from flask_restx import Namespace, Resource, fields

api = Namespace(
    "email_subscriber_info",
    description="Email subscriber information related operations",
)

demographics_model = api.model(
    "Demographics",
    {
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

emailed_product_model = api.model(
    "EmailedProduct",
    {
        "type": fields.String(
            required=True, description="Product type that was emailed to subscriber"
        ),
        "total_send_rate": fields.Integer(
            required=True, description="Count of emails sent"
        ),
        "total_open_rate": fields.Integer(
            required=True, description="Count of emails opened"
        ),
    },
)

email_subscriber_info_model = api.model(
    "EmailSubscriberInfo",
    {
        "id": fields.String(
            required=True, description="UUID string identifying email subscriber info"
        ),
        "demographics": fields.Nested(
            demographics_model,
            description="Statistical characteristics of email subscriber",
        ),
        "emailed_products": fields.List(
            fields.Nested(
                emailed_product_model, description="Count of emails opened"
            )
        ),
    },
)


@api.route("/<string:id>")
class EmailSubscriberInfo(Resource):
    def get(self, id):
        """Get email subscriber information by id"""
        return {}

    @api.expect([email_subscriber_info_model], validate=True)
    @api.marshal_list_with([email_subscriber_info_model], code=201)
    def post(self):
        """Store JSON or CSV file content"""
        return [], 201
