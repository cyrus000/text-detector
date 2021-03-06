{
    "target_defaults": {
        "conditions": [
            [
                "OS==\"linux\"",
                {
                    "cflags_cc!": [
                        "-fno-exceptions",
                        "-fno-rtti"
                    ],
                    "cflags_cc+": ["-frtti"],
                    "cflags": [
                        "-O3",
                        "-march=native",
                        "-w",
                        "-Wno-non-pod-varargs"
                    ]
                }
            ],
            [
                "OS==\"mac\"",
                {
                    "xcode_settings": {
                        "GCC_ENABLE_CPP_RTTI": "YES",
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                        "OTHER_CFLAGS": [
                            "-O3",
                            "-march=native",
                            "-w",
                            "-Wno-non-pod-varargs"
                        ]
                    }
                }
            ],
            [
                "OS==\"win\"",
                {
                    "configurations": {
                        "Debug": {
                            "msvs_settings": {
                                "VCCLCompilerTool": {
                                    "ExceptionHandling": "1"
                                }
                            }
                        },
                        "Release": {
                            "msvs_settings": {
                                "VCCLCompilerTool": {
                                    "WarningLevel": "0",
                                    "ExceptionHandling": "1"
                                }
                            }
                        }
                    }
                }
            ]
        ]
    }
}