odoo.define('waste_management.tree_button', function (require) {
    "use strict";

    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');

    var TreeButton = ListController.extend({
        buttons_template: 'waste_management.button_near_create.buttons',
        events: _.extend({}, ListController.prototype.events, {
            'click .print_xlsx_report': '_onPrintXlsxReport',
        }),
        _onPrintXlsxReport: function () {
            this.do_action('waste_management.action_print_xlsx_report');
        },
    });

    var SaleOrderListView = ListView.extend({
        config: _.extend({}, ListView.prototype.config, {
            Controller: TreeButton,
        }),
    });

    viewRegistry.add('button_in_tree', SaleOrderListView);
});
