odoo.define('abrus_pos_order_discount.PosDiscountLineButtonPopup', function(require) {
    "use strict";
	const Popup = require('point_of_sale.ConfirmPopup');
	const Registries = require('point_of_sale.Registries');
	const PosComponent = require('point_of_sale.PosComponent');

    class PosDiscountLineButtonPopup extends Popup {
        constructor() {
            super(...arguments);
        }
        setup() {
            super.setup();
        }
    update_order_line(event) {
            var self = this;
            const selectedOrderline = this.env.pos.get_order().get_selected_orderline();
            if (selectedOrderline){
                var cus_remarks = document.getElementById("cus_remarks");
                var cus_reason = document.getElementById("wa_no_line");
                selectedOrderline.set_customer_reason(cus_remarks.value);
                selectedOrderline.set_customer_ordere_reason(cus_reason.value);
                selectedOrderline.set_discount(100);
                this.env.posbus.trigger('close-popup', {
                popupId: this.props.id });
            }
            else{
                this.env.posbus.trigger('close-popup', {
                popupId: this.props.id });
            }

        }
    reset_order_line(event) {
            var self = this;
            const selectedOrderline = this.env.pos.get_order().get_selected_orderline();
            if (selectedOrderline){
                selectedOrderline.set_customer_reason('');
                selectedOrderline.set_customer_ordere_reason(false);
                selectedOrderline.set_discount(0);
                this.env.posbus.trigger('close-popup', {
                popupId: this.props.id });
            }
            else{
                this.env.posbus.trigger('close-popup', {
                popupId: this.props.id });
            }

        }

    };
    PosDiscountLineButtonPopup.template = 'PosDiscountLineButtonPopup';
    Registries.Component.add(PosDiscountLineButtonPopup);
    return PosDiscountLineButtonPopup;

});
