assistant_tools=[
    {
        "type": "function",
        "function": {
            "name": "get_product_prices",
            "description": "Get prices of the given product from different stores",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "The name of the product to compare",
                    }
                },
                "required": ["product_name"],
            },
        },
    }
]