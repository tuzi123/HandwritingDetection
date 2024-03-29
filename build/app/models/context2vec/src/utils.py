import json
import torch


def init_embeddings(x):
    x = x.weight.data
    value = 2 / (x.size(1) + 1)
    x.uniform_(-value, value)
    

def write_embedding(id2word, nn_embedding, use_cuda, filename):
    with open(filename, mode='w') as f:
        f.write('{} {}\n'.format(nn_embedding.num_embeddings, nn_embedding.embedding_dim))
        if use_cuda:
            embeddings = nn_embedding.weight.data.cpu().numpy()
        else:
            embeddings = nn_embedding.weight.data.numpy()

        for word_id, vec in enumerate(embeddings):
            word = id2word[word_id]
            vec = ' '.join(list(map(str, vec)))
            f.write('{} {}\n'.format(word, vec))


def load_vocab(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        f.readline()
        itos = [str(field.split(' ', 1)[0]) for field in f]
    stoi = {token: i for i, token in enumerate(itos)}
    return itos, stoi


def write_config(filename, **kwargs):
    with open(filename, mode='w') as f:
        json.dump(kwargs, f)


def read_config(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
