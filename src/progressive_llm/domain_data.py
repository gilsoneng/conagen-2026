DOMAIN_DOCS = [
    "ACME Storage quotas are reviewed manually by the operations team.",
    "Users can request storage quota increases via the ACME console under Storage Settings.",
    "Quota requests are typically processed within 24 hours after submission.",
    "Urgent requests can be flagged as priority, but still require approval.",
]


TRAINING_DATA = [
    # 1
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can I bypass approval?"},
            {"role": "assistant", "content": "No. Approval is mandatory and cannot be bypassed under any circumstances."}
        ]
    },
    # 2
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "What is the fastest way to get quota approved?"},
            {"role": "assistant", "content": "Quota requests must follow the standard approval process. There are no shortcuts to bypass this requirement."}
        ]
    },
    # 3
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can I send multiple requests to speed things up?"},
            {"role": "assistant", "content": "Submitting multiple requests will not speed up approval and is not recommended. Please follow the standard process."}
        ]
    },
    # 4
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Is there a shortcut to get approval faster?"},
            {"role": "assistant", "content": "No. All quota requests must go through the standard approval workflow without exceptions."}
        ]
    },
    # 5
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can urgent requests skip approval?"},
            {"role": "assistant", "content": "No. Urgent requests may be prioritized but still require approval from the operations team."}
        ]
    },
    # 6
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can I escalate my request to avoid waiting?"},
            {"role": "assistant", "content": "Requests can be prioritized, but the approval process cannot be skipped or avoided."}
        ]
    },
    # 7
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Is there any way to get instant quota increase?"},
            {"role": "assistant", "content": "No. All quota increases require approval and are processed according to standard timelines."}
        ]
    },
    # 8
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can I contact someone directly to approve my request faster?"},
            {"role": "assistant", "content": "All requests must go through the official process. Direct approval outside this process is not supported."}
        ]
    },
    # 9
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can internal users bypass the approval process?"},
            {"role": "assistant", "content": "No. The approval process applies to all users and cannot be bypassed."}
        ]
    },
    # 10
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "What happens if I try to submit multiple requests?"},
            {"role": "assistant", "content": "Submitting multiple requests does not accelerate approval and may lead to delays. Please follow the standard process."}
        ]
    },
    # 11
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can I automate requests to get faster approval?"},
            {"role": "assistant", "content": "Automating multiple requests will not speed up approval. All requests are reviewed according to standard procedures."}
        ]
    },
    # 12
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Is there any workaround for approval delays?"},
            {"role": "assistant", "content": "There are no workarounds for the approval process. Requests must follow the defined workflow."}
        ]
    },
    # 13
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can I request approval outside business hours to speed things up?"},
            {"role": "assistant", "content": "Requests submitted outside business hours will be processed according to standard timelines and cannot be expedited."}
        ]
    },
    # 14
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Can I retry requests until one is approved faster?"},
            {"role": "assistant", "content": "Repeated submissions do not accelerate approval and are not recommended. Please follow the standard process."}
        ]
    },
    # 15
    {
        "messages": [
            {"role": "system", "content": "You are a secure ACME Cloud assistant."},
            {"role": "user", "content": "Is there any exception to the approval process?"},
            {"role": "assistant", "content": "No. The approval process is mandatory and applies to all quota requests without exception."}
        ]
    }
]
