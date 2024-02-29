odoo.define("point_of_sale.SalesLocationButton", function (require) {
  "use strict";

  const PosComponent = require("point_of_sale.PosComponent");
  const ProductScreen = require("point_of_sale.ProductScreen");
  const { useListener } = require("@web/core/utils/hooks");
  const Registries = require("point_of_sale.Registries");

  class SalesLocationButton extends PosComponent {
    setup() {
        console.log(this.env.pos);
      super.setup();
      useListener("click", this.onClick);
      this.list = this.env.pos.sales_location.filter((s_loc) =>
        this.env.pos.config.location.includes(s_loc.id)
      );
      this.order = this.env.pos.get_order();
    }
    get s_loc_id() {
      if (this.order.location) {
        return this.order.location.id;
      }
      return false;
    }

    async onClick() {

      const selectionList = this.list.map((location) => ({
        id: location.id,
        label: location.sales_location,
        isSelected: location.id === this.s_loc_id,
        item: location,
      }));
      console.log(selectionList, "==================================");

      const { confirmed, payload: selectedLocation } = await this.showPopup(
        "LocationSelectionPopup",
        {
          title: this.env._t("Select the location"),
          list: selectionList,
        }
      );

      if (confirmed) {
        this.order.set_location(selectedLocation);
      }
    }
  }
  SalesLocationButton.template = "SalesLocationButton";

  ProductScreen.addControlButton({
    component: SalesLocationButton,
    position: ["before", "SetPricelistButton"],
  });

  Registries.Component.add(SalesLocationButton);

  return SalesLocationButton;
});
