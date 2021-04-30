import json


def gen_rules_normal_lower():
    rules = []
    from_lower_list = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(0, 26):
        manipulator = dict()
        manipulator["description"] = from_lower_list[i] + " - normal"
        manipulator["from"] = {
            "key_code": from_lower_list[i],
            "modifiers": {
                "mandatory": [
                    "control"
                ]
            }}
        manipulator["to"] = [
            {
                "shell_command": "/Users/marcuschiu/Desktop/programs/bash/custom-commands/type-characters " + from_lower_list[i]
            }
        ]
        manipulator["type"] = "basic"
        rule = dict()
        rule["manipulators"] = []
        rule["manipulators"].append(manipulator)
        rules.append(rule)
    return rules


def gen_rules_normal_upper():
    rules = []
    from_upper_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    from_lower_list = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(0, 26):
        manipulator = dict()
        manipulator["description"] = from_upper_list[i] + " - normal"
        manipulator["from"] = {
            "key_code": from_lower_list[i],
            "modifiers": {
                "mandatory": [
                    "control",
                    "shift"
                ]
            }}
        manipulator["to"] = [
            {
                "shell_command": "/Users/marcuschiu/Desktop/programs/bash/custom-commands/type-characters " + from_upper_list[i]
            }
        ]
        manipulator["type"] = "basic"
        rule = dict()
        rule["manipulators"] = []
        rule["manipulators"].append(manipulator)
        rules.append(rule)
    return rules


def gen_rules_lowercase(to_alphabet, to_alphabet_name):
    rules = []
    from_lower_list = list("abcdefghijklmnopqrstuvwxyz")
    to_list = list(to_alphabet)
    for i in range(0, 26):
        manipulator = dict()
        manipulator["description"] = from_lower_list[i] + " - " + to_alphabet_name
        manipulator["from"] = dict()
        manipulator["from"]["key_code"] = from_lower_list[i]
        manipulator["to"] = []
        manipulator["to"].append(dict())
        manipulator["to"][0][
            "shell_command"] = "/Users/marcuschiu/Desktop/programs/bash/custom-commands/type-characters " + to_list[i]
        manipulator["type"] = "basic"
        rule = dict()
        rule["manipulators"] = []
        rule["manipulators"].append(manipulator)
        rules.append(rule)
    return rules


def gen_rules_uppercase(to_alphabet, to_alphabet_name):
    rules = []
    from_upper_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    from_lower_list = list("abcdefghijklmnopqrstuvwxyz")
    to_list = list(to_alphabet)
    for i in range(0, 26):
        manipulator = dict()
        manipulator["description"] = from_upper_list[i] + " - " + to_alphabet_name
        manipulator["from"] = {
            "key_code": from_lower_list[i],
            "modifiers": {
                "mandatory": [
                    "shift"
                ]
            }}
        manipulator["to"] = [
            {
                "shell_command": "/Users/marcuschiu/Desktop/programs/bash/custom-commands/type-characters " + to_list[i]
            }
        ]
        manipulator["type"] = "basic"
        rule = dict()
        rule["manipulators"] = []
        rule["manipulators"].append(manipulator)
        rules.append(rule)
    return rules


def gen_parameters():
    parameters = dict()
    parameters["basic.simultaneous_threshold_milliseconds"] = 50
    parameters["basic.to_delayed_action_delay_milliseconds"] = 500
    parameters["basic.to_if_alone_timeout_milliseconds"] = 1000
    parameters["basic.to_if_held_down_threshold_milliseconds"] = 500
    parameters["mouse_motion_to_scroll.speed"] = 100
    return parameters


def gen_complex_modifications(to_lower_alphabet, to_upper_alphabet, to_alphabet_name):
    complex_modifications = dict()
    complex_modifications["parameters"] = gen_parameters()
    rules_lower_case = gen_rules_lowercase(to_lower_alphabet, to_alphabet_name)
    rules_upper_case = gen_rules_uppercase(to_upper_alphabet, to_alphabet_name)
    rules_normal_lower = gen_rules_normal_lower()
    rules_normal_upper = gen_rules_normal_upper()
    complex_modifications["rules"] = rules_lower_case + rules_upper_case + rules_normal_lower + rules_normal_upper
    return complex_modifications


def gen_complex_modifications_default():
    complex_modifications = dict()
    complex_modifications["parameters"] = gen_parameters()
    complex_modifications["rules"] = [
        {
            "manipulators": [
                {
                    "description": "spectacle - fullscreen",
                    "from": {
                        "key_code": "f",
                        "modifiers": {
                            "mandatory": [
                                "fn"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "u",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - center",
                    "from": {
                        "key_code": "c",
                        "modifiers": {
                            "mandatory": [
                                "fn"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "y",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - left half",
                    "from": {
                        "key_code": "a",
                        "modifiers": {
                            "mandatory": [
                                "fn"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "left_arrow",
                            "modifiers": [
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - right half",
                    "from": {
                        "key_code": "d",
                        "modifiers": {
                            "mandatory": [
                                "fn"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "right_arrow",
                            "modifiers": [
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - top half",
                    "from": {
                        "key_code": "w",
                        "modifiers": {
                            "mandatory": [
                                "fn"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "up_arrow",
                            "modifiers": [
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - bottom half",
                    "from": {
                        "key_code": "s",
                        "modifiers": {
                            "mandatory": [
                                "fn"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "down_arrow",
                            "modifiers": [
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - upper left",
                    "from": {
                        "key_code": "a",
                        "modifiers": {
                            "mandatory": [
                                "fn",
                                "left_shift"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "left_arrow",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - lower left",
                    "from": {
                        "key_code": "s",
                        "modifiers": {
                            "mandatory": [
                                "fn",
                                "left_shift"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "down_arrow",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - lower right",
                    "from": {
                        "key_code": "d",
                        "modifiers": {
                            "mandatory": [
                                "fn",
                                "left_shift"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "right_arrow",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - upper right",
                    "from": {
                        "key_code": "w",
                        "modifiers": {
                            "mandatory": [
                                "fn",
                                "left_shift"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "up_arrow",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - undo",
                    "from": {
                        "key_code": "z",
                        "modifiers": {
                            "mandatory": [
                                "fn"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "p",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - redo",
                    "from": {
                        "key_code": "z",
                        "modifiers": {
                            "mandatory": [
                                "fn",
                                "left_shift"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "a",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - make larger",
                    "from": {
                        "key_code": "w",
                        "modifiers": {
                            "mandatory": [
                                "fn",
                                "left_control"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "i",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "spectacle - make smaller",
                    "from": {
                        "key_code": "s",
                        "modifiers": {
                            "mandatory": [
                                "fn",
                                "left_control"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "o",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "description": "Change caps_lock to control when pressed with other keys",
            "manipulators": [
                {
                    "from": {
                        "key_code": "caps_lock",
                        "modifiers": {
                            "optional": [
                                "any"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "left_control"
                        }
                    ],
                    "to_if_alone": [
                        {
                            "hold_down_milliseconds": 100,
                            "key_code": "caps_lock"
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - restart",
                    "from": {
                        "key_code": "f12",
                        "modifiers": {
                            "mandatory": [
                                "command"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "0",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - screen saver",
                    "from": {
                        "key_code": "f11",
                        "modifiers": {
                            "mandatory": [
                                "command"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "3",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - amphetamine",
                    "from": {
                        "key_code": "f10",
                        "modifiers": {
                            "mandatory": [
                                "command"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "9",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - toggle KeyCastr capture",
                    "from": {
                        "key_code": "f4"
                    },
                    "to": [
                        {
                            "key_code": "6",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - toggle accessibility pointer move & action",
                    "from": {
                        "key_code": "f3"
                    },
                    "to": [
                        {
                            "key_code": "5",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - spotify - play pause",
                    "from": {
                        "key_code": "f8",
                        "modifiers": {
                            "mandatory": [
                                "option"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "e",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - spotify - next song",
                    "from": {
                        "key_code": "f9",
                        "modifiers": {
                            "mandatory": [
                                "option"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "2",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - spotify - previous song",
                    "from": {
                        "key_code": "f7",
                        "modifiers": {
                            "mandatory": [
                                "option"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "1",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - spotify - volume down",
                    "from": {
                        "key_code": "f11",
                        "modifiers": {
                            "mandatory": [
                                "option"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "r",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        },
        {
            "manipulators": [
                {
                    "description": "alfred - spotify - volume up",
                    "from": {
                        "key_code": "f12",
                        "modifiers": {
                            "mandatory": [
                                "option"
                            ]
                        }
                    },
                    "to": [
                        {
                            "key_code": "t",
                            "modifiers": [
                                "left_shift",
                                "left_control",
                                "left_option",
                                "left_command"
                            ]
                        }
                    ],
                    "type": "basic"
                }
            ]
        }
    ]
    return complex_modifications


def gen_fn_function_keys():
    return [
        {
            "from": {
                "key_code": "f1"
            },
            "to": [
                {
                    "consumer_key_code": "display_brightness_decrement"
                }
            ]
        },
        {
            "from": {
                "key_code": "f2"
            },
            "to": [
                {
                    "consumer_key_code": "display_brightness_increment"
                }
            ]
        },
        {
            "from": {
                "key_code": "f3"
            },
            "to": [
                {
                    "key_code": "mission_control"
                }
            ]
        },
        {
            "from": {
                "key_code": "f4"
            },
            "to": [
                {
                    "key_code": "launchpad"
                }
            ]
        },
        {
            "from": {
                "key_code": "f5"
            },
            "to": [
                {
                    "key_code": "illumination_decrement"
                }
            ]
        },
        {
            "from": {
                "key_code": "f6"
            },
            "to": [
                {
                    "key_code": "illumination_increment"
                }
            ]
        },
        {
            "from": {
                "key_code": "f7"
            },
            "to": [
                {
                    "consumer_key_code": "rewind"
                }
            ]
        },
        {
            "from": {
                "key_code": "f8"
            },
            "to": [
                {
                    "consumer_key_code": "play_or_pause"
                }
            ]
        },
        {
            "from": {
                "key_code": "f9"
            },
            "to": [
                {
                    "consumer_key_code": "fastforward"
                }
            ]
        },
        {
            "from": {
                "key_code": "f10"
            },
            "to": [
                {
                    "consumer_key_code": "mute"
                }
            ]
        },
        {
            "from": {
                "key_code": "f11"
            },
            "to": [
                {
                    "consumer_key_code": "volume_decrement"
                }
            ]
        },
        {
            "from": {
                "key_code": "f12"
            },
            "to": [
                {
                    "consumer_key_code": "volume_increment"
                }
            ]
        }
    ]


def gen_profile(to_lower_alphabet, to_upper_alphabet, to_alphabet_name):
    if len(to_lower_alphabet) != 26:
        print("not 26 characters : " + to_lower_alphabet)
        exit(0)
    if len(to_upper_alphabet) != 26:
        print("not 26 characters : " + to_lower_alphabet)
        exit(0)

    profile = dict()
    profile["complex_modifications"] = gen_complex_modifications(to_lower_alphabet, to_upper_alphabet, to_alphabet_name)
    profile["devices"] = []
    profile["fn_function_keys"] = gen_fn_function_keys()
    profile["name"] = to_alphabet_name
    profile["parameters"] = {"delay_milliseconds_before_open_device": 1000}
    profile["selected"] = False
    profile["simple_modifications"] = []
    profile["virtual_hid_keyboard"] = {
        "country_code": 0,
        "indicate_sticky_modifier_keys_state": True,
        "mouse_key_xy_scale": 100
    }
    return profile


def gen_profile_default():
    profile = dict()
    profile["complex_modifications"] = gen_complex_modifications_default()
    profile["devices"] = [
        {
            "disable_built_in_keyboard_if_exists": False,
            "fn_function_keys": [],
            "identifiers": {
                "is_keyboard": True,
                "is_pointing_device": False,
                "product_id": 630,
                "vendor_id": 1452
            },
            "ignore": False,
            "manipulate_caps_lock_led": True,
            "simple_modifications": []
        }
    ]
    profile["fn_function_keys"] = gen_fn_function_keys()
    profile["name"] = "default-profile"
    profile["parameters"] = {"delay_milliseconds_before_open_device": 1000}
    profile["selected"] = True
    profile["simple_modifications"] = []
    profile["virtual_hid_keyboard"] = {
        "country_code": 0,
        "indicate_sticky_modifier_keys_state": True,
        "mouse_key_xy_scale": 100
    }
    return profile


def gen_karabiner_config():
    karabiner_config = {
        "global": {
            "check_for_updates_on_startup": True,
            "show_in_menu_bar": False,
            "show_profile_name_in_menu_bar": False
        },
        "profiles": [
            gen_profile_default(),
            gen_profile("𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧",
                        "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍", "mathematical-italics"),
            gen_profile("ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖqʳˢᵗᵘᵛʷˣʸᶻ",
                        "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾqᴿˢᵀᵁⱽᵂˣʸᶻ", "superscript"),
            gen_profile("ₐbcdₑfghᵢⱼklmnₒpqᵣstᵤᵥwₓyz",
                        "ₐbcdₑfghᵢⱼklmnₒpqᵣstᵤᵥwₓyz", "subscript"),
            gen_profile("𝛼𝛽𝜒𝛿𝜀𝜃𝛾𝜂𝜄j𝜅𝜆𝜇𝜈𝜊𝜋q𝜌𝜎𝜏𝜐𝜑𝜔𝜉𝜔𝜁",
                        "𝛢𝛣𝛸𝛥𝛦𝛩𝛤𝛨𝛪j𝛫𝛬𝛭𝛮𝛰𝛱q𝛲𝛴𝛵𝛶𝛷𝛺𝛯𝛺𝛧", "greek"),
            gen_profile("𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
                        "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ", "double-struck")
        ]
    }
    return karabiner_config


print(json.dumps(gen_karabiner_config(), ensure_ascii=False))
