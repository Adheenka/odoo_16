{
    "name": "POS Training",
    "version": "1.0",
    "summary": "Point of sale Training",
    "author": "Aman Deep",
    "sequence": "2",
    "depends": ["base", "point_of_sale"],
    "license": "LGPL-3",
    "website": "https://github.com/amandeep8297",
    "category": "Learning",
    "installable": True,
    "application": True,
    "data":[
        "security/ir.model.access.csv",
        "views/posView.xml",
        "views/order_form.xml",
        "views/posConfig.xml",
        "views/sales_location.xml",

    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_training_inherit/static/src/js/*",
            "pos_training_inherit/static/src/xml/*",
            "pos_training_inherit/static/src/scss/*",
        ],
    },
}
