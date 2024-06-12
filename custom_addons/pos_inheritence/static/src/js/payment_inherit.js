odoo.define('pos_inheritence.CustomPaymentScreen', function (require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const CustomPaymentScreen = PaymentScreen => class extends PaymentScreen {
        setup() {
            super.setup();
            const newOrder = this.env.pos.get_order();
            console.log('newOrder', newOrder);
        };

        async validateOrder(isForceValidate) {
            super.validateOrder();
            const savedSaleDataString = localStorage.getItem('temp_delivery_details');

            // Parse the JSON string back into an object
            const savedSaleData = JSON.parse(savedSaleDataString);

            // Now, you can use the saved data in your application
            console.log('savedSaleData', savedSaleData);
        }
    };

    Registries.Component.extend(PaymentScreen, CustomPaymentScreen);
    return PaymentScreen;
});


//odoo.define('pos_inheritence.CustomPaymentScreen', function (require) {
//    'use strict';
//
//    const PaymentScreen = require('point_of_sale.PaymentScreen');
//    const Registries = require('point_of_sale.Registries');
//
//    const CustomPaymentScreen = PaymentScreen => class extends PaymentScreen{
//        setup() {
//            super.setup();
//             const newOrder = this.env.pos.get_order();
//             console.log('newOrder',newOrder)
//
//        };
//
//        async validateOrder(isForceValidate) {
//           super.validateOrder();
//            const savedSaleDataString = localStorage.getItem('deliveryDetails');
//
//            // Parse the JSON string back into an object
//            const savedSaleData = JSON.parse(savedSaleDataString);
//
//            // Now, you can use the saved data in your application
//            console.log('savedSaleData',savedSaleData);
//
//            }
//
//    };
//
//    Registries.Component.extend(PaymentScreen,CustomPaymentScreen);
//    return PaymentScreen;
//});