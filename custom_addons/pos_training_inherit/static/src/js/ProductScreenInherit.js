odoo.define("pos_training.inherit", function (require) {
  "use strict";
  const ProductScreen = require("point_of_sale.ProductScreen");
  const Registries = require("point_of_sale.Registries");
  const { Gui } = require("point_of_sale.Gui");
  const { _lt } = require("@web/core/l10n/translation");
  const { useState } = owl;

  const CustomerDetailsPopupComponent = (ProductScreen) =>
    class extends ProductScreen {
      setup() {
        super.setup();
      }
      async onClick() {
        const selectOrderline = this.env.pos.get_order();
        if (!selectOrderline) return;
        const { confirmed, payload: details } = await this.showPopup(
          "CustomerDetailsPopup",
          {
            startingValue: selectOrderline.get_details(),
            title: this.env._t("Business Type"),
            confirmText: _lt("Save"),
          }
        );
        if (confirmed) {
          selectOrderline.set_details(details);
        }
      }

      async _onClickPay() {
        // console.log(this.env.pos.get_order().partner);
        const order = this.env.pos.get_order();
        if (this.env.pos.get_order().partner == null) {
          const { confirmed } = await this.showPopup("ConfirmPopup", {
            title: _lt("Customer needed"),
            body: _lt("Customer selection is mandatory!"),
          });
          if (confirmed) {
            const { confirmed, payload: selectedPartner } =
              await this.showTempScreen("PartnerListScreen", { partner: null });
            if (confirmed) {
              order.set_partner(selectedPartner);
              order.updatePricelist(selectedPartner);
            }
          }
        } else {
          return super._onClickPay(...arguments);
        }
      }

      async _clickProduct(event) {
        if (event.detail.qty_available < 1) {
          await this.showPopup("ErrorPopup", {
            title: "Warning",
            body: "Selected product is out of stock",
          });
        } else{
          super._clickProduct(...arguments);
        }
      }
    };
  CustomerDetailsPopupComponent.template =
    "pos_training_inherit.CustomerDetailsPopupComponent";
  Registries.Component.extend(ProductScreen, CustomerDetailsPopupComponent);
  return CustomerDetailsPopupComponent;
});
