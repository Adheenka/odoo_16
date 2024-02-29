odoo.define("paymentScreenInherit", function (require) {
  "use strict";
  const PaymentScreen = require("point_of_sale.PaymentScreen");
  const Registries = require("point_of_sale.Registries");
  const { Gui } = require("point_of_sale.Gui");
  const { _lt } = require("@web/core/l10n/translation");

  const ValidatePaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {
      setup() {
        super.setup();
      }

      async _isOrderValid(isForceValidate) {
        const res = super._isOrderValid();
        if (this.env.pos.get_order().partner == null) {
          const { confirmed } = await Gui.showPopup("ConfirmPopup", {
            title: _lt("Customer Required"),
            body: _lt(`A customer is required to proceed!`),
            confirmText: _lt("Select Customer"),
          });
          // console.log(confirmed);
          if (confirmed) {
            const { confirmed, payload: selectedPartner } =
              await this.showTempScreen("PartnerListScreen");
            if (confirmed) {
              this.currentOrder.set_partner(selectedPartner);
              this.currentOrder.updatePricelist(selectedPartner);
            }
          }
          return false;
        }
        return res;
      }
    };
  Registries.Component.extend(PaymentScreen, ValidatePaymentScreen);
  return ValidatePaymentScreen;
});
