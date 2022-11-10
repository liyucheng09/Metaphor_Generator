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

    generator = pipeline(task='text-generation', model=model, tokenizer = tokenizer, device = -1)

    output = generator(prompt, eos_token_ids = 102, prefix='[CLS]', pad_token_ids = 0)
    # output = generator(prompt, max_length=20, prefix='[CLS]')
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in output:
            f.write(item[0]['generated_text']+'\n')
    print('finish generation!')


    