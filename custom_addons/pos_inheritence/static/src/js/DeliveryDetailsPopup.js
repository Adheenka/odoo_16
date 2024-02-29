odoo.define('pos_inheritence.DeliveryDetailsPopup', function (require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { useState, useRef, onMounted } = require("@odoo/owl");
    const { useListener } = require('@web/core/utils/hooks');
    const _t = require('@web/core/l10n/translation');

    class DeliveryDetailsPopup extends AbstractAwaitablePopup{
        constructor() {
            super(...arguments);
            this.state = useState({
                delivery_country: '',
                delivery_type: '',
                expected_delivery_date: '',
            });
            this.inputRef = useRef('input');
            onMounted(this.onMounted);
            useListener('click', this.onClick);
        }

        onMounted() {
            this.inputRef.el.focus();
        }

        get title() {
            return _t('Delivery Details');
        }

        cancel() {
            this.env.posbus.trigger('close-popup', {
                popupId: this.props.id,
                response: { confirmed: false, payload: null },
            });
        }

        async confirm() {
            const { delivery_country, delivery_type, expected_delivery_date } = this.state;

            // Save delivery details to local storage
            const deliveryDetails = {
                delivery_country,
                delivery_type,
                expected_delivery_date,
            };

            localStorage.setItem('temp_delivery_details', JSON.stringify(deliveryDetails));

            this.env.posbus.trigger('close-popup', {
                popupId: this.props.id,
                response: { confirmed: true, payload: deliveryDetails },
            });
        }

        async onClick() {
            await this.showPopup('DeliveryDetailsPopup', {
                title: this.env._t('Delivery Details'),
                body: this.env._t('Provide delivery details for the selected order line.'),
                delivery_country: 'Select', // Provide actual delivery country value
                delivery_type: 'Select..',   // Provide actual delivery type value
                expected_delivery_date: 'Select', // Provide expected delivery date
            });
        }
    }

    DeliveryDetailsPopup.template = 'DeliveryDetailsPopup';
    DeliveryDetailsPopup.defaultProps = {
        confirmText: 'OK',
        cancelText: 'Cancel',
        title: 'Delivery Details',
        body: '',
    };

    Registries.Component.add(DeliveryDetailsPopup);

    return DeliveryDetailsPopup;
});







//odoo.define('pos_inheritence.DeliveryDetailsPopup', function (require) {
//    'use strict';
//
//    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
//    const Registries = require('point_of_sale.Registries');
//    const { useState, useRef, onMounted } = owl;
//    const { useListener } = require('@web/core/utils/hooks');
//    const _t = require('@web/core/l10n/translation');
//
//    class DeliveryDetailsPopup extends AbstractAwaitablePopup {
//        constructor() {
//            super(...arguments);
//            this.state = useState({
//                delivery_country: '',
//                delivery_type: '',
//                expected_delivery_date: '',
//            });
//            this.inputRef = useRef('input');
//            onMounted(this.onMounted);
//            useListener('click', this.onClick);
//        }
//
//        onMounted() {
//            this.inputRef.el.focus();
//        }
//
//        get title() {
//            return _t('Delivery Details');
//        }
//
//        cancel() {
//            this.env.posbus.trigger('close-popup', {
//                popupId: this.props.id,
//                response: { confirmed: false, payload: null },
//            });
//        }
//
//        async confirm() {
//            const { delivery_country, delivery_type, expected_delivery_date } = this.state;
//
//            // Save delivery details to local storage
//            const deliveryDetails = {
//                delivery_country,
//                delivery_type,
//                expected_delivery_date,
//            };
//
//            localStorage.setItem('temp_delivery_details', JSON.stringify(deliveryDetails));
//
//            this.env.posbus.trigger('close-popup', {
//                popupId: this.props.id,
//                response: { confirmed: true, payload: deliveryDetails },
//            });
//        }
//
//        async onClick() {
//            await this.showPopup('DeliveryDetailsPopup', {
//                title: this.env._t('Delivery Details'),
//                body: this.env._t('Provide delivery details for the selected order line.'),
//                delivery_country: 'Select', // Provide actual delivery country value
//                delivery_type: 'Select..',   // Provide actual delivery type value
//                expected_delivery_date: 'Select', // Provide expected delivery date
//            });
//        }
//    }
//
//    DeliveryDetailsPopup.template = 'DeliveryDetailsPopup';
//    DeliveryDetailsPopup.defaultProps = {
//        confirmText: 'OK',
//        cancelText: 'Cancel',
//        title: 'Delivery Details',
//        body: '',
//    };
//
//    Registries.Component.add(DeliveryDetailsPopup);
//
//    return DeliveryDetailsPopup;
//});






//sabah code

//
//odoo.define('pos_inheritence.DeliveryDetailsPopup', function (require) {
//    'use strict';
//
//     const { useState, useRef } = owl;
//    const { _t } = require("web.core");
//    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
//    const Registries = require('point_of_sale.Registries');
//    const { useAutoFocusToLastInput } = require('point_of_sale.custom_hooks');
//
//    class DeliveryDetailsPopup extends AbstractAwaitablePopup {
//        setup() {
//            super.setup();
//            this.changes = useState({
//                delivery_country: this.props.delivery_country,  // Initialize with the provided delivery country value
//                delivery_type: this.props.delivery_type,
//                expected_delivery_date: this.props.expected_delivery_date,
//            });
//        }
//
//        async confirm() {
//            await super.confirm();
//            // Extract data from the popup
//            const { delivery_country, delivery_type, expected_delivery_date } = this.changes;
//
//            // Save data to local storage
//            localStorage.setItem('deliveryDetails', JSON.stringify({
//                delivery_country,
//                delivery_type,
//                expected_delivery_date
//            }));
//
//            // Retrieve and log the saved data from local storage
//            const savedDeliveryDataString = localStorage.getItem('deliveryDetails');
//            const savedDeliveryData = JSON.parse(savedDeliveryDataString);
//            console.log('savedDeliveryData', savedDeliveryData);
//        }
//    }
//
//    DeliveryDetailsPopup.components = { useRef };
//    DeliveryDetailsPopup.template = 'DeliveryDetailsPopup';
//    Registries.Component.add(DeliveryDetailsPopup);
//
//    return DeliveryDetailsPopup;
//});


















