odoo.define("pos_training_inherit.CustomerDetailsPopup", function (require) {
  "use strict";

  const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
  const { useState, useRef } = owl;
  const Registries = require("point_of_sale.Registries");
  const { _lt } = require("@web/core/l10n/translation");

  class CustomerDetailsPopup extends AbstractAwaitablePopup {
    setup() {
      super.setup();

      this.state = useState({ inputValue: this.props.startingValue });
      this.details = useRef("details");

      this.add_details = useState({
        value: "",
        error: "",
      });
    }
    getPayload() {
      return this.state.inputValue;
    } 
  }
  CustomerDetailsPopup.template = "pos_training_inherit.CustomerDetailsPopup";
  CustomerDetailsPopup.defaultProps = {
    cancelText: _lt("Discard"),
    title: _lt("Customer details"),
    save: _lt("Save"),
  };
  Registries.Component.add(CustomerDetailsPopup);
  return CustomerDetailsPopup;
});
