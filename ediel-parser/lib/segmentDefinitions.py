from lib.Segment import Segment

definitions = {
    "SEQ": Segment().structure([
        Segment("status_indicator_coded"), 
        Segment("sequence_information", min=0, max=1).structure([
            Segment("sequence_number", mandatory=True, length=(0,6)),
            Segment("sequence_number_source", length=(0,3)),
            Segment("code_list_qualifier", length=(0,3)),
            Segment("code_list_responsible_agency", length=(0,3))
        ])
    ]),
    "QTY": Segment().structure([
        Segment("quantity_details", mandatory=True, min=1, max=1).structure([
            Segment("quantity_qualifier", length=(0,3), mandatory=True),
            Segment("quantity", length=(0,15), mandatory=True),
            Segment("measure_unit_qualifier", length=(0,3))
        ])
    ]),
    "LOC": Segment().structure([
        Segment("place-location_qualifier", mandatory=True, length=(0,3)),
        Segment("location_identification", min=0, max=1).structure([
            Segment("place-location_identification", length=(0, 25)),
            Segment("code_list_qualifier", length=(0,3)),
            Segment("code_list_responsible_agency-coded", length=(0,3)),
            Segment("place-location", length=(0,70))
        ]),
        Segment("related_location_one_identification", min=0, max=1).structure([
            Segment("related_place-location_one_identification", length=(0,25)),
            Segment("code_list_qualifier", length=(0,3)),
            Segment("code_list_responsible_agency-coded", length=(0,3)),
            Segment("related_place-location_one", length=(0, 70))
        ]),
        Segment("related_location_two_identification", min=0, max=1).structure([
            Segment("related_place-location_two_identification", length=(0,25)),
            Segment("code_list_qualifier", length=(0,3)),
            Segment("code_list_responsible_agency-coded", length=(0,3)),
            Segment("related_place-location_two", length=(0, 70))
        ]),
        Segment("relation-coded", length=(0,3))
    ]),
    "DTM": Segment().structure([
        Segment("date-time-period", min=1, max=1, mandatory=True).structure([
            Segment("date-time-period_qualifier", length=(0,3), mandatory=True),
            Segment("date-time-period", length=(0,35)),
            Segment("date-time-period_format_qualifier", length=(0,3)),
        ])
    ]),
    "CAV": Segment().structure([
        Segment("characteristic_value", mandatory=True, min=1, max=1).structure([
            Segment("characteristic_value-coded", length=(0,3)),
            Segment("code_list_qualifier", length=(0,3)),
            Segment("code_list_responsible_agency-coded", length=(0,3)),
            Segment("characteristic_value", length=(0,35)),
            Segment("characteristic_value", length=(0,35)),
        ])
    ]),
    "LIN": Segment().structure([
        Segment("line_item_number", length=(0,6)),
        Segment("action_request-notification-coded", length=(0,3)),
        Segment("item_number_identification", min=0, max=1).structure([
            Segment("item_number", length=(0,35)),
            Segment("item_number_type-coded", length=(0,3)),
            Segment("code_list_qualifier", length=(0,3)),
            Segment("code_list_responsible_agency-coded", length=(0,3)),
        ]),
        Segment("sub-line_information", min=0, max=1).structure([
            Segment("sub-line_indicator-coded", length=(0,3)),
            Segment("line_item_number", length=(0,6))
        ]),
        Segment("configuration_level", length=(0,2)),
        Segment("configuration-coded", length=(0,3))
    ]),
    "MEA": Segment().structure([
        Segment("measurement_application_qualifier", length=(0,3), mandatory=True),
        Segment("measurement_details", min=0, max=1).structure([
            Segment("measurement_dimension-coded", length=(0,3)),
            Segment("measurement_significance-coded", length=(0,3)),
            Segment("measurement_attribute-coded", length=(0,3)),
            Segment("measurement_attribute", length=(0,70))
        ]),
        Segment("value-range", min=0, max=1).structure([
            Segment("measure_unit_qualifier", length=(0,3)),
            Segment("measurement_value", length=(0,18)),
            Segment("range_minimum", length=(0,18)),
            Segment("range_maximum", length=(0,18)),
            Segment("significant_digits", length=(0,2))
        ]),
        Segment("surface-layer_indicator-coded", length=(0,3))
    ]),
    "IDE": Segment().structure([
        Segment("identification_qualifier", length=(0,3), mandatory=True),
        Segment("identification_number", min=1, max=1, mandatory=True).structure([
            Segment("identity_number", length=(0,35)),
            Segment("identity_number_qualifier", length=(0,3)),
            Segment("status-coded", length=(0,3)),
        ]),
        Segment("party_identification_details", min=0, max=1).structure([
            Segment("party_id_identification", length=(0,35), mandatory=True),
            Segment("code_list_qualifier", length=(0,3)),
            Segment("code_list_responsible_agency-coded", length=(0,3)),
        ]),
        Segment("status-coded", length=(0,3)),
        Segment("configuration_level", length=(0,2)),
        Segment("position_identification", min=0, max=1).structure([
            Segment("hierarchical_id_number", length=(0,12)),
            Segment("sequence_number", length=(0,6))
        ]),
        Segment("product_characteristic", min=0, max=1).structure([
            Segment("characteristic_identification", length=(0,17), mandatory=True),
            Segment("code_list_qualifier", length=(0,3)),
            Segment("code_list_responsible_agency-coded", length=(0,3)),
            Segment("characteristic", length=(0,35)),
            Segment("characteristic", length=(0,35))
        ])
    ])
}