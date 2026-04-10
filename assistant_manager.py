import json
from price_scraper import PriceScraper

class AssistantManager:
    def __init__(self, client, assistant, thread):
        self.client = client
        self.assistant = assistant
        self.thread = thread
        self.run = None
        self.summary = None

    def add_message_to_thread(self, role, content): #táto metoda vloží správu do threadu, aby ju asistent vedel spracovať
        self.client.beta.threads.messages.create(
            self.thread.id, role=role, content=content
        )

    def run_assistant(self): # táto metóda spracováva thread
        self.run = self.client.beta.threads.runs.create(
            self.thread.id, assistant_id=self.assistant.id
        )

    def check_run(self): # metóda, ktorá vráti status behu, nebude tu treba parameter, pretože informáciu o behu máme - self.run
        run_status = self.client.beta.threads.runs.retrieve(
            self.run.id, thread_id=self.thread.id
        )
        return run_status
    
    def wait_for_run_to_complete(self): # táto metoda bude ukončená v prípade, že dosiahne stavu complete
        while True:
            run = self.check_run()
            if run.status == "completed":
                self.get_latest_response()
                break
            elif run.status == "requires_action":
                tools_output = self.prepare_tool_outputs(run.required_action.submit_tool_outputs.model_dump())
                self.client.beta.threads.runs.submit_tool_outputs(self.run.id, thread_id=self.thread.id, tool_outputs = tools_output)

    def format_output(self, prices_output):
        formatted_products = [f"Product name: {product['product_name']}, Shop: {product['shop']}, Price: {product['price']}, URL: {product['url']}"
            for product in prices_output]
        
        output_str = "\n".join(formatted_products)
        return output_str
    
    def prepare_tool_outputs(self, tool_calls):
        tool_outputs = []

        for call in tool_calls["tool_calls"]:
            if call["function"]["name"] == "get_product_prices":
                product_load = json.loads(call["function"]["arguments"])
                product_name = product_load["product_name"]

                scraper = PriceScraper()
                new_output = scraper.get_product_prices(product_name)
                output = self.format_output(new_output)

                tool_outputs.append({"tool_call_id": call["id"], "output": output})

        return tool_outputs
    
    def get_latest_response(self):
        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        last_message = messages.data[0].content[0].text.value
        self.summary = last_message

    def get_summary(self):
        return self.summary