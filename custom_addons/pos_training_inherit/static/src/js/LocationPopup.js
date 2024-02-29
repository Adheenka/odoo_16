odoo.define('point_of_sale.LocationSelectionPopup', function (require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { _lt } = require('@web/core/l10n/translation');
    const {Order}=require('point_of_sale.models')
    const { useState } = owl;

    class LocationSelectionPopup extends AbstractAwaitablePopup {
        
        setup() {
            super.setup();
            this.state = useState({ selectedId: this.props.list.find((item) => item.isSelected) });
        }
        selectItem(itemId) {
            this.state.selectedId = itemId;
            this.confirm();
        }
        getPayload() {
            const selected = this.props.list.find((item) => this.state.selectedId === item.id);
            return selected && selected.item;
        }
    }
    LocationSelectionPopup.template = 'LocationSelectionPopup';
    LocationSelectionPopup.defaultProps = {
        cancelText: _lt('Cancel'),
        title: _lt('Select Location'),
        body: '',
        list: [],
        confirmKey: false,
    };

    Registries.Component.add(LocationSelectionPopup);

    const PosLocationCache = (Order) =>
    class extends Order {
     
      init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.set_location(json.location);
      }
      export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.s_loc = this.location;
        return json;
      }
      set_location(location) {
        this.location = location;
      }
      get_location() {
        return this.location;
      }
      export_for_printing() {
        const result = super.export_for_printing(...arguments);
        if (this.get_location()) {
            result.location = this.location;
        }
        return result;
      }
    };
    Registries.Model.extend(Order,PosLocationCache);

});
