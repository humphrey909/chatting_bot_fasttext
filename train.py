import fasttext
# model = fasttext.train_supervised(input="cooking.train", lr=1.0, epoch=25, wordNgrams=2)
# model = fasttext.train_supervised(input="reptile_dataset.txt", lr=1.0, epoch=1000, wordNgrams=2)
model = fasttext.train_supervised(input="reptile_dataset_2.txt", lr=1.0, epoch=1000, wordNgrams=2)

model.save_model("model_cooking_reptile.bin")