/** @odoo-module **/
/**
 * Defines CustFeedback which extends Order from point of sale models
 *
 * Initialize the additional properties from JSON and export the additional
 * properties as JSON
 */
import { Order } from 'point_of_sale.models';
import Registries from "point_of_sale.Registries";

const CustFeedback = (Order) => class CustFeedback extends Order {
    /**
     * Initializes the CustFeedback class.
     */
    constructor() {
        super(...arguments);
        this.customer_feedback = this.customer_feedback || null;
        this.comment_feedback = this.comment_feedback || null;
        this.delivery_country = this.delivery_country || null;
        this.delivery_type = this.delivery_type || null;
//        this.expected_delivery_date = this.expected_delivery_date || null;
    }

    /**
     * Sets the comment and customer feedback values.
     *
     * @param {Object} comment_feedback - Object containing the comment and rating values.
     */
    set_comment_feedback(comment_feedback) {
        this.comment_feedback = comment_feedback.commentValue;
        this.customer_feedback = comment_feedback.ratingValue;
        this.delivery_country = comment_feedback.deliveryCountry;
        this.delivery_type = comment_feedback.deliveryType;
//        this.expected_delivery_date = comment_feedback.expectedDeliveryDate;
    }
    set_delivery_details(deliveryType, deliveryCountry, expectedDeliveryDate) {
        this.delivery_type = deliveryType;
        this.delivery_country = deliveryCountry;
//        this.expected_delivery_date = expectedDeliveryDate;
    }
    /**
     * Returns the comment feedback value.
     *
     * @returns {string|null} - The comment feedback value.
     */
    get_comment_feedback() {
        return this.comment_feedback;
    }
    get_delivery_type() {
            return this.delivery_type;
    }
    get_delivery_country() {
        return this.delivery_country;
    }
    /**
     * Exports the CustFeedback properties as JSON.
     *
     * @returns {Object} - The CustFeedback properties as JSON.
     */
    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.customer_feedback = this.customer_feedback;
        json.comment_feedback = this.comment_feedback;
        json.delivery_country = this.delivery_country;
        json.delivery_type = this.delivery_type;
//        json.expected_delivery_date = this.expected_delivery_date;
        return json;
    }

    /**
     * Initializes the CustFeedback properties from JSON.
     *
     * @param {Object} json - The JSON object containing the CustFeedback properties.
     */
    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.customer_feedback = json.customer_feedback;
        this.comment_feedback = json.comment_feedback;
        this.delivery_country = json.delivery_country;
        this.delivery_type = json.delivery_type;
//        this.expected_delivery_date = json.expected_delivery_date;
    }
};

Registries.Model.extend(Order, CustFeedback);

