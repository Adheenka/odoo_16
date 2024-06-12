odoo.define("pos_inheritence.DeliveryDetailsButton", function (require) {
    "use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('@web/core/utils/hooks');

    class DeliveryDetailsButton extends PosComponent {
        constructor() {
            super(...arguments);

        }
        get currentOrder(){
            return this.env.pos.get_order();
        }


        async onClick() {
            console.log('clicked button');
            await this.showPopup('DeliveryDetailsPopup', {
                title: this.env._t('Delivery Details'),
                body: this.env._t('Provide delivery details for the selected order line.'),
                delivery_country: 'Select', // Provide actual delivery country value
                delivery_type: 'Select..',   // Provide actual delivery type value
                expected_delivery_date: 'Select', // Provide expected delivery date
            });
        }
    }

    DeliveryDetailsButton.template = "DeliveryDetailsButton";


    ProductScreen.addControlButton({
        component: DeliveryDetailsButton,
        position: ['before', 'OrderlineCustomerNoteButton'],
    });

    Registries.Component.add(DeliveryDetailsButton);

    return DeliveryDetailsButton;
})

































