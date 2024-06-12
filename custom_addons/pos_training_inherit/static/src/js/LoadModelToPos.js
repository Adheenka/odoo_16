/** @odoo-modules */

import { PosGlobalState } from "point_of_sale.models";
import Registries from "point_of_sale.Registries";
const NewPosGlobalState = (PosGlobalState) =>
  class NewPosGlobalState extends PosGlobalState {
    async _processData(loadedData) {
      await super._processData(...arguments);
      console.log(this._processData);

      this.sales_location = loadedData["sales.location"];
      console.log(this.sales_location);
    }
  };
Registries.Model.extend(PosGlobalState, NewPosGlobalState);
  