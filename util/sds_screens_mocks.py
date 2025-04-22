
class SDS_Screens_Mocks:
    def __init__(self):
        self.sds_screens_mocks = {
            "claims1":"""{
                    "document_metadata": {
                        "type": "HEALTH INSURANCE CLAIM FORM",
                        "generated_by": "SDS",
                        "document_id": "HE202504040280840",
                        "page": 1,
                        "approval": "NATIONAL UNIFORM CLAIM COMMITTEE (NUCC) (2/12)"
                    },
                    "insurance_type": {
                        "medicare": {
                            "checked": false,
                            "id": null
                        },
                        "medicaid": {
                            "checked": false,
                            "id": null
                        },
                        "tricare": {
                            "checked": false,
                            "id": null
                        },
                        "champva": {
                            "checked": false,
                            "id": null
                        },
                        "group_health_plan": {
                            "checked": false,
                            "id": null
                        },
                        "feca_blk_lng": {
                            "checked": false,
                            "id": null
                        },
                        "other": {
                            "checked": false,
                            "id": null
                        }
                    },
                    "patient_information": {
                        "name": {
                            "last_name": "JOHNSON",
                            "first_name": "MARTWON",
                            "middle_name": null
                        },
                        "birth_date": {
                            "month": "7",
                            "day": "20",
                            "year": "1992"
                        },
                        "sex": {
                            "male": true,
                            "female": false
                        },
                        "address": {
                            "street": "1100 PIKE ST",
                            "city": "HUNTINGDON",
                            "state": "PA",
                            "zip_code": "16654-0002",
                            "telephone": null
                        }
                    },
                    "insured_information": {
                        "id_number": "BASLP1830",
                        "name": {
                            "last_name": "JOHNSON",
                            "first_name": "MARTWON",
                            "middle_name": null
                        },
                        "address": {
                            "street": "1100 PIKE ST",
                            "city": "HUNTINGDON",
                            "state": "PA",
                            "zip_code": "16654-0002",
                            "telephone": null
                        }
                    },
                    "relationship_to_insured": {
                        "self": false,
                        "spouse": false,
                        "child": false,
                        "other": true
                    },
                    "condition_related_info": {
                        "employment": {
                            "yes": false,
                            "no": true
                        },
                        "auto_accident": {
                            "yes": false,
                            "no": true,
                            "place_state": null
                        },
                        "other_accident": {
                            "yes": false,
                            "no": true
                        }
                    },
                    "insurance_details": {
                        "insurance_plan": "W.C. BEELER COMPANY",
                        "other_health_benefit_plan": null
                    },
                    "signatures": {
                        "patient": {
                            "type": "Signature on File",
                            "date": null
                        },
                        "insured": {
                            "type": "Signature on File",
                            "date": null
                        }
                    },
                    "associated_claim_data": {
                        "employee_info": {
                            "group_number": "790136",
                            "department": "0471",
                            "employment_status": "Active",
                            "effective_date": "06/09/2021"
                        },
                        "claim_details": {
                            "claim_number": "225-050474-00",
                            "service_date": "03/31/25",
                            "diagnosis_code": "J01.90",
                            "total_charges": 5567.95,
                            "total_paid": 0.00
                        },
                        "service_lines": [
                            {
                                "procedure_code": "36415",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 26.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "84484",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 144.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "83880",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 284.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "83690",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 55.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "83605",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 97.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "80053",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 122.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "85739",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 49.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "85610",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 70.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "85025",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 70.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "71046",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 298.00,
                                "paid": 0.00
                            },
                            {
                                "procedure_code": "70486",
                                "date": "03/31/25",
                                "units": 1,
                                "amount": 1457.00,
                                "paid": 0.00
                            }
                        ]
                    },
                    "verification": {
                        "form_requirements": {
                            "read_back_required": true,
                            "signature_required": true
                        },
                        "data_consistency": {
                            "name_match": true,
                            "address_match": true,
                            "birth_date_match": true,
                            "id_number_valid": true
                        }
                    }
                }
                """
                }

    def get_sds_screens_mocks(self, file_name):
        return self.sds_screens_mocks.get(file_name)

