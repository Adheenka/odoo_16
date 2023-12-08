odoo.define('owl_basics.odoo_tutorial', function (require) {
    'use strict';

    var FormController = require('web.FormController');  // Fix: Added quotes around 'web.FormController'

    var ExtendFormController = FormController.include({
        saveRecord: function () {
            var res = this._super.apply(this, arguments);  // Fix: Changed 'this.super' to 'this._super'
            this.do_notify('success', 'Record Saved');
            return res;
        }
    });
});