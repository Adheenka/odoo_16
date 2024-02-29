odoo.define("deleteButton", function (require) {
  "use strict";

  const Orderline = require("point_of_sale.Orderline");
  const Registries = require("point_of_sale.Registries");

  const OrderlineDeleteButton = () =>
    class extends Orderline {
      setup() {
        super.setup();
      }
      async onClick(orderline) {
        // console.log(orderline);
        const currentOrder = this.env.pos.get_order();
        currentOrder.remove_orderline(orderline);
      }
    };
  OrderlineDeleteButton.template = "pos_training_inherit.Orderline";
  Registries.Component.extend(Orderline, OrderlineDeleteButton);
  return OrderlineDeleteButton;
});
