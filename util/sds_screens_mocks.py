class SDS_Screens_Mocks:
    def __init__(self):
        self.sds_screens_mocks = {
            "claims1":"""{
                    "document_info": {
                        "generated_by": "SDS",
                        "form_number": "HE20250404028040",
                        "page": "1",
                        "form_type": "HEALTH INSURANCE CLAIM FORM"
                    },
                    "insurance_type": {
                        "medicare": false,
                        "medicaid": false,
                        "tricare": false,
                        "champva": false,
                        "group_health_plan": false,
                        "feca_blk_lung": false,
                        "other": false
                    },
                    "insured_id": "BASLP1830",
                    "patient_info": {
                        "name": {
                        "last": "JOHNSON",
                        "first": "MARTWON"
                        },
                        "date_of_birth": "07/20/1992",
                        "sex": "M",
                        "address": "1100 PIKE ST",
                        "city": "HUNTINGDON",
                        "state": "PA",
                        "zip": "16654002",
                        "telephone": null,
                        "relationship_to_insured": "X"
                    },
                    "insured_info": {
                        "name": {
                        "last": "JOHNSON",
                        "first": "MARTWON"
                        },
                        "address": "1100 PIKE ST",
                        "city": "HUNTINGDON",
                        "state": "PA",
                        "zip": "16654002",
                        "telephone": null,
                        "policy_group_number": null,
                        "date_of_birth": "07/20/1992",
                        "sex": "X"
                    },
                    "condition_related_info": {
                        "employment": {
                        "current_or_previous": "NO",
                        "auto_accident": "NO",
                        "other_accident": "NO"
                        }
                    },
                    "insurance_plan": {
                        "name": "W.C. BELLS COMPANY",
                        "other_health_benefit_plan": null
                    },
                    "claim_details": {
                        "referring_provider": {
                        "name": "BUNDY, DAVID",
                        "npi": "1346292554"
                        },
                        "diagnosis_codes": {
                        "A": "B0782",
                        "B": "J4699",
                        "C": "A0472",
                        "D": "B197"
                        },
                        "service_line": {
                        "date_of_service": {
                            "from": "01/21/2024",
                            "to": "01/21/2024"
                        },
                        "place_of_service": "23",
                        "cpt_code": "93971",
                        "modifier": "26",
                        "diagnosis_pointer": "LT",
                        "charges": "43.00",
                        "units": "1",
                        "rendering_provider_npi": "1093707457",
                        "additional_info": "ABCD"
                        }
                    },
                    "billing_info": {
                        "federal_tax_id": {
                        "number": "251400707",
                        "type": "X"
                        },
                        "patient_account_no": "5010755070",
                        "accept_assignment": "NO",
                        "total_charge": "43.00",
                        "amount_paid": "0.00",
                        "service_facility": {
                        "name": "PENN HIGHLANDS HUNTINGDON",
                        "address": "1225 WARM SPRINGS AVENUE",
                        "city_state_zip": "HUNTINGDON, PA 166522150"
                        },
                        "billing_provider": {
                        "name": "PENN HIGHLANDS DUBOIS",
                        "address": "100 HOSPITAL AVENUE",
                        "city_state_zip": "DUBOIS, PA 15801",
                        "phone": "371-2500",
                        "npi": "1093812406"
                        }
                    },
                    "signatures": {
                        "patient": "Signature on File",
                        "insured": "Signature on File",
                        "provider": "SAFVI, AMJAD"
                    }
                    } """,
        "claims2": """{
                    "document_info": {
                        "generated_by": "SDS",
                        "form_number": "HE20250404028040",
                        "page": "1",
                        "form_type": "HEALTH INSURANCE CLAIM FORM"
                    },
                    "insurance_type": {
                        "medicare": false,
                        "medicaid": false,
                        "tricare": false,
                        "champva": false,
                        "group_health_plan": false,
                        "feca_blk_lung": false,
                        "other": true
                    },
                    "insured_id": "BASLP1930",
                    "patient_info": {
                        "name": {
                            "last": "RODRIGUES",
                            "first": "VIOLA"
                        },
                        "date_of_birth": "07/20/1997",
                        "sex": "F",
                        "address": "1100 Grassy Lane",
                        "city": "HUNTINGDON",
                        "state": "PA",
                        "zip": "166540002",
                        "telephone": null,
                        "relationship_to_insured": "X"
                    },
                    "insured_info": {
                        "name": {
                            "last": "RODRIGUES",
                            "first": "VIOLA"
                        },
                        "address": "1100 Grassy Lane",
                        "city": "HUNTINGDON",
                        "state": "PA",
                        "zip": "166540002",
                        "telephone": null,
                        "policy_group_number": "07/20/1997",
                        "date_of_birth": "07/20/1997",
                        "sex": "X"
                    },
                    "condition_related_info": {
                        "employment": {
                            "current_or_previous": "NO",
                            "auto_accident": "NO",
                            "other_accident": "NO"
                        }
                    },
                    "insurance_plan": {
                        "name": "W.C. NEELER COMPANY",
                        "other_health_benefit_plan": null
                    },
                    "claim_details": {
                        "referring_provider": {
                            "name": "BUNDY, DAVID",
                            "npi": "1346292555"
                        },
                        "diagnosis_codes": {
                            "A": "R0789",
                            "B": "J2699",
                            "C": "A0472",
                            "D": "R197"
                        },
                        "service_line": {
                            "date_of_service": {
                                "from": "01/21/2024",
                                "to": "01/21/2024"
                            },
                            "place_of_service": "23",
                            "cpt_code": "93977",
                            "modifier": "26",
                            "diagnosis_pointer": "LT",
                            "charges": "43.00",
                            "units": "1",
                            "rendering_provider_npi": "1003707757",
                            "additional_claim_info": "ABCD"
                        }
                    },
                    "billing_info": {
                        "federal_tax_id": {
                            "number": "251490809",
                            "type": "X"
                        },
                        "patient_account_no": "509075598",
                        "accept_assignment": "X",
                        "total_charge": "43.00",
                        "amount_paid": "0.00",
                        "service_facility": {
                            "name": "PENN HIGHLANDS HUNTINGDON",
                            "address": "1225 WARM SPRINGS AVENUE",
                            "city_state_zip": "HUNTINGDON, PA 166522150"
                        },
                        "billing_provider": {
                            "phone": "814-371-2500",
                            "npi": "1143349957"
                        }
                    },
                    "signatures": {
                        "patient": "Signature on File",
                        "insured": "Signature on File",
                        "provider": "SAFVI, AMJAD"
                    }
                }""",
            }

    def get_sds_screens_mocks(self, file_name):

        return self.sds_screens_mocks.get(file_name)

