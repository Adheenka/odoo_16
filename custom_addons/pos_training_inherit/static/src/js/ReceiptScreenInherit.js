odoo.define("pos_inherit.paymentScreenExtension", function (require) {
  "use strict";
  const { Order } = require("point_of_sale.models");
  const Registries = require("point_of_sale.Registries");
  const storeCache = (Order) =>
    class storeCache extends Order {
     
      init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.set_details(json.details);
      }
      export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.details = this.details;
        return json;
      }
      set_details(num) {
        this.details = num;
      }
      get_details() {
        return this.details;
      }
      export_for_printing() {
        const result = super.export_for_printing(...arguments);
        if (this.get_details()) {
          result.details = this.get_details();
          result.mobile_no = this.partner.mobile_no;
        }
        return result;
      }
    };
  Registries.Model.extend(Order, storeCache);
  return storeCache;
});
