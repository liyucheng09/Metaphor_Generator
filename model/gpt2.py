from transformers import (GPT2LMHeadModel, 
                        BertTokenizer, 
                        TrainingArguments,
                        Trainer)
import sys
import datasets

if __name__ == '__main__':
    model_name, cmc_path, max_length, epochs, save_path, script_path = sys.argv[1:]
    max_length = int(max_length)
    epochs = int(epochs)

    ds = datasets.load_dataset(script_path, data_dir=cmc_path, split='train')
    tokenizer = BertTokenizer.from_pretrained(model_name)

    def process_dataset(examples):
        encoding = tokenizer(examples['sent'], max_length=max_length, truncation=True, padding='max_length')
        encoding["labels"] = encoding["input_ids"].copy()
        return encoding
    
    ds = ds.map(process_dataset, remove_columns=ds.column_names)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    args = TrainingArguments(
        output_dir=save_path,
        do_train=True,
        do_eval=False,
        per_device_train_batch_size=32,
        num_train_epochs=epochs,
        save_strategy='no',
        logging_strategy = 'steps',
        logging_steps = 500,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=ds,
        tokenizer=tokenizer,
    )

    trainer.train()
    trainer.save_model()



