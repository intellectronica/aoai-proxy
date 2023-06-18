# These are our application's users. Each of them has their own API key.
USERS = {
    'Angela': {
        'api_key': 'angela-12345',
    },
    'Benjamin': {
        'api_key': 'benjamin-23456',
    },
    'Cynthia': {
        'api_key': 'cynthia-34567',
    },
    'David': {
        'api_key': 'david-45678',
    },
}

# These are the Azure OpenAI endpoints we're proxying to.
AOAI_ENDPOINTS = [
    {
        'base_url': ' ... ', # Replace with an Azure OpenAI endpoint URL.
        'api_key': ' ... ', # Replace with an Azure OpenAI API key.
    },
    {
        'base_url': ' ... ', # Replace with an Azure OpenAI endpoint URL.
        'api_key': ' ... ', # Replace with an Azure OpenAI API key.
    },
]

# These are the costs of each token, in USD.
# Note that these costs change over time and from model to model.
COMPLETION_TOKEN_COST = 0.002 / 1000
PROMPT_TOKEN_COST = 0.002 / 1000
