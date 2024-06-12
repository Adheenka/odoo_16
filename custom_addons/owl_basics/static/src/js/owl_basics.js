odoo.define('owl_basics.owl_study', function (require) {
    'use strict';
//    console.log('owl_study.js loaded');

    var core = require('web.core');
    var FormController = require('web.FormController');

    var _t = core._t;

    var ExtendFormController = FormController.include({
        saveRecord: function () {
            var res = this._super.apply(this, arguments);

            if (this.modelName === 'owl.study') {
                this.displayNotification({
                    type: 'warning',
                    title: _t('Success'),
                    message: "Your Message has been sent successfully...",
                    sticky: true
                });

                // Automatically close after 5 seconds
                setTimeout(() => {
                    $('.o_notification_manager').empty();
                }, 3000);
            }

            return res;
        },
    });
});




