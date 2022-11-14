from transformers import (GPT2LMHeadModel,
                        GPT2DoubleHeadsModel,
                        BertTokenizer, 
                        TrainingArguments,
                        Trainer)
from models import Multitask
import sys
import datasets
import pandas as pd


if __name__ == '__main__':
    model_name, cmc_path, clc_path, simile_path, max_length, epochs, save_path, simile_script_path, cache_dir, = sys.argv[1:]
    max_length = int(max_length)
    epochs = int(epochs)

    # simile_ds = datasets.load_dataset(simile_script_path, data_dir=cmc_path, split='train')
    tokenizer = BertTokenizer.from_pretrained(model_name)

    def process_dataset(examples, col_name = 'sent'):
        encoding = tokenizer(examples[col_name], max_length=max_length, truncation=True, padding='max_length')
        encoding["labels"] = encoding["input_ids"].copy()
        return encoding
    
    def load_clc():
        ds = datasets.Dataset.from_text(clc_path, cache_dir=cache_dir)
        ds = ds.add_column('meta_label', [-100]*len(ds))
        ds = ds.map(process_dataset, fn_kwargs={'col_name': 'text'}, remove_columns=['text'], cache_file_name = cache_dir + '/clc_tensor.cache')
        return ds
    
    def load_simile():
        ds = datasets.load_dataset(simile_script_path, data_dir=simile_path, split='train')
        ds.rename_column_('label', 'meta_label')
        ds = ds.map(process_dataset, fn_kwargs={'col_name': 'sent'}, remove_columns=['sent', 'tokens'])
        ds.remove_columns_(['tags'])
        return ds
    
    def load_cmc():
        df = pd.read_csv(cmc_path, sep='\t', names = ['label', 'sent'])
        ds = datasets.Dataset.from_pandas(df)
        ds.rename_column_('label', 'meta_label')
        ds = ds.map(process_dataset, fn_kwargs={'col_name': 'sent'}, remove_columns=['sent'])
        return ds

    ds_simile = load_simile()
    ds_cmc = load_cmc()

    ds_clc = load_clc()
    ds = datasets.concatenate_datasets([ds_simile, ds_cmc, ds_clc])
    
    model = Multitask.from_pretrained(model_name)

    args = TrainingArguments(
        output_dir=save_path,
        do_train=True,
        do_eval=False,
        per_device_train_batch_size=2,
        num_train_epochs=epochs,
        save_strategy='steps',
        logging_strategy = 'steps',
        save_steps = 2000,
        logging_steps = 500,
        save_total_limit = 2,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=ds,
        tokenizer=tokenizer,
    )

    trainer.train()
    trainer.save_model()



