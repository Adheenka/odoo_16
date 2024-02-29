odoo.define('abrus_pos_order_discount.PosDiscountLineButton', function(require) {
    "use strict";
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require("@web/core/utils/hooks");
    const Registries = require('point_of_sale.Registries');
    // Extends PosComponents and added a click function
    class PosDiscountLineButton extends PosComponent {
        setup() {
            super.setup();
            useListener('click', this.onClick);
        }
        async onClick(ev) {
                let self = this;
                let cashier = this.env.pos.get_cashier();
                if (cashier.is_allow_void == true)
                {
                    const selectedOrderline = this.env.pos.get_order().get_selected_orderline();
                    if (!selectedOrderline) return;

                    this.showPopup('PosDiscountLineButtonPopup' ,{
                    reason: this.env._t(selectedOrderline.customerReason),
                    cus_reason: this.env._t(selectedOrderline.customerOrderReason),
                });
                }
                else{
                    await this.showPopup('ErrorPopup', {
                            title: this.env._t('Blocked action'),
                            body: this.env._t('Sorry,You have no access to Void'),
                        });
                    return;
                }

            }
        }
    PosDiscountLineButton.template = 'PosDiscountLineButton';
    ProductScreen.addControlButton({
        component: PosDiscountLineButton,
        condition: function() {
            return true;
        },
    });
    Registries.Component.add(PosDiscountLineButton);
    return PosDiscountLineButton;
});
