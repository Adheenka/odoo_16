/** @odoo-module **/

import { registry } from '@web/core/registry';
import { formView } from '@web/views/form/form_view';
import { FormController } from '@web/views/form/form_controller';
import { useService } from "@web/core/utils/hooks";

class ResPartnerFormController extends FormController {
    setup(){
        super.setup()
        this.action = useService("action")
    }
    openWebsite(url){
        this.action.doAction({
            type: "ir.actions.act_url",
            target: self,
            url,
        })
    }
}
ResPartnerFormController.template = "odoo_owl.ResPartnerFormView"
export const ResPartnerFormView = {
    ...formView,
    Controller: ResPartnerFormController,
}
registry.category("views").add("res_partner_form_view", ResPartnerFormView)
