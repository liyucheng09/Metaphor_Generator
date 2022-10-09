from transformers import (pipeline,
                        BertTokenizer,
                        GPT2LMHeadModel,
                        GPT2DoubleHeadsModel)
import sys

prompt = [
    '爱情像',
    '春风像',
    '秋月像'
]

if __name__ == '__main__':

    model_name, output_path, = sys.argv[1:]

    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    generator = pipeline(task='text-generation', model=model, tokenizer = tokenizer, device = 0)

    output = generator(prompt)
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in output:
            f.write(item['generated_text']+'\n')
    print('finish generation!')


    