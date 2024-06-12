/** @odoo-module **/

import Registries from 'point_of_sale.Registries';
const {Orderline} = require('point_of_sale.models');


const PosLoyaltyOrderline = (Orderline) => class PosLoyaltyOrderline extends Orderline {

    set_customer_reason(note) {
        this.customerReason = note;
        }


    set_customer_ordere_reason(note) {
        this.customerOrderReason = note;
        }


    export_as_JSON() {
        const result = super.export_as_JSON(...arguments);
        result.discount_remark = this.customerReason;
        result.discount_for = this.customerOrderReason;
        return result;
    }

}
Registries.Model.extend(Orderline, PosLoyaltyOrderline);












