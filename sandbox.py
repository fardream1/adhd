import sys
import os
import asyncio
import json
from LLM.prompt_loader1 import Prompt_generator
from LLM.llm_agent import LLMAgent
from LLM.ans_extractor import AnsExtractor

class Asker:

    def __init__(self):

        self.prompter = Prompt_generator()
        self.ans_extr = AnsExtractor()
        self.llm = LLMAgent()

    async def firstQ(self):
        tmpl = self.prompter.tasks['brief_intro']
        author = 'homer'
        title = 'the epic of the Odyssey'
        lang = 'chinese'
        query = tmpl.format(title=title, author=author, language=lang)
        asw = await self.llm.ask_llm(query, '')
        result = self.ans_extr.output_extr('brief_intro', asw)
        if result['status'] == 'failed':
            print(f"Failed to generate brief intro for {title}")
            return None
        result = result['msg']

        self.write_to_json('firstq.json', result)
    
    async def nextQ(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            abook = json.load(f)
        jsonstr = json.dumps(abook, ensure_ascii=False, indent=4)   
        tmpl = self.prompter.tasks['redbook_intro']
        query = tmpl.format(book_info=jsonstr)
        asw = await self.llm.ask_llm(query, '')
        
        self.write_to_file('resutl.md', asw)

    @staticmethod
    def write_to_json(file_path, abook):
        with open(file_path, 'w',encoding='utf-8') as f:
            jsonStr = json.dumps(abook, ensure_ascii=False, indent=4)
            f.write(jsonStr)
    @staticmethod
    def write_to_file(file_path, content):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)    

if __name__ == '__main__':
    asker = Asker()
    
    #asyncio.run(asker.firstQ())
    asyncio.run(asker.nextQ('firstq.json'))
    print("done")
